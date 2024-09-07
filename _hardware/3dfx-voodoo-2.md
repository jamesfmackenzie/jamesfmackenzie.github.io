---
layout: post
title: 3Dfx Voodoo 2
summary: 
date: '2024-08-29 11:33:00'
#tags: [3Dfx, Graphics Cards, PC, Voodoo]
tags: [Graphics Cards]
---

![3Dfx Voodoo2](/img/hardware/3dfx-voodoo-2-board.jpg)

The legendary Voodoo2 is a PC 3D accelerator from 3Dfx. Released in February 1998 as a replacement for the original Voodoo Graphics accelerator, the card runs at a chipset clock rate of 90 MHz and uses 100 MHz EDO DRAM.

As with the original Voodoo, the Voodoo2 is a dedicated 3D accelerator, and has to be used in conjunction with a conventional 2D graphics card. It requires an external pass-through VGA cable connected from the 2D card to the Voodoo card's passthrough VGA port.

The Voodoo2 comes in two models: one with 8 MB RAM and one with 12 MB RAM. The 4 MB framebuffer on both cards support a maximum screen resolution of 800 × 600, while the increased texture memory on the 12 MB card allows more detailed textures.

The Voodoo2 also introduced Scan-Line Interleave (SLI) capability. In SLI mode, two Voodoo2 boards installed in a PC run in parallel, with each unit drawing half the lines of the display. Voodoo2 SLI not only doubles rendering throughput, it also increases the total framebuffer memory, increasing the maximum supported screen resolution to an impressive (for the time) 1024 × 768.

3Dfx's Glide API played an essential role in the card's success, with many PC games tailored towards Glide versus other 3D APIs like Direct3D or OpenGL. Long after the chipset's obsolescence, 3Dfx cards still remain in high demand due to their unique ability to run Glide games.

The Voodoo2 enjoyed remarkably long usage in many computer systems, as a Voodoo2 SLI setup was competitive with newer cards like NVIDIA's RIVA TNT2, Matrox's Millennium G400, and even NVIDIA's GeForce 256.

# Drivers

Add drivers here.

# Videos

<ul>
{% for post in site.posts %}
  {% if post.tags contains "Voodoo" %}
    {% if post.layout == "youtube" %}
<li>
  <img src="/img/layout/youtube-icon.png" style="display: inline-block; vertical-align:middle;" />
  <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
</li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

# Tweets

<ul>
{% for post in site.posts %}
  {% if post.tags contains "Voodoo" %}
    {% if post.layout == "tweet" %}
<li>
  <img src="/img/layout/twitter-icon.png" style="display: inline-block; vertical-align:middle;" />
  <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
</li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>



