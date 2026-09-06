---
layout: post
title: "Building a Retro Gaming PC from an Industrial Single-Board Computer"
date: '2024-10-05 09:30:00'
tags: [MS-DOS, PC, Posts, Retrocomputing, Retrogaming, Windows 98]
image: TODO.jpg
---

<!-- DRAFT — skeleton from the project note; enrich from the video script (eGxguvyLegg) -->

Industrial PCs are built backwards from a normal desktop. Instead of a motherboard with a CPU socket and expansion slots, the whole computer — chipset, CPU, RAM, graphics — is crammed onto a single card. That card plugs into a **passive backplane** whose only job is to supply power and break out ISA and PCI slots. I wanted to know whether one of these boards, never designed for gaming, could be turned into a genuine DOS and Windows 98 machine.

Short answer: yes, and the "just swap the card" upgrade path is a real bonus.

## The hardware

- **SBC:** MiTAC MSC-373 — 440BX chipset, Socket 370, Pentium III
- **Backplane:** MBP-PCI6R-ATX — 4 ISA slots, 3 PCI slots (two of them wired for the PICMG edge connector the SBC plugs into)
- **Graphics:** onboard Chips & Technologies B69000
- **Sound:** an ISA sound/modem combo card

<!-- TODO: exact RAM, storage setup, PSU, case -->

## Getting it to power on

There's no documentation for the backplane, so the first job was working out how to turn it on at all:

- an **ATX vs AT power** selection jumper that had to be guessed
- no front-panel connector — I had to find the bare **power-switch header** and short it by hand

<!-- TODO: which jumper block, photos, the moment it first posted -->

## DOS

Once it booted, it turned out to be a genuinely capable little DOS PC:

- 64MB of RAM, which is plenty for the era
- Sound Blaster Pro-compatible audio from the ISA combo card — FM and PCM both fine
- clean runs of **Commander Keen 4**, **Jazz Jackrabbit**, and **Tyrian**
- strong Doom / Quake numbers — enough headroom for SVGA **Duke Nukem 3D**

<!-- TODO: benchmark figures from the video, which DOS benchmark suite -->

## Windows 98

Windows 98 installed cleanly. The onboard C&T B69000 is predictably weak — no Direct3D acceleration at all — so I added a [3dfx Voodoo 3]({% link _hardware/3dfx-voodoo-3.md %}), which fixed it completely:

- 3DMark and Quake II under Direct3D / OpenGL
- Unreal via Glide
- a Glide-patched copy of Tomb Raider running straight from DOS

<!-- TODO: driver versions, the Tomb Raider Glide patch details -->

## Why the form factor is interesting

The whole computer is that one card. Swapping it out is the entire upgrade path — the same backplane and peripherals could just as easily host a 386, a 486, or a much faster Pentium 4-class SBC. It's a modular retro platform hiding inside an industrial control cabinet.

### Watch on YouTube

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/eGxguvyLegg?rel=0" allowfullscreen class="youtube-video"></iframe>
</div>

### Related on this site

- [This Fully Functional PC Fits on a Single Card!]({% link _projects/this-fully-functional-pc-fits-on-a-single-card.md %}) — the project notes
- [3dfx Voodoo 3]({% link _hardware/3dfx-voodoo-3.md %})
- [MiTAC MSC-373 board reference (TheRetroWeb)](https://theretroweb.com/motherboards/s/mitac-trigon-msc-373)
