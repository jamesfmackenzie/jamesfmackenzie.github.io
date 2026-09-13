---
layout: post
title: mt32-pi
summary: A bare-metal Raspberry Pi kernel that turns cheap hardware into a genuinely convincing Roland MT-32 and Sound Canvas replacement for DOS gaming.
date: '2025-11-26 23:35:00'
tags: [MIDI, Sound]
---

mt32-pi is a bare-metal kernel that turns a Raspberry Pi 3 or later into a Roland MT-32 emulator (via Munt) and a SoundFont synthesizer (via FluidSynth). MT-32 mode covers early-90s DOS games written for the real hardware; SoundFont mode covers later General MIDI and Sound Canvas titles — between the two, it spans most of the era of DOS games with real MIDI soundtracks.

It natively supports GPIO MIDI interfaces, which is what makes [PI-MIDI]({% link _hardware/pi-midi.md %}) work: the HAT handles the MIDI and audio I/O, mt32-pi does the actual synthesis, and together they're a small, cheap, authentic-sounding stand-in for hardware that's expensive and increasingly hard to find in good condition.

### Related on this site

- [PI-MIDI]({% link _hardware/pi-midi.md %})
- [Get the Best MS-DOS Audio With mt32-pi]({% link _howto/how-to-setup-mt32-pi.md %})
- [Connecting PI-MIDI / mt32-pi to MiSTer FPGA for MIDI Audio]({% post_url 2022-12-10-how-to-connect-pi-midi-mt32-pi-to-mister-fpga-for-great-midi-audio %})
