---
layout: post
title: Dell OptiPlex 380
summary: My take on the Dell OptiPlex 380 as a cheap Core 2 retro PC, with the bits that matter for DOS, Windows 98, and Windows XP.
date: '2025-12-29 10:30:00'
tags: [Computers, PC]
---

![](/img/posts/dell-optiplex-380-small.png)

The Dell OptiPlex 380 is an unassuming late-2000s business desktop, but it's become one of my favourite cheap retro PC bases. It's common, it's dirt cheap on the second-hand market, and it's just old enough to retain the legacy I/O that makes DOS and Windows 98 actually livable.

### What it is

Most OptiPlex 380 systems share the same baseline:

- **CPU:** Intel Core 2 Duo (commonly E7xxx or E8xxx series)
- **Chipset:** Intel G41 with ICH7 southbridge
- **Memory:** DDR3 (officially supported up to 4GB)
- **Storage:** SATA hard drive or SSD
- **Optical:** DVD-ROM or DVD-RW
- **Graphics:** Intel GMA X4500 (onboard)

It shipped in both desktop and small-form-factor (SFF) cases. I'd steer you toward the desktop version — better expansion and cooling for anything beyond stock use.

### Why I like it

- genuine legacy I/O still on the rear panel: VGA, serial, parallel, and PS/2 via a motherboard header and bracket
- both PCI and PCI Express expansion
- a BIOS **OS Install** option that limits RAM to 256MB, which makes Windows 98 setup far less painful
- SATA storage that can be made Windows 98-friendly with the right patches
- cheap and everywhere on the second-hand market

![](/img/posts/dell-optiplex-380-serial-ps2-ribbon-cable-header-extension.jpg)

That's the PS/2 header extension I ran out to the back of the case — well worth doing, since USB input can be unreliable in DOS.

### My take

- **DOS:** excellent
- **Windows 98:** unusually good for hardware this new
- **Windows XP:** completely at home

It's rare to find a cheap PC that covers all three eras this convincingly.

### Windows 98

Out of the box: no. With patches and the right add-in card: yes, very usable.

There are no official Intel G41 Windows 98 drivers, which is expected for hardware this late. To get there you need a SATA patch (I used rloew's) and third-party chipset INF files — the onboard graphics aren't usable for Win9x at all, so plan on a PCIe card. **ATI Radeon X600 to X850-era cards** gave me the best results, with excellent Windows 98 gaming performance once everything's configured.

### DOS

DOS on any post-ICH5 chipset is always a bit of a compromise, and the 380 is no exception — but it's a good one. Anything that leans on CPU performance, VESA graphics modes, or OPL FM synthesis does very well here; late DOS titles that struggle in DOSBox often run great on real 380 hardware.

Sound is the catch. The ICH7 southbridge doesn't support DDMA or PC/PCI, which rules out most PCI sound cards for native DOS digital audio — and there's no ISA slot to fall back on. What did work well for me: **Yamaha YMF7x4 PCI cards** (724, 744, 754), with genuine OPL3 FM synthesis and DSDMA support.

### Windows XP

This is where the 380 feels completely at home — full chipset and storage driver support, broad PCIe GPU compatibility, stable onboard audio, and enough performance for early-to-mid-2000s games. It handled Return to Castle Wolfenstein, Half-Life 2, and Doom 3 comfortably, and can stretch further with reduced settings.

### Pros

- huge CPU headroom for demanding DOS games
- genuinely useful legacy I/O (VGA, serial, parallel, PS/2 via header)
- BIOS RAM-limiting mode makes Windows 98 setup far easier
- SATA storage can be made to work with the right patches
- PCIe Radeon options give strong late-Win98 performance
- broad GPU support and strong performance under Windows XP
- extremely low cost and easy to find

### Cons

- no ISA slots, so native DOS digital audio depends on picking the right PCI sound card
- some Radeon X600 variants are surprisingly incompatible
- SFF cases badly restrict GPU choice and cooling — get the desktop case
- still needs patches and manual setup for Windows 98, not a stock plug-and-play experience

### Other useful things to know

- USB keyboards and mice can be laggy or unreliable in DOS — the PS/2 header is worth the extra wiring.
- After installing Windows 98 with the RAM-limiting BIOS option, you can either stay capped or apply third-party RAM patches.

## Related on this site

- [The Ugly Dell That Became My Dream Retro Gaming PC]({% post_url 2025-12-28-the-ugly-dell-optiplex-that-became-my-dream-retro-gaming-pc %}) — the full build story, benchmarks, and parts choices.
- [Building a Retro Rocket PC on the Cheap]({% link _projects/building-a-retro-rocket-pc-on-the-cheap.md %}) — the project summary page with the overall goal, outcome, and video link.
