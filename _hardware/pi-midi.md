---
layout: post
title: PI-MIDI
summary: My take on the PI-MIDI, a MIDI HAT for the Raspberry Pi that turns a Pi running mt32-pi into a plug-and-play Roland MT-32 and Sound Canvas replacement for DOS gaming.
date: '2024-08-29 11:33:00'
tags: [MIDI, PC, Peripherals, Sound]
---

![PI-MIDI connected to a Raspberry Pi](/img/pi-midi-connected.jpg){: width="680"}

The PI-MIDI is a MIDI HAT for the Raspberry Pi. It attaches to the Pi's GPIO pins and gives it a proper MIDI input, stereo RCA output, an audio input for mixing, and a dedicated port for connecting to MiSTer FPGA. Paired with the [mt32-pi](https://github.com/dwhinham/mt32-pi) software synth, it becomes a small, cheap, authentic-sounding stand-in for a Roland MT-32 or Sound Canvas.

### What it is

On the connectivity side the board provides:

- a **MIDI DIN input** for connecting MIDI devices (including a DOS PC via a gameport MIDI cable)
- **stereo RCA output**, a big step up in quality from the Pi's own audio jack
- a **2.5 mm audio input**, so Sound Blaster effects from the PC can be mixed with the synthesised MIDI into one output
- a **user port** that looks like USB but is a direct IO connection for MiSTer FPGA

It also has a rotary dial, jog wheel, two buttons and a 1.3" OLED screen for changing volume, synth mode and options without a keyboard.

### mt32-pi

mt32-pi is a bare-metal kernel that turns a Raspberry Pi 3 or later into a Roland MT-32 emulator (via Munt) and a SoundFont synthesizer (via FluidSynth). It natively supports GPIO MIDI interfaces like the PI-MIDI, so the two together make a DIY MIDI appliance with the sound and feel of a classic synth. MT-32 mode covers early-90s games; SoundFont mode covers later General MIDI and Sound Canvas titles.

### Why I rate it

If you cannot get hold of a real MT-32 or Sound Canvas, a Pi plus PI-MIDI is the option I would recommend. It is plug and play, simple to operate from the front-panel controls, and to my ear produces very authentic sound. The MIDI-DIN input also lifts the DOS-extender limitation of the cheaper serial-MIDI approach (where games like Doom will not work).

### The MiSTer connection

The mt32-pi and MiSTer projects collaborated on a direct cabling solution: a single USB A-to-A cable between the PI-MIDI's user port and the [MiSTer IO board]({% link _hardware/mister-fpga-io-board.md %}) user port carries MIDI data *and* powers the Pi. The PC, Atari ST, Amiga and X68000 cores can all use it.

### Related on this site

- [PI-MIDI Review – Supercharge your mt32-pi]({% post_url 2022-06-04-pi-midi-review-supercharge-your-mt32-mt-32-pi %})
- [Get the Best MS-DOS Audio With mt32-pi]({% link _howto/how-to-setup-mt32-pi.md %})
- [DreamBlaster X2GS]({% link _hardware/dreamblaster-x2gs.md %})
