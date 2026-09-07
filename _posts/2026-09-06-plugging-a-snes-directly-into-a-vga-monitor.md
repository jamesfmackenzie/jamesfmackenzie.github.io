---
layout: post
title: "Plugging a SNES Directly Into a VGA Monitor Actually Works"
summary: |-
  A RetroTINK HD15 dongle, a monitor with a rare 15kHz-capable VGA input, and a hunch that shouldn't have paid off — but did.
date: '2026-09-06 23:45:00'
image: retrotink-hd15-dongle-snes-full.jpg
tags: [Nintendo, Retrogaming]
---

I bought a [RetroTINK HD15 Dongle](https://www.retrotink.com/shop/hd15-dongle-snes) mainly for a boring, sensible reason: to get clean RGB video out of my SNES and into my [Datapath VisionAV-HD capture cards]({% link _hardware/datapath-visionav-hd.md %}), whose DVI-I inputs happily accept VGA-format analog RGB with a simple adapter. The dongle plugs into the SNES's multi-out AV connector and breaks the video out to a standard HD15/VGA connector — it's not an upscaler, just an active signal conditioner, built to feed something like a RetroTINK-4K.

![The RetroTINK HD15 dongle for SNES](/img/retrotink-hd15-dongle-snes-full.jpg)

<div class="image-row">
  <img src="/img/retrotink-hd15-dongle-snes-connector.jpg" alt="The dongle's SNES multi-out connector">
  <img src="/img/retrotink-hd15-dongle-vga-connector.jpg" alt="The dongle's HD15/VGA connector">
</div>

But I had a second, much less sensible hope: that it might work plugged *directly* into a VGA monitor, no scaler in between at all.

### Why that shouldn't work

The SNES outputs a 15kHz video signal. Almost every VGA monitor made in the last twenty-five years wants 31kHz or higher and will simply refuse the signal — out-of-range error, blank screen, nothing. That's the entire reason scalers and upscalers exist in this hobby.

So before buying anything, I went looking for whether my specific monitor — a BenQ RL2455HM — was one of the rare exceptions. It turns out it is: the [15khz.miraheze.org](https://15khz.miraheze.org/wiki/Snapshot.csv?action=raw) community database — a crowdsourced list of exactly which modern-ish monitors will actually sync to 15kHz — lists the RL2455HM as fully 15kHz-capable on its VGA input, previously tested there with a Sega Mega Drive.

Even with that box checked, there was a second problem. The RetroTINK dongle outputs composite sync on pin 13 only — pin 14, where a monitor expecting proper RGBHV would look for a separate vertical sync signal, isn't driven at all. The documented setup for the RL2455HM on that same wiki page used a **SyncStrike** adapter (a sync separator) to bridge that gap, along with manually switching the monitor's input colour mode from YUV to RGB and forcing 4:3 in its on-screen menu.

Reading all that, my honest expectation was: plausible with the right chain, not plausible with just the dongle and a bare cable.

### It just worked

I tried it anyway.

![Star Fox running on the BenQ RL2455HM via the RetroTINK dongle](/img/retrotink-snes-starfox-cart-and-screen.jpg)

Star Fox booted straight up — title screen, then gameplay, no drama, no out-of-range error, no missing sync.

<div class="image-row">
  <img src="/img/retrotink-snes-starfox-title-screen.jpg" alt="Star Fox title screen on the BenQ monitor">
  <img src="/img/retrotink-snes-starfox-gameplay.jpg" alt="Star Fox gameplay on the BenQ monitor">
</div>

I also tried a Japanese Super Mario World cartridge — this particular SNES has a region-free mod (a whole separate story: [I Just Wanted to Power My PAL SNES in America…]({% post_url 2026-09-06-i-just-wanted-to-power-my-pal-snes-in-america %})), so it happily ran straight through to a Japanese level-name screen too.

![A Japanese Super Mario World cartridge running on the same setup](/img/retrotink-snes-super-mario-world-jp.jpg)

### What I still don't know

I'm genuinely not sure yet whether this worked *because* I already had a sync separator somewhere in the chain, or whether the RL2455HM turns out to be more forgiving about combined sync than the documented setup assumes. That's worth pinning down properly before I call this a clean, repeatable result — I'll update this once I've confirmed exactly what was in the signal path.

Either way: a $20-ish dongle, a monitor most people wouldn't think twice about, and a "we'll see" that actually paid off.

### Related on this site

- [Super Nintendo (SNES)]({% link _hardware/super-nintendo.md %}) — hardware reference page
- [I Just Wanted to Power My PAL SNES in America…]({% post_url 2026-09-06-i-just-wanted-to-power-my-pal-snes-in-america %}) — the same console's other story
- [Datapath VisionAV-HD]({% link _hardware/datapath-visionav-hd.md %})
