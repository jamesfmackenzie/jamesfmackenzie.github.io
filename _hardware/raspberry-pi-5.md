---
layout: post
title: Raspberry Pi 5
summary: My notes on the Raspberry Pi 5 — the single-board computer behind a native Half-Life 2/Portal build and a genuine modern GPU eGPU rig.
date: '2026-09-14 00:30:00'
tags: [Computers, PC]
hero: raspberry-pi-5-official-cooler.jpg
hero_alt: Raspberry Pi 5 with official Active Cooler attached
---

The Raspberry Pi 5 is the current flagship of the Raspberry Pi single-board computer line: a Broadcom BCM2712 (quad-core Cortex-A76 @ 2.4GHz) paired with a VideoCore VII GPU, PCIe 2.0 x1 exposed via an external FPC connector, and real gigabit Ethernet and USB 3.0 on board. Mine is the 4GB variant, fitted with the official Active Cooler (a small heatsink/fan/blower combo that clips directly onto the board) and powered by the official 27W USB-C supply.

### Why it keeps showing up here

The PCIe lane is the interesting part for a lot of what I've used it for — it's what makes plugging a real GPU into a Pi possible at all, and it's fast enough that the board can genuinely run native, non-emulated PC-era code rather than just retro emulation.

- Building Valve's Source Engine from source (via the [nillerusr/source-engine](https://github.com/nillerusr/source-engine) ARM64 fork) and running Half-Life 2 and Portal natively, no emulation involved — see [I Made Half-Life 2 Work on Raspberry Pi!]({% post_url 2024-10-19-i-made-halflife-2-half-life-2-work-on-raspberry-pi %}) and the [full how-to guide]({% link _howto/how-to-install-half-life-2-halflife-2-on-raspberry-pi.md %})
- Using that same PCIe lane, via an M.2-to-OCuLink adapter, to run a full desktop Radeon RX 580/RX 6600 XT as an eGPU — see [I Installed a Modern GPU on Raspberry Pi (and it's AWESOME!)]({% post_url 2024-11-17-i-installed-a-modern-radeon-rx-580-rx-6600-xt-gpu-on-raspberry-pi %})

### Where it fits

For anything that needs genuine PCIe bandwidth — an external GPU, fast storage — the Pi 5 is the first Raspberry Pi that actually makes that practical. For everything else it's still just a very capable, very cheap ARM Linux board: fast enough now that "can this run natively on a Pi" is a real question worth asking for surprisingly demanding PC software, not just retro consoles.

### Related on this site

- [I Made Half-Life 2 Work on Raspberry Pi!]({% post_url 2024-10-19-i-made-halflife-2-half-life-2-work-on-raspberry-pi %})
- [I Installed a Modern GPU on Raspberry Pi (and it's AWESOME!)]({% post_url 2024-11-17-i-installed-a-modern-radeon-rx-580-rx-6600-xt-gpu-on-raspberry-pi %})
- [Radeon RX 580]({% link _hardware/ati-radeon-rx-580.md %})
- [Radeon RX 6600 XT]({% link _hardware/ati-radeon-rx-6600-xt.md %})
