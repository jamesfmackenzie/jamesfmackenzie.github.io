---
layout: post
title: Radeon GPU on a Raspberry Pi 5
date: '2026-09-15 00:35:00'
tags: [Projects, Raspberry Pi, Retrogaming, Videogames]
status: completed
hero: pi5-egpu-rig-front.jpg
hero_alt: A Sapphire Radeon RX 580 mounted above a Raspberry Pi 5 and OCuLink adapter board
---

A Raspberry Pi 5 exposes a real PCIe lane, which means a real desktop graphics card can be wired into one over an OCuLink connection. Nobody sane needs an RX 580 on a Pi. That's rather the point.

### Project Notes

Status | Completed
Goal | Get a modern Radeon GPU running on a Raspberry Pi 5 over PCIe/OCuLink, using a custom kernel built on Jeff Geerling and Coreforge's AMDGPU work for the Pi 5's ARM CPU.

The hardware side is a PCIe-to-M.2 HAT, an M.2-to-OCuLink adapter board, an OCuLink cable, a 600W PC power supply, and an OCuLink eGPU dock for the card itself. None of it works without the software side, though: Coreforge's `rpi-6.6.y-gpu` kernel fork, plus their optimised memcpy library, patched in and registered via `/etc/ld.so.preload`.

First up was a Sapphire Radeon RX 580 — confirmed working with a 4K desktop and `neofetch` correctly reading back the card. Half-Life 2 and Portal both ran maxed out at 4K, Half-Life 2 hitting just under 300fps (the Source engine's own cap), with GravityMark benchmarking the card at 40fps.

Then a PowerColor Radeon RX 6600 XT went in — about four years newer and roughly twice as fast on paper. It just worked, the same boot process, and Doom 3 ran a locked 4K60. GravityMark came back at 80fps — almost exactly double the RX 580's result.

More details:

- [I Got a Modern Radeon GPU Running on a Raspberry Pi 5]({% post_url 2026-09-15-i-installed-a-modern-radeon-gpu-on-a-raspberry-pi-5 %}) — the full story
- [Raspberry Pi 5]({% link _hardware/raspberry-pi-5.md %})
- [Radeon RX 580]({% link _hardware/ati-radeon-rx-580.md %})
- [Radeon RX 6600 XT]({% link _hardware/ati-radeon-rx-6600-xt.md %})
- [I Installed a Modern GPU on Raspberry Pi (and it's AWESOME!)]({% post_url 2024-11-17-i-installed-a-modern-radeon-rx-580-rx-6600-xt-gpu-on-raspberry-pi %}) — the original video

And also in video form below. Enjoy!

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/J0z09Ddr58w?rel=0"
allowfullscreen class="youtube-video"></iframe>
</div>

<br />
