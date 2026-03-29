---
layout: post
title: XTIDE Notes
summary: A practical working draft on getting XTIDE and CompactFlash storage booting on an older PC, including the failures along the way.
tags: [DOS, PC Hardware, Retrocomputing, XTIDE]
---

This draft is meant to become one large practical XTIDE article first, with smaller spin-off posts later if needed.

## Candidate Subtopics

- preparing a CF card
- using Serial Drive
- common XTIDE boot problems

## Hardware and Starting Point

The notes are based on a **TexElec XTIDE** board with the BIOS already installed.

The goal was simple:

- use a CF card as storage
- get the machine to boot reliably
- use Serial Drive where necessary to get around floppy and install limitations

## What Did Not Work

The failed steps are useful because they show where the traps are.

### First Attempt

- wrote a bootable OS image to a 64MB CF card with Rufus
- machine got stuck at `Booting C>>C`

### Second Attempt

- booted DOS 3.3 from floppy
- used `fdisk` and `format /s`
- drive became visible and usable after booting from floppy
- but native boot still failed

### Another Useful Finding

`fdisk /mbr` fixed the `Booting C>>C` hang, but then the system fell into a different failure:

- `Boot sector not found`

That suggests several issues can masquerade as "XTIDE does not work" when the real problem is the partition or boot record state.

## Serial Drive Notes

Serial Drive turned out to be important, but not entirely straightforward.

- it was not included in the latest Universal IDE binaries being used
- an older copy had to be found separately
- booting DOS over serial was still useful for repair and setup work

## What Ultimately Worked

The notes already contain a strong final recipe:

1. Install XTIDE in the PC1640
2. Get Serial Drive working
3. Use a USB serial adapter plus null modem
4. Boot a DOS 5 floppy image over serial
5. Run `fdisk /mbr`
6. Partition the CF card with `fdisk`
7. Run `format c: /u /s`
8. Reboot and confirm the card boots normally

That is the core of the finished article.

## Other Useful Findings

- smaller cards may be easier to work with, depending on DOS version and geometry limits
- DOS 3.3 has file system limits that affect cylinder choices
- DOS 6.22 did not behave as cleanly as hoped in this setup
- the original MFM controller and XTIDE may conflict, preventing the XTIDE BIOS from loading

## What the Final Version Should Add

- exact Serial Drive version and source
- clearer explanation of the `Booting C>>C` and boot sector failures
- a note on why DOS 5 worked better here
- slot order and MFM controller behaviour in the PC1640
