---
layout: post
title: "HP Compaq t5710 – Using a PS/2 Splitter Cable"
date: '2021-11-13 23:30:00:00'
summary: The PS/2 port on the HP Compaq t5710 supports a Y splitter cable, so you can connect keyboard and mouse simultaneously.
image: t5710-monoprice-ps2-y-splitter-cable.jpg
tags: [MS-DOS, PC, Posts, Retrocomputing, Retrogaming]
---

![](/img/posts/t5710-monoprice-ps2-y-splitter-cable.jpg)

I've had several queries on using a PS/2 splitter cable to connect keyboard and mouse to the [t5710]({% post_url 2021-07-11-hp-compaq-t5710-review-great-for-dos-and-windows-98-gaming %}) simultaneously. The good news? It works great. I purchased <a href="https://www.ebay.com/itm/392826957006" target="_blank">this Monoprice cable</a> and have keyboard/mouse working with the following setup:

* Connect your PS/2 keyboard to the *Mouse* connector and your PS/2 mouse to the *Keyboard* connector (yes, it's backwards – perhaps a manufacturing error with the splitter cable)

* <a href="https://www.parkytowers.me.uk/thin/hp/bios.shtml" target="_blank">BIOS 786R1</a> (Version 1.07, Revision A):

![](/img/posts/t5710-bios-107-786r1.png)

* Set <code>PS2 KB/MS</code> to *Keyboard*:

![](/img/posts/t5710-bios-ps2-y-splitter-cable-keyboard-mouse.png)

Good luck!


### More t5710 articles

{% include t5710.md %}



