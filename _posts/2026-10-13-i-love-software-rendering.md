---
layout: post
title: "I Love Software Rendering"
date: '2026-10-13 01:00:00'
summary: "Sharp pixels, gritty colour banding, and DOS games running at resolutions their own era couldn't manage. Why I still prefer the software renderer, and why it needs a fast PC."
tags: [MS-DOS, PC, Posts, Retrogaming, Videogames]
hero: software-rendering-quake-action-gib.png
hero_alt: "An ogre caught by a rocket in a Quake corridor, square particles flying through the air"
hero_caption: "Quake in its DOS software renderer. Look at those square particles!"
---

I love software rendering. The best DOS experience I've had in a long while was Quake in its software rendering mode at 800×600, running at a **locked** 60fps on [my Dell OptiPlex 380]({% post_url 2025-12-28-the-ugly-dell-optiplex-that-became-my-dream-retro-gaming-pc %}). It's one of the best-looking things I've seen a DOS game do.

But that's not how most people remember these games looking. In the 90s you either ran them in software at a low resolution, or you bought a 3D card and played the accelerated version. Today there's a third option: run the software renderer on a machine fast enough to push it at resolutions that *nobody* could use back then.


### What software rendering is

In a software-rendered game, the CPU draws every pixel. There's no 3D card involved: the game works out each frame in its own code and writes it straight to video memory. Doom, Duke Nukem 3D, Blood and the original Quake all work this way.

When 3D cards arrived, many games got accelerated versions. GLQuake came after Quake, and Blood and Tomb Raider got 3dfx modes too. These versions hand the drawing off to the graphics card, and they look different.


### Why I like the look

**It's sharp.** Software renderers generally sample textures pixel by pixel, so every texel stays a crisp square. Early 3D cards smoothed textures with bilinear filtering, which looked impressive in 1997 but turns everything soft and blurry to my eye now.

![A Quake rune on a wall, every texel a crisp square](/img/software-rendering-quake-rune.png)

**It's gritty.** Most of these games ran in 256 colours, with lighting done through lookup tables into that palette. Shadows fall off in visible steps rather than smooth gradients. Technically that's colour banding, a limitation. In practice it gives the games a rough, grimy texture that I really like, and that hardware rendering smooths away.

![Lava glowing through openings in a grimy stone wall in Quake](/img/software-rendering-quake-lava-window.png)

![An ogre with a chainsaw on a ledge above a lava pool in Quake](/img/software-rendering-quake-lava-ogre.png)

**It's how the games were built.** Quake was released with its software renderer, and GLQuake followed. Doom and the Build engine games were designed around their software renderers from the start.

It isn't always the better option. When I got [a Voodoo 2 running in a modern PC]({% post_url 2026-08-30-voodoo-2-on-a-modern-pc %}), Blood ran fast in its 3dfx mode, but the VESA software modes were the better-looking option. Tomb Raider went the other way: its underwater sections look noticeably better [accelerated]({% link _software/tomb-raider.md %}) than in the DOS software renderer. So it's a preference, not a rule. But for most of the DOS games I care about, I'd pick the software renderer.

It's not just nostalgia, either. Ion Fury, a Build engine game from 2019, still ships with a software renderer.


### The catch: it needs a fast PC

Software rendering scales with the CPU. Every extra pixel is work for the processor, so the high VESA resolutions that many late DOS games offered were well beyond the hardware of the day.

Luckily for us, modern hardware can power through. On my OptiPlex 380, Quake at 800×600 holds a locked 60fps. However, the heaviest games push even very fast machines. In [his video on the Portwell RUBY-9719](https://www.youtube.com/watch?v=6eew0uRZ84E), Rasteri shows Build engine games needing far more power at high resolutions, to the point where even a 3.3GHz quad-core Xeon "isn't quite enough to run Shadow Warrior at full 1600 by 1200".

So if you want to see these games at their best, you want the fastest machine you can get that still runs them.


### Why native DOS?

Of course there are other ways to get software rendering on a modern PC. Source ports of Doom and Quake will happily run their software renderers on Windows. But that's not what I'm after. I want these games *as they were released*, running the original executables, at their *most authentic best*.

On a modern machine, the most obvious way to do this is DOSBox — and for most DOS games it's brilliant. However, DOSBox emulates the CPU, and that hurts us in performance. Every extra pixel is more instructions to emulate, so the further you push the resolution, the harder the emulator has to work to keep up.

On real hardware there's no emulation layer. A Core 2 runs Quake's own code directly, and at 800×600 my OptiPlex 380 doesn't even break a sweat.

So the answer is a real, fast PC, running native DOS.


### Games worth trying

- **Quake**, in software at 800×600 or higher.
- **Blood**, whose VESA software modes I actually prefer to its 3dfx mode.
- **Duke Nukem 3D**, which also has high-resolution VESA modes.
- **Screamer**, which looks great at 640×480.

<div class="image-row">
  <img src="/img/software-rendering-duke3d-street.png" alt="A city street in Duke Nukem 3D's first level">
  <img src="/img/software-rendering-duke3d-pig-cop.png" alt="A Pig Cop in a store in Duke Nukem 3D">
</div>


### One final challenge: sound

So this is easy, right? Just boot to FreeDOS and play those great DOS games.

Not quite. These games need a sound card they can talk to directly, and modern PCs don't have one. But that's [a story for another day]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %}).


### Related on this site

- [Get PCI Sound Cards Working on a Modern PC]({% link _projects/get-pci-sound-cards-working-on-a-modern-pc.md %}) — the project this post starts
- [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %})
- [The Ugly Dell That Became My Dream Retro Gaming PC]({% post_url 2025-12-28-the-ugly-dell-optiplex-that-became-my-dream-retro-gaming-pc %})
- [I made 3Dfx Voodoo2 work on a modern PC!]({% post_url 2026-08-30-voodoo-2-on-a-modern-pc %})
- [Tomb Raider]({% link _software/tomb-raider.md %})
- [Doom on a Core i7 PC in native DOS, with SBEMU]({% post_url 2023-03-07-you-can-run-doom-on-a-core-i7-pc-in-native-dos-with-sbemu %})
