---
layout: post
title: Amstrad PC1640 Notes
summary: Restoring a childhood Amstrad PC1640 — hardware, GEM, video modes, an XTIDE saga, and getting files off a dying hard drive.
tags: [Amstrad, PC, Retrocomputing]
---

This Amstrad PC1640 was a childhood PC of mine. Years later, I wanted to get it working again.

This is intended as one big reference-style post collecting the most useful PC1640 notes in one place — restoration, GEM, video modes, storage — rather than lots of small scattered articles. If a specific subtopic turns out to be interesting enough on its own, it can get broken out into its own post later.

See also the companion [hardware reference page]({% link _hardware/amstrad-pc1640.md %}), and the related post on [CGA gaming on an MDA monochrome monitor]({% post_url 2025-08-17-cga-gaming-on-an-mda-ttl-monochrome-monitor-with-the-ati-graphics-solution-sr-amstrad-pc1640 %}), which covers the ATI Graphics Solution SR card in more depth.

## The short version

Bought hardware for it — notably an XT-IDE adapter, and later an ATI Graphics Solution SR card — and got it working again. The rest of this post is the detail behind that.

## History and hardware overview

<!-- TODO: model background, IBM PC-compatible history, model variants, floppy/hard drive configurations, mouse and joystick support, monochrome vs. colour display behaviour — not yet written up -->

**My model:** the mono version. <!-- TODO: photos -->

One useful point already known: the monochrome display defaults to a Hercules-style mode, and games won't display unless they specifically support Hercules or another suitable monochrome mode. The adapter can also emulate EGA on the monochrome display, though — worth demonstrating visually (show it working, then switching the physical switches across to simulate EGA mode).

## Software: GEM

<!-- TODO: what shipped with the machine, how usable GEM still feels, running applications like Timeworks Publisher -->

To install GEM, edit the `assign.sys` file (in the GEM sys directory) to change the graphics mode.

## Disassembly and restoration

<!-- TODO: disassembly instructions, cleaning/restoration work actually done -->

DOS and GEM floppy images (and a BIOS program) are available from [DOS Days](https://www.dosdays.co.uk/computers/Amstrad%20PC1000/software/download.php) if installing from original media isn't an option.

## Copying files off a dying hard drive

The hard drive on this particular machine started failing — file allocation table errors — which pushed file recovery and storage workarounds to the top of the priority list. Bought a spare PC just to receive the files.

**What worked:** a serial cable, using Kermit for the transfer (XMODEM also works), with Procomm as the client software on the PC side.

<!-- TODO: exact cable type, terminal settings, which software runs on the Amstrad side, typical transfer speed/reliability -->

## Installing XTIDE

Bought the TexElec-manufactured [Lo-tech XT-CF adapter]({% link _hardware/lo-tech-xt-cf.md %}) — BIOS comes pre-installed. Getting it actually booting from a modern CF card turned into a proper saga: four failed attempts before a DOS 5 floppy booted over `serdrive` (part of [XTIDE Universal BIOS]({% link _software/xt-ide.md %})) finally cracked it. Full story, including the exact recipe and the gotcha with the original MFM controller, over on [Getting XTIDE Working on the Amstrad PC1640]({% post_url 2026-09-04-getting-xtide-working-on-the-amstrad-pc1640 %}).

## Future hardware wishlist

The PC1640 has four 8-bit-only ISA expansion slots (no 16-bit AT support), which conveniently matches most of the current hobbyist ISA reproduction-hardware scene — PicoGUS, PicoMem, Graphics Gremlin, and similar projects are all designed around 8-bit ISA/XT-bus compatibility as their baseline. <!-- TODO: pull in the specific shortlist from the vault project note once it's worth writing up as its own section — currently a long reference list rather than blog-ready prose -->

## References

- [PCem emulator forum thread](http://pcem-emulator.co.uk/phpBB3/viewtopic.php?t=3402)
- [reenigne's GEM notes](https://www.reenigne.org/blog/gem/)
- [WinWorld PC — GEM 3.x archive](https://winworldpc.com/product/gem/3x)
- [minuszerodegrees.net's XTIDE/Serial Drive writeup](https://www.minuszerodegrees.net/xtide/Serial%20drive/Serial%20drive.htm)
- [XTIDE Universal BIOS wiki — Serial Drives](https://www.xtideuniversalbios.org/wiki/SerialDrives)

## Still to do

- Photos: the machine itself, disassembly steps, GEM running in different video modes.
- Write disassembly/restoration and hardware/software overview sections from real experience — currently placeholders.
- Decide whether the file-transfer section deserves its own dedicated post too, the way the XTIDE saga did.
