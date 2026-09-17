---
layout: post
title: ATi Radeon X700 Pro
summary: Notes on the Radeon X700 Pro — a mid-2000s mainstream DX9 card that froze Windows 98 outright in my testing, and has since developed problems of its own.
date: '2025-12-28 21:00:00'
tags: [3D Graphics, ATi, PC]
hero: connect3d-radeon-x700-pro-front.jpg
hero_alt: My Connect3D Radeon X700 Pro
---

The X700 Pro sits a step below the [X800 XL]({% link _hardware/ati-radeon-x800-xl.md %}) in ATi's mid-2000s lineup — a mainstream PCI Express card rather than a flagship. On paper it's a solid late-DX9 option. In practice, mine has given me nothing but trouble, first in testing and now in old age.

### What it is

The X700 Pro is a PCI Express card built on ATi's RV410 GPU, launched in 2004 as a mainstream option below the X800 series. It has 8 pixel pipelines on a 128-bit memory interface, paired with 128MB or 256MB of GDDR3, and was positioned as a card fast enough for real DirectX 9 gaming without the power and heat of the flagship cards above it.

### Specifications

- **Released:** 2004
- **GPU:** RV410
- **Pixel pipelines:** 8
- **Memory:** 128MB or 256MB GDDR3, 128-bit bus
- **Core clock:** around 425MHz

### My card

Mine is the 128MB Connect3D Radeon X700 Pro.

<div class="image-row">
  <img src="/img/connect3d-radeon-x700-pro-front.jpg" alt="Connect3D Radeon X700 Pro, front">
  <img src="/img/connect3d-radeon-x700-pro-back.jpg" alt="Connect3D Radeon X700 Pro, back">
</div>

### Windows 98

Not a success story. Testing it in a [Dell Dimension E520]({% link _hardware/dell-dimension-e520.md %}), the X700 Pro froze Windows 98 outright as soon as the Catalyst driver loaded — the exact same failure as the [Radeon X600]({% link _hardware/ati-radeon-x600.md %}) on the same machine, with no difference between Catalyst 6.2 and 9.0c. See the [full write-up]({% post_url 2026-03-30-i-tried-to-turn-a-dell-dimension-e520-into-a-windows-98-retro-pc %}) for the rest of that machine's driver troubleshooting.

### Showing its age

The years haven't been kind to this card since. The fan bearings have worn out, leaving an audible grinding noise, and both text and graphics-mode video are now corrupted — pointing at a VRAM fault.

![Connect3D Radeon X700 Pro graphics corruption](/img/connect3d-radeon-x700-corrupted-graphics.jpg)

It needs proper attention before it's useful for anything again.

### Pros

- solid mainstream DX9 performance for its era
- modest power and heat compared with the flagship X800 cards

### Cons

- froze Windows 98 outright in my testing — a Windows XP card, not a Win98 one
- mine now has a failing fan and VRAM corruption

### Related on this site

- [ATi]({% link _hardware/ati.md %})
- [ATi Radeon X600]({% link _hardware/ati-radeon-x600.md %})
- [ATi Radeon X800 XL]({% link _hardware/ati-radeon-x800-xl.md %})
- [Dell Dimension E520]({% link _hardware/dell-dimension-e520.md %})
