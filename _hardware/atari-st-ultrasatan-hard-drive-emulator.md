---
layout: post
title: Atari ST UltraSatan
summary: My take on the UltraSatan, an SD-card hard drive replacement for the Atari ST that connects to the ACSI port — bulk storage for a whole game library, and a fast way to load files from a PC.
date: '2024-08-29 11:33:00'
tags: [Atari ST, Peripherals, Storage Devices]
---

The UltraSatan is a hard disk replacement for the Atari ST that stores everything on SD cards. It connects to the ST's ACSI port and, once set up, behaves like a set of hard drive partitions — but with no moving parts, no noise, and cards you can pull out and read on a modern PC.

### What it is

The unit takes one or two SD cards and needs only a micro-USB power supply (a phone charger will do). On the ST side you install hard disk drivers and a partitioner — I used **Peter Putnik's "PP" drivers**, which bundle both, along with a ready-made SD card image to get you booting without a floppy.

### As storage

This is the main reason to fit one. An 8 GB SD card is effectively the perfect size: the ST supports up to 14 partitions, and at ~510 MB per partition (255 MB on TOS 1.02 and earlier) that fills the card almost exactly. That is more than enough room for a complete game and application library, always available at the desktop.

### As a transfer method

Because the partitions are formatted as GEMDOS drives, the same SD card mounts on a PC. Pull the card, drag files onto it in Windows, put it back in the UltraSatan, reboot the ST and the files are there. It is the fastest transfer method available — you are only limited by how quickly the PC writes to the card — and it needs no working floppy drive at either end.

### Pros

- silent, solid-state bulk storage for the whole library
- doubles as the fastest PC-to-ST file transfer route
- no floppy drive required

### Cons

- more expensive than the cable-based transfer options
- initial setup (imaging, partitioning, installing drivers, re-adding drive letters in GEM) takes some patience

### Related on this site

- [Using SD Card / UltraSatan to Transfer Files from PC to ST]({% link _howto/how-to-use-ultrasatan-sd-card-to-transfer-files-from-pc-to-st.md %})
- [Transferring Files from PC to ST]({% link _howto/how-to-transfer-files-from-pc-to-atari-st.md %})
- [Atari ST]({% link _hardware/atari-st.md %})
- [Atari ST NetUSBee]({% link _hardware/atari-st-netusbee-usb-ethernet-adapter.md %})
