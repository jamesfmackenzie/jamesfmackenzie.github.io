---
layout: post
title: "My Xbox Series X Keeps Shutting Down, Part 2: The Fix"
date: '2026-09-21 09:00:00'
summary: Back inside the Xbox Series X that kept shutting itself off — this time going all the way to the die itself to find out if the theory from Part 1 was actually right.
tags: [Xbox, Consoles, Videogames]
hero: xbox-series-x-dried-paste-macro.jpg
hero_alt: The Xbox Series X APU die, covered in completely dry, cracked thermal paste
---

[Part 1]({% post_url 2026-09-20-my-xbox-series-x-keeps-shutting-down-part-1-chasing-the-fault %}) ended with a working theory rather than a fix: a degraded APU thermal interface, inferred from how the console behaved rather than seen directly. Cold starts bought about twenty minutes before Halo or Minecraft could kill it; a hot restart failed almost instantly. That shape of fault — fine when cool, fails fast once soaked — is a classic sign of a heatsink that isn't actually doing its job anymore. Time to find out.

### Getting to the die

Previous sessions never went past the outer case. This time I went all the way in: undoing a ribbon cable connector to separate the small SSD/WiFi daughtercard from the main board, then working on the main board itself.

Under an outer EMI shield — which took a fair bit of prying with tweezers — sits the actual heatsink retention mechanism, a spring-loaded bracket known as the "X clamp." Four screws, even pressure, holding the heatsink down against the APU package.

![The X clamp, four spring-loaded screws visible at its corners](/img/xbox-series-x-x-clamp.jpg)

With the clamp off, the heatsink itself still needed prising free with a plastic tool — it wasn't just resting there, it was genuinely stuck to the die.

### The paste was completely dead

This was the moment the whole theory either held up or didn't. It held up.

The old thermal paste wasn't just past its best — it was bone dry, cracked into a hardened crust rather than sitting as an even, wet layer. No wonder heat wasn't moving off that die properly.

Cleaning it off with isopropyl alcohol and cotton swabs turned up a nice bonus: the die's own printed markings, invisible until then. **`PROJECT SCARLETT`** — the Series X's internal codename during development — right there on the silicon, along with its part number and a "diffused in Taiwan, made in Malaysia" line.

![The cleaned die, showing its Project Scarlett markings](/img/xbox-series-x-die-cleaned-markings.jpg)

### Repasting and reassembly

Fresh Arctic MX-6 on the die, spread thin with a plastic card edge — no bare silicon showing, no excess piled up either — then the X clamp torqued back down evenly across its four corners.

![MX-6 applied and the X clamp reseated](/img/xbox-series-x-mx6-applied-clamp-reseated.jpg)

Reassembly had its own small drama. First power-on after putting the case back together: completely dead, nothing at all. Turned out I'd simply forgotten to reconnect one of the PSU's two internal connectors — an easy thing to miss with as many cables as this teardown involved, and a good reminder to check both before assuming something's actually wrong.

Once that was plugged back in, there was a second, stranger moment: the first four or five power-on attempts showed the console's light come on and then switch straight back off, before it suddenly started working normally and hasn't missed a beat since. My best explanation is a marginal connector — this reassembly involved reconnecting more cables than any previous step, plenty of chances for one to not be fully seated — rather than anything to do with the repaste itself. The failure happened right at power-on, before there'd have been any time for heat to build, which points away from a thermal cause. It's stayed completely reliable since.

### Did it work

Two tests, the same two games that killed the console fastest and most reliably back in Part 1:

- **Minecraft** — 15 minutes, no failure. Previously the single fastest failure of the whole investigation, dying almost at the title screen.
- **Halo Campaign Evolved** — a full hour, no failure. Previously this one didn't even survive past its animated menu, failing within seconds.

![Halo Campaign Evolved running an hour in, no signs of trouble](/img/xbox-series-x-post-repaste-halo.jpg)

An hour of the single most reliable failure case in the entire investigation, completely stable, is about as clean a result as this could have gone. Dried, caked paste explained everything — the cold-start grace period, the near-instant hot-restart failures, why "light" workloads like Minecraft's bursty startup could trip it faster than "heavy" ones like Forza's steady load. Once the actual thermal interface was replaced, all of it went away at once.

A six-year-old console with its first repaste. Not exciting as fixes go, but it's the one that actually worked.
