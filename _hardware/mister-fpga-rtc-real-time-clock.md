---
layout: post
title: MiSTer FPGA RTC Real Time Clock
summary: My take on the RTC board for MiSTer FPGA, a tiny battery-backed real-time-clock add-on that keeps the correct date and time offline — for accurate file timestamps and the cores that need a clock.
date: '2024-08-29 11:33:00'
tags: [Emulation, MiSTer FPGA]
---

The RTC board is one of the smallest and cheapest MiSTer add-ons. It plugs into the DE10-Nano's LTC connector and gives the system a battery-backed **real-time clock**, so it always knows the correct date and time even with no network connection.

### What it is

A small board built around a DS3231 — a very accurate temperature-compensated I²C real-time clock — with a coin-cell battery that keeps time running while the MiSTer is powered off.

### What it is for

- **Correct file timestamps.** Anything written to the microSD card (save states, screenshots, config changes) gets the right date and time instead of a default epoch.
- **Cores that use a clock.** Some cores read the system time — ao486 and Minimig for the host OS clock, and a handful of games such as *Pokémon Ruby/Sapphire* on the GBA core that have an in-cartridge RTC.
- **Running headless.** If your MiSTer is not on Wi-Fi, this is the only way it will have an accurate clock at all.

### Where it fits

It is a "set and forget" quality-of-life board rather than something you interact with. If your MiSTer is permanently online it matters less, since MiSTer can pull time from the network. For an offline setup, or if you just want tidy timestamps and full core compatibility, it is an easy addition.

### Related on this site

- [Supercharge your MiSTer FPGA (video)]({% post_url 2022-11-12-supercharge-your-mister-fpga-with-add-ons %})
- [MiSTer FPGA]({% link _hardware/mister-fpga.md %})
- [MiSTer FPGA IO Board]({% link _hardware/mister-fpga-io-board.md %})
