---
layout: post
title: Innovation i-Link 6 Port Hub
summary: My notes on the Innovation i-Link 6 Port Hub — a FireWire hub sold explicitly to link PlayStation 2s for Gran Turismo 3's hidden triple-screen mode, and one of the few accessories I own built around a single Easter egg.
date: '2026-09-14 22:00:00'
tags: [Peripherals, Sony PlayStation]
hero: innovation-i-link-6-port-hub-box.jpg
hero_alt: Boxed Innovation i-Link 6 Port Hub, marketed for Gran Turismo 3
---

Most FireWire hubs are generic — six ports, works with anything speaking i.LINK. This one isn't. The box says **PS2 compatible** right on the front, and the actual bullet point underneath it reads: "Use this Hub to connect up to 6 PS2 systems to play Gran Turismo 3 with up to 6 Players." It exists because of one hidden mode in one PlayStation 2 racing game.

### What it is

A 6-port i-Link/FireWire hub — compatible with standard i-Link and 4-pin IEEE 1394 cables, so nothing about the wiring itself is PS2-specific. Inside, it's built around a Texas Instruments **TSB41LV06A** FireWire hub/repeater chip, on a board marked `FWH-6T4`. It takes its own DC power input rather than running bus-powered off the FireWire lines, which matters for keeping six linked PS2s stable rather than relying on whichever console happens to be pushing power down the chain.

Opened mine up to confirm all of this rather than go on the box copy alone:

![The board, showing the TI TSB41LV06A hub chip](/img/i-link-hub-board-top.jpg){: width="600"}
![The underside of the board, marked FWH-6T4](/img/i-link-hub-board-bottom.jpg){: width="600"}
![A closer look at the TSB41LV06A chip itself](/img/i-link-hub-chip-closeup.jpg){: width="480"}

### Why I'm keeping notes on it

This is a genuinely obscure product — a PS2-era FireWire hub, explicitly branded for a single game's hidden multiplayer trick, with the actual chip inside it undocumented anywhere I could find. If you're trying to replicate [Gran Turismo 3's i.LINK Battle mode]({% link _projects/gran-turismo-3-on-multi-monitors.md %}) yourself and go looking for what's actually inside the box that makes it work, this is that information.

### Related on this site

- [How to Play Gran Turismo 3 Across Three Screens with Three PlayStation 2s]({% post_url 2026-09-14-how-to-play-gran-turismo-3-across-three-screens-with-three-ps2s %})
- [Gran Turismo 3 on Multi Monitors]({% link _projects/gran-turismo-3-on-multi-monitors.md %})
- [Sony PlayStation 2]({% link _hardware/sony-playstation-2.md %})
