#!/usr/bin/env python3
"""CSS regression check: builds the site, renders a fixed set of pages in headless
Chrome at desktop and mobile widths, and records every element's computed style
plus a full-page screenshot.

    python3 tools/css-regression.py baseline   # before a CSS/layout change
    python3 tools/css-regression.py compare    # after it; exits 1 on real differences

Elements are matched by tag path (not class names), so renaming classes doesn't
count as a difference. Differences of 0.5px or less are reported as minor. An
element that merely moved because something above it changed size isn't listed
again, so the report points at the cause.

Needs Google Chrome and `pip3 install selenium pillow`. Output lives in
$TMPDIR/css-regression (override with --out).
"""
import argparse, http.server, json, os, shutil, subprocess, sys, tempfile, threading
from functools import partial

PAGES = {
    'home':        '/',
    'post-rich':   '/2026/09/15/i-installed-a-modern-radeon-gpu-on-a-raspberry-pi-5/',
    'post-table':  '/2026/09/12/akihabara-retro-game-shopping-guide/',
    'post-quote':  '/2026/09/06/i-just-wanted-to-power-my-pal-snes-in-america/',
    'post-lists':  '/getting-started-with-the-pocket-developer-api/',
    'tweet':       '/2025/07/12/three-playstation-3-three-copies-of-gran-turismo-5-one-awesome-experience-2/',
    'youtube':     '/2025/07/12/gran-turismo-5-in-ultra-widescreen-triple-screen/',
    'hardware':    '/hardware/dell-optiplex-760/',
    'guide':       '/howto/getting-started-with-webassembly-part-1-hello-world/',
    'listing':     '/hardware/',
    'reference':   '/reference/',
    'sitemap':     '/sitemap/',
    'not-found':   '/404.html',
}
WIDTHS = {'desktop': 1280, 'mobile': 390}
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROPS = ['display', 'position', 'float', 'box-sizing',
         'margin-top', 'margin-right', 'margin-bottom', 'margin-left',
         'padding-top', 'padding-right', 'padding-bottom', 'padding-left',
         'border-top-width', 'border-right-width', 'border-bottom-width', 'border-left-width',
         'border-top-color', 'border-bottom-color', 'border-left-color', 'border-top-left-radius',
         'max-width', 'gap', 'align-items', 'justify-content', 'flex-wrap',
         'font-family', 'font-size', 'font-weight', 'font-style', 'line-height', 'letter-spacing',
         'color', 'background-color', 'text-transform', 'text-decoration-line', 'text-decoration-thickness',
         'text-underline-offset', 'text-align',
         'vertical-align', 'list-style-type', 'white-space', 'opacity', 'fill', 'stroke', 'stroke-width']

