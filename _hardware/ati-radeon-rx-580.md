---
layout: post
title: Radeon RX 580
summary: Notes on the Radeon RX 580 — a ubiquitous 2017 budget card, and the modern GPU I got running on a Raspberry Pi 5 over PCIe.
date: '2024-08-29 11:33:00'
tags: [ATi Graphics, Graphics Cards, PC]
---

The Radeon RX 580 is a mainstream graphics card from 2017, built on AMD's Polaris architecture. It sold in enormous numbers, held its value for years through the crypto-mining booms, and is still one of the most common used GPUs you can buy. By lineage it descends from the [ATi]({% link _hardware/ati.md %}) Radeon line — ATi was absorbed by AMD in 2006 and the brand retired in 2010, but "Radeon" carried on.

It is not a retro card. It earns a place here for a different reason.

### A modern GPU on a Raspberry Pi

Thanks to work on the Linux **amdgpu** driver and the Pi 5's exposed PCIe lane, it is now possible to plug a card like the RX 580 (or an RX 6600 XT) into a Raspberry Pi and have it actually work — hardware-accelerated OpenGL and Vulkan, driving a real desktop and games at speed.

The result is genuinely fast, far beyond what the Pi's own VideoCore GPU can do. It is one of those projects that is interesting less for its practicality than for the fact that it works at all: a cheap single-board computer and a used graphics card doing something neither was designed for.

### Related on this site

- [I Installed a Modern GPU on Raspberry Pi (and it's AWESOME!)]({% post_url 2024-11-17-i-installed-a-modern-radeon-rx-580-rx-6600-xt-gpu-on-raspberry-pi %})
- [ATi]({% link _hardware/ati.md %})
