---
layout: post
title: Homebrew 8088
summary: My Homebrew 8088 — a modern single-board PC/XT that drops straight into an ATX case and an 8-bit ISA backplane.
date: '2024-08-29 11:33:00'
tags: [Computers, PC]
---

The Homebrew 8088 is a genuinely new 8088 PC — a single-board computer built to fit a standard ATX case, rather than a restored original. Mine came assembled, bought directly from Elijah Miller (EMM Computers, homebrew8088.com).

### What it is

An 8088 PC on a card: an 8MHz 8088 CPU, 640KB of RAM, an 8237 DMA controller, and a PS/2 keyboard port, built around its own motherboard design rather than a repurposed original. It's sold in a few versions with different numbers of ISA slots, and mine plugs into an existing 8-bit ISA backplane I already had — 16-bit cards won't work on it, only 8-bit ones.

### Getting it running

A few real gotchas from setting mine up:

- **-5V rail**: ATX power supplies don't usually provide the -5V rail some ISA cards expect. [Phil's Computer Lab's Voltage Blaster](https://www.philscomputerlab.com/voltage-blaster--5v.html) is the fix if a card needs it.
- **Floppy/serial**: a generic multi-I/O card works fine, even a 16-bit one — they're reverse-compatible with the 8-bit bus. One catch: only 720K floppy disks work, not 1.44MB.
- **Storage**: I paired it with a [USB ISA storage card]({% link _hardware/usb-isa-storage-card.md %}), also from Elijah, rather than an XT-IDE/CF setup.

Elijah was genuinely helpful throughout — recommending his own USB storage card over alternatives like the PicoMEM (which he hadn't tested himself and had heard of reliability issues with) or CF adapters, and pointing me at his own reference videos for compatibility.

### Related on this site

- [USB ISA Storage Card]({% link _hardware/usb-isa-storage-card.md %})
- [Lo-tech XT-CF]({% link _hardware/lo-tech-xt-cf.md %})
