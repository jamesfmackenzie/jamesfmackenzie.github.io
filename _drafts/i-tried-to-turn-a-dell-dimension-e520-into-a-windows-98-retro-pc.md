---
layout: post
title: I Tried to Turn a Dell Dimension E520 into a Windows 98 Retro PC
summary: A case-study draft on why the Dell Dimension E520 looked promising for Windows 98, but turned into a more mixed DOS, Win98, and XP experiment.
tags: [DOS, PC Hardware, Retrogaming, Windows 98, Windows XP]
---

The Dell Dimension E520 looked like it should be a good retro sleeper build: cheap Core 2-era hardware, PCI and PCIe expansion, a BIOS RAM-limiting option for Windows 98 setup, and just enough weirdness to make it interesting.

What I found was more complicated. The E520 can be pushed into some genuinely useful retro roles, but it is much less straightforward than an earlier beige-box Win98 build. In practice it feels more like a hybrid machine with partial Win98 support than a clean all-in-one answer.

For the broader hardware overview, see the companion page for the **[Dell Dimension E520]({% link _hardware/dell-dimension-e520.md %})**.

## Hardware Overview

The important details for this experiment were:

- Intel `G965` chipset with `ICH8`
- two PCI slots plus PCIe expansion
- a BIOS **OS Install** mode that can cap RAM at 256MB
- no native PS/2 or serial ports on the back panel

That RAM-limiting feature is one of the main reasons the E520 was worth trying at all. It removes one of the first major Windows 98 problems before installation even starts.

My specific machine is based on:

- **CPU:** Core 2 Duo `E4300`
- **Memory:** 3GB DDR2 RAM
- **Audio:** Intel HD Audio with a Sigmatel codec

![](/img/posts/dell-dimension-e520-bios-processor-info.jpg)

![](/img/posts/dell-dimension-e520-bios-memory-info.jpg)

## Why I Thought It Might Work

At a glance, the E520 has several things going for it:

- BIOS-assisted RAM limiting for Win98 setup
- SATA storage that can at least be patched into submission
- enough CPU performance to crush late DOS and Win9x games
- PCI and PCIe expansion for graphics and sound experiments
- Voodoo 2 results that looked more promising than on the OptiPlex 760

That was enough to make it worth a proper attempt.

## First Test: Can Windows 98 Install Cleanly?

The basic install recipe was sensible enough:

- enable **OS Install** in BIOS
- prepare a FAT32 system disk
- install Windows 98 normally
- apply the storage and memory patches where needed
- add the unofficial Intel INF files

Useful ingredients from the notes were:

- **rloew SATA patch**
- optional **PATCHMEM**
- **LoneCrusader** Intel INF files

That was enough to get Windows 98 onto the machine, but not enough to make it comfortable.

![](/img/posts/dell-dimension-e520-bios-memory-limiting-option.jpg)

## The Big Problem: Disk Access Was Unstable

The main problem was not simply installation. It was what happened afterwards.

Observed behaviour included:

- long black-screen pauses during boot
- repeated hangs during final setup
- the machine eventually loading, suggesting timeout or controller trouble rather than a clean hard crash

The key workaround was to **disable 32-bit disk access** in Windows 98.

That costs performance, but it made the system behave much better. More than anything else, that defines the E520 as a Windows 98 platform: possible, but only once you accept that storage behaviour is going to be part of the fight.

## Graphics: The Radeon Route Was Not the Easy Answer

The onboard graphics were never the point. The interesting part was how add-in cards behaved.

The notes suggest:

- Radeon **X600** and **X700** cards were unstable under Catalyst on this machine
- **VBEMP** drivers gave a much more usable fallback
- Quake II in software mode already ran very well

That makes the E520 a useful reminder that a "supported" late Win98 GPU is not always a stable one once PCIe and newer Intel chipsets enter the picture.

![](/img/posts/dell-dimension-e520-windows-98-using-the-vbe-driver-as-a-fallback.jpg)

## The Good News: Voodoo 2 Looked Much Better

Unlike the OptiPlex 760, the Voodoo 2 notes here are actually encouraging.

- **FastVoodoo 4.6** installed
- Quake II, Unreal, and 3DMark reportedly worked well
- Glide support looked strong enough to make the machine worth pursuing

That is a big point in the E520's favour. A hybrid setup with VBE for 2D and Voodoo 2 for Glide is much more convincing than a pure PCIe Radeon-based Win98 plan.

One of the screenshots in the notes shows a **3DMark 99 Max score of 4796** with the Voodoo 2 installed, which is a good sign that the hybrid approach is more than just theoretically workable.

![](/img/posts/dell-dimension-e520-windows-98-3dmark-99-max-score-with-voodoo-2.jpg)

## DOS

DOS on the E520 is surprisingly viable, but not effortless.

The biggest annoyance is laggy USB keyboard behaviour in native DOS. That is a recurring problem on some Dell systems of this era, and the E520 is made worse by the lack of easy rear-panel PS/2 or serial options.

Possible routes from the notes:

1. unlock or flash the BIOS for better USB legacy support
2. explore the motherboard header pads for a serial or PS/2-style input solution

Sound is also more of a workaround story than a clean period-correct one, but **SBEMU** looks like a practical option when dedicated DOS-friendly sound hardware is not available.

Even without a lot of polishing, though, the machine already looked fast and interesting for software-rendered DOS games.

![](/img/posts/dell-dimension-e520-doom-running-in-dos-mode.jpg)

## Windows XP

Windows XP looks like the natural fit for the E520.

The hardware generation is much more comfortable there than it is under Windows 98:

- proper chipset and storage support
- no need to fight the platform just to boot reliably
- much more sensible graphics-card options

That does not make the XP result surprising, but it does make it useful. If you want a cheap XP-era gaming machine that can also do some interesting DOS and Win98 experiments, the E520 starts to make more sense.

## Verdict So Far

The Dell Dimension E520 is not a dead end for retro gaming, but it is also not the simple sleeper Win98 build it first appears to be.

My current verdict is:

- **Windows 98:** possible, but temperamental
- **PCIe Radeon drivers:** the weak point
- **Voodoo 2:** surprisingly promising
- **DOS:** viable, but input and sound need thought
- **Windows XP:** the real comfort zone

That still makes it an interesting machine. Just not for the neat, low-drama "one box does everything" story I first hoped for.
