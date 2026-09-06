---
layout: post
title: 3Dfx
summary: An overview of 3Dfx's graphics hardware and the pages on this site — the Voodoo line that made 3D acceleration mainstream, and the Glide API that still ties games to it.
date: '2024-08-29 11:33:00'
tags: [3Dfx Voodoo, Graphics Cards, PC]
redirect_from:
  - /hardware/3dfx-voodoo/
---

![3Dfx Original Logo](/img/3dfx-original-logo-design.png)

3Dfx Interactive built the graphics hardware that made 3D acceleration mainstream on the PC. The original **Voodoo Graphics** (1996) was a 3D-only add-on card, paired with your existing 2D card over a pass-through cable, and its **Glide API** — far simpler to target than Direct3D or OpenGL at the time — meant a generation of games were written to it directly. That is why Voodoo cards are still sought after: for a lot of late-90s titles, real 3Dfx hardware is the most authentic way to run them.

**Voodoo 2** (1998) added SLI, splitting the frame across two cards. **Voodoo 3** (1999) finally merged 2D and 3D onto one board. But the company over-extended, and Nvidia acquired what was left in 2000.

### 3Dfx cards

<ul>
{% assign dfx_cards = site.hardware | sort_natural: "title" %}
{% for card in dfx_cards %}
  {% if card.tags contains "3Dfx Voodoo" and card.url != "/hardware/3dfx/" %}
  <li><a href="{{ card.url }}">{{ card.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 3Dfx guides

<ul>
{% for page in site.howto %}
  {% if page.tags contains "3Dfx Voodoo" %}
  <li><a href="{{ page.url }}">{{ page.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### 3Dfx posts

<ul>
{% for page in site.posts %}
  {% if page.tags contains "3Dfx Voodoo" %}
  <li>
    {% if page.layout == "youtube" %}<img src="/img/youtube-icon.png" style="display: inline-block; vertical-align:middle;" />
    {% elsif page.layout == "tweet" %}<img src="/img/twitter-icon.png" style="display: inline-block; vertical-align:middle;" />
    {% endif %}<a href="{{ page.url }}">{{ page.title }}</a> - {{ page.date | date_to_string }}
  </li>
  {% endif %}
{% endfor %}
</ul>
