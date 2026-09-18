---
layout: post
title: AVerMedia GC573 Live Gamer 4K
summary: Hardware overview of the AVerMedia GC573 Live Gamer 4K, a reliable PCIe capture card for 4K60 and high-frame-rate video capture.
date: '2024-08-29 11:33:00'
tags: [PC, Video Capture]
---

Most of my capture work is retro — analog signals, unusual sync, cards that need real troubleshooting to get right. The GC573 is the opposite of that: a modern HDMI capture card that's just supposed to work, and does.

### What it is

The GC573 is an internal PCIe card for capturing HDMI sources: 4K60 with HDR10, and high-frame-rate modes up to 1440p144 or 1080p240. It connects over PCIe x4 rather than USB, and passes signal through with no added lag, so a display can stay connected downstream of it.

### Specifications

- **Interface:** PCIe x4
- **Capture:** up to 4K60 with HDR10
- **Passthrough:** 2160p60 HDR / 1440p144 / 1080p240
- **Recording bitrate:** 150–240 Mbps

### Where it fits

This is the card I reach for when the source is modern — a current console, a PC, anything HDMI-first — rather than the [Micomsoft SC-512N1-L/DVI]({% link _hardware/micomsoft-sc-512-n1-l-dvi-pci-e-capture-card.md %}) I use for older analog and retro-console capture. The two do different jobs: the Micomsoft earns its keep on awkward analog and sync edge cases, and the GC573 is what I use when I just want a clean, dependable HDMI capture without a fight.

### Pros

- reliable 4K60 HDR capture with no added passthrough lag
- handles high-frame-rate 1440p/1080p sources well
- internal PCIe card — no USB bandwidth or driver quirks to fight

### Cons

- HDMI-only — no help with analog or older retro sources
- needs a free PCIe slot, unlike a USB capture box

### Related on this site

- [AVerMedia Live Gamer 4K – Cheap and Reliable 4K60 Video Capture]({% post_url 2022-11-06-avermedia-gc573-live-gamer-4k-4k60-video-capture-card %})
- [Micomsoft SC-512N1-L/DVI]({% link _hardware/micomsoft-sc-512-n1-l-dvi-pci-e-capture-card.md %})
