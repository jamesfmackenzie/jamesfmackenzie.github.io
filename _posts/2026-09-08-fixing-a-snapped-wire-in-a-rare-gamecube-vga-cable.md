---
layout: post
title: "Fixing a Snapped Wire in a Rare GameCube VGA Cable"
date: '2026-09-08 10:15:00'
summary: |-
  A hand-hacked GameCube VGA cable from the early 2000s lost its red channel. Working out what it even was turned out to be impossible — fixing it turned out to be easy.
image: gamecube-vga-mario-sunshine-clean-colour.jpg
tags: [Nintendo, Retrogaming]
---

I've had a GameCube VGA cable since somewhere around 2002–2004. It's not an official product — it's a hand-hacked job, built by cutting the TV end off one of Nintendo's own digital AV cables and wiring on a VGA connector instead. It only works with the original DOL-001 GameCube, because that's the only revision with a digital AV port to plug into. It's old enough, and rare enough, that I'd rather fix it than replace it.

Recently the colours went wrong. Everything played fine, but the picture looked off — like the red channel had simply stopped existing.

### What the cable even is

Officially, Nintendo made two cables for the GameCube's digital AV port: **DOL-009**, which ends in a D-terminal connector, and **DOL-010**, which ends in three RCA plugs for component video. Nintendo's own description of the pair is that they're "essentially the same internal component but with different connectors." My memory says this one started life as a D-terminal cable, but I wanted to check rather than just trust that.

It turns out you can't check. DOL-009 and DOL-010 use the *exact same* connector on the GameCube end — the two cables only differ at the TV end, and that's precisely the part that got cut off and replaced with VGA. I opened the cable up looking for a model number anyway, and found one: the wire itself is **Taiyo-branded, marked `E676647-WH`**. That looked promising until I worked out what it actually is — a UL file number, which certifies the wire stock, not the finished Nintendo product. It would print exactly the same regardless of which of the two cables Nintendo built from that reel. So: still unknown. Best guess remains memory — a repurposed D-terminal cable — and it'll probably stay a guess forever.

### The actual fault

With the mystery of its origins unsolved, I opened up the VGA end to look for the more solvable mystery: the missing red. It didn't take long. The red wire had snapped clean off inside the connector, fully disconnected from HD15 pin 1 — the VGA pin red lives on. There was still a blob of solder sitting on the pin with a stub of the original wire in it, but the wire itself had separated completely. No continuity, no red channel, no surprise.

![The re-soldered VGA connector, wires trimmed and reattached to their pins](/img/gamecube-vga-cable-resoldered-pins.jpg)

Fixing it should have been a two-minute job — strip the wire, re-solder it to the pin — except the snapped red wire was now the shortest wire in the bundle by a fair margin. Re-attaching it as-is would have put tension on the joint the moment the connector got handled at all. So every other wire had to be cut back and re-stripped to match the red wire's new, shorter length before any of them went back on their pins. The result looks like a crime scene. It measured clean on the multimeter afterwards, though — no shorts anywhere — which is the only opinion that actually matters here.

### It works

Plugged it into a real GameCube, into the BenQ monitor, and loaded up Super Mario Sunshine. Full colour, red channel very much present — Mario's hat, his shirt, his nose, all exactly where they should be.

![Mario mid-level, colours clean across the whole scene](/img/gamecube-vga-mario-sunshine-action.jpg)

![Mario Sunshine running in full colour after the repair](/img/gamecube-vga-mario-sunshine-working.jpg)

![A wider shot showing accurate colour across the whole scene](/img/gamecube-vga-mario-sunshine-clean-colour.jpg)

A snapped wire is about as boring a fault as electronics gets. But this is a cable I can't buy again — whatever it started life as, it isn't for sale anywhere — so it was worth the ugly repair to keep it working rather than let a two-inch length of copper end its life.
