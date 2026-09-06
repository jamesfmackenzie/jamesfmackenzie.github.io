# This repo

The published blog — a Jekyll static site at **jamesfmackenzie.com** (built from
`master` by GitHub Pages, canonical repo `jamesfmackenzie/jamesfmackenzie.github.io`).
Subject: fixing and breaking old computers and consoles. Voice: first-person,
personal, understated — James writing about his own work.

This file is the quick-reference for any AI session in this repo. It is the
*downstream* half of a two-repo setup — see the next section.

## Relationship to the Obsidian vault

The vault at `/Users/jamesmackenzie/Documents/Obsidian Sync/` (its own `CLAUDE.md`
explains it) is the **capture layer**: one `Projects/` note per piece of real work,
published or not, tagged `#blog/ideas` → `#blog/published` as it moves through.

This repo is where a project's work becomes **published content**. When writing here:

- **Pull from the vault project note** for ground truth about what actually happened —
  purchase prices and dates, the chronology, the dead ends, the specific quirks.
  The note is the record of the work; this repo is the edited public version of it.
- **Published pages are their own source of truth once live.** Don't rewrite a
  published page just because a vault note phrases something differently — reconcile
  deliberately, and only when it matters.
- **Never invent detail.** If the vault note doesn't say it and the code or photos
  don't show it, don't claim it. (Fact-check hardware specs against primary sources.)
- **Vault notes may hold private material** — email addresses, third-party
  correspondence, personal context. Never copy that verbatim into published content;
  paraphrase and strip identifying details.

## Content types — when to create what

Don't default to the heaviest option. Match the content to its actual shape.

1. **`_posts/` · `layout: post`** — the default publishing unit. One project (or one
   finished phase of one) that tells a complete, self-contained story needing no other
   content to make sense. Most published work lands here first.
2. **`_posts/` · `layout: youtube`** (`videoId:`) — a post built around a video. Body
   text still renders below the embed. Same bar as a post.
3. **`_posts/` · `layout: tweet`** (`tweetId:`) — the lightest unit. Too small for a
   post: "just arrived", a single fact, a before/after. No build narrative.
4. **`_howto/` (Guides)** — a reproducible procedure someone else follows to get the
   same result. A *post* narrates what I did and learned (dead ends, opinions); a
   *guide* is the distilled steps that work, in order, with the detours removed. Often
   spun out of a post once the process is nailed down. `layout: post`, tag `How To`.
5. **`_hardware/`** — a canonical reference for a specific, reusable piece of hardware:
   what it is, spec, verdict, where it fits. Stays generic — never a testing-session
   narrative (that belongs in the post). Worth creating alongside the first post that
   features the hardware, even with no concrete plan to reuse it.
6. **`_software/`** — same rule, for a tool / driver / patch / emulator / utility.
7. **`_reference/`** — a maintained list or table (compatibility lists, "games with X").
   A living document updated over time, not a narrative.
8. **`_projects/`** — the highest bar, and downstream of the others rather than a
   substitute. Create one only when **2+ already-published separate pieces** exist about
   the same work **and** no single one tells the whole story. If a post already links
   out to its hardware page, that post *is* the sewn-together home — a project page on
   top adds nothing. Earns its place for a genuine multi-part series over time.
   `projects.html` lists these by `status:` (`in progress` / `completed`).

## Repo mechanics

- **Jekyll.** Posts use `permalink: pretty` → `/YYYY/MM/DD/title/`. Named collections
  (`projects`, `howto`, `hardware`, `software`, `reference`) use `/:collection/:path/`,
  slug from filename.
- **`future: false`** — a post dated after the build machine's clock is silently
  excluded, which breaks every `{% link %}` / `{% post_url %}` pointing at it. Check
  `date "+%F %T %Z"` before dating a post; never post-date.
- **Layouts:** `post`, `youtube`, `tweet`, `section` (collection landing), `index`
  (home), `sitemap`, `nodate`, `nocomments`, `missing` (404). `youtube` and `tweet`
  both render `{{ content }}`, so body prose on them displays.
- **`summary:`** feeds the `<meta description>`, the home-feed preview text, and the
  visible intro line on `youtube` / `tweet` layouts. It is **not** shown as a deck on
  regular post pages, and shouldn't be added as one without an editorial pass — many
  existing summaries are written as truncated teasers ending "…" or as SEO strings.
- **`jekyll-redirect-from`** — use `redirect_from:` (or `redirect_to:`) whenever a
  published URL changes.
- **`_drafts/`** — unpublished WIP. Skeleton drafts carry `<!-- DRAFT -->`,
  `<!-- TODO -->`, `<!-- HOLD -->` markers. `bundle exec jekyll build --drafts`
  validates their `{% link %}` tags.
- **Build check before every commit:**
  `bundle exec jekyll build --drafts 2>&1 | grep -iE "error|warn|liquid|could not find|done in"`
  then `rm -rf _site`.
- **Verify the Pages deploy:**
  `gh api repos/jamesfmackenzie/jamesfmackenzie.github.io/pages/builds/latest --jq '"\(.status) \(.commit[0:8]) \(.error.message // "no error")"'`
