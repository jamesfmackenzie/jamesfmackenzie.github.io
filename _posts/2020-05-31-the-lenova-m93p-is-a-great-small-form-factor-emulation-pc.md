---
layout: post
title: The Lenovo M93p is an awesome mini emulation PC
date: '2020-05-31 00:02:30:00'
summary: Thoughts on the Lenovo M93p Tiny as a small form factor emulation machine
tags: [How To, Videogames, Retrogaming]
---

![](/img/posts/lenovo-m93p.jpg)

In search of a thin-and-light retrogaming device, I recently purchased a <a href="https://www.lenovo.com/us/en/desktops/thinkcentre/m-series-tiny/m93-m93p/" target="_blank">Lenovo ThinkCenter M93p Tiny Desktop</a> from eBay for ~$100. The form factor looks great under a TV and the spec handily beats most Single Board Computers out there:

- Intel Core i5-4570T (2 cores @2.9GHz)
- 8GB DDR3 1600MHz RAM
- 500GB HDD
- Intel HD Graphics 4600

The on-board graphics do hold it back a little vs a dedicated GPU, but there are always trade-offs in a form factor like this. The good news: emulators usually lean heavily on CPU and light on GPU. There's more than enough grunt here for a great emulation experience and even some light PC gaming.

4K resolution is supported, but only at 30Hz. Move a touch lower to 1440p and you get full 60Hz. The recommended gaming resolution for this device is 1080p.

## Performance Summary

SNES, Genesis | Perfect | Runs perfectly, even with filters and upscaling. Expect anything older than this to run perfectly too
PlayStation | Perfect | Full speed at PlayStation native and 2x native resolution
PSP | Perfect | Full speed at native and 2x native resolution
Dreamcast | Perfect | Full speed even with 720p upscale
Gamecube/Wii | Perfect | Expect full speed at native GC resolution. Pushing to 2x native works well on some games but others struggle
Saturn | Good | 2D games run perfectly at full speed. 3D games like Sega Rally or Panzer Dragoon struggle a little

## Upgrade Options

There's space inside for one 2.5" SATA HDD. My unit arrived with a 500GB, 7200rpm drive - but you could easily upgrade to SSD

Max memory is 16GB (2x 8GB PC3-12800 DDR3 SODIMMs). My unit arrived with 8GB which is more than enough for retrogaming - with the possible exception of Cemu

You can upgrade the CPU. Standard upgrade options are the Core i7-4765T (4 cores @2.0GHz) and the Core i7-4785T (4 cores @2.2GHz). Some Xeon CPUs are compatible too. Find the full parts list <a href="https://download.lenovo.com/parts/ThinkCentre/m93_m93p_tiny_07012016.pdf" target="_blank">here</a>.

If you want to go off-road in pursuit of max performance, you can get <a href="https://www.ebay.com/itm/293555594492" target="_blank">this beast</a>. It's a laptop Core i7-4750HQ CPU rehoused to fit a Desktop CPU socket. You'll need an upgraded 90W power brick, but the result is a much faster 4-core CPU and (as a bonus) a GPU upgrade to Intel Iris Pro Graphics 5200 - which roughly doubles the 3D graphics capability. The stock cooling seems to be sufficient - learn more <a href="https://forum.kodi.tv/showthread.php?tid=346041" target="_blank">here</a>.

<!---
## Dreamcast Performance

Notes on ReDream vs Reicast/Flycast

## Gamecube Performance

Native OK, 720p nearly OK but some slowdown

## PlayStation 2 Performance

TBD
--->
