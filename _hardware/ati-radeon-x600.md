---
layout: post
title: ATi Radeon X600
summary: Hardware overview of the ATI Radeon X600, a surprisingly useful PCIe-era graphics card for late Windows 98 and Windows XP retro experiments.
date: '2024-08-29 11:33:00'
tags: [3D Graphics, ATi, PC]
---

The Radeon X600 is an unusual card in retro PC terms. It comes from the early PCI Express era, which immediately makes it suspect for Windows 98 builders, but it's also close enough to ATi's better-supported Radeon generations that it can work far better than you'd expect — depending entirely on which machine it ends up in.

### What it is

The X600 is an early PCI Express card built on ATi's RV370 GPU, sold widely through OEM channels like Dell in the mid-2000s. It's a modest card by later standards, but it landed close enough to the end of ATi's official Windows 98 driver support window that it's worth testing rather than dismissing outright.

### Specifications

- **Released:** 2004
- **GPU:** RV370
- **Pixel pipelines:** 4
- **Memory:** 128MB DDR, 128-bit bus
- **Core clock:** around 400MHz

### Windows 98: it depends on the machine

This is the real story of the card — "supported GPU" and "stable GPU" are not the same thing, and the X600 makes that obvious.

- On a [Dell OptiPlex 760]({% link _hardware/dell-optiplex-760.md %}), it installed quickly with Catalyst 6.2 and worked properly, hardware Direct3D acceleration included. See the [full write-up]({% post_url 2026-03-29-i-tried-to-turn-a-dell-optiplex-760-into-a-windows-98-retro-pc %}).
- On a [Dell Dimension E520]({% link _hardware/dell-dimension-e520.md %}), the exact opposite happened — it froze Windows 98 outright as soon as the Catalyst driver loaded, with no difference between Catalyst 6.2 and 9.0c. The [Radeon X700 Pro]({% link _hardware/ati-radeon-x700-pro.md %}) failed identically on the same machine. See the [full write-up]({% post_url 2026-03-30-i-tried-to-turn-a-dell-dimension-e520-into-a-windows-98-retro-pc %}).
- On a [Dell OptiPlex 380]({% link _hardware/dell-optiplex-380.md %}), X600-to-X850-era ATi cards are still some of the more interesting Win98 options to test.

Same driver, same GPU family, two very different outcomes depending on the chipset underneath it.

### Why I like it

- an early PCIe card that still sits inside ATi's Windows 98 driver support window
- cheap and common, thanks to years of OEM use
- when it works, it's a genuinely elegant bridge between classic Win98 gaming and newer hardware
- when it doesn't, it's a useful, fast way to find out a platform's limits

### Pros

- fast enough for demanding late Windows 98 and Windows XP games
- inexpensive and easy to find
- official-era ATi driver support

### Cons

- platform-dependent to the point of being unpredictable — works perfectly on one machine, freezes another outright
- early PCIe on a late-9x OS is inherently a bit of a gamble

### Related on this site

- [ATi]({% link _hardware/ati.md %})
- [ATi Radeon X700 Pro]({% link _hardware/ati-radeon-x700-pro.md %})
- [I Tried to Turn a Dell OptiPlex 760 into a Windows 98 Retro PC]({% post_url 2026-03-29-i-tried-to-turn-a-dell-optiplex-760-into-a-windows-98-retro-pc %})
- [Dell OptiPlex 380]({% link _hardware/dell-optiplex-380.md %})
- [Dell Dimension E520]({% link _hardware/dell-dimension-e520.md %})
