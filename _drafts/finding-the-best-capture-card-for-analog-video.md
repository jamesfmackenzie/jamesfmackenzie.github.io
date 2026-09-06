---
layout: post
title: Finding the Best Capture Card for Analog Video
summary: Why I went looking for a capture card built for video walls and broadcast, rather than retro gaming — and ended up with a pair of Datapath VisionAV-HD cards.
tags: [PC, Retrogaming, Video Capture]
---

![Datapath VisionAV-HD capture card](/img/datapath-visionav-hd.jpg)

I wanted a way to capture video from old analog consoles — SNES, PlayStation, PS2, that whole era — and from PCs too, without landing on either side of a bad tradeoff: an expensive dedicated scaler, or a cheap modern capture card that only understands digital HDMI. What I actually needed was the best of both eras in one device: real support for legacy analog modes (VGA, SVGA, 240p, 480i, 480p) alongside the more modern digital ones (720p, 1080i, 1080p).

### The research

Digging around, one brand kept coming up with genuinely specific, credible praise from the retro-capture community — not vague "good reviews," but dedicated coverage: **Datapath**.

- [RetroRGB's review](https://retrorgb.com/datapath-visionav-hd-true-hdmi-480i-passthrough.html) is built specifically around the VisionAV-HD's 480i capture quality — exactly the kind of legacy mode most modern capture hardware botches. RetroRGB also maintains a whole [Datapath tag](https://retrorgb.com/tag/datapath) and a [direct-capture setup guide](https://retrorgb.com/datapathcapture.html), the kind of ongoing dedicated coverage that signals a card the community has actually standardized on.
- [Nerdly Pleasures](http://nerdlypleasures.blogspot.com/2019/02/ideal-analog-retro-video-capture-with.html) independently lands on the same Datapath card family as the serious answer for analog retro capture.

One honest caveat surfaced by that same research: these cards were originally built for video walls and commercial AV installs, not retro gaming. That means direct 240p capture has real quirks — it needs precise phase configuration to get clean results, so it's not quite plug-and-play for that specific mode, even though the output is excellent once it's set up.

### What I bought

Two [Datapath VisionAV-HD]({% link _hardware/datapath-visionav-hd.md %}) cards. Each one actually has **three** independent, simultaneous capture inputs, not two as I first assumed: two HD-capable DVI-I inputs (each handling HDMI, DVI, RGB, or analog Component/YPbPr directly over the DVI-I connector) plus a third, separate composite video input for standard-def sources. Confirmed spec: resolutions up to 4096×4096, and up to 1080p60 on the HD inputs.

The two DVI-I inputs are the flexible ones — a simple adapter gets VGA or component video into them, since DVI-I already carries the analog RGB/component signal directly, just via a different connector shape. With two cards, that's up to four independent HD inputs total — which is exactly what made capturing [three PlayStation 2s into one combined feed]({% link _projects/gran-turismo-3-on-multi-monitors.md %}) possible.

A nice bit of bargain-hunting along the way: I found these cheap specifically because they were missing their PCIe bracket — the metal I/O plate that normally holds the connectors in place at the back of the case. No bracket makes a card look incomplete to most buyers, which knocked the price down, but it's a purely cosmetic mounting problem, not a functional one. Replacement brackets were easy and cheap to source elsewhere, and I screwed them on myself — a genuinely good deal as a result.

### The verdict

They work amazingly well, and the bundled software is solid. Used successfully for the [Gran Turismo 3 multi-screen capture]({% link _projects/gran-turismo-3-on-multi-monitors.md %}), combining three PS2 feeds into one seamless ultra-widescreen picture.

Two honest caveats worth flagging, so this reads as a real review and not an ad: per RetroRGB's testing, the audio capture is fine for streaming or webcam-style use but not quite archival grade — worth capturing audio separately if that level of quality matters for a specific project. And as mentioned above, the video-wall heritage means 240p specifically needs careful phase tuning rather than working out of the box.

More details on the card itself — full spec table, the same caveats, and more — are on the [hardware page]({% link _hardware/datapath-visionav-hd.md %}).
