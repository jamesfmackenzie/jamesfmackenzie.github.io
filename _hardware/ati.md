---
layout: post
title: ATi
summary: An overview of ATi's graphics hardware and the pages on this site — from its mid-1980s multi-standard cards, through the Radeon era, to the AMD buyout and the modern Radeons that followed.
date: '2024-08-29 11:33:00'
tags: [ATi Graphics, Graphics Cards, PC]
---

ATi (Array Technology Inc., founded in Toronto in 1985) spent its first decade building a reputation for graphics cards that were more flexible than IBM's reference designs — driving several display standards from a single board — before the Rage and then Radeon lines made it one of the two names that mattered in PC 3D graphics.

**AMD acquired ATi in 2006** and retired the ATi brand name in 2010. "Radeon" carried on as AMD's graphics brand, so the modern RX cards are, by lineage, the same family.

This page groups the ATi and Radeon hardware covered on this site across that whole span.

### Early ATi cards

The mid-1980s cards are the interesting ones for a collector: multi-standard boards that could drive CGA, Hercules and mono displays at a time when most cards did exactly one thing.

<ul>
{% assign ati_cards = site.hardware | sort_natural: "title" %}
{% for card in ati_cards %}
  {% if card.tags contains "ATi Graphics" and card.url != "/hardware/ati/" %}
  {% unless card.title contains "Radeon" %}
  <li><a href="{{ card.url }}">{{ card.title }}</a></li>
  {% endunless %}
  {% endif %}
{% endfor %}
</ul>

### ATi Radeon

The Radeon line is where ATi cards start turning up in retro PC *building* rather than retro *collecting* — late DirectX 9 GPUs that make strong bridge cards for machines spanning Windows 98 through Windows XP.

<ul>
{% for card in ati_cards %}
  {% if card.tags contains "ATi Graphics" and card.title contains "Radeon" %}
  {% unless card.title contains "RX" %}
  <li><a href="{{ card.url }}">{{ card.title }}</a></li>
  {% endunless %}
  {% endif %}
{% endfor %}
</ul>

### Modern era

Well past the point where calling it "ATi" makes literal sense — but it is the same Radeon lineage, and these turn up here for their own reasons rather than as retro hardware.

<ul>
{% for card in ati_cards %}
  {% if card.tags contains "ATi Graphics" and card.title contains "RX" %}
  <li><a href="{{ card.url }}">{{ card.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>

### ATi posts

<ul>
{% for post in site.posts %}
  {% if post.tags contains "ATi Graphics" %}
  <li>
    {% if post.layout == "youtube" %}<img src="/img/layout/youtube-icon.png" style="display: inline-block; vertical-align:middle;" />
    {% elsif post.layout == "tweet" %}<img src="/img/layout/twitter-icon.png" style="display: inline-block; vertical-align:middle;" />
    {% endif %}<a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
  </li>
  {% endif %}
{% endfor %}
</ul>
