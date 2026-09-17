---
layout: post
title: 3Dfx Voodoo 2
summary: Notes on the 3Dfx Voodoo 2 — the 1998 Glide accelerator I've now chased across a thin client, two Dell office PCs, and a modern Windows 10 build.
date: '2024-08-29 11:33:00'
tags: [3D Graphics, 3Dfx Voodoo, PC]
hero: 3dfx-voodoo-2-board.jpg
hero_alt: My 3Dfx Voodoo 2 card
---

The Voodoo 2 is the 3dfx card people mean when they just say "a 3dfx card." No other card in the lineup gets chased on eBay, argued about in comment sections, or shoved into machines it was never meant for quite as often. I've now put one into a fanless thin client, two different Dell office PCs, and a modern Windows 10 build with no PCI slots at all — and every single one of those was its own separate fight.

### What it is

Released in February 1998 as the follow-up to the original [Voodoo Graphics]({% link _hardware/3dfx-voodoo-1.md %}), the Voodoo 2 is a dedicated 3D-only accelerator — like its predecessor, it needs a separate 2D card and an external VGA pass-through cable, rather than doing 2D and 3D itself. It came in 8MB and 12MB versions: both have a 4MB framebuffer capping single-card resolution at 800×600, with the extra memory on the 12MB card going toward texture storage instead.

Its standout feature was Scan-Line Interleave (SLI) — running two Voodoo 2 boards in parallel, each drawing half the screen's lines. SLI doubled rendering throughput and pooled the framebuffer memory, pushing the maximum resolution up to 1024×768, which was genuinely impressive for 1998. A Voodoo 2 SLI pair stayed competitive for years afterward, holding its own against cards like the Riva TNT2 and Matrox G400.

### Specifications

- **Released:** February 1998
- **Chipset clock:** 90MHz
- **Memory:** 8MB or 12MB EDO DRAM at 100MHz (4MB framebuffer, plus 4MB or 8MB texture memory)
- **Max resolution:** 800×600 single card, 1024×768 in SLI
- **API:** Glide (3dfx's proprietary API)
- **Interface:** PCI, with an external VGA pass-through cable from a separate 2D card

### Why I like it

- one of the deepest Glide back catalogues of any 3dfx card
- SLI is a genuinely interesting piece of 3D-accelerator history, not just a spec-sheet footnote
- still common and affordable enough to actually experiment with
- it turns any PC with a spare PCI slot — or even one without, with the right adapter — into a Glide machine

### Where it fits

Every time I've installed one, it's become a project in its own right rather than a quick add-in. In an [HP Compaq t5710 thin client]({% link _hardware/hp-compaq-t5710.md %}) it meant fighting for the machine's one PCI slot. On a modern Z97 board with no PCI slots at all, it meant a PCIe-to-PCI adapter, mounting the card horizontally to fit, an unsigned 64-bit driver from the 3dfxzone forums, disabling Windows 10 driver signature enforcement, and — bizarrely — a Windows XP-era fix for a "trying to map memory" error before Glide finally ran. It's also the card that pushed a [Dell OptiPlex 760]({% link _hardware/dell-optiplex-760.md %}) out of easy Windows 98 territory and into crashes.

None of that makes it a difficult card to recommend — it makes it a card that rewards patience.

### Pros

- huge, well-loved Glide game library
- SLI is a fascinating piece of 3D history
- can be made to work on hardware it was never designed for, with enough persistence

### Cons

- needs a separate 2D card and a pass-through cable
- period drivers don't officially support modern OSes — expect workarounds
- SLI needs two matched cards and a motherboard with two PCI slots to bridge

### Related on this site

- [3Dfx]({% link _hardware/3dfx.md %})
- [3Dfx Voodoo Graphics]({% link _hardware/3dfx-voodoo-1.md %}) — the original
- [3Dfx Voodoo 3]({% link _hardware/3dfx-voodoo-3.md %})
- [I Made 3Dfx Voodoo2 Work on a Modern PC!]({% post_url 2026-08-30-voodoo-2-on-a-modern-pc %})
- [Adding 3dfx Voodoo2 to a Thin Client PC]({% post_url 2022-02-15-adding-3dfx-voodoo2-to-a-thin-client-pc %})
- [HP Compaq t5710]({% link _hardware/hp-compaq-t5710.md %})
- [How To Play 3Dfx Glide Games in DOS]({% link _howto/how-to-play-3dfx-voodoo-glide-games-in-dos.md %})
