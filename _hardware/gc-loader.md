---
layout: post
title: GC Loader
summary: My notes on the GC Loader — an optical drive emulator that replaces a GameCube's disc drive entirely and boots games straight off an SD card.
date: '2026-09-13 12:00:00'
tags: [Nintendo, Consoles, Peripherals]
hero: gc-loader-pnp-board.jpg
hero_alt: GC Loader PnP optical drive emulator board
---

The GC Loader, designed by Daniel Kraak, is an optical drive emulator (ODE) for the Nintendo GameCube. Rather than reusing the original drive's shell like some slot-loading ODEs, it replaces the entire physical drive assembly — motor, laser sled and all — with a small board that boots ISOs directly from an SD card.

### What it does

The board mounts onto the GameCube's original drive-bay shield bracket, in the space the optical drive used to occupy, using the drive's original ribbon/data connector footprint — no motherboard modification needed. Underneath, it's built around an ESP32-WROOM-32E module and a Trion T20F256 FPGA, with a micro SD slot and LAN1/OPT1 header rows for accessories. Once installed, the SD slot sits where a disc would normally go, accessible through the disc-lid opening.

It can boot ISOs directly on its own, but is commonly paired with **Swiss**, a homebrew loader/front-end, for a proper menu system and extras like forcing 480p on supported titles.

### Why I rate it

It's a clean, no-compromise way to retire an aging, failure-prone optical drive without giving up original hardware — the console still looks stock from the outside, and there's no drive belt or laser left to wear out. Losing the physical drive entirely (rather than reusing its shell) also means one less mechanically-worn part staying in the console.

### Pros

- no motherboard modification — mounts on the original drive-bay bracket via the stock connector
- removes the GameCube's most failure-prone original part (the optical drive) entirely
- boots straight from SD, with Swiss available as an optional front-end for extras like forced 480p

### Cons

- installation means fully removing and discarding use of the physical drive — not a reversible-in-seconds mod
- requires a security-bit driver, since GameCube case screws aren't standard Phillips

### Related on this site

- [Nintendo GameCube]({% link _hardware/nintendo-gamecube.md %})
