---
layout: post
title: Fixing an Xbox Series X That Kept Shutting Down
date: '2026-09-21 09:30:00'
tags: [Consoles, Projects, Videogames, Xbox]
status: completed
hero: xbox-series-x-dried-paste-macro.jpg
hero_alt: The Xbox Series X APU die, covered in completely dry, cracked thermal paste
---

My Xbox Series X started powering itself off mid-game — but only in some games, which ruled out most of the easy explanations straight away. Working out why turned into a proper electrical and thermal diagnosis, ending with the console fully stripped down to the bare APU die.

### Project Notes

Status | Completed
Goal | Diagnose and fix an Xbox Series X that shut itself down during certain games, without just replacing parts on a guess.

Systematic testing across a range of games narrowed the fault down to something load-dependent rather than simply "3D games bad" — Forza Horizon 2 ran complex 3D graphics indefinitely, while Minecraft's bursty startup killed the console almost instantly. A teardown and PSU voltage test ruled out an outright dead power supply, and a control test after reassembly looked briefly like a fix (connector reseating) before extended testing proved the fault was still there, just needing longer to show up.

That longer-to-show-up behavior turned out to be the real clue: a hot restart failed almost instantly, while a cold start bought about twenty minutes — a classic heat-soak profile. Stripping the console all the way down to the bare APU die confirmed it directly: the factory thermal paste was completely dry and cracked, six years after the console's original build. A repaste with fresh Arctic MX-6 fixed it — an hour of the single most reliable failure case in the whole investigation (Halo Campaign Evolved) ran with zero issues afterward.

More details:

- [My Xbox Series X Keeps Shutting Down, Part 1: Chasing the Fault]({% post_url 2026-09-20-my-xbox-series-x-keeps-shutting-down-part-1-chasing-the-fault %}) — the diagnosis
- [My Xbox Series X Keeps Shutting Down, Part 2: The Fix]({% post_url 2026-09-21-my-xbox-series-x-keeps-shutting-down-part-2-the-fix %}) — the repaste and the result

<br />