# Async script run in each page: freeze animations, wait for images, load exactly
# one infinite-scroll batch on the home feed (so JS-rendered feed markup is checked
# too), then return every element's box and computed style.
CAPTURE_JS = """
var PROPS = arguments[0], done = arguments[arguments.length - 1];
var freeze = document.createElement('style');
// iframes hold third-party content (YouTube) that renders differently run to run
freeze.textContent = '*,*::before,*::after{animation:none!important;transition:none!important} iframe{visibility:hidden!important}';
document.head.appendChild(freeze);
var failed = new Set();
[].forEach.call(document.images, function (i) { i.addEventListener('error', function () { failed.add(i); }); });
function unsized() { return [].filter.call(document.images, function (i) { return !failed.has(i) && !(i.complete && i.naturalWidth > 0); }); }
// resolves once every image is decoded and has real dimensions (or failed); gives up after 20s
function images() {
  return Promise.all([].map.call(document.images, function (i) { return i.decode().catch(function () {}); })).then(function () {
    return new Promise(function (ok) {
      var t0 = Date.now(), retried = false;
      waitFor(function () {
        // a request to the local server occasionally stalls; re-request once
        if (!retried && Date.now() - t0 > 5000) { retried = true; unsized().forEach(function (i) { i.src = i.src.split('#')[0] + '#retry'; }); }
        return !unsized().length || Date.now() - t0 > 20000;
      }, ok);
    });
  });
}
function path(el) { var p = []; while (el && el !== document.body) { var i = 1, s = el; while ((s = s.previousElementSibling)) if (s.tagName === el.tagName) i++; p.unshift(el.tagName.toLowerCase() + ':' + i); el = el.parentElement; } return p.join('>'); }
function styles(cs) { var o = {}; PROPS.forEach(function (k) { o[k] = cs.getPropertyValue(k); }); return o; }
function collect() {
  var out = {height: document.documentElement.scrollHeight, els: {},
             unsized: unsized().map(function (i) { return i.getAttribute('src'); })};
  document.querySelectorAll('body *').forEach(function (el) {
    if (/^(SCRIPT|STYLE|NOSCRIPT)$/.test(el.tagName)) return;
    var r = el.getBoundingClientRect();
    var rec = {rect: [r.left + scrollX, r.top + scrollY, r.width, r.height].map(function (v) { return Math.round(v * 10) / 10; }),
               s: styles(getComputedStyle(el))};
    ['::before', '::after'].forEach(function (ps) { var c = getComputedStyle(el, ps); if (c.content && c.content !== 'none' && c.content !== 'normal') rec[ps] = styles(c); });
    out.els[path(el)] = rec;
  });
  done(out);
}
function waitFor(test, then) { var t = setInterval(function () { if (test()) { clearInterval(t); then(); } }, 50); }
var feed = !!document.querySelector('.infinite-spinner');
function feedLoaded() { return performance.getEntriesByType('resource').some(function (e) { return /all-posts\\.json/.test(e.name); }); }
waitFor(function () { return document.readyState === 'complete' && (!feed || feedLoaded()); }, function () {
  images().then(function () {
    if (!feed) return setTimeout(collect, 150);
    window.scrollTo(0, document.body.scrollHeight);
    jQuery(window).triggerHandler('scroll');   // appends one batch synchronously...
    jQuery(window).off('scroll');              // ...and nothing more after that
    window.scrollTo(0, 0);
    images().then(function () { setTimeout(collect, 150); });
  });
});
"""


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


def capture(out_dir):
    from selenium import webdriver
    site = os.path.join(out_dir, 'site')
    shutil.rmtree(out_dir, ignore_errors=True); os.makedirs(out_dir)
    r = subprocess.run(['bundle', 'exec', 'jekyll', 'build', '-d', site], cwd=REPO, capture_output=True, text=True)
    if r.returncode: sys.exit('jekyll build failed:\n' + r.stderr)
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=site))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{srv.server_address[1]}'
    opts = webdriver.ChromeOptions()
    for a in ('--headless=new', '--hide-scrollbars', '--force-device-scale-factor=1'): opts.add_argument(a)
    driver = webdriver.Chrome(options=opts)
    driver.set_script_timeout(60)
    try:
        for wname, w in WIDTHS.items():
            for name, url in PAGES.items():
                driver.set_window_size(w, 900)
                driver.get(base + url)
                data = driver.execute_async_script(CAPTURE_JS, PROPS)
                json.dump(data, open(os.path.join(out_dir, f'{name}.{wname}.json'), 'w'))
                driver.set_window_size(w, min(int(data['height']), 16000))
                driver.save_screenshot(os.path.join(out_dir, f'{name}.{wname}.png'))
                print(f'  captured {name:10} {wname}')
    finally:
        driver.quit(); srv.shutdown()


def num(v):
    v = v.strip()
    return float(v[:-2]) if v.endswith('px') and v[:-2].replace('.', '', 1).lstrip('-').isdigit() else None


# computed values that differ as strings but render identically on this (LTR) site
EQUIVALENT = [{'left', 'start'}, {'normal', 'flex-start'}]


