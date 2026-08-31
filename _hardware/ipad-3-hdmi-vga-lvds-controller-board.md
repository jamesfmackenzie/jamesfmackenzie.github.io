---
layout: post
title: iPad 3 HDMI and VGA Controller Board
summary: Notes on driving a salvaged iPad 3 / iPad 4 Retina panel as a standalone monitor with a cheap LVDS controller board — a sharp, fast, 4:3 display for MiSTer FPGA and retro use.
date: '2024-08-29 11:33:00'
tags: [Monitors]
---

The 9.7" Retina panel from the iPad 3 and iPad 4 (an LG **LP097QX1**) is a genuinely nice display: **2048×1536**, 4:3, IPS, and a response time around **1ms**. Millions were made, so panels are cheap, and you can drive one as a standalone monitor with a small LVDS controller board.

### What it is

The kit is a generic controller board plus cabling that accepts **HDMI and VGA input** and drives the panel over eDP/LVDS. You supply power, mount the panel however you like, and you have a compact high-DPI monitor for well under the price of anything comparable off the shelf.

### Why it is good for retro use

- **4:3 aspect** — the right shape for a huge amount of retro console and computer output, without pillarboxing
- **very high pixel density** — integer-scaled low-res sources look clean and sharp
- **fast response** — no noticeable lag, which matters for a gaming display
- **small and light** — easy to build into a MiSTer setup, a portable rig, or a second screen

The obvious use here is [MiSTer FPGA]({% link _hardware/mister-fpga.md %}) over HDMI, but it works with anything that outputs HDMI or VGA.

### Trade-offs

It is still a fixed 60Hz LCD, so it will not give you CRT motion or true 15kHz sync — for that you want something like the [Microvitec AKF50]({% link _hardware/microvitec-akf50.md %}). As a sharp, modern flat panel in an unusually useful shape, though, it is hard to beat for the money.

### Related on this site

- [iPad 3 panel plus HDMI converter board — a great screen for MiSTer FPGA]({% post_url 2022-05-07-ipad-3-screen-plus-hdmi-converter-board-great-for-mister-fpga %})
