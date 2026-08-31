---
layout: post
title: Microvitec AKF50
summary: My take on the Microvitec AKF50 — an Acorn-era CRT that turned out to be a switching multisync doing both 15kHz and VGA, and a cheap alternative to a PVM.
date: '2024-08-29 11:33:00'
tags: [Monitors]
---

The Microvitec AKF50 is a 14" CRT monitor from Microvitec's range of Acorn-badged displays. I had one for years without realising quite what it was.

### The discovery

It turns out the AKF50 is a **switching / multisync** display: it locks to both **15kHz** (PAL/NTSC-rate RGB, as used by consoles and home computers) *and* standard **31.5kHz VGA**. Feed it a 15kHz RGB signal and it syncs; feed it VGA and it syncs to that too.

That makes it far more useful than a fixed-frequency monitor, and the picture quality is genuinely excellent — sharp, with clean scanlines on 15kHz material and no processing in the chain.

### Why it matters

PVMs and BVMs get all the attention in retro circles, and prices have climbed to match. A good multisync CRT like the AKF50 gets you most of the way there for a fraction of the cost:

- native 15kHz RGB, so no line doubling or deinterlacing
- VGA support as well, so it doubles as a period PC monitor
- strong scanline presentation straight out of the tube

A typical console chain is RGB SCART into a sync strike (or similar) to clean up and break out the signal, then straight into the monitor.

### Related on this site

- [Microvitec AKF50 – a 15kHz/VGA switching multisync CRT]({% post_url 2021-12-31-microvitec-akf450-15khz-multisync-switching-monitor-pvm-bvm %})
- [Acorn Archimedes]({% link _hardware/acorn-archimedes.md %}) — the machine this monitor was made for
