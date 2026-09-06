---
layout: post
title: ITX Llama
summary: My take on the ITX Llama, an open-source ITX motherboard built from scratch for real DOS and early Windows gaming — no emulation involved.
date: '2024-08-29 11:33:00'
tags: [Computers, PC]
---

![My ITX Llama, with the OPL3 module, a Raspberry Pi for MT-32, a D1 Mini Wi-Fi modem, and a Noctua fan fitted](/img/hardware/itx-llama.jpg){: width="680"}

The ITX Llama is not a repurposed old PC — it's a brand new motherboard, designed from scratch, purely to run real MS-DOS and early Windows (95/98) games on real x86 hardware. No emulation, no compromise. I picked one up through a community group buy and it's become one of my favourite pieces of retro hardware.

### What it is

At the core is a Vortex86EX system-on-module — an x86-compatible CPU that behaves roughly like a Pentium/Pentium MMX, selectable from about 60 to 500MHz.

![The DM&P SOM-128-EX module the ITX Llama is built around](/img/hardware/som-128-ex.png){: width="420"}

It's paired with 128MB of DDR3 on the module itself, a Crystal CS4237B audio chip (AdLib, Sound Blaster Pro 2, and Windows Sound System compatible), a single 3.3V-keyed AGP-format slot (electrically PCI at 66MHz), and the full set of legacy PC I/O: PS/2, RS-232 serial, gameport/MIDI, and USB 2.0. Internally there are headers for a real Yamaha OPL3 module, a Wave Blaster wavetable daughterboard, and a Raspberry Pi. It boots from SD card, SATA, or USB. The whole project is open source — schematics, board files, and BIOS are all published, and boards have circulated through community group buys rather than a normal retail channel.

### Why I like it

- it runs actual DOS and Windows 9x on real x86 silicon, not an emulator
- a single AGP-format slot — electrically it's PCI at 66MHz — that takes genuine period cards like a Voodoo3 or Radeon 9200
- the onboard Crystal CS4237B covers AdLib and Sound Blaster Pro 2 with a good built-in OPL3-compatible synth — and there's a header for a real-Yamaha-chip OPL3 module if you want 100% authentic FM
- for MIDI there's a Wave Blaster header for a [wavetable daughterboard]({% link _hardware/dreamblaster-x2gs.md %}), plus an onboard Raspberry Pi header — seat a Pi Zero 2 running mt32-pi and you get both Roland MT-32 and SoundFont (General MIDI) synthesis, with no separate interface needed
- it's small enough to disappear next to a modern PC, unlike a full-size vintage tower

### My take

For DOS gaming specifically, this is about as close to "just works" as modern retro hardware gets. Sound Blaster and AdLib support are there from the start, timing behaves the way real period hardware behaves, and the AGP slot means you're not stuck with onboard graphics. Windows 98 runs too, though it's the DOS side where the board really shines.

### Pros

- real hardware, not emulation — no chasing down obscure timing or driver quirks
- genuinely good audio out of the box, with a path to real OPL3, wavetable, and MT-32 if you want it
- the AGP-format slot takes real period graphics cards
- open-source design, so it isn't tied to one supplier

### Cons

- only available through community group buys, not a normal retail purchase
- early boards had some analog audio downmixing quirks — worth checking which revision you're getting
- the slot runs in PCI mode, so not every AGP card will work — stick to known-good ones

### Related on this site

- [ITX Llama: A Brand New PC for 1990s DOS Games!]({% post_url 2024-09-07-itx-llama-a-brand-new-pc-for-dos-retro-games %})
- [ITX Llama Part 2: A Sonic Supercharge]({% post_url 2024-09-21-adding-raspberry-pi-to-the-itx-llama-for-a-roland-mt32-sonic-supercharge %})
- [There is a New Group Buy for ITX Llama]({% post_url 2024-10-14-there-is-a-new-group-buy-for-itx-llama %})
