---
layout: post
title: Radeon RX 6600 XT
summary: Notes on the Radeon RX 6600 XT — a 2021 RDNA2 card, and the faster of the two modern GPUs I got running on a Raspberry Pi 5 over PCIe.
date: '2026-09-13 23:08:00'
tags: [3D Graphics, ATi, PC]
hero: powercolor-radeon-rx-6600-xt.jpg
hero_alt: PowerColor Radeon RX 6600 XT graphics card
---

The Radeon RX 6600 XT is a 2021 graphics card built on AMD's RDNA2 architecture, with 8GB of GDDR6. Mine is a PowerColor dual-fan model. By lineage it descends from the [ATi]({% link _hardware/ati.md %}) Radeon line — ATi was absorbed by AMD in 2006 and the brand retired in 2010, but "Radeon" carried on.

It is not a retro card. It earns a place here for a different reason.

### A modern GPU on a Raspberry Pi

Like the [Radeon RX 580]({% link _hardware/ati-radeon-rx-580.md %}), thanks to work on the Linux **amdgpu** driver and the Pi 5's exposed PCIe lane, this card runs on a Raspberry Pi 5 — hardware-accelerated OpenGL and Vulkan, driving a real desktop and games at speed. Being about four years newer than the RX 580 and roughly twice as fast, it pushed the same Pi 5 eGPU rig noticeably further — Doom 3 at 4K/Ultra, and a healthy framerate lead over the RX 580 in synthetic benchmarks like GravityMark.

### Related on this site

- [Radeon GPU on a Raspberry Pi 5]({% link _projects/radeon-gpu-on-a-raspberry-pi-5.md %}) — the project notes
- [I Got a Modern Radeon GPU Running on a Raspberry Pi 5]({% post_url 2026-09-15-i-installed-a-modern-radeon-gpu-on-a-raspberry-pi-5 %})
- [Raspberry Pi 5]({% link _hardware/raspberry-pi-5.md %})
- [Radeon RX 580]({% link _hardware/ati-radeon-rx-580.md %})
- [ATi]({% link _hardware/ati.md %})
