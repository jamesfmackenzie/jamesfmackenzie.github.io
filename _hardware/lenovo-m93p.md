---
layout: post
title: Lenovo M93p Tiny
summary: My take on the Lenovo M93p Tiny as a small-form-factor emulation PC — quiet, tiny, and still handles Dreamcast and GameCube well.
date: '2024-08-29 11:33:00'
tags: [Computers, PC]
---

![](/img/lenovo-m93p.jpg)

I spent years looking for the perfect emulation box: small, quiet, sits under the TV, works with a wireless controller, and has enough horsepower for 32-bit consoles. A Raspberry Pi with RetroPie got close, but it wasn't enough for PlayStation or Saturn. The Lenovo M93p Tiny — a business desktop from Lenovo's ThinkCentre line — turned out to be the answer.

### What it is

Mine is a Core i5-4570T (2 cores @ 2.9GHz) with 8GB of DDR3-1600 and a 500GB 7200rpm hard drive, bought off eBay for about $100. The onboard graphics are Intel HD 4600 — not a discrete GPU, but emulators lean heavily on CPU and lightly on GPU, so it's rarely the bottleneck. It supports 4K at 30Hz or 1440p at full 60Hz; I run mine at 1080p, which is the sweet spot for this hardware.

### Why I like it

- the "Tiny" form factor genuinely disappears under a TV — no tower, no fan noise
- performance handily beats any single-board computer I've tried
- there's room to grow: max RAM is 16GB (2× 8GB SODIMMs), and the CPU can be swapped for an i7-4765T, i7-4785T, or even a rehoused laptop i7-4750HQ that also upgrades the GPU to Intel Iris Pro 5200
- one internal 2.5" SATA bay, so an SSD upgrade is trivial

### My take

For the price, it's hard to beat. SNES, Genesis, and PlayStation all run perfectly, PSP is flawless even at 2x native resolution, and Dreamcast runs full speed via the Redream emulator (other Dreamcast emulators don't keep up on this hardware). GameCube and Wii run great at native resolution, though pushing the resolution higher causes slowdown in some games. Saturn is a mixed bag — 2D games are perfect, but 3D titles like Sega Rally or Panzer Dragoon can stutter. PlayStation 2 is where it runs out of steam: some games hit full speed, but graphically demanding ones like God of War or Gran Turismo 4 only manage 70-80%, which is noticeable in play.

### Pros

- tiny, quiet, and genuinely TV-friendly
- excellent price-to-performance for anything up to Dreamcast/GameCube
- upgradeable RAM, storage, and even CPU/GPU
- handles a wide spread of consoles without a discrete graphics card

### Cons

- PlayStation 2 is inconsistent — fine for some games, sluggish for demanding ones
- anything past PS2 (Wii U, PS3, etc.) is off the table
- onboard graphics cap out 4K at 30Hz

### Related on this site

- [Lenovo M93p Tiny Review – The Best Mini PC for Emulation?]({% post_url 2020-05-31-the-lenova-m93p-is-a-great-small-form-factor-emulation-pc %})
- [Building a Thin and Light Emulation PC]({% link _projects/building-a-thin-and-light-emulation-pc-lenovo-m93p-tiny.md %})
