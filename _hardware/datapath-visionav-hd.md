---
layout: post
title: Datapath VisionAV-HD
summary: A PCIe capture card built for video walls and broadcast, repurposed for the one job most modern capture cards can't do well — genuine legacy analog capture, from 240p up to 1080p.
date: '2026-09-06 00:00:00'
tags: [PC, Video Capture]
hero: datapath-visionav-hd.jpg
hero_alt: Datapath VisionAV-HD capture card
---

Most modern capture cards assume everything coming in is digital HDMI. That's a problem when the thing you want to capture is an SNES, a PS1, or a PS2 — genuine analog video, often in modes like 240p and 480i that budget capture hardware handles badly or not at all. Rather than buy an expensive dedicated scaler, I went looking at cards built for a completely different market.

### Why this card

Datapath cards kept coming up in the retro-capture community with specific, credible praise — not vague "good reviews" but dedicated coverage. [RetroRGB's review](https://retrorgb.com/datapath-visionav-hd-true-hdmi-480i-passthrough.html) is built around its 480i capture quality, and [Nerdly Pleasures](http://nerdlypleasures.blogspot.com/2019/02/ideal-analog-retro-video-capture-with.html) independently lands on the same card family as the serious answer for analog retro capture.

Worth knowing going in: these cards were designed for video walls and commercial AV installs, not retro gaming. Direct 240p capture has real quirks as a result — it needs precise phase configuration to get clean results, so it's not quite plug-and-play for that specific mode, even though the output is excellent once it's set up.

### Specifications

| Component | Details |
|---|---|
| **Inputs** | 3 independent, simultaneous capture channels: 2× HD-capable **DVI-I** (each handling HDMI, DVI, RGB, or analog Component/YPbPr directly) plus 1× **Composite Video** for standard-def sources |
| **Resolution** | Up to 4096×4096; up to 1080p at 60fps on the HD inputs |
| **Interface** | PCIe, full 16-lane physical connector, notched to fit x4/x8/x16 slots |
| **Audio** | Embedded HDMI audio capture, plus an optional AM2 module for balanced/unbalanced analog audio |

The two DVI-I inputs are the flexible ones — a simple adapter gets VGA or component video into them, since DVI-I already carries the analog RGB/component signal directly, just on a different connector.

### The verdict

It works genuinely well, and the bundled software is solid. Two honest caveats: per RetroRGB's testing, the audio capture is fine for streaming or webcam-style use but not quite archival grade — capture audio separately if that matters — and the video-wall heritage means 240p specifically needs careful phase tuning rather than working out of the box.

Mine, like most on the secondhand market, arrived without its PCIe bracket — the metal plate that holds the connectors in place at the back of the case. That's why these turn up cheap: it's purely a mounting part, not functional, and replacement brackets are easy to source.

### Related on this site

- "Finding the Best Capture Card for Analog Video" — my full writeup on choosing this card (drafted, not yet published — update this to a real link once it's out)
- [Micomsoft SC-512N1-L/DVI]({% link _hardware/micomsoft-sc-512-n1-l-dvi-pci-e-capture-card.md %})
- [Capturing Native-Resolution Video Without a Scaler]({% post_url 2026-01-11-clean-video-capture-without-a-scaler %})
- [Gran Turismo 3 in ULTRA WIDESCREEN (3 PS2s, 3 Screens!)]({% post_url 2025-03-08-gran-turismo-in-ultra-widescreen-triple-screen %})
