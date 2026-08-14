---
layout: post
title: "I Got Ridge Racer's Three-Monitor Arcade Version Running in MAME"
date: '2026-08-14 00:30:00:00'
summary: |-
  Namco's 1994 Ridge Racer Three Monitor Version cabinet links three arcade PCBs together over a proprietary serial chip to drive three screens. I built a proper emulation of that chip for MAME and got it running — three linked instances, correct per-screen camera views, and (crucially) no garbled graphics.
image: ridge-racer-three-monitor-version-mame-3-screen.jpg
tags: [Posts, Emulation, Programming, Retrogaming]
---

![Three linked MAME windows running Ridge Racer Three Monitor Version](/img/posts/ridge-racer-three-monitor-version-mame-3-screen.jpg)

Back in the arcade heyday, Namco built some genuinely wild multi-screen cabinets: **Ridge Racer Full Scale** and **Ridge Racer Three Monitor Version**, each spreading a single race across three physically adjacent screens. Three identical PCBs, each rendering its own camera angle, all kept in lockstep over a proprietary serial link. It's the kind of hardware that looks completely impossible to emulate — which is exactly why I wanted to try.

The code and full technical writeup are <a href="https://github.com/jamesfmackenzie/mame" target="_blank">on GitHub</a>.

### The chip nobody had properly emulated

The thing making these cabinets tick is a Namco custom chip called the **C139** — a serial interface controller that lets multiple arcade boards talk to each other over a 9-bit, 1–2 Mbps link. It's used across two decades of Namco hardware for linked cabinet play and multi-screen setups, but mainline MAME's implementation is a 113-line stub that just returns a hardcoded status value. Every linked Namco game from 1987 to 1997 — Final Lap, Winning Run, Ridge Racer and around 40 others — has effectively zero linking support in official MAME.

A couple of people had taken cracks at it before me. John Bennett built a working proof-of-concept using MAME's built-in LAN sockets, which established a lot of the protocol fundamentals but was hacky by design and never meant to go anywhere near mainline. Ariane Fugmann (SailorSat) later did a serious rewrite on top of that work, moving to a proper ASIO networking thread and a real register model — much closer to something submittable.

### Building a canonical implementation

Starting from hardware measurements (direct chip testing with an Arduino jig, ROM watchpoint traces, schematic study), I built out a full C139 device model for MAME:

- All 8 hardware registers, correct bit masks, correct power-on defaults
- ASIO TCP networking on a background thread with lock-free FIFOs
- A clean topology system — `CENTER` / `FORWARDER` / `SLAVE` roles — configured by the game driver rather than hardcoded into the device itself
- Mode 0x0C support, which is what both three-screen Ridge Racer variants use

For the three-screen ring topology, the real hardware does something MAME can't literally replicate: the center PCB's serial output is physically Y-split — soldered to feed both side screens simultaneously. MAME can only do point-to-point TCP, so the emulated topology approximates it as a relay chain instead: center sends to the right screen, and the right screen immediately forwards to the left screen in the network thread, without ever involving its own CPU. From the game's perspective, the behaviour is identical.

### The graphics problem (and the game that sidesteps it)

The obvious first target was **Ridge Racer Full Scale**, but it turns out the Full Scale graphics ROMs have never been publicly dumped. The available dump swaps in the standard Ridge Racer graphics, which don't match the Full Scale program code, so it currently boots with corrupted, mismatched graphics. Frustrating, but I already knew that going in.

**Ridge Racer Three Monitor Version (`ridgerac3m`)** is a different story. In MAME's driver, it's declared as a clone of the standard `ridgerac` set — meaning it reuses the ordinary, fully and correctly dumped Ridge Racer graphics, sound, and 3D model ROMs. Only four program ROMs are unique to it. When a proper dump of those turned up, I verified all four against MAME's expected checksums — exact match — and realised this game could actually run clean.

It did.

### Three screens, correctly

Running three linked instances (left/slave, center/master, right/forwarder) over TCP, everything connected cleanly: DIP-switch role selection worked, the forwarder relayed thousands of frames with zero errors or overflows, and the game rendered without a hint of graphical corruption.

The genuinely exciting part is in the screenshot above. That's not three copies of the same frame — the center screen shows a full attract-mode scene, while the left and right monitors show tight, close-up canyon-wall views consistent with a wraparound side-camera perspective mid-corner. Each PCB is receiving the broadcast scene state over the C139 link and computing its own distinct camera viewport from it, exactly as the real cabinet would.

### What's next

Attract mode running cleanly is a solid checkpoint, but it doesn't prove long-run sync under actual play. Next up is inserting credits and driving an actual race across all three screens to confirm they stay locked together, then working through the other linked modes (Final Lap, Winning Run, Ace Driver, and the rest) that the same C139 device should eventually support.

Full technical detail — register maps, wire formats, ROM traces, and the implementation plan — is in <a href="https://github.com/jamesfmackenzie/mame/blob/master/C139_TECHNICAL_REFERENCE.md" target="_blank">C139_TECHNICAL_REFERENCE.md</a> in the repo, if you want to go deeper.
