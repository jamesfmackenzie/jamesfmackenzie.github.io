---
layout: post
title: Moonlight
summary: An open-source NVIDIA GameStream client that streams PC gameplay to whatever's under the TV — the fix for a Raspberry Pi not having the horsepower for GameCube or PS2 emulation.
date: '2025-11-26 23:35:00'
tags: [PC, Utilities]
---

Moonlight is an open-source client for NVIDIA's GameStream protocol. It streams gameplay from a PC to another device on the network — a [Raspberry Pi running RetroPie]({% link _software/retropie.md %}), in my case — so heavier emulation than the receiving device could ever run natively becomes playable on the living room TV.

That covers the gap RetroPie leaves on its own: PlayStation 2, GameCube, and Dreamcast emulation are all too much for a Pi to run directly, but stream fine from a proper PC over Moonlight. I first tried it running Dolphin over GameStream to an Apple TV for Mario Sunshine at 1080p60 — smooth, no noticeable latency, genuinely playable.

### Related on this site

- [Stream PC Games to your Raspberry Pi with GameStream and Moonlight]({% link _howto/how-to-stream-pc-games-to-retropie-with-gamestream-and-moonlight.md %})
- [RetroPie]({% link _software/retropie.md %})
