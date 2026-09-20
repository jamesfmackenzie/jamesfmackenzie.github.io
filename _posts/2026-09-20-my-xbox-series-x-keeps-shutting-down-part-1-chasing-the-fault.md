---
layout: post
title: "My Xbox Series X Keeps Shutting Down, Part 1: Chasing the Fault"
date: '2026-09-20 12:00:00'
summary: My Xbox Series X started powering itself off mid-game, but only in some games. Working out why turned into a proper electrical diagnosis, and it ended up somewhere I didn't expect.
tags: [Xbox, Consoles, Videogames]
hero: xbox-series-x-halo-control-test.jpg
hero_alt: My Xbox Series X back together on the desk, running Halo during a control test
---

My Xbox Series X started powering itself off mid-game. Not crashing to the dashboard — it plays its normal shutdown chime, then switches off completely. No error message, no overheating warning. Turn it back on and everything looks fine, until it happens again.

The odd part was which games did it. The dashboard is completely stable. Braid runs forever over Xbox 360 backward compatibility. Forza Horizon 2, a substantial Xbox One 3D game, ran fine too. But Halo shut the console down within seconds of reaching its animated menu, and Minecraft died even faster, somewhere in its title-screen loading. Crysis Remastered lasted a few minutes before it went the same way.

That killed off the easy explanations quickly. It isn't 2D versus 3D — Forza is real 3D and rock solid. It isn't backward-compatible versus native — Vampire Survivors is a native Series X/S title and runs indefinitely. It isn't the internal SSD — the stable native title and all three failing titles live on the same drive. And it isn't simple overheating: leaving the console switched off for ten minutes barely changed how fast Halo failed, which is backwards from what you'd expect if it just needed to cool down.

First things to rule out were outside the console entirely — a different wall outlet, a different power cable. Same result, Halo died just as fast. That pointed the problem inward.

### Opening it up

Inside, the fan was clean and spun freely, no blocked airflow. The PSU's connectors looked fine too, no discoloration or corrosion.

![My Xbox Series X opened up, disc drive and heatsink still in place](/img/xbox-series-x-teardown-open.jpg){: width="480"}

The PSU itself is a Chicony-made unit, date-stamped 16 June 2020 — about six years old, and roughly five months older than the console's actual launch, so an early-production part.

![The Xbox Series X PSU's label, showing the Chicony manufacturer stamp and June 2020 date code](/img/xbox-series-x-psu-label.jpg){: width="480"}

Microsoft's own repair guide is emphatic that you don't open the PSU casing — it holds mains-voltage capacitors that can stay charged after unplugging — so with it unplugged and sitting loose, I measured the DC output at its low-voltage connector instead.

![A multimeter reading 11.90V at the Xbox Series X PSU's output connector](/img/xbox-series-x-psu-voltage-test.jpg){: width="480"}

11.90V, dead steady, comfortably inside the ±5% tolerance for a nominal 12V rail. That rules out a dead supply, but not much else — it was an unloaded reading, taken with nothing drawing current. If the fault only shows up under a sudden load spike, a perfectly healthy-looking idle voltage tells you nothing about what happens under one.

### A control test that lied

Before ordering a replacement PSU, I put the console back together, untouched otherwise, and reran the fastest-failing test as a control. Halo played straight through the point that used to kill it in seconds, into actual gameplay.

For a moment that looked like the fix: both PSU connectors had been unplugged and replugged during the teardown, and a marginal, oxidised, or slightly-backed-out contact fits the whole picture surprisingly well. Contact resistance drops voltage in proportion to current, so it's invisible at idle and only bites under a heavy transient — which would explain the load-dependence, the lack of any thermal signature, and the normal shutdown chime (the system detecting an out-of-spec rail and shutting down deliberately, not losing power outright).

It wasn't the whole story. Ten minutes into Halo, then ten minutes into Minecraft, the console shut down again, the same way it always had. Reseating the connectors had genuinely helped — cold-start endurance went from seconds to about twenty minutes — but something else was still wrong underneath it.

### The fault is thermal after all

That twenty-minute number is what turned things around. A fault that takes a while to show up and then reliably does is a classic heat-soak profile, and the earlier reason for dismissing heat — failures within seconds of a cold start — no longer applied once cold starts were actually surviving twenty minutes.

Restarting immediately after a shutdown, with the console still hot, confirmed it: both Minecraft and Halo failed almost instantly, versus the twenty minutes a cold start bought. Cold runs a while, hot fails fast — a much cleaner problem than the original puzzle of why "light" Minecraft died faster than "heavy" Forza.

That original puzzle actually has a tidy answer once you think in terms of heat instead of average graphics load. The APU die and its heatsink have wildly different thermal mass — the heatsink takes minutes to heat up, but the bare silicon underneath can jump twenty or thirty degrees in well under a second on a sudden load step, which is exactly what a bursty startup sequence like Minecraft's produces. Die temperature is roughly heatsink temperature plus a jump proportional to how much resistance sits in the thermal interface between them. From a cold heatsink, that jump lands below the threshold. From a heatsink that's already soaked for twenty minutes, the same instant jump goes straight over it. A degraded thermal interface is exactly what would inflate that jump.

There was a messy detour here too — after enough hot-restart cycles back to back, the console stopped responding to the power button entirely and needed a full unplug to clear, a classic latched protection response in switching power supplies. And once I moved on to testing with the case open, in preparation for a fan test, results got briefly worse across the board, including a first-ever failure on the previously bulletproof Forza. That turned out to be a confound rather than real decline: the case isn't just cosmetic, it ducts the fan's airflow across the heatsink, and testing with it off meant genuinely worse cooling than stock. Closing the case back up brought Forza straight back to indefinite stability, and narrowed the real remaining fault to something contained — Minecraft still failing within a few minutes, cold, sealed, but nothing like the instant failures seen with the case open.

### Where that leaves it

The console's PSU is six years old, and the Series X's APU is a "naked" die with no integrated heat spreader — exactly the part of a console most likely to show its age first, and exactly consistent with everything above. The working diagnosis is dried-out factory thermal paste.

The fan test that would normally come next means opening the case again, which just reintroduces the exact airflow confound I'd only just untangled — so I'm skipping it and going straight to an APU repaste. New paste (Arctic MX-6, chosen over the MX-4 and thermal pad already on hand) and gloves have arrived; **Part 2** covers taking the heatsink off a Series X APU for the first time, doing the repaste properly on a bare die, and finding out whether it actually fixes anything for good.
