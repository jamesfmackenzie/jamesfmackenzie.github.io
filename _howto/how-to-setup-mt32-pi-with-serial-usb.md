---
layout: post
title: "How to Connect mt32-pi Over USB Serial"
summary: The easiest way to wire an mt32-pi to a retro gaming PC — a plain USB-to-serial cable instead of the old RS232-to-TTL converter and GPIO wiring.
date: '2021-07-25 12:00:00:00'
image: mt32-pi-serial-midi-hardware-connection.jpg
tags: [How To, MIDI, MS-DOS, Retrocomputing, Retrogaming, Sound]
---

The [main mt32-pi guide]({% link _howto/how-to-setup-mt32-pi.md %}) connects the Pi to a DOS PC by wiring an **RS232-to-TTL converter module** onto the Pi's GPIO header. From release **v0.10.0**, mt32-pi supports **USB serial devices** directly — so you can drop the converter and the wiring and just use a plain USB-to-serial cable.

### What you need

- A **USB-to-serial cable** (e.g. <a href="https://www.amazon.com/gp/product/B00IDSM6BW" target="_blank">this one</a>)
- A **null-modem serial adapter** (e.g. <a href="https://www.amazon.com/gp/product/B075XGRLXW" target="_blank">this one</a>)

Plug the USB end into the Pi and the serial end — via the null-modem adapter — into the PC's serial port.

### Set the baud rate

Edit <a href="https://github.com/dwhinham/mt32-pi/wiki/Configuration-file" target="_blank"><code>mt32-pi.cfg</code></a> on the Pi's microSD card. A DOS PC serial port can't run at MIDI's standard 31250 bps, so tell mt32-pi to use 38400 — the closest "PC standard" rate. Replace:

```
usb_serial_baud_rate = 31250
```

with:

```
usb_serial_baud_rate = 38400
```

### Everything else is the same

The rest of the setup is identical to the [main guide]({% link _howto/how-to-setup-mt32-pi.md %}): run **SoftMPU** on the DOS PC pointed at `COM1`, configure your games for Roland MT-32, Roland Sound Canvas or General MIDI on **port 330**, and switch synth modes from the front panel. (As with any SoftMPU setup, games that use a DOS extender — Doom, for example — won't work over serial MIDI.)

I tested it with **The Secret of Monkey Island**. Works great.

### Watch on YouTube

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/SxMjDsT9rEo?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

### More MIDI articles

{% include midi.md %}
