#!/usr/bin/env python3
"""Snapshot YouTube view counts into the `stats: views:` front matter of every
`layout: youtube` post, formatted the way YouTube shows them (987, 4.3K, 12K, 1.2M).

    python3 tools/youtube-views.py            # dry run: print a table, change nothing
    python3 tools/youtube-views.py --write    # update the posts

Counts are read from each video's public watch page. Videos whose count can't be
read (private, removed, or the page layout changed) are reported and left alone.
"""
import argparse, glob, re, sys, time, urllib.request

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'


def fetch_views(video_id):
    req = urllib.request.Request(f'https://www.youtube.com/watch?v={video_id}', headers={'User-Agent': UA, 'Accept-Language': 'en'})
    html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
    m = re.search(r'"viewCount":"(\d+)"', html)
    return int(m.group(1)) if m else None


def youtube_format(n):
    """YouTube's short form: truncated, not rounded (4,358 -> 4.3K, 12,999 -> 12K)."""
    for size, suffix in ((1_000_000_000, 'B'), (1_000_000, 'M'), (1_000, 'K')):
        if n >= size:
            v = n / size
            s = f'{int(v * 10) / 10:.1f}' if v < 10 else str(int(v))
            return s.removesuffix('.0') + suffix
    return str(n)


def set_views(text, views):
    """Set stats.views in the front matter, keeping any other stats and formatting."""
    head, sep, body = text.partition('\n---\n')[0], '\n---\n', text.partition('\n---\n')[2]
    if re.search(r'^stats:\n(  .*\n)*?  views: .*$', head + '\n', re.M):
        head = re.sub(r'^(stats:\n(?:  .*\n)*?  views: ).*$', rf'\g<1>{views}', head + '\n', count=1, flags=re.M).rstrip('\n')
    elif re.search(r'^stats:$', head, re.M):
        head = re.sub(r'^stats:$', f'stats:\n  views: {views}', head, count=1, flags=re.M)
    else:
        head = re.sub(r'^(videoId: .*)$', rf'\1\nstats:\n  views: {views}', head, count=1, flags=re.M)
    return head + sep + body


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--write', action='store_true', help='update the posts (default is a dry run)')
    args = ap.parse_args()
    posts = []
    for f in sorted(glob.glob('_posts/*.md')):
        text = open(f, encoding='utf-8').read()
        head = text.split('\n---\n', 1)[0]
        if re.search(r'^layout: *youtube\s*$', head, re.M):
            vid = re.search(r'^videoId: *(\S+)', head, re.M)
            old = re.search(r'^stats:\n(?:  .*\n)*?  views: (.*)$', head + '\n', re.M)
            posts.append((f, vid.group(1).strip('"\'') if vid else None, old.group(1) if old else '', text))
    failed = []
    for f, vid, old, text in posts:
        n = fetch_views(vid) if vid else None
        if n is None:
            failed.append(f); print(f'  ??      {"":>10}  {f}  (count not found)'); continue
        new = youtube_format(n)
        print(f'  {new:>6}  {n:>10,}  {f}' + (f'  (was {old})' if old and old != new else ''))
        if args.write and new != old:
            open(f, 'w', encoding='utf-8').write(set_views(text, new))
        time.sleep(0.5)
    print(f'\n{len(posts)} video posts, {len(posts) - len(failed)} counts read, {len(failed)} failed'
          + ('' if args.write else ' — dry run, nothing written (use --write)'))
    sys.exit(1 if failed else 0)
