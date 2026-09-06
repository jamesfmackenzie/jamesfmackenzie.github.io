---
layout: post
title: Micomsoft SC-512N1-L/DVI
summary: My take on the Micomsoft SC-512N1-L/DVI — a PCIe capture card that samples analog RGB cleanly enough to rebuild native-resolution retro video in software, no scaler required.
date: '2024-08-29 11:33:00'
tags: [PC, Video Capture]
---

![Micomsoft SC-512N1-L/DVI Capture Card](/img/posts/micomsoft-sc-512n1-l-dvi-capture-card.jpg)

The Micomsoft SC-512N1-L/DVI is a Japanese PCIe capture card that keeps coming up in retro-video circles for one reason: it samples low-resolution analog RGB without forcing its own scaling or filtering on the way in. That makes it a good starting point if you want to reconstruct a source's exact pixel grid in software rather than let a hardware scaler make those decisions for you.

### What it is

A PCIe card that captures analog RGB and component video as well as DVI and HDMI, plus composite for standard-def sources. A passive adapter gets VGA into it. The point of difference for retro use isn't a feature so much as an absence — it doesn't insist on cleaning up or rescaling what it captures.

### Why I use it

I paired it with an ArcadeForge Sync Strike and an Atari Mega ST to capture 288p50 at a high sample rate, then rebuilt the native 320×200 grid with integer-only scaling in software. The result is sharper and more faithful than most "budget" capture paths, and every scaling decision stays visible and repeatable. The full workflow is in [Capturing Native-Resolution Video Without a Scaler]({% post_url 2026-01-11-clean-video-capture-without-a-scaler %}).

It's not a plug-and-play scaler replacement — it still wants clean sync, decent cables, and deliberate post-processing. But for archival and documentation capture, where accuracy matters more than convenience, it earns its place.

### Related on this site

- [Capturing Native-Resolution Video Without a Scaler]({% post_url 2026-01-11-clean-video-capture-without-a-scaler %})
- [Raw Video Capture Experiments with a Micomsoft SC-512N1-L/DVI Capture Card]({% post_url 2016-01-30-raw-video-capture-experiments-with-micomsoft-sc-512n1-l-dvi-capture-card-and-atari-st %})
- [Datapath VisionAV-HD]({% link _hardware/datapath-visionav-hd.md %})
