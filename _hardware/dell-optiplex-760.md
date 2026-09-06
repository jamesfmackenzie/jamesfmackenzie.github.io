---
layout: post
title: Dell OptiPlex 760
summary: Hardware notes on the Dell OptiPlex 760 — a cheap late-Core-2 Dell that's happier under XP and DOS than Windows 98.
date: '2025-12-29 10:30:00'
tags: [Computers, PC]
hero: dell-optiplex-760.jpg
hero_alt: Dell OptiPlex 760 tower
---

The Dell OptiPlex 760 is the kind of machine I find hard to ignore: a cheap, slightly boring office PC that looks like it might have hidden retro potential. It has some — but less than it first appears.

If you want a clean, low-drama Windows 98 build, reach for something earlier — or the [OptiPlex 380]({% link _hardware/dell-optiplex-380.md %}). As a cheap Windows XP machine that can also do some interesting DOS experiments, the 760 makes more sense.

### Specifications

- **Chipset:** Intel Q45 with an `ICH10` controller hub
- **Audio:** Analog Devices `AD1984A` HD Audio codec
- **Memory:** DDR2
- **Storage:** SATA
- **Expansion:** PCI and PCI Express, plus a motherboard serial header

My own machine is a modest one: a Pentium Dual-Core `E5200`, 2GB of DDR2, BIOS `A02`, on a board dated `2009-03-17` — the sort of ordinary office box you'd actually end up with rather than a maxed-out example.

![](/img/dell-optiplex-760-bios.jpg){: width="640"}

### Things worth knowing before you use one

- **The motherboard serial header** is the 760's best retro feature. With a bracket it gives you proper PS/2 keyboard and mouse input — much nicer than fighting USB in DOS.
- **No BIOS RAM-limiting mode.** Unlike the OptiPlex 380, there's no "OS Install" option to cap memory, so Windows 98 setup needs a real memory strategy rather than wishful thinking.
- **`ICH10` and the HD Audio codec** are late enough that neither was designed with Windows 98 in mind — onboard audio under Win98 is still unresolved. The [WDMHDA](https://github.com/andrew-hoffman/WDMHDA) driver installs but doesn't yet support this `AD1984A` codec; there's a [Vogons thread](https://www.vogons.org/viewtopic.php?t=109373) tracking it.
- Worth disabling multi-core support, SpeedStep, and C-states in the BIOS before any serious retro testing.

### Where it fits

DOS is better than expected, Windows XP is the natural fit, and Windows 98 is possible but awkward — and a Voodoo 2 pushes the platform out of easy territory fast.

For the full experiment — the Radeon X600 success, the Voodoo 2 crashes, the unresolved Win98 audio, and where it landed — see [I Tried to Turn a Dell OptiPlex 760 into a Windows 98 Retro PC]({% post_url 2026-03-29-i-tried-to-turn-a-dell-optiplex-760-into-a-windows-98-retro-pc %}), with the [project notes]({% link _projects/turning-a-dell-optiplex-760-into-a-retro-gaming-pc.md %}) tracking the open threads.
