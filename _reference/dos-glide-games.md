---
layout: post
title: DOS Glide Games
summary: A reference list of DOS games with 3Dfx Glide support, split by how they talk to the card — statically linked (Voodoo 1/2 only) versus dynamically linked via glide2x.ovl (any Voodoo card).
date: '2026-09-18 23:45:00'
tags: [3Dfx Voodoo, Lists, MS-DOS]
---

DOS games with [3Dfx Glide]({% link _software/glide.md %}) support split into two groups, and which one a game falls into decides which Voodoo cards it'll actually run on.

- **Statically linked** — Voodoo support is baked directly into the game binary. These only work with the [Voodoo 1]({% link _hardware/3dfx-voodoo-1.md %}) and [Voodoo 2]({% link _hardware/3dfx-voodoo-2.md %}) — without one of those cards present, the game or PC will usually just freeze.
- **Dynamically linked** — the game looks for a `glide2x.ovl` file at startup instead of talking to the hardware directly. Copy the right `glide2x.ovl` from any official Voodoo driver package into the game directory, and these will run on a [Voodoo 3]({% link _hardware/3dfx-voodoo-3.md %}), 4, or 5 too.

Full setup steps, environment variables, and troubleshooting: [How To Play 3Dfx Glide Games in DOS]({% link _howto/how-to-play-3dfx-voodoo-glide-games-in-dos.md %}).

### Statically linked (Voodoo 1/2 only)

- Actua Soccer '96
- Battle Arena Toshinden
- EF2000: TactCom
- Fatal Racing / Whiplash
- Starfighter 3000

### Dynamically linked (any Voodoo card, via glide2x.ovl)

- Descent II
- Tomb Raider
- Screamer 2
- XCar: Experimental Racing

Even some dynamically linked games have their own quirks — Archimedean Dynasty is a known example with compatibility problems despite using `glide2x.ovl`. More detail on individual game compatibility: <a href="https://www.vogons.org/viewtopic.php?t=886" target="_blank">Vogons</a>.

### Related on this site

- [How To Play 3Dfx Glide Games in DOS]({% link _howto/how-to-play-3dfx-voodoo-glide-games-in-dos.md %})
- [Glide]({% link _software/glide.md %})
- [3Dfx Voodoo 2]({% link _hardware/3dfx-voodoo-2.md %})
- [3Dfx Voodoo 3]({% link _hardware/3dfx-voodoo-3.md %})
