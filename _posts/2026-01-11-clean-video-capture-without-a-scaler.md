---
layout: post
title: "Capturing Native-Resolution Video Without a Scaler"
date: '2026-01-11 15:10:00:00'
summary: |-
  You don't need a RetroTINK or Framemeister to get sharp, native-resolution capture of a classic computer — with a good capture card and deliberate post-processing, you can reconstruct the original pixel grid yourself.
tags: [Posts, Video Capture]
image: micomsoft-sc-512n1-l-dvi-capture-card.jpg
---

![Micomsoft SC-512N1-L/DVI Capture Card](/img/micomsoft-sc-512n1-l-dvi-capture-card.jpg)

Good capture of a classic computer usually means an external scaler — a RetroTINK or a Framemeister sitting in the signal chain. Those are excellent devices. But for documenting Atari ST video I wanted something a scaler doesn't really give you: the *exact* original pixel grid, reconstructed deliberately, with every scaling step under my control.

It turns out you can do that with just a capture card and some careful post-processing. This is the workflow I settled on, using an Atari Mega ST as the example — its native resolution is 320×200, but the same approach works for other classic machines.

For the card itself, see my notes on the [Micomsoft SC-512N1-L/DVI]({% link _hardware/micomsoft-sc-512-n1-l-dvi-pci-e-capture-card.md %}).

### The idea: do the scaler's job in software

A scaler does three things: it samples the analogue signal, works out the active image area, and scales that cleanly to a modern resolution. Split those apart and you can do each one deliberately — the capture card samples, and software handles the framing and scaling, using only integer operations so the source pixels are never resampled or blurred.

The output is native-resolution, free of the softness and ringing an analogue chain introduces, and sized for a modern platform (1080p50 or 1080p60).

### Hardware

- **Atari Mega ST**
- **Atari ST RGB SCART cable** (Retro Computer Shack)
- **ArcadeForge Sync Strike** — extracts clean sync from the ST's RGB output
- **Micomsoft SC-512N1-L/DVI** capture card — samples low-resolution analogue video without forcing its own scaling or filtering

### Software

Both free and well established:

- **<a href="http://www.amarectv.com/english/amarectv_e.htm" target="_blank">AmaRecTV Live</a>** — captures uncompressed video
- **<a href="http://www.virtualdub.org/" target="_blank">VirtualDub</a>** — does the deliberate, step-by-step scaling

### The workflow

Raw analogue RGB to clean native-resolution output:

1. Capture uncompressed in **AmaRecTV** at **288p50**, **720 pixels per line sampled**.
2. Upscale to **1280×288** with **Lanczos3** — more horizontal precision before cropping.
3. Crop to **960×200** — isolates the active Atari ST display area.
4. Divide width by **3** with **Nearest Neighbour** — restores the original **320×200** grid.
5. Multiply width and height by **5** with **Nearest Neighbour** — **1600×1000**, perfect integer scaling.
6. Frame into **1920×1080** (1080p50) — no fractional scaling.
7. Compress with **H.264**.

From step 4 on, everything is integer-only — no filtering or resampling touches the source pixels. Oversampling horizontally during capture (step 1) is what makes it possible to recover exact pixel boundaries later.

### Example captures

Three clips produced with this workflow, embedded from unlisted uploads.

#### Atari ST GEM desktop

Good for judging line sharpness, font clarity, and pixel alignment.

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/juoKlq_RCYw?rel=0" allowfullscreen class="youtube-video"></iframe>
</div>

#### Loom (Lucasfilm Games)

Dithered gradients and fine detail that benefit from clean sampling.

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/hBIWsdJ2jz0?rel=0" allowfullscreen class="youtube-video"></iframe>
</div>

#### Xenon 2 (Bitmap Brothers)

High-contrast pixel art, fast scrolling, steady 50Hz motion — a good stress test.

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/LBQ5VUifQSg?rel=0" allowfullscreen class="youtube-video"></iframe>
</div>

### Is it worth it over a scaler?

For live use or a multi-system setup, no — a scaler is the right tool. But if you're capturing for archival or documentation, this gets you native-resolution ST video that's sharp, accurate, and faithful to the hardware, with nothing in the chain making decisions you can't see.