def compare_values(a, b):
    """'' if equal, 'minor' if every px value differs by <= 0.5, else 'major'."""
    if a == b or {a, b} in EQUIVALENT: return ''
    pa, pb = a.split(), b.split()
    if len(pa) == len(pb) and all(num(x) is not None and num(y) is not None for x, y in zip(pa, pb)):
        return 'minor' if all(abs(num(x) - num(y)) <= 0.5 for x, y in zip(pa, pb)) else 'major'
    return 'major'


def compare(base_dir, cur_dir, limit):
    from PIL import Image, ImageChops
    total_major = 0
    for wname in WIDTHS:
        for name in PAGES:
            key = f'{name}.{wname}'
            ja = json.load(open(os.path.join(base_dir, key + '.json')))
            jb = json.load(open(os.path.join(cur_dir, key + '.json')))
            a, b = ja['els'], jb['els']
            for label, j in (('baseline', ja), ('current', jb)):
                if j.get('unsized'): print(f'WARN {key}: {label} captured before these images loaded: {j["unsized"]}')
            major, minor = [], []
            moved = {}
            for p in sorted(set(a) | set(b)):
                if p not in b: major.append(f'{p}: element removed'); continue
                if p not in a: major.append(f'{p}: element added'); continue
                ra, rb = a[p]['rect'], b[p]['rect']
                delta = tuple(round(y - x, 1) for x, y in zip(ra, rb))
                moved[p] = delta
                parent = p.rsplit('>', 1)[0] if '>' in p else None
                if any(abs(d) > 0.5 for d in delta):
                    # only a knock-on shift if the parent moved identically and our size didn't change
                    if not (parent in moved and moved[parent][:2] == delta[:2] and abs(delta[2]) <= 0.5 and abs(delta[3]) <= 0.5):
                        major.append(f'{p}: box {ra} -> {rb}')
                elif delta != (0, 0, 0, 0):
                    minor.append(f'{p}: box {ra} -> {rb}')
                for part in ('s', '::before', '::after'):
                    sa, sb = a[p].get(part, {}), b[p].get(part, {})
                    if bool(sa) != bool(sb): major.append(f'{p} {part}: present {bool(sa)} -> {bool(sb)}'); continue
                    for k in sa:
                        kind = compare_values(sa[k], sb.get(k, ''))
                        if kind: (major if kind == 'major' else minor).append(f'{p} {"" if part == "s" else part + " "}{k}: {sa[k]!r} -> {sb.get(k)!r}')
            ia = Image.open(os.path.join(base_dir, key + '.png')).convert('RGB')
            ib = Image.open(os.path.join(cur_dir, key + '.png')).convert('RGB')
            if ia.size != ib.size:
                shot = f'size {ia.size} -> {ib.size}'
            else:
                diff = ImageChops.difference(ia, ib).convert('L').point(lambda v: 255 if v > 24 else 0)
                changed = diff.histogram()[255]
                shot = 'identical' if not changed else f'{changed} px changed ({100 * changed / (ia.width * ia.height):.3f}%), bbox {diff.getbbox()}'
            print(f'{"OK" if not major else "DIFF":4} {key:20} major={len(major):4} minor={len(minor):4} screenshot: {shot}')
            for line in major[:limit]: print('       ' + line)
            if len(major) > limit: print(f'       … {len(major) - limit} more')
            total_major += len(major)
    return total_major


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode', choices=['baseline', 'compare'])
    ap.add_argument('--out', default=os.path.join(tempfile.gettempdir(), 'css-regression'))
    ap.add_argument('--limit', type=int, default=15, help='max differences listed per page')
    args = ap.parse_args()
    base_dir, cur_dir = os.path.join(args.out, 'baseline'), os.path.join(args.out, 'current')
    if args.mode == 'baseline':
        capture(base_dir)
    else:
        if not os.path.isdir(base_dir): sys.exit('no baseline yet — run `baseline` first')
        capture(cur_dir)
        n = compare(base_dir, cur_dir, args.limit)
        print(f'\n{"no major differences" if not n else f"{n} major differences"}')
        sys.exit(1 if n else 0)
