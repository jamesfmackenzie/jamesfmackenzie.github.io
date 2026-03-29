---
layout: post
title: Turn a Dell Dimension e520 into a Monster Retro PC
summary: A practical draft on turning the Dell Dimension e520 into a strong DOS, Windows 98, and Windows XP retro gaming machine.
tags: [DOS, PC Hardware, Retrogaming, Windows 98, Windows XP]
---

The Dell Dimension e520 is an unglamorous mid-2000s home PC, but it sits in a very interesting place for retro gaming. It is new enough to be fast, cheap, and easy to find, but still old enough to offer some surprisingly useful legacy behaviour.

## Why the e520 Is Interesting

The platform has a few standout traits:

- Intel `G965` / `ICH8`
- two PCI slots plus PCIe expansion
- SATA storage that can be made usable under Windows 98
- a BIOS **OS Install** mode that limits memory to 256MB

That last point is especially useful, because too much RAM is one of the quickest ways to make Windows 98 setup painful on newer systems.

## My Test System

The notes for this machine are based on a configuration with:

- Core 2 Duo `E4300`
- 3GB DDR2 RAM
- Intel HDA audio with a Sigmatel codec

## Windows 98

### Install Approach

The notes already point to a workable Win98 path:

- enable **OS Install** in BIOS
- prepare a FAT32 system disk
- use the usual Win98 install media
- apply the storage and memory patches where needed
- add the unofficial Intel INF files

Useful components mentioned in the notes:

- RLoew SATA patch
- optional RLoew PATCHMEM
- Lone Crusader Intel INF files

### Disk Access Problems

The big complication on this build is not just installation, but stability after installation.

Observed behaviour:

- long black-screen pauses during boot
- repeated hangs during final setup
- system eventually loading, suggesting timeout or compatibility issues rather than a hard crash

One major finding was that disabling **32-bit disk access** made the machine behave much better, although at a performance cost.

That makes storage behaviour one of the core themes of this article.

### Graphics

The onboard route is not the point here. The interesting part is how add-in cards behave.

The notes suggest:

- Radeon X600 and X700 cards were unstable under Catalyst on this machine
- VBEMP drivers gave a usable fallback with better colour depth and resolution
- Quake II in software mode already ran very well

That makes the e520 a useful example of a machine where "period-correct supported GPU" is not the same thing as "stable GPU."

### Voodoo 2

Unlike the OptiPlex 760, the Voodoo 2 notes here are actually promising:

- FastVoodoo 4.6 installed
- Quake II, Unreal, and 3DMark reportedly worked well

That is a strong point in the machine's favour and probably one of the best reasons to keep refining this build.

## Windows XP

Windows XP looks like the natural fit for the e520, and the final article should likely make that explicit. The hardware is much more comfortable there than it is under Windows 98.

## DOS

DOS on the e520 is surprisingly viable, but not effortless.

### Keyboard Issues

The major annoyance is laggy USB keyboard behaviour in native DOS.

Possible routes from the notes:

1. unlock or flash the BIOS for better USB legacy support
2. add a serial header and build around alternate input options

### Performance

Even without a lot of tuning, DOS performance is already interesting on this class of hardware.

The final post should preserve the practical angle:

- which games ran well
- what input problems appeared
- how much effort it took to get a satisfying DOS experience

## What the Final Version Should Add

- a cleaner hardware table
- a tighter explanation of the Windows 98 disk-access issue
- which graphics cards are worth trying first
- a verdict on whether the e520 is best thought of as a hybrid DOS/XP machine with partial Win98 support
