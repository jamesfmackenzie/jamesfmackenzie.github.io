---
layout: post
title: I Tried to Turn a Dell Dimension E520 into a Windows 98 Retro PC
date: '2026-03-30 08:00:00'
summary: A case-study post on why the Dell Dimension E520 looked promising for Windows 98, but turned into a more mixed DOS, Win98, and XP experiment.
image: dell-dimension-e520.jpg
tags: [DOS, PC, Retrogaming, Windows 98, Windows XP]
---

![Dell Dimension E520 tower](/img/dell-dimension-e520.jpg){: width="500"}

The Dell Dimension E520 looked like it should be a good retro sleeper build: cheap Core 2-era hardware, PCI and PCIe expansion, a BIOS RAM-limiting option for Windows 98 setup, and just enough weirdness to make it interesting.

What I found was more complicated. The E520 can be pushed into some genuinely useful retro roles, but it is much less straightforward than an earlier beige-box Win98 build. In practice it feels more like a hybrid machine with partial Win98 support than a clean all-in-one answer.

For the broader hardware overview, see the companion page for the **[Dell Dimension E520]({% link _hardware/dell-dimension-e520.md %})**; the running [project notes]({% link _projects/turning-a-dell-dimension-e520-into-a-retro-gaming-pc.md %}) track where the build is up to.

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

<div class="image-row">
  <img src="/img/dell-dimension-e520-bios-processor-info.jpg" alt="E520 BIOS screen showing the Core 2 Duo E4300">
  <img src="/img/dell-dimension-e520-bios-memory-info.jpg" alt="E520 BIOS screen showing 3GB of DDR2">
</div>

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

The pieces I needed were the **rloew SATA patch**, optionally **PATCHMEM**, and the **LoneCrusader** Intel INF files.

That was enough to get Windows 98 onto the machine, but not enough to make it comfortable.

![The BIOS "OS Install" option, which caps RAM at 256MB](/img/dell-dimension-e520-bios-memory-limiting-option.jpg){: width="620"}

## The Big Problem: Disk Access Was Unstable

The main problem was not simply installation. It was what happened afterwards.

Observed behaviour included:

- long black-screen pauses during boot
- repeated hangs during final setup
- the machine eventually loading, suggesting timeout or controller trouble rather than a clean hard crash

Disabling ACPI at setup (`setup /p i`) didn't help. The key workaround was to **disable 32-bit disk access** in Windows 98.

That costs performance, but it made the system behave much better. More than anything else, that defines the E520 as a Windows 98 platform: possible, but only once you accept that storage behaviour is going to be part of the fight.

## Graphics: The Radeon Route Was Not the Easy Answer

The onboard graphics were never the point. The interesting part was how add-in cards behaved.

Radeon **X600** and **X700** cards froze Windows outright on driver load — I tried Catalyst 6.2 and later 9.0c, with no difference. My best guess is a VRAM-aperture / memory-mapping conflict between this late chipset's AGP emulation and Windows 98's memory handling. **VBEMP** Miniport drivers gave a much more usable fallback — no Direct3D, but higher colour depth and DirectDraw, and Quake II in software mode already ran very well. `softgpu` is another route I haven't tried yet.

That makes the E520 a useful reminder that a "supported" late Win98 GPU is not always a stable one once PCIe and newer Intel chipsets enter the picture.

![Windows 98 running on the VBEMP display driver as a fallback](/img/dell-dimension-e520-windows-98-using-the-vbe-driver-as-a-fallback.jpg){: width="620"}

## The Good News: Voodoo 2 Looked Much Better

Unlike the OptiPlex 760, the Voodoo 2 results here were actually encouraging. **FastVoodoo 4.6** installed, Quake II, Unreal, and 3DMark all worked well, and Glide support looked strong enough to make the machine worth pursuing.

That is a big point in the E520's favour. A hybrid setup with VBE for 2D and Voodoo 2 for Glide is much more convincing than a pure PCIe Radeon-based Win98 plan.

I got a **3DMark 99 Max score of 4796** with the Voodoo 2 installed — a good sign the hybrid approach is more than just theoretically workable.

![3DMark 99 Max scoring 4796 with the Voodoo 2 installed](/img/dell-dimension-e520-windows-98-3dmark-99-max-score-with-voodoo-2.jpg){: width="620"}

## DOS

DOS on the E520 is surprisingly viable, but not effortless.

The biggest annoyance is laggy USB keyboard behaviour in native DOS. That is a recurring problem on some Dell systems of this era, and the E520 is made worse by the lack of easy rear-panel PS/2 or serial options.

Two routes I want to try:

1. unlock or flash the BIOS for better USB legacy support
2. explore the motherboard header pads for a serial or PS/2-style input solution

Sound is also more of a workaround story than a clean period-correct one, but **SBEMU** looks like a practical option when dedicated DOS-friendly sound hardware is not available.

Even without a lot of polishing, though, the machine already looked fast and interesting for software-rendered DOS games.

![Doom running in native DOS mode on the E520](/img/dell-dimension-e520-doom-running-in-dos-mode.jpg){: width="620"}

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
