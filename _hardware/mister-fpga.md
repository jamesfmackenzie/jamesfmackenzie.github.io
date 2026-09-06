---
layout: post
title: MiSTer FPGA
summary: My overview of MiSTer FPGA — what it actually is, why FPGA recreation beats software emulation for accuracy and latency, and the add-on boards that turn a bare dev board into a real retro platform.
date: '2024-08-29 11:33:00'
tags: [Computers, Consoles, Emulation, MiSTer FPGA]
---

![The MiSTer's DE10-Nano board with an SDRAM add-on fitted](/img/mister-fpga-hardware.jpg){: width="680"}

MiSTer is an open project that recreates classic computers, consoles and arcade machines on modern FPGA hardware. Instead of a program *interpreting* what old hardware did, an FPGA is wired up to *behave* like that hardware at the logic level — which, done well, gets you extremely close to the real thing on timing, video and audio.

I have been running one since 2020, mostly for the retro PC (ao486), Atari ST and console cores.

### What it actually is

"MiSTer" is really four things stacked together:

- **The board** — a Terasic **DE10-Nano**, an FPGA development kit built around a Cyclone V SoC (FPGA fabric plus a dual-core ARM that runs the host OS)
- **Cores** — hardware definitions, written in HDL, for each system you want to run
- **A Linux OS** on the microSD card that loads and manages those cores
- **Add-on boards** — SDRAM, I/O, USB and more, that fill in what the bare DE10-Nano is missing

The whole project is open source and community-run, with new cores and fixes landing constantly.

### Why I rate it

The appeal is accuracy without the fight. Software emulators can be excellent, but they still model the hardware in code, and the gaps show up as frame-timing wobble, audio glitches or input lag. MiSTer recreates the circuitry itself, so a lot of that simply goes away. It is most worth it for timing-sensitive genres — shoot-'em-ups, platformers, rhythm games — and for systems with awkward video or audio hardware.

The other thing I like is the breadth: NES, SNES, Genesis, Neo Geo, Atari ST, Amiga, C64, arcade boards and IBM PC compatibles, all from one box.

### The add-on ecosystem

A bare DE10-Nano boots MiSTer, but you will want at least the SDRAM board — most computer and console cores need it. Beyond that, the common upgrades each have their own page here:

- [I/O Board]({% link _hardware/mister-fpga-io-board.md %}) — analog video for CRTs, cooling, a tidier build
- [USB Hub]({% link _hardware/mister-fpga-usb-hub.md %}) — room for multiple controllers, keyboard and storage
- [RTC board]({% link _hardware/mister-fpga-rtc-real-time-clock.md %}) — a battery-backed clock for offline setups
- [PlayStation SNAC adapter]({% link _hardware/mister-fpga-playstation-snac-adapter.md %}) — original PlayStation controllers wired straight to the FPGA

### Related on this site

- [MiSTer FPGA Part 1 – Intro and Hardware Overview]({% post_url 2020-08-22-mister-fpga-introduction-and-hardware-overview %})
- [How to Install and Set Up MiSTer FPGA]({% link _howto/how-to-setup-mister-fpga.md %})

### MiSTer FPGA videos

<ul>
{% for post in site.posts %}
  {% if post.tags contains "MiSTer FPGA" and post.layout == "youtube" %}
  <li>
    <img src="/img/youtube-icon.png" style="display: inline-block; vertical-align:middle;" />
    <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
  </li>
  {% endif %}
{% endfor %}
</ul>

### MiSTer AO486 guides

{% include mister-fpga-howto-series.md %}
