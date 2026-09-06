#!/usr/bin/env python3
"""Re-matte hero images onto the site ground colour, trim dead margins,
and convert opaque photo-PNGs to JPEG (updating the frontmatter/body refs).
Full-frame photos and screenshots are left untouched. Re-run-safe."""
import re, pathlib, sys
from PIL import Image, ImageDraw, ImageChops

GROUND = (0xF8, 0xF5, 0xEF)
CONTENT_DIRS = ['_hardware', '_posts', '_projects', '_howto', '_software', '_drafts', '_reference']
# PNG heroes that must stay PNG (logos / pixel art / screenshots)
KEEP_PNG = {
    '3dfx-original-logo-design.png', '8-bit-Memories.png', 'keen.png',
    'moonlight.png', 'retropie_logo.png',
    'lotus-ste-lotus-esprit-turbo-challenge-car-atari-st.png',
}

def hero_map():
    m = {}
    for d in ['_hardware', '_posts', '_projects', '_howto', '_software']:
        for p in pathlib.Path(d).glob('*.md'):
            mm = re.search(r'^hero:\s*(\S+)\s*$', p.read_text(), re.M)
            if mm:
                m.setdefault(mm.group(1), []).append(p)
    return m

def has_transparency(im):
    if im.mode in ('RGBA', 'LA'):
        return im.convert('RGBA').getchannel('A').getextrema()[0] < 250
    return im.mode == 'P' and 'transparency' in im.info

def near_white_border(rgb):
    w, h = rgb.size
    cs = [rgb.getpixel(p) for p in [(0,0),(w-1,0),(0,h-1),(w-1,h-1)]]
    return all(max(c)-min(c) < 12 for c in cs) and all(sum(c)/3 > 236 for c in cs)

def replace_white_bg(rgb, ff_thresh=45):
    d = rgb.copy()
    w, h = d.size
    for seed in [(0,0),(w-1,0),(0,h-1),(w-1,h-1),(w//2,0),(w//2,h-1),(0,h//2),(w-1,h//2)]:
        try:
            if sum(d.getpixel(seed)) / 3 > 235:
                ImageDraw.floodfill(d, seed, GROUND, thresh=ff_thresh)
        except Exception:
            pass
    px = d.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if r >= 243 and g >= 241 and b >= 235 and max(r, g, b) - min(r, g, b) < 16:
                px[x, y] = GROUND
    return d

def autotrim(rgb, pad_frac=0.04, floor=0.5):
    w, h = rgb.size
    bg = Image.new('RGB', rgb.size, GROUND)
    diff = ImageChops.difference(rgb, bg).point(lambda x: 0 if x < 18 else x)
    bbox = diff.getbbox()
    if not bbox:
        return rgb
    l, t, r, b = bbox
    pad = int(max(w, h) * pad_frac)
    l, t = max(0, l - pad), max(0, t - pad)
    r, b = min(w, r + pad), min(h, b + pad)
    # never shrink a dimension below `floor` of the original
    if r - l < w * floor:
        grow = (int(w * floor) - (r - l) + 1) // 2
        l, r = max(0, l - grow), min(w, r + grow)
    if b - t < h * floor:
        grow = (int(h * floor) - (b - t) + 1) // 2
        t, b = max(0, t - grow), min(h, b + grow)
    if (l, t, r, b) == (0, 0, w, h):
        return rgb
    return rgb.crop((l, t, r, b))

def process_image(path):
    im = Image.open(path)
    o = im.size
    if has_transparency(im):
        src = im.convert('RGBA')
        base = Image.new('RGB', src.size, GROUND)
        base.paste(src, mask=src.split()[3])
        rgb, kind = base, 'matte'
    else:
        rgb = im.convert('RGB')
        if near_white_border(rgb):
            rgb, kind = replace_white_bg(rgb), 'rematte'
        else:
            return None
    rgb = autotrim(rgb)
    # decide output format
    name = path.name
    if path.suffix.lower() == '.png' and name not in KEEP_PNG:
        newpath = path.with_suffix('.jpg')
        rgb.save(newpath, quality=86, optimize=True, progressive=True)
        if newpath != path:
            path.unlink()
        return (kind, o, rgb.size, path.name, newpath.name)
    if path.suffix.lower() in ('.jpg', '.jpeg'):
        rgb.save(path, quality=86, optimize=True, progressive=True)
    else:
        rgb.save(path, optimize=True)
    return (kind, o, rgb.size, path.name, path.name)

def update_refs(old, new):
    if old == new:
        return
    for d in CONTENT_DIRS:
        dp = pathlib.Path(d)
        if not dp.is_dir():
            continue
        for p in dp.glob('*.md'):
            t = p.read_text()
            if old in t:
                p.write_text(t.replace(old, new))
    for extra in ['all-posts.json', 'feed.xml', 'sitemap.html', '_layouts/index.html']:
        p = pathlib.Path(extra)
        if p.exists() and old in p.read_text():
            p.write_text(p.read_text().replace(old, new))

hm = hero_map()
report = []
for f, pages in sorted(hm.items()):
    ip = pathlib.Path('img') / f
    if not ip.exists():
        print(f"  MISSING {f}"); continue
    r = process_image(ip)
    if r:
        kind, o, n, oldname, newname = r
        if newname != oldname:
            update_refs(oldname, newname)
        report.append((newname, kind, o, n))

print(f"\nprocessed {len(report)} heroes\n")
for name, kind, o, n in report:
    kb = (pathlib.Path('img') / name).stat().st_size // 1024
    print(f"  {name:<48} {kind:<8} {str(o):<12} -> {str(n):<12} {kb:>4}KB")
