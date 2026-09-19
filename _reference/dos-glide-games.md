---
layout: post
title: DOS Glide Games
summary: A reference list of DOS games with 3Dfx Glide support, split by how they talk to the card — statically linked (Voodoo 1/2 only), dynamically linked too (any Voodoo card), or just Glide-compatible with no linking noted.
date: '2026-09-18 23:45:00'
tags: [3Dfx Voodoo, Lists, MS-DOS]
---

DOS games with [3Dfx Glide]({% link _software/glide.md %}) support don't all behave the same way, and which group a game falls into decides which Voodoo cards it'll actually run on.

- **Statically linked** — Voodoo support is baked directly into the game binary. These only work with the [Voodoo 1]({% link _hardware/3dfx-voodoo-1.md %}) and [Voodoo 2]({% link _hardware/3dfx-voodoo-2.md %}) — without one of those cards present, the game or PC will usually just freeze.
- **Statically and dynamically linked** — a small handful of games shipped two patches, so they work either way.
- **Dynamically linked** — the game looks for a `glide2x.ovl` file at startup instead of talking to the hardware directly. Copy the right `glide2x.ovl` from any official Voodoo driver package into the game directory, and these will run on a [Voodoo 3]({% link _hardware/3dfx-voodoo-3.md %}), 4, or 5 too.

Full setup steps, environment variables, and troubleshooting: [How To Play 3Dfx Glide Games in DOS]({% link _howto/how-to-play-3dfx-voodoo-glide-games-in-dos.md %}).

### Statically linked (Voodoo 1/2 only)

- Actua Soccer '96
- Battle Arena Toshinden
- Descent II ("D2VOODOO" patch, Destination Quartzon, The Infinite Abyss)
- EuroFighter 2000 (incl. v2.0)
- Fatal Racing / Whiplash
- Starfighter 3000
- UEFA Champions League 96/97
- VR Soccer '96

### Statically and dynamically linked (both patches exist)

- Tomb Raider (incl. Tomb Raider Gold, Unfinished Business)
- X-CAR: Experimental Racing

### Also Glide-supported, linking not specified

These are confirmed Glide-compatible, but the source doesn't say whether they're statically or dynamically linked:

- Archimedean Dynasty / Schleichfahrt
- Battlecruiser 3000AD
- Blood (incl. Blood Plasma Pack, One Unit Whole Blood)
- Burnout: Championship Drag Racing
- Carmageddon (incl. Max Pack, Splat Pack)
- Dreams To Reality
- Extreme Assault
- Grand Theft Auto (incl. Mission Pack #1 – London 1969)
- Jet Fighter III: Platinum Edition
- Jet Fighter: Full Burn
- Lands of Lore 2: Guardians of Destiny
- NASCAR Racing 2 (incl. Grand National Series Expansion Pack)
- NASCAR Racing 1999 Edition
- Pył
- Prost Grand Prix (1998)
- Redguard: The Elder Scrolls Adventures
- Screamer 2
- Screamer Rally
- Shadow Warrior
- Tie Break Tennis 98

Even a "dynamic" or unspecified game can have its own quirks — Archimedean Dynasty is a known example with compatibility problems despite using `glide2x.ovl`.

Source and more detail on individual game compatibility: <a href="https://www.vogons.org/viewtopic.php?t=886" target="_blank">Vogons</a>.

### Related on this site

- [How To Play 3Dfx Glide Games in DOS]({% link _howto/how-to-play-3dfx-voodoo-glide-games-in-dos.md %})
- [Glide]({% link _software/glide.md %})
- [3Dfx Voodoo 2]({% link _hardware/3dfx-voodoo-2.md %})
- [3Dfx Voodoo 3]({% link _hardware/3dfx-voodoo-3.md %})
