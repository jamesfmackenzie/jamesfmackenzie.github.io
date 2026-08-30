---
layout: post
title: Dreamblaster X2GS
summary: My take on the DreamBlaster X2GS, a modern Wave Blaster wavetable daughterboard with an officially licensed Roland GS bank — one of the easiest ways to get authentic MIDI music in DOS games.
date: '2024-08-29 11:33:00'
tags: [MIDI, PC, Peripherals, Sound]
---

![DreamBlaster X2GS wavetable daughterboard](/img/posts/dreamblaster-x2-x2gs-wavetable-daughterboard-2.jpg){: width="680"}

The DreamBlaster X2GS is a modern wavetable daughterboard that plugs into the Wave Blaster header found on many DOS-era sound cards. It is one of the simplest ways to add high quality MIDI music to a retro PC without hunting down a 1990s Roland synth.

### What it is

The X2GS is a small board that sits on the 26-pin Wave Blaster header of a compatible sound card. MIDI data from the host card is rendered on the daughterboard's own sample ROM and piped back out through the sound card's line output, so no extra cabling or power is needed.

It carries two banks:

- a read-only 16 MB bank with an **officially licensed Roland GS** sound set (full GM/GS implementation, 128 GM instruments, 200+ drum sounds)
- an updatable user bank of up to 48 MB that you flash over USB with your own samples

You switch between banks using NRPN messages.

### Why I rate it

The licensed Roland GS bank is the headline. To my ear it sounds very close to real Sound Canvas hardware like the SC-55 and SC-88 — which is exactly what a huge number of General MIDI and GS-era DOS games were scored for. Set a game to Sound Canvas, General MIDI or MPU-401 and it simply springs to life. No serial cable, no external box, no separate power supply. It is the lowest-friction route to good DOS MIDI I have used.

### Where it fits

The X2GS is the right choice when your sound card already has a Wave Blaster header and your library leans towards General MIDI and GS rather than the earlier Roland MT-32. If your games are mostly MT-32-era, a real MT-32 or an [mt32-pi]({% link _hardware/pi-midi.md %}) setup is a better match. For the GM/GS wave, the X2GS is hard to beat for the money.

### Pros

- officially licensed Roland GS bank that sounds genuinely close to a Sound Canvas
- no cables, box or power supply — it just fits the header
- user-flashable second bank for custom soundfonts

### Cons

- needs a host sound card with a Wave Blaster header
- not an MT-32 substitute — early-90s MT-32 scores still want dedicated hardware or emulation

### Related on this site

- [DreamBlaster X2GS – A New MIDI Challenger?]({% post_url 2021-10-02-dreamblaster-x2-x2gs-a-new-midi-challenger %})
- [DreamBlaster X2GS Review (video)]({% post_url 2021-09-11-dreamblaster-dream-blaster-x2gs-x2-gs-review-a-new-midi-challenger %})
- [Doom Episode 1 soundtrack, General MIDI version on DreamBlaster X2GS]({% post_url 2021-12-18-doom-episode-1-soundtrack-general-midi-version-on-dreamblaster-x2gs %})
- [PI-MIDI]({% link _hardware/pi-midi.md %})
