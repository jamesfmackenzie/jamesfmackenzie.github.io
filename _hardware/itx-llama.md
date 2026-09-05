---
layout: post
title: ITX Llama
summary: My take on the ITX Llama, an open-source ITX motherboard built from scratch for real DOS and early Windows gaming — no emulation involved.
date: '2024-08-29 11:33:00'
tags: [Computers, PC]
---

![](/img/hardware/som-128-ex.png)

The ITX Llama is not a repurposed old PC — it's a brand new motherboard, designed from scratch, purely to run real MS-DOS and early Windows (95/98) games on real x86 hardware. No emulation, no compromise. I picked one up through a community group buy and it's become one of my favourite pieces of retro hardware.

### What it is

At the core is a Vortex86EX system-on-module — an x86-compatible CPU that behaves roughly like a Pentium/Pentium MMX, selectable from about 60 to 500MHz. It's paired with 128MB of DDR3 on the module itself, a Crystal CS4237B audio chip (Sound Blaster Pro 2, AdLib, and Windows Sound System support out of the box), a 3.3V-keyed AGP slot via a PCIe-to-AGP bridge, and the full set of legacy PC I/O: PS/2, RS-232 serial, gameport/MIDI, and USB 2.0. It boots from SD card, SATA, or USB. The whole project is open source — schematics, board files, and BIOS are all published, and boards have circulated through community group buys rather than a normal retail channel.

### Why I like it

- it runs actual DOS and Windows 9x on real x86 silicon, not an emulator
- the AGP slot works with genuine period graphics cards, not just PCI ones
- the audio setup is properly authentic: real AdLib FM and Sound Blaster Pro 2 compatibility, plus a header for a genuine Yamaha OPL3 module if you want to go further
- the MIDI header let me add Roland MT-32 support with nothing more than a Raspberry Pi and [PI-MIDI]({% link _hardware/pi-midi.md %}) running mt32-pi
- it's small enough to disappear next to a modern PC, unlike a full-size vintage tower

### My take

For DOS gaming specifically, this is about as close to "just works" as modern retro hardware gets. Sound Blaster and AdLib support are there from the start, timing behaves the way real period hardware behaves, and the AGP slot means you're not stuck with onboard graphics. Windows 98 runs too, though it's the DOS side where the board really shines.

### Pros

- real hardware, not emulation — no chasing down obscure timing or driver quirks
- genuinely good audio out of the box, with a path to real OPL3 and MT-32 if you want it
- AGP support opens the door to real period graphics cards
- open-source design, so it isn't tied to one supplier

### Cons

- only available through community group buys, not a normal retail purchase
- early boards had some analog audio downmixing quirks — worth checking which revision you're getting
- AGP compatibility depends on 3.3V-keyed cards, so not every period GPU will fit

### Related on this site

- [ITX Llama: A Brand New PC for 1990s DOS Games!]({% post_url 2024-09-07-itx-llama-a-brand-new-pc-for-dos-retro-games %})
- [ITX Llama Part 2: A Sonic Supercharge]({% post_url 2024-09-21-adding-raspberry-pi-to-the-itx-llama-for-a-roland-mt32-sonic-supercharge %})
- [There is a New Group Buy for ITX Llama]({% post_url 2024-10-14-there-is-a-new-group-buy-for-itx-llama %})
- [PI-MIDI]({% link _hardware/pi-midi.md %})
