---
layout: post
title: Amstrad PC1640
summary: Hardware overview and restoration notes for the Amstrad PC1640, the late-1980s IBM-compatible home PC I grew up on.
date: '2025-08-20 06:33:00'
tags: [Computers, Amstrad, PC]
hero: amstrad-pc1640-2.jpg
hero_alt: Amstrad PC1640 with monitor and keyboard
---

I grew up using an Amstrad PC1640, and it's a machine I'd always wanted to own again. Decades after my original was lost, I was lucky enough to track one down and start restoring it — this page is the reference notes for that ongoing project.

### What it is

Launched in 1987, the PC1640 was Amstrad's follow-up to the PC1512 — a faster, more expandable IBM-compatible aimed at the same UK home and small-business market. Like the 1512, it followed Amstrad's all-in-one approach: a complete bundle of system unit, monitor, keyboard, and mouse, sold as a package rather than assembled piecemeal. That combination of price and completeness helped Amstrad take a real share of the late-80s UK PC market from more established American brands.

Its integrated graphics — a genuine EGA-compatible Paradise PEGA1A chipset — could do CGA, Hercules/MDA, and EGA-compatible modes without an add-in card, which was a real cost advantage at the time. Mine is the monochrome (PC-MD) version.

### Specifications

| Component | Details |
|---|---|
| **CPU** | Intel 8086 @ 8MHz |
| **RAM** | Up to 640KB |
| **Graphics** | Onboard Paradise PEGA1A chipset — CGA, Hercules/MDA, and EGA-compatible modes |
| **Storage** | One or two 5.25" 360KB floppy drives; optional 20MB hard disk |
| **Display** | Monochrome (PC-MD), colour CGA (PC-CD), or enhanced colour EGA (PC-ECD) |
| **OS** | MS-DOS 3.2, often bundled with GEM Desktop 3 |
| **Expansion** | 4× 8-bit ISA slots |

### Restoring mine

Getting a 1987 PC back into daily-usable shape means solving the storage problem first — a dying original hard disk isn't repairable, and the machine won't take a modern drive on its own terms. I fitted a [Lo-tech XT-CF adapter]({% link _hardware/lo-tech-xt-cf.md %}) running [XTIDE Universal BIOS]({% link _software/xt-ide.md %}), which lets a CompactFlash card stand in for the hard drive — getting it to actually boot took several failed attempts before finding the right combination. See [Getting XTIDE Working on the Amstrad PC1640]({% post_url 2026-09-04-getting-xtide-working-on-the-amstrad-pc1640 %}) for the full troubleshooting story.

The other addition is an [ATI Graphics Solution SR]({% link _hardware/ati-graphics-solution-sr.md %}) card, which does something genuinely unusual: it emulates CGA output on the PC1640's monochrome MDA-style monitor, rather than needing a colour display to play CGA games. See [CGA Gaming on an MDA Monochrome Monitor]({% post_url 2025-08-17-cga-gaming-on-an-mda-ttl-monochrome-monitor-with-the-ati-graphics-solution-sr-amstrad-pc1640 %}) for how that works.

### Why I like it

- it's the machine I actually learned DOS on — editing `AUTOEXEC.BAT` and `CONFIG.SYS` for the first time
- the onboard Paradise chipset is genuinely flexible for its era — CGA, MDA, and EGA-compatible modes from one card
- four 8-bit ISA slots leave real room for storage and graphics upgrades, even if 8-bit-only limits what fits
- it's old enough that almost every part of keeping it running is its own small project

### Pros

- a real EGA-compatible chipset built in, not just CGA
- simple, well-documented ISA expansion
- genuinely reliable 8086-era hardware once storage is sorted

### Cons

- 8-bit-only ISA slots rule out most later expansion cards
- original storage (5.25" floppies, MFM hard disk) is a real bottleneck without an adapter like the XT-CF

### Related on this site

- [Getting XTIDE Working on the Amstrad PC1640]({% post_url 2026-09-04-getting-xtide-working-on-the-amstrad-pc1640 %})
- [CGA Gaming on an MDA Monochrome Monitor]({% post_url 2025-08-17-cga-gaming-on-an-mda-ttl-monochrome-monitor-with-the-ati-graphics-solution-sr-amstrad-pc1640 %})
- [Lo-tech XT-CF]({% link _hardware/lo-tech-xt-cf.md %})
- [ATI Graphics Solution SR]({% link _hardware/ati-graphics-solution-sr.md %})
