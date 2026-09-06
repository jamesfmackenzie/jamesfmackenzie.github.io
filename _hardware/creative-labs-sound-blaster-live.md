---
layout: post
title: Creative Labs Sound Blaster Live!
summary: My take on the Sound Blaster Live! — a strong Windows card, a compromised DOS card, and a handy SBEMU target on machines too modern for real DOS audio.
date: '2024-08-29 11:33:00'
tags: [Creative Labs, PC, Sound, Sound Cards]
---

![Creative Sound Blaster Live! Value (CT4670)](/img/posts/creative-labs-sound-blaster-live-value-ct4670.jpg){: width="600"}

{% include image-credit.html
  source_url="https://commons.wikimedia.org/wiki/File:Creative_Labs_Sound_Blaster_Live!_Value_(CT4670).jpg"
  source_label="Kronach Fotos via Wikimedia Commons"
  license_url="https://creativecommons.org/licenses/by-sa/4.0/"
  license_label="CC BY-SA 4.0"
%}

The Sound Blaster Live! isn't the neatest answer to any one retro-audio problem, but it's hard to ignore. It was everywhere in late-90s and early-2000s Windows PCs, it still turns up for pocket change, and it keeps becoming relevant again whenever a later PCI system gets pushed into DOS territory.

### What it is

A late-1990s PCI sound card from Creative, built around the EMU10K1. It was one of the most common Windows gaming upgrades of its day. Today it's interesting in two roles: a period-correct Windows 98/XP card, and a target device for [SBEMU]({% link _software/sbemu.md %}) on machines too modern for real DOS audio.

### My take

For Windows 98 and XP it's an easy pick — common, cheap, well supported. For DOS it depends what you're doing:

- for straightforward native DOS audio I'd reach for a [Yamaha YMF724]({% link _hardware/yamaha-ymf724.md %}) instead — it's cleaner and more predictable across a range of hardware
- `SBINIT.COM` can coax the Live! into working in DOS, but the result varies a lot with the host platform
- on a machine that's simply too new for native DOS sound, SBEMU can emulate Sound Blaster audio through the Live! and get a lot of DOS games running anyway — which is the main reason to keep one around now

### Pros

- everywhere, and cheap
- a strong Windows 98 and XP card
- works as an SBEMU target on modern PCI machines

### Cons

- not a first choice for clean native DOS audio
- DOS behaviour depends heavily on the host platform

### Related on this site

- [SBEMU]({% link _software/sbemu.md %})
- [How To Install SBEMU on a Bootable USB Stick]({% post_url 2023-03-22-how-to-install-sbemu-on-bootable-usb-stick %})
- [SBEMU Just Killed Your DOS Gaming PC]({% post_url 2023-03-12-sbemu-just-killed-your-dos-gaming-pc %})
- [Yamaha YMF724]({% link _hardware/yamaha-ymf724.md %})
