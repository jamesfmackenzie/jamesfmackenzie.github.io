---
layout: post
title: MiSTer FPGA IO Board
summary: Hardware overview of the MiSTer FPGA IO Board, the add-on that brings analog video, cooling, and a SNAC/mt32-pi user port to a DE10-Nano setup.
date: '2024-08-29 11:33:00'
tags: [Emulation, MiSTer FPGA]
---

A bare DE10-Nano runs MiSTer fine, but it still feels like a dev board on a desk. The IO Board is one of the add-ons that starts turning it into something closer to a finished machine.

### What it is

The Digital IO Board adds HDMI output via the DE10-Nano, a cooling fan, system buttons and status LEDs, mini-TOSLINK digital audio out, a power switch, an ADC input for audio, and support for a secondary SDRAM board. It also has a user port — the physical connection point for accessories like a SNAC adapter or an mt32-pi MIDI synth — and a secondary SD card slot reserved for computer cores, not extra game storage.

### Why I like it

- the user port is genuinely useful, not just a spec-sheet feature — it's how I've connected both a [SNAC PlayStation adapter]({% link _hardware/mister-fpga-playstation-snac-adapter.md %}) and an mt32-pi MIDI synth
- proper cooling and case-friendly mounting instead of a bare board
- system buttons and LEDs make it feel like real hardware, not a dev kit

### My take

I bought mine as part of a wider MiSTer accessories haul alongside a USB hub, RTC module, and extra SDRAM — see [Supercharge your MiSTer FPGA]({% post_url 2022-11-12-supercharge-your-mister-fpga-with-add-ons %}). The user port earned its keep twice over: it's how the [SNAC adapter]({% link _hardware/mister-fpga-playstation-snac-adapter.md %}) connects a real PS1 controller and memory card, and separately how an mt32-pi MIDI synth hooks up over a USB-A-to-A cable — MiSTer auto-detects it in the core menu, and it played Space Quest 3's MIDI score without any fuss.

Since moving to an [Ironclad Lite case]({% link _hardware/mister-fpga-mini-itx-ironclad-lite.md %}), some of the IO Board's jobs — audio out, power switching — now overlap with what the case itself provides, so it's worth deciding what actually carries over rather than wiring up both.

### Pros

- real, useful I/O: HDMI, TOSLINK audio, a proper user port for SNAC/mt32-pi
- built-in cooling and case-friendly mounting
- makes a bare DE10-Nano feel like finished hardware

### Cons

- some features overlap with what a case like the Ironclad Lite already provides
- one more board to fit and wire up if you're not using a case designed around it

### Related on this site

- [MiSTer FPGA]({% link _hardware/mister-fpga.md %})
- [MiSTer FPGA USB Hub]({% link _hardware/mister-fpga-usb-hub.md %})
- [MiSTer FPGA PlayStation SNAC Adapter]({% link _hardware/mister-fpga-playstation-snac-adapter.md %})
- [MiSTer FPGA Mini-ITX Ironclad Lite]({% link _hardware/mister-fpga-mini-itx-ironclad-lite.md %})
- [Supercharge your MiSTer FPGA]({% post_url 2022-11-12-supercharge-your-mister-fpga-with-add-ons %})
