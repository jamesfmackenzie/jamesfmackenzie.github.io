import re, sys, pathlib

DIRS = ['_hardware', '_posts', '_projects', '_software', '_howto']
FM = re.compile(r'^---\n(.*?\n)---\n', re.S)
IMG = re.compile(r'^!\[(?P<alt>[^\]]*)\]\((?:/img/)?(?P<file>[^)\s]+)\)(?:\{:[^}]*\})?\s*$')
CAP = re.compile(r'^\*(?P<cap>[^*].*?)\*\s*$')

report = []
for d in DIRS:
    for p in sorted(pathlib.Path(d).glob('*.md')):
        text = p.read_text()
        m = FM.match(text)
        if not m:
            continue
        fm, body = m.group(1), text[m.end():]
        if 'hero:' in fm:
            continue
        lines = body.split('\n')
        i = 0
        while i < len(lines) and lines[i].strip() == '':
            i += 1
        if i >= len(lines):
            continue
        im = IMG.match(lines[i].strip())
        if not im:
            continue
        hero_file = im.group('file')
        hero_alt = im.group('alt').strip()
        # consume the image line
        drop_to = i + 1
        hero_caption = None
        # optional caption on the next non-blank line, but only if it's immediately after (0 or 1 blank line)
        j = drop_to
        blanks = 0
        while j < len(lines) and lines[j].strip() == '':
            blanks += 1; j += 1
        if blanks <= 1 and j < len(lines):
            cm = CAP.match(lines[j].strip())
            if cm:
                hero_caption = cm.group('cap').strip()
                drop_to = j + 1
        # rebuild body without the consumed lines
        new_body_lines = lines[:i] + lines[drop_to:]
        new_body = '\n'.join(new_body_lines).lstrip('\n')
        # build new frontmatter: insert hero fields before closing ---
        fm_lines = fm.rstrip('\n').split('\n')
        # drop a redundant `image:` that equals the hero
        fm_lines = [l for l in fm_lines
                    if not re.match(r'\s*image:\s*'+re.escape(hero_file)+r'\s*$', l)]
        add = [f'hero: {hero_file}']
        if hero_alt and hero_alt.lower() not in ('', hero_file.lower()):
            add.append(f'hero_alt: {hero_alt}')
        if hero_caption:
            # yaml-safe: quote if it has a colon
            v = hero_caption
            if ':' in v or v.startswith(('"', "'", '[', '{', '&', '*', '#', '|', '>', '%', '@', '`')):
                v = '"' + v.replace('"', '\\"') + '"'
            add.append(f'hero_caption: {v}')
        new_fm = '\n'.join(fm_lines + add) + '\n'
        new_text = '---\n' + new_fm + '---\n\n' + new_body
        p.write_text(new_text)
        report.append((str(p), hero_file, hero_alt or '-', hero_caption or '-'))

print(f"migrated {len(report)} files\n")
for r in report:
    print(f"  {r[0]:<62} hero={r[1]:<38} cap={r[3][:40]}")
