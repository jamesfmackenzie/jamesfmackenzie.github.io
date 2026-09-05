---
layout: post
title: Dell OptiPlex 380
summary: Hardware notes on the Dell OptiPlex 380 — a cheap Core 2-era Dell that covers DOS, Windows 98, and Windows XP unusually well.
date: '2025-12-29 10:30:00'
tags: [Computers, PC]
---

![](/img/posts/dell-optiplex-380-small.png)

The Dell OptiPlex 380 is an unassuming late-2000s business desktop, and it's become one of my favourite cheap retro PC bases. It's common, dirt cheap on the second-hand market, and just old enough to keep the legacy I/O that makes DOS and Windows 98 livable — while being fast enough to crush anything from that era.

Unlike the [Dimension E520]({% link _hardware/dell-dimension-e520.md %}) and the [OptiPlex 760]({% link _hardware/dell-optiplex-760.md %}), which both fight back under Windows 98, the 380 covers all three eras without much drama. It's a great retro machine!

### Specifications

Most OptiPlex 380 systems share the same baseline:

- **CPU:** Intel Core 2 Duo (commonly E7xxx or E8xxx series)
- **Chipset:** Intel G41 with an ICH7 southbridge
- **Memory:** DDR3, officially up to 4GB
- **Storage:** SATA
- **Graphics:** Intel GMA X4500 onboard
- **Expansion:** 1× PCI Express, 2× PCI

It shipped in both desktop and small-form-factor (SFF) cases — go for the desktop, since the SFF badly restricts GPU choice and cooling.

My own machine is a Core 2 Duo `E7600 @ 3.06GHz` with 4GB of DDR3, a 500GB hard disk, and a DVD writer — picked up complete for $60 shipped.

### Things worth knowing before you use one

- **Genuine legacy I/O on the rear panel:** VGA, serial, and parallel, plus PS/2 via a motherboard header and a Dell bracket. USB keyboards can be unreliable in DOS, so the PS/2 route is worth the extra wiring.
- **BIOS "OS Install" mode** caps available RAM at 256MB — exactly what Windows 98 setup wants, especially with 4GB fitted.
- **No ISA slots**, and the ICH7 southbridge doesn't support DDMA or PC/PCI, so native DOS digital audio depends on picking the right PCI card. Yamaha YMF7x4 cards (724, 744, 754) are the ones that work — real OPL3 plus DSDMA.

![The PS/2 header extension run out to the back of the case](/img/posts/dell-optiplex-380-serial-ps2-ribbon-cable-header-extension.jpg){: width="405"}

### Where it fits

This is the rare cheap PC that genuinely covers all three eras: excellent for DOS, unusually good for Windows 98 (with patches and a period Radeon), and completely at home under Windows XP.

For the full build — the Radeon X800 XL, the Yamaha sound card, the Win98 SATA patching, benchmarks, and Crysis running on a $100 machine — see [The Ugly Dell That Became My Dream Retro Gaming PC]({% post_url 2025-12-28-the-ugly-dell-optiplex-that-became-my-dream-retro-gaming-pc %}).
