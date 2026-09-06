---
layout: post
title: "Building the ITX Llama: A Brand-New DOS Gaming PC"
date: '2024-09-21 12:00:00'
tags: [MS-DOS, PC, Posts, Retrocomputing, Retrogaming]
image: TODO.jpg
---

<!-- DRAFT — HOLD until the build is "all done" (Velocity 100 + SG13B case). -->
<!-- Skeleton from the project note + the Eivind Bøhler email exchange. Enrich from the video scripts (ogHqmjn6sY4, ZCnQOgArgMk). -->

Rather than hunt down and babysit a 30-year-old PC, I built a new one. The [ITX Llama]({% link _hardware/itx-llama.md %}) is an open-source motherboard designed from scratch around a Vortex86EX system-on-module to be period-correct DOS hardware — real Sound Blaster and AdLib support, correct timing, no emulator quirks.

## Getting started

- Picked up a board through one of the project's community group buys — it isn't sold retail.
- Fitted a new-old-stock **Radeon 9200 SE** in the AGP-format slot.
- Flashed the BIOS to set up the onboard **Crystal CS4237B** audio.

<!-- TODO: first boot, DOS install, initial impressions from Part 1 video -->

## Roland MT-32 from a Raspberry Pi

The Llama has an onboard MIDI header wired for a Raspberry Pi. Running [mt32-pi](https://github.com/dwhinham/mt32-pi) on a Pi Zero seated straight on the board gives Roland MT-32 (and General MIDI / SoundFont) synthesis with no separate interface.

<!-- TODO: setup detail from Part 2 video -->

## The overclocking saga

The Vortex86EX module runs at **300&nbsp;MHz** stock, with 400 and 500&nbsp;MHz options in the BIOS.

- **500&nbsp;MHz** made Windows 98 unstable — Explorer crashing before the desktop loaded — no matter how I cooled it.
- Backing off to **400&nbsp;MHz** *bricked the board* (it hung with no BIOS access). Per Eivind Bøhler, who designed the Llama, the DDR memory runs slightly faster at the 400 setting than at 300 or 500, and the clocks are linked inflexibly — so 400 is the fragile one on some boards. Recovering it needed a BIOS reflash with a SOP8 clip. <!-- TODO: link the SOP8 recovery post once published -->
- A later BIOS added a **466&nbsp;MHz** option. That's the stable sweet spot for my particular chip — the 500&nbsp;MHz trouble was just the silicon lottery.

### Cooling

The board ships with a heat spreader on the SOM. For the overclock I removed it and fitted a **16.5&nbsp;mm Wakefield Thermal heatsink (LTN20069)** directly to the SoC, plus a **40&nbsp;mm Noctua fan** on the 3D-printed bracket from the project's GitHub. Exact fan placement doesn't matter much — any airflow is enough. Rule of thumb from Eivind: if you can hold a finger on the heatsink without it hurting, you're comfortably under the 60&nbsp;°C spec.

<!-- TODO: photos, temps if measured -->

## Still to come

- Windows 98 gaming performance — GL Quake, Quake 3
- Swapping the Radeon for a [3Dfx Velocity 100]({% link _hardware/3dfx-voodoo-velocity-100.md %}) — an OEM Voodoo 3 in disguise — as a more period-appropriate GPU
- Moving the build into a SilverStone SG13B mini-ITX case

### Watch on YouTube

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/ogHqmjn6sY4?rel=0" allowfullscreen class="youtube-video"></iframe>
</div>

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/ZCnQOgArgMk?rel=0" allowfullscreen class="youtube-video"></iframe>
</div>

### Related on this site

- [ITX Llama]({% link _hardware/itx-llama.md %}) — the hardware reference
- [Building the ITX Llama]({% link _projects/building-the-itx-llama-a-brand-new-dos-gaming-pc.md %}) — the project notes
- Recovering a Bricked BIOS with a SOP8 Clip <!-- TODO: link once published -->
- [PI-MIDI]({% link _hardware/pi-midi.md %})
