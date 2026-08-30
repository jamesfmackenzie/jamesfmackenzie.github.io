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

Bought the TexElec version — BIOS comes pre-installed. Getting it actually booting from a modern CF card turned into a proper saga.

**What didn't work, in order:**

1. Rufus, writing a bootable image straight to a 64MB CF card — stuck at "Booting C>>C".
2. Booting from a DOS 3.3 floppy, then `fdisk` + `format /s` on the CF card directly. DOS 3.3's filesystem limits meant capping the cylinder count low (200) — the card mounted and was usable once booted from floppy, but still wouldn't boot from the CF card itself.
3. `serdrive`, mounting a floppy over COM1 (not included in current XTIDE Universal BIOS builds — needed an older version), booting an MS-DOS 6.2 disk via serdrive, then `fdisk /mbr` — fixed the "Booting C>>C" hang, but produced a new error: "Boot sector not found".
4. A bigger 16GB CF card, `fdisk` via serdrive-booted DOS 6.22 to create a 2GB partition — `fdisk` worked, but DOS 6.22's `format` failed outright. Formatting the partition from Windows 10 succeeded, but produced a non-bootable partition.

**What finally worked:**

1. Install XTIDE in the PC1640's slot.
2. Download `serdrive`.
3. USB-to-serial cable, with a null modem adapter.
4. A DOS 5 boot floppy image.
5. Boot from serdrive.
6. `FDISK /mbr` to proactively fix any master boot record/boot sector issues on the CF card.
7. `FDISK` to partition the card.
8. `Format c: /u /s`.
9. Reboot to verify.

Useful hotkey: **Alt** searches COM ports for mounted serial drives.

One limitation found along the way: the Amstrad's original MFM hard drive and XTIDE can't be mounted concurrently — the XTIDE BIOS doesn't load when the MFM controller card is also connected. Seems to come down to whichever card sits in the first ISA slot.

Possible follow-up: try installing from the original Amstrad disk images instead of a generic DOS floppy — not attempted yet.

## Future hardware wishlist

The PC1640 has four 8-bit-only ISA expansion slots (no 16-bit AT support), which conveniently matches most of the current hobbyist ISA reproduction-hardware scene — PicoGUS, PicoMem, Graphics Gremlin, and similar projects are all designed around 8-bit ISA/XT-bus compatibility as their baseline. <!-- TODO: pull in the specific shortlist from the vault project note once it's worth writing up as its own section — currently a long reference list rather than blog-ready prose -->

## References

- [PCem emulator forum thread](http://pcem-emulator.co.uk/phpBB3/viewtopic.php?t=3402)
- [reenigne's GEM notes](https://www.reenigne.org/blog/gem/)
- [WinWorld PC — GEM 3.x archive](https://winworldpc.com/product/gem/3x)
- [minuszerodegrees.net's XTIDE/Serial Drive writeup](https://www.minuszerodegrees.net/xtide/Serial%20drive/Serial%20drive.htm) — good structural reference for a dedicated XTIDE post, if that ever gets split out.
- [XTIDE Universal BIOS wiki — Serial Drives](https://www.xtideuniversalbios.org/wiki/SerialDrives)

## Still to do

- Photos: the machine itself, disassembly steps, GEM running in different video modes.
- Write disassembly/restoration and hardware/software overview sections from real experience — currently placeholders.
- Decide whether XTIDE installation and/or file transfer deserve to be split into their own dedicated posts, now that there's real content for both.
