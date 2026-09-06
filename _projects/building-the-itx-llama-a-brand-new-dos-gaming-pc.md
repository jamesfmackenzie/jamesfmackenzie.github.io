---
layout: post
title: Building the ITX Llama - A Brand New DOS Gaming PC
date: '2024-09-21 12:00:00'
tags: [MS-DOS, PC, Projects, Retrocomputing, Retrogaming]
status: in progress
---

I wanted real MS-DOS and early Windows 98 compatibility — real Sound Blaster and AdLib support, correct timing, no emulator quirks — without hunting down and babysitting an actual 30-year-old PC. The [ITX Llama]({% link _hardware/itx-llama.md %}) solves that by being brand new: an open-source motherboard built from scratch around a Vortex86EX system-on-module, purpose-designed to be period-correct DOS hardware rather than a repurposed antique.

### Project Notes

Status | In progress
Goal | Build and expand a brand-new, purpose-built DOS/Windows 98 gaming PC — no emulation.

Picked up a board through one of the project's community group buys (it isn't sold through a normal retail channel), and started with the essentials: a new-old-stock Radeon 9200 SE for the AGP-format slot, and flashing the BIOS to set up the board's Crystal CS4237B audio chip. From there it's been about exploring what the board's expansion headers actually enable — starting with adding a Raspberry Pi for Roland MT-32 synthesis via the onboard MIDI header, using the [mt32-pi](https://github.com/dwhinham/mt32-pi) project.

Full board details — specs, audio options, the AGP slot's real electrical behaviour — live on the [ITX Llama hardware page]({% link _hardware/itx-llama.md %}).

**Still to come**: Windows 98 gaming performance (GL Quake, Quake 3), and swapping in a [3Dfx Velocity 100]({% link _hardware/3dfx-voodoo-velocity-100.md %}) — the OEM Voodoo-3-in-disguise card — as a more period-appropriate GPU than the Radeon.

More details:

- [ITX Llama hardware page]({% link _hardware/itx-llama.md %})
- [Public Service Announcement: a new group-buy for the ITX Llama]({% post_url 2024-10-14-there-is-a-new-group-buy-for-itx-llama %})

### Part 1: A Brand New PC for 1990s DOS Games

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/ogHqmjn6sY4?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

<br />

### Part 2: A Sonic Supercharge (Roland MT-32 via Raspberry Pi)

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/ZCnQOgArgMk?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

<br />