- **Home page is infinite scroll** (`js/infinite-jekyll.js` + `all-posts.json`). The
  feed markup exists twice — in `_layouts/index.html` (Liquid) and `infinite-jekyll.js`
  (JS-injected) — keep them in sync. The footer is unreachable on the home page.

## Voice & tone

Model page: `_hardware/dell-optiplex-760.md`.

- First person, personal, understated. Ground everything concrete — the real price, the
  real date, the actual quirk, the actual dead end.
- When writing from your own project notes, write in first person. Not "the notes
  suggest" — it's your work.

**AI-tells to cut:**

- rhetorical section headers ("The card is not magic")
- "That [verb]…" as a repeated sentence opener
- marketing superlatives and breathless enthusiasm
- staccato rhetorical questions ("Wait… 3D? As in shutter-glasses 3D? I had to learn more!")
- `---` horizontal-rule section dividers — they read as AI; use whitespace and headings
- triple-redundant sections restating the same point
- the "My take is that X is one of the…" template opener on hardware pages

## Design

`css/main.css` is a single stylesheet built on `:root` tokens (colour + type +
layout). Ground `#f8f5ef` (warm paper), ink `#222a33`, accent `#0f8576`, dark code
blocks. **Source Serif 4** body / **Space Grotesk** headings + UI (loaded in
`_includes/head-includes.md`); `code.css` is the matching dark syntax theme. Layout is
a centred column: ~928px chrome, ~752px media, ~656px running text, all left-aligned.
Keep new CSS token-driven and in that file.

## House styles

- **Hardware page shape:** personal-hook intro → `### What it is` / `### Specifications`
  → `### Why I like it` (bullets) → `### My take` / `### Where it fits` → single
  `### Pros` / `### Cons` (lighter for consoles) → `### Related on this site`.
  Sentence-case headers.
- **Project page body:** `### Project Notes`, then loose two-column `Status | In progress`
  / `Goal | …` lines, then prose, then a `More details:` link list, then video
  embed(s), then `<br />`.
- **Cross-linking:** every hardware / project / post ends with `### Related on this
  site`. When pointing at "how I used it", link the build *post*, not the hardware page.
- **Kicker:** the small label above a page title — `HARDWARE`, `GUIDE`, `SOFTWARE`,
  `PROJECT`, `REFERENCE`, `VIDEO`, `TWEET`. Derived from the collection (or the
  `youtube` / `tweet` layout) in `_includes/post-intro.md`. Plain `_posts` get no kicker.
- The page intro (kicker + `<h1>` + one-line meta + optional hero) is
  `_includes/post-intro.md`, used by post / nodate / nocomments; section + sitemap
  layouts render their own `.intro`.

### Images

- `img/` is a single flat folder — no subfolders. Reference every image as `/img/<file>`.
- **`hero:`** — the lead image, in frontmatter (filename only; `hero_alt:`,
  `hero_caption:` optional). Rendered frameless in a fixed slot below the title, wider
  than the text column, sitting directly on the ground colour `#f8f5ef`.
- Hero images are **re-matted onto `#f8f5ef` and margin-trimmed** by
  `tools/hero-rematte.py` (transparent → composite; near-white studio bg → replace;
  trim dead space, never below 50% of a dimension; opaque photo-PNGs → JPEG with refs
  updated). Re-run it if the ground colour ever changes. Full-frame photos and
  screenshots are left alone.
- **`image:`** — the home-page / feed thumbnail (filename only). **If absent, the
  thumbnail falls back to `hero:`.** Set `image:` explicitly only when the thumbnail
  should differ from the hero.
- **Feed thumbnails are frameless too** (same treatment as heroes). **Body images**
  (anything inside the article) are framed on a white card — hairline + rounded corners;
  add `{: .cutout}` for a transparent render that needs inner padding.
- **Prefer James's own photos** over stock product renders where one exists, and caption
  a personal photo to say so — e.g. *"My own Saturn — a boxed Model 2 I picked up in
  Tokyo."*
- `{: width="680"}` IAL to constrain a wide inline image; `.image-row` for a
  side-by-side pair.
- Source limits: 1600px long edge; JPEG ~q82; PNG only where an alpha channel is
  actually needed (convert photo PNGs to JPEG otherwise); `gifsicle -O3 --colors 256`
  for animated GIFs; `pngquant` for screenshot PNGs.
- On a filename collision when consolidating, rename the less-canonical file (precedent:
  the stock hardware Saturn shot became `sega-saturn-console.jpg`, later dropped once
  the personal photo took over).

## Working practices

- **Commit / push only when asked.** Small content and style changes go direct to
  `master` (repo convention); larger multi-phase work goes on a branch first.
- **Stage explicit paths** — never `git add -A` / `git add .`. Staging bleed has
  produced wrong commit messages here.
- **Commit messages:** concise imperative subject; body explains the *why* plus any
  verification done; end with the `Co-Authored-By:` and `Claude-Session:` trailers.
- **Before deleting or overwriting** an image or page, look at it — if it's not what
  it was described as, or you didn't create it, surface that first.
