---
layout: post
title: "Recovering a Bricked BIOS with a SOP8 Clip"
date: '2024-10-06 12:00:00'
tags: [PC, Posts, Repairs, Retrocomputing]
image: TODO.jpg
---

<!-- DRAFT — skeleton from the ITX Llama email exchange + the tweet (1842597901836681384) -->

I bricked my [ITX Llama]({% link _hardware/itx-llama.md %}) trying to change its CPU clock speed. Here's how I got it back with a clip, a cheap programmer, and about twenty minutes.

## How I broke it

The Llama's Vortex86EX module runs at 300&nbsp;MHz out of the box, and the BIOS exposes 400 and 500&nbsp;MHz options. With some extra cooling I tried 500&nbsp;MHz — and Windows 98 fell apart: Explorer crashing before the desktop finished loading, apps failing the moment they opened.

Trying to be sensible, I stepped *down* to 400&nbsp;MHz. That's the setting that actually killed it. The board hung on boot with no way into the BIOS. Eivind Bøhler, who designed the Llama, later explained why: the DDR memory is clocked slightly higher for the 400&nbsp;MHz CPU setting than for 300 or 500, and the clocks are tied together in an inflexible way, so 400 is the fragile one on some boards.

Either way, I was locked out. The only way back in was to reflash the BIOS chip directly.

## What you need

- a **SOP8 test clip** (also called an SOIC-8 clip) that grips the flash chip's legs without desoldering
- an EEPROM programmer — I used a **TL866 II Plus** (I'd also bought a cheap CH341A as a backup)
- the flash chip on the Llama is a **Macronix MX25U6435F**, a 64&nbsp;Mbit SPI part that runs at **1.8&nbsp;V** — worth knowing, because a 3.3&nbsp;V-only programmer or adapter can damage a 1.8&nbsp;V chip

<!-- TODO: photos of the clip on the chip, the programmer, software (minipro / Xgpro) -->

## The recovery

1. Clip onto the flash chip with the board unpowered.
2. Read the chip first, save a backup.
3. Flash a known-good BIOS image. For the Llama, the current BIOS resets the CPU multiplier back to 300&nbsp;MHz as part of the ROM itself, so flashing it is guaranteed to bring the board back to a bootable state.
4. Remove the clip, power on, done.

<!-- TODO: exact minipro commands, verify step, first successful boot -->

## The actual fix for the overclock

Once it was alive again: the 500&nbsp;MHz instability was down to the "silicon lottery" — my particular chip just doesn't like it, no matter the cooling. A later BIOS added a **466&nbsp;MHz** option, and that turned out to be the stable sweet spot for this board. (More on the cooling and overclocking in the [ITX Llama build writeup]({% link _hardware/itx-llama.md %}).)

## Watch on YouTube

<!-- TODO: is there a video? otherwise embed the tweet -->

### Related on this site

- [ITX Llama]({% link _hardware/itx-llama.md %})
- [Building the ITX Llama]({% link _projects/building-the-itx-llama-a-brand-new-dos-gaming-pc.md %}) — the project notes
