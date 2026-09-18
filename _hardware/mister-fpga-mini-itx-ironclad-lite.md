---
layout: post
title: MiSTer FPGA Mini-ITX Ironclad Lite
summary: My MiSTer Mini-ITX Ironclad Lite — the interface board that houses a DE10-Nano in a standard PC case, with a built-in PSU, fan control, and SNAC-compatible USB.
date: '2024-08-29 11:33:00'
tags: [Emulation, MiSTer FPGA]
---

A bare DE10-Nano is a dev board on a desk. The Ironclad Lite is what turns it into something that mounts in a standard Mini-ITX/Micro-ATX/DTX/ATX case and behaves like a finished PC.

### What it is

The Ironclad Lite is an interface board that houses a real DE10-Nano (or a QMTECH Cyclone V KFB / MiSTer Pi) inside a standard PC case. It has a built-in PSU — just needs a 5V/2A+ power brick — with over-voltage, short-circuit, and over-current protection, 5-speed PWM smart fan control, a USB 3.0-shaped SNAC-compatible controller port among 6 USB ports total, Toslink digital plus noise-isolated analog audio, and standard RGB video out. The Lite tier specifically drops a real-time clock and the DB9 SNAC port that the Plus/DX models include — SNAC controllers connect via the USB3.0-shaped port instead.

### My build

I bought mine from d3fmod in March 2024, along with the Massive Heatsink add-on, the Remote Control Kit (the Lite doesn't bundle a remote by default), an I/O backplate cut for the case I was using, and a Mt32-Pi PRO internal HAT for authentic Roland MT-32 MIDI. It then sat unbuilt for over two years before I finally got around to assembling it.

Since the Ironclad Lite has no built-in RTC, I reused the [RTC module]({% link _hardware/mister-fpga-rtc-real-time-clock.md %}) from an earlier MiSTer accessories order rather than buying a new one, and carried over the 128MB SDRAM board from the same haul. Its [IO Board]({% link _hardware/mister-fpga-io-board.md %}) and [USB hub]({% link _hardware/mister-fpga-usb-hub.md %}) partly overlap with what the Ironclad Lite already provides on its own — its own TOSLINK audio, USB ports, and power/button wiring — so it's worth deciding what actually still needs to be installed alongside it rather than fitting both.

### Related on this site

- [MiSTer FPGA]({% link _hardware/mister-fpga.md %})
- [MiSTer FPGA IO Board]({% link _hardware/mister-fpga-io-board.md %})
- [MiSTer FPGA USB Hub]({% link _hardware/mister-fpga-usb-hub.md %})
- [MiSTer FPGA RTC Real-Time Clock]({% link _hardware/mister-fpga-rtc-real-time-clock.md %})
- [Supercharge your MiSTer FPGA]({% post_url 2022-11-12-supercharge-your-mister-fpga-with-add-ons %})
