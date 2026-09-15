---
layout: post
title: Half-Life 2 and Portal on Raspberry Pi
date: '2026-09-14 23:00:00'
tags: [Projects, Raspberry Pi, Retrogaming, Videogames]
status: completed
---

Valve's Source Engine — the engine behind Half-Life 2, Counter-Strike, and Portal — has its full source available via the [nillerusr/source-engine](https://github.com/nillerusr/source-engine) ARM64 fork. Having the actual source code means it can, at least in theory, be built for any platform you want. Including a Raspberry Pi 5.

### Project Notes

Status | Completed
Goal | Build the Source Engine natively on a Raspberry Pi 5, no emulation, and get Half-Life 2 — then Portal — running on it.

Half-Life 2 came first: build tools, dependencies, then the engine itself, cross-compiled straight on the Pi. That build took 25 minutes 12 seconds on the Pi 5's CPU. Game assets aren't part of the source — those got copied over separately from an Ubuntu PC with Steam installed.

Portal followed the same process, just pointed at a different build target, and came together faster: 18 minutes. Both needed a graphics-settings pass once running — default settings are choppy on the Pi 5's GPU, so resolution and detail had to come down before either game was properly playable, with texture detail the one setting worth keeping high.

Powering it all: the [Raspberry Pi 5]({% link _hardware/raspberry-pi-5.md %}) itself, its official 27W USB-C supply, and the official Active Cooler to keep it fed and cool through two from-scratch compiles.

More details:

- [I Made Half-Life 2 Run Natively on a Raspberry Pi 5]({% post_url 2026-09-14-i-made-half-life-2-run-natively-on-a-raspberry-pi-5 %}) — the full story
- [How to Install Half-Life 2 on Raspberry Pi]({% link _howto/how-to-install-half-life-2-halflife-2-on-raspberry-pi.md %}) — the step-by-step guide, covering Portal too
- [I Made Half-Life 2 Work on Raspberry Pi!]({% post_url 2024-10-19-i-made-halflife-2-half-life-2-work-on-raspberry-pi %}) — the original story video
- [How To Install Half-Life 2 (and Portal!) on Raspberry Pi]({% post_url 2024-11-02-how-to-install-half-life-2-and-portal-video %}) — the how-to video
- [Raspberry Pi 5]({% link _hardware/raspberry-pi-5.md %})

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/-S_J-3CJsPU?rel=0"
allowfullscreen class="youtube-video"></iframe>
</div>

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/ipQ1trbWeX0?rel=0"
allowfullscreen class="youtube-video"></iframe>
</div>

<br />
