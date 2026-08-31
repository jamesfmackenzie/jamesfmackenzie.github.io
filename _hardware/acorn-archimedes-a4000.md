---
layout: post
title: Acorn Archimedes A4000
summary: Notes on the Acorn A4000, my entry-level Archimedes-family machine — and the leaking battery that nearly killed it.
date: '2024-08-29 11:33:00'
tags: [Acorn Archimedes, Computers]
---

The Acorn A4000 is a 1992 machine from the tail end of the [Archimedes]({% link _hardware/acorn-archimedes.md %}) family. It sits at the affordable end of the range: an ARM250 (integrating the ARM3-class core and support chips onto one part), RISC OS 3, and a slimline all-in-one case styled to match Acorn's early-90s look.

### What it is

The A4000 was aimed at homes and schools that wanted an Archimedes without the price of an A5000. Functionally it is close to the A3010/A3020 machines of the same era — same ARM250, similar capabilities — in a case with a single internal expansion slot and a 3.5" drive bay.

It is not the fastest or most expandable Archimedes, but it runs the same RISC OS and the same software, and it is a pleasant, compact machine to own.

### The battery problem

Like almost every Acorn machine of this period, the A4000 has a **rechargeable battery on the mainboard** that leaks with age. The electrolyte creeps across the PCB, eats through traces and component legs, and if left long enough will destroy the board.

Mine had started to go. Catching it in time — removing the battery, cleaning up the residue, and repairing any affected traces — is the single most important thing you can do for one of these. **Never power on an untested A4000 without checking the battery first.**

### Related on this site

- [Battery leak in the A4000]({% post_url 2021-12-30-acorn-archimedes-a4000-battery-leak %})
- [Saving an Acorn A4000 from battery damage]({% post_url 2021-12-31-acorn-a4000-battery-repair %})
- [Acorn Archimedes]({% link _hardware/acorn-archimedes.md %})
- [Microvitec AKF50]({% link _hardware/microvitec-akf50.md %})
