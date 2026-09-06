---
layout: post
title: PicoGUS
summary: My notes on PicoGUS — a modern Raspberry Pi Pico-based ISA card that gives old DOS PCs Gravis Ultrasound and Sound Blaster audio without vintage-hardware prices.
date: '2024-08-29 11:33:00'
tags: [PC, Sound, Sound Cards]
---

![](/img/posts/picogus-2-official.jpg)

{% include image-credit.html
  source_url="https://picogus.com/"
  source_label="PicoGUS official site"
  license_url="https://picogus.com/"
  license_label="Source"
%}

PicoGUS is a modern 8-bit ISA sound card built around the Raspberry Pi Pico's RP2040. Rather than being original 1990s hardware, it emulates period sound cards in software — Gravis Ultrasound, Sound Blaster, AdLib, Tandy, and more — with swappable firmware, so one cheap board can be whichever card a given game wants.

### What it does

The appeal is straightforward: original ISA sound cards, and Gravis Ultrasound cards especially, have become scarce and expensive. PicoGUS puts that capability back within reach for anyone building a DOS machine to actually use rather than to display, and because the firmware is swappable it covers a lot of ground from a single slot.

### Why I want one

It's on my shortlist for a future 8-bit ISA build. It's exactly the kind of modern hardware I like — it makes classic systems more usable instead of trying to replace them, and it keeps the hobby accessible rather than gated behind collector prices. I don't have one yet.

### Related on this site

- [USB ISA Storage Card]({% link _hardware/usb-isa-storage-card.md %})
- [8088 PC XT ISA Card SBC]({% link _hardware/8088-pc-xt-isa-card-sbc.md %})
- [ISA slot + Raspberry Pi GPIO = Gravis Ultrasound clone]({% post_url 2022-06-12-gravis-ultrasound-gus-clone-using-rasperry-pi %})
