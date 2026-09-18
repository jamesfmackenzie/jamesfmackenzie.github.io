---
layout: post
title: ESS Solo-1
summary: Notes on the ESS Solo-1 (ES1938S) — a single-chip PCI sound card with real Sound Blaster Pro compatibility, which I run in my HP Compaq t5710 thin client.
date: '2024-08-29 11:33:00'
tags: [PC, Sound Cards]
---

The ESS Solo-1 is one of the PCI-era sound cards that actually bothered with DOS compatibility, rather than treating it as an afterthought. It's the card I run in my [HP Compaq t5710 thin client]({% link _hardware/hp-compaq-t5710.md %}), whose single PCI slot doesn't leave room for much else.

### What it is

Built around ESS's single-chip ES1938S, the Solo-1 is a 16-bit stereo PCI sound card with programmable sample rates from 6kHz to 48kHz and full-duplex operation. It includes an MPU-401 (UART mode) interface for MIDI and wavetable synths, 32-voice software wavetable synthesis, and Sound Blaster Pro-compatible legacy audio for DOS — with the usual PCI-era caveat that how well that compatibility holds up depends on the driver mode and the motherboard's chipset, not just the card itself.

### Where it fits

I use mine in the t5710 specifically because it's a genuine PCI card with real onboard DOS-era compatibility, in a machine with exactly one PCI slot to spend. It's part of a wider PCI-sound-in-DOS interest alongside cards like the Sound Blaster Live! and Yamaha YMF724 — how well any of them behave under real DOS depends heavily on DMA support on the host chipset, which is where PCI sound in DOS gets genuinely interesting (and often frustrating) on newer machines.

### Related on this site

- [HP Compaq t5710]({% link _hardware/hp-compaq-t5710.md %})
- [Creative Labs Sound Blaster Live!]({% link _hardware/creative-labs-sound-blaster-live.md %})
- [Yamaha YMF724]({% link _hardware/yamaha-ymf724.md %})
