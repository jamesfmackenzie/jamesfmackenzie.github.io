---
layout: post
title: ATi Small Wonder Graphics Solution
summary: A look at the ATI Small Wonder Graphics Solution, the earlier and rarer sibling of the Graphics Solution SR, with the same CGA-on-MDA trick.
date: '2025-08-19 18:47:00'
tags: [ATi Graphics, Graphics Cards, PC]
---

![ATI Small Wonder Graphics Solution](/img/posts/ati-small-wonder-graphics-solution-v1.png)

The Small Wonder Graphics Solution is ATI's first real graphics card, released not long after the company was founded in 1985, and it's the earlier sibling to the [Graphics Solution SR]({% link _hardware/ati-graphics-solution-sr.md %}) I run on my [Amstrad PC1640]({% link _hardware/amstrad-pc1640.md %}). Same core idea, simpler execution: an 8-bit ISA card that speaks CGA, MDA, and Hercules, and can even fake CGA colour as grayscale on a monochrome monitor.

### What it does

- CGA graphics and text modes
- MDA and Hercules monochrome modes (including Hercules' 720×348 high-res graphics)
- CGA-on-MDA grayscale emulation, controlled via DIP switches — the same trick the later Graphics Solution SR is built around
- standard 8-bit ISA, so it fits an original PC, XT, or early AT

### How it compares to the Graphics Solution SR

They solve the same problem — colour CGA games on a monitor that can't actually display colour — but the SR is the more refined version, with cleaner emulation modes and better surviving documentation. The Small Wonder is the rougher, earlier attempt: interesting mainly because it's where ATI started before it became a serious player in PC graphics, long before EGA Wonder, VGA Wonder, and eventually Radeon.

### Related on this site

- [ATi]({% link _hardware/ati.md %})
- [ATi Graphics Solution SR]({% link _hardware/ati-graphics-solution-sr.md %})
