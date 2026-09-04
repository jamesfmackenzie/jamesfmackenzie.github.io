---
layout: post
title: XTIDE Universal BIOS
summary: My notes on XTIDE Universal BIOS — the open-source option-ROM that lets 8-bit ISA storage adapters boot modern CompactFlash and IDE storage on vintage PCs.
date: '2024-08-29 11:33:00'
tags: [MS-DOS, PC, Utilities, XTIDE]
---

XTIDE Universal BIOS is the open-source software that makes cards like the [Lo-tech XT-CF adapter]({% link _hardware/lo-tech-xt-cf.md %}) actually work. It's a BIOS extension — an option ROM, flashed onto the card itself — that teaches an 8-bit machine's BIOS how to see and boot from IDE and CompactFlash storage that didn't exist when the machine was designed.

### What it actually does

Without it, an XT-class BIOS has no concept of an IDE or CF drive at all. XTIDE Universal BIOS sits between the two: it intercepts the BIOS's disk-access calls, translates them for whatever adapter hardware it's running on, and adds things period BIOSes never had — LBA addressing, and support for cards and drive sizes far beyond what the original hardware's boot ROM ever anticipated.

It isn't tied to one specific card. The BIOS supports a range of "adapter types" — different ISA IDE/CF card designs, including the Lo-tech XT-CF family — set at flash time or via its own configuration tool.

### Serial Drive

The feature that mattered most for me was **Serial Drive**: it lets the BIOS mount a disk image held on a modern PC over a plain serial cable, and boot from it as if it were local. That solves the chicken-and-egg problem of setting up a fresh CF card on a machine with no other working boot device — you boot a known-good DOS image over serial first, then use *that* to partition and format the CF card properly. It's what got me out of a real dead end; see the [full story]({% post_url 2026-09-04-getting-xtide-working-on-the-amstrad-pc1640 %}).

One thing to know: Serial Drive support isn't included in every recent build — I had to track down an older release to get it.

### Related on this site

- [Lo-tech XT-CF]({% link _hardware/lo-tech-xt-cf.md %})
- [Getting XTIDE Working on the Amstrad PC1640]({% post_url 2026-09-04-getting-xtide-working-on-the-amstrad-pc1640 %})
- [Amstrad PC1640]({% link _hardware/amstrad-pc1640.md %})
