---
layout: post
title: Yamaha YMF724
summary: My take on the Yamaha YMF724 — the PCI sound card I trust most for DOS compatibility, with superb XG MIDI under Windows.
date: '2024-08-29 11:33:00'
tags: [PC, Sound, Sound Cards, Yamaha]
hero: yamaha-ymf724.jpg
hero_alt: The Yamaha YMF724 card I bought — listed on eBay only as a "DCS S81X-SF CARD"
---

The Yamaha YMF724 is one of my favourite retro-PC bargains. I found mine on eBay for `$20` in February 2022, listed only as a "DCS S81X S817 S81X-SF CARD" — the seller clearly had no idea it was a sought-after Yamaha card. I could just make out the chips in the listing photo and took the risk. It paid off: proper eBay bargains still exist if you pay attention.

### What it is

Part of Yamaha's YMF7x4 family of PCI sound chips. What makes these cards special for retro use is a rare combination: real Yamaha FM synthesis, easy Windows support, and unusually good DOS compatibility for a PCI card — the thing most PCI audio simply can't do.

### Why I like it

- it gets you strong DOS audio without needing an ISA slot
- **DSDMA** keeps DOS sound working on surprisingly modern hardware, where most PCI cards fall apart entirely
- Windows support is straightforward
- the MIDI is a genuine highlight

### My take

This is the most DOS-compatible PCI sound card I've used. DSDMA support is the headline — it got native DOS audio working on an ICH7 machine, which is well past where I'd expect a PCI card to still function. The MIDI side surprised me too: General MIDI already sounds good, but **XG MIDI** sounds fantastic on this card. The shame is that so little software targets XG, because when you do hear it properly it's a real highlight.

I reach for a YMF724 before a [Sound Blaster Live!]({% link _hardware/creative-labs-sound-blaster-live.md %}) whenever DOS compatibility is the priority. It's the card I fitted in my [OptiPlex 380 retro build]({% post_url 2025-12-28-the-ugly-dell-optiplex-that-became-my-dream-retro-gaming-pc %}).

### Pros

- the best DOS compatibility I've seen from a PCI sound card
- DSDMA keeps DOS sound alive on quite modern machines
- real Yamaha FM synthesis
- easy Windows support, and XG MIDI sounds superb

### Cons

- General MIDI in DOS is the weak point — it only really works under Windows
- XG MIDI is wonderful but barely any software uses it

### Related on this site

- [Yamaha YMF724F sound card has arrived — trying to get DOS sound working on an ICH7 southbridge]({% post_url 2022-02-26-yamaha-ymf724-pci-sound-card-has-arrived %})
- [The Ugly Dell That Became My Dream Retro Gaming PC]({% post_url 2025-12-28-the-ugly-dell-optiplex-that-became-my-dream-retro-gaming-pc %})
- [Creative Labs Sound Blaster Live!]({% link _hardware/creative-labs-sound-blaster-live.md %})
- [Dell OptiPlex 380]({% link _hardware/dell-optiplex-380.md %})
