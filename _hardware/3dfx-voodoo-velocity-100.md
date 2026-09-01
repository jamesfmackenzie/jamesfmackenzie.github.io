---
layout: post
title: 3Dfx Velocity 100
summary: Overview of the 3Dfx Velocity 100, a 1999 budget card that is essentially a Voodoo3 with one texture unit disabled in the drivers — plus the well-known tweak to turn it back on.
date: '2024-08-29 11:33:00'
tags: [3Dfx Voodoo, Graphics Cards, PC]
---

The 3Dfx Velocity 100 is a budget AGP graphics card released in 1999, based directly on the [Voodoo3]({% link _hardware/3dfx-voodoo-3.md %}) architecture. It was aimed at the low end of the market and sold for around $50, largely through OEM channels. I made a whole video about it — [The Secret 3Dfx Graphics Card (You Never Knew Existed)]({% post_url 2024-11-30-the-secret-3dfx-graphics-card-velocity-100 %}).

### What it is

Hardware-wise the Velocity 100 is close to a **Voodoo3 2000**. It runs at the same 143 MHz core and memory clock, uses the same Avenger chip, and outputs a single unified 2D/3D pipeline — no pass-through cable, unlike the earlier [Voodoo]({% link _hardware/3dfx-voodoo-1.md %}) and [Voodoo2]({% link _hardware/3dfx-voodoo-2.md %}).

The differences are cost-cutting ones:

- **8 MB of SGRAM** instead of 16 MB
- only **one texture mapping unit (TMU)** exposed in OpenGL and Glide

Both TMUs are physically present and both work under Direct3D. 3Dfx disabled the second one in the OpenGL and Glide drivers to stop the smaller 8 MB framebuffer being overwhelmed at higher resolutions.

### Turning the second TMU back on

This is the card's claim to fame. A documented Windows registry change re-enables the second TMU for OpenGL and Glide, moving the core configuration from `1:0:1:1` to `1:0:2:1` — the same as a Voodoo3 2000. With it applied, the Velocity 100 performs virtually identically to a Voodoo3 2000 in Glide and OpenGL titles like *Quake III* and *Expendable*. It effectively becomes the card it was cut down from.

### Where it fits

For a period Windows 98 build it is a cheap way onto the Voodoo3 / Glide 2 platform, provided you apply the tweak and keep resolutions sensible given the 8 MB of memory. If you can find a plain Voodoo3 for a similar price, that is the simpler buy.

### Related on this site

- [The Secret 3Dfx Graphics Card (You Never Knew Existed)]({% post_url 2024-11-30-the-secret-3dfx-graphics-card-velocity-100 %}) — my video on this card
- [3Dfx]({% link _hardware/3dfx.md %})
- [3Dfx Voodoo 2]({% link _hardware/3dfx-voodoo-2.md %})
- [How To Play 3Dfx Glide Games in DOS]({% link _howto/how-to-play-3dfx-voodoo-glide-games-in-dos.md %})
- [Does this Arcade Machine Voodoo 3 work on PC?]({% post_url 2024-02-16-the-cheapest-3dfx-voodoo3-voodoo-3 %})
