---
layout: post
title: XT-IDE
summary: My notes on the XT-IDE — an 8-bit ISA adapter that gives pre-AT PCs modern IDE and CompactFlash storage — including the boot problems I hit and the recipe that finally worked.
date: '2024-08-29 11:33:00'
tags: [PC, Storage Devices]
---

The XT-IDE is an 8-bit ISA storage adapter for early PCs. Original XT-class machines predate the AT's built-in hard disk support, and their original MFM/RLL controllers and drives are now slow, noisy and failure-prone. An XT-IDE lets you connect a normal IDE drive — or, more usefully, a **CompactFlash card** — and boot from it, via the open-source **XTIDE Universal BIOS**.

Mine is the **TexElec** version, which ships with the BIOS already flashed.

### Getting it booting

Fitting the card is the easy part. Getting a machine to boot reliably from a fresh CF card took several attempts, and the failures are worth knowing about because they all *look* like "the XT-IDE doesn't work" when the real problem is elsewhere:

- **Rufus-written bootable image** → stuck at `Booting C>>C`
- **`fdisk` + `format /s` from a DOS 3.3 floppy** → drive usable once booted from floppy, but still no native boot
- **`fdisk /mbr`** → fixed the `Booting C>>C` hang, but then `Boot sector not found`

DOS version matters. DOS 3.3 has filesystem and geometry limits that force awkward cylinder choices; DOS 6.22 misbehaved in other ways here. **DOS 5** turned out to be the sweet spot.

### What finally worked

1. Install the XT-IDE in the machine
2. Get **Serial Drive** working (an older XTIDE Universal BIOS build — it was dropped from recent releases) using a USB-to-serial adapter and a null-modem
3. Boot a DOS 5 floppy image over serial
4. `fdisk /mbr` to clean up the master boot record
5. `fdisk` to partition the CF card
6. `format c: /u /s`
7. Reboot and confirm it boots from the card

### One gotcha

On a machine that still has its original MFM controller fitted — such as the [Amstrad PC1640]({% link _hardware/amstrad-pc1640.md %}) — the XT-IDE BIOS may not load at all. The two cards conflict, and it comes down to which one sits in the first ISA slot. Pull the MFM controller.

### Related on this site

- [Amstrad PC1640]({% link _hardware/amstrad-pc1640.md %})
