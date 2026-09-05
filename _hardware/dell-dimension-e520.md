---
layout: post
title: Dell Dimension E520
summary: My take on the Dell Dimension E520 as a Core 2-era retro PC, with the bits that matter for DOS, Windows 98, and Windows XP.
date: '2025-12-29 10:30:00'
tags: [Computers, PC]
---

![Dell Dimension E520 tower](/img/posts/dell-dimension-e520.jpg){: width="500"}

The Dell Dimension E520 is the kind of PC nobody would call exciting on paper — a no-frills mid-2000s home machine built around Intel's G965 platform. What makes it interesting to me is timing: it's fast enough to brute-force a lot of late DOS and Win9x games, but new enough that older operating systems stop behaving naturally the moment you install them.

My own machine has a Core 2 Duo `E4300 @ 1.80GHz` on an 800MHz bus with 2MB of L2 cache, and 3GB of DDR2-667 running in dual interleaved mode (512MB, 1GB, 1GB, 512MB across the four DIMMs), with Intel HD Audio and a Sigmatel codec for sound. Nothing exotic — the kind of ordinary office or family PC configuration that still turns up cheaply today.

![](/img/posts/dell-dimension-e520-bios-processor-info.jpg)

![](/img/posts/dell-dimension-e520-bios-memory-info.jpg)

### What it is

The E520 is built around Intel's G965 Express chipset with an `ICH8` southbridge — solid for its Windows XP-era home-PC role, but never designed with Windows 98 or DOS in mind. That later southbridge is a big part of why the machine feels far more natural under XP than under Win98 or native DOS.

![](/img/posts/dell-dimension-e520-nh82801hh-ich-8-chip.jpg)

Specs vary by configuration, but most E520 systems share:

- **Chipset:** Intel G965 Express
- **Southbridge / I/O controller:** Intel `ICH8`
- **Memory:** DDR2-533 or DDR2-667
- **Storage:** SATA
- **Graphics:** Intel GMA 3000 onboard
- **Expansion:** PCI Express x16, PCI Express x1, 2 PCI
- **Networking:** integrated Ethernet

### Why I keep it

- Core 2-class performance for late DOS and Win9x games — enough to brute-force where subtlety fails
- both PCI and PCIe expansion give me room to experiment
- a BIOS **OS Install** option that limits RAM to 256MB, which takes a lot of the pain out of Windows 98 setup
- SATA storage that can be made usable under Windows 98 with the right patches

![](/img/posts/dell-dimension-e520-bios-memory-limiting-option.jpg)

### My take

- **DOS:** interesting, but compromised
- **Windows 98:** possible, but temperamental
- **Windows XP:** the natural fit

That split is really the story of the machine. The E520 is powerful enough to be appealing, but it sits right on the boundary where Win98 and DOS stop being comfortable.

### Pros

- Core 2 performance makes late DOS and Win9x games an easy win
- PCI plus PCIe expansion leaves room for sound-card and GPU experiments
- BIOS RAM-limiting mode takes a lot of the pain out of Windows 98 setup
- SATA storage can be patched into working shape under Windows 98
- **SBEMU** gives a practical fallback for DOS sound
- Voodoo 2 results look more promising here than on the OptiPlex 760
- Windows XP just works — stable storage and chipset support, enough performance for a wide range of early-2000s games

### Cons

- `ICH8` was never designed with Windows 98 in mind, and it shows in post-install disk behaviour
- PCIe Radeon cards don't behave as cleanly as they should under Win98
- onboard audio remains a weak point throughout
- no native PS/2 or serial ports on the rear I/O, and USB keyboards can be laggy or buffered in DOS
- native DOS digital audio is still limited by the later chipset design
- if Windows XP is your only goal, there are plenty of other Core 2 machines that will do the job just as well

### Other useful things to know

- The motherboard does appear to have solder pads for a serial or PS/2 header. I haven't tried it myself — more of an experimental path than a solved convenience.
- VBE and other software-rendered DOS games are an easy win here, even before you've sorted out sound.

## Related on this site

- [I Tried to Turn a Dell Dimension E520 into a Windows 98 Retro PC]({% post_url 2026-03-30-i-tried-to-turn-a-dell-dimension-e520-into-a-windows-98-retro-pc %})
