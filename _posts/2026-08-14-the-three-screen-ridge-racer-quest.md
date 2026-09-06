---
layout: post
title: "The Three-Screen Ridge Racer Quest: Chasing a Cabinet Nobody Could Emulate"
date: '2026-08-14 09:00:00:00'
summary: |-
  Namco built an arcade cabinet that stitches three screens into one race. Nobody had properly emulated the chip that makes it possible. This is the full story — two other people's abandoned attempts, a ROM dump that can't be released, a canonical chip emulation built from scratch, and a discovery near the end that changed everything.
tags: [Posts, Emulation, Programming, Retrogaming]
hero: ridge-racer-full-scale-arcade-cabinet.jpg
hero_alt: Ridge Racer Full Scale arcade cabinet, three-screen sit-down cabinet with a real Eunos Roadster body
---

In 1993, Namco built an arcade cabinet that shouldn't have made sense as a business decision. Ridge Racer Full Scale wraps three screens around a real Eunos Roadster body — an actual convertible car shell, cut down to a cockpit, with three PCBs behind it working in concert to render your peripheral vision as well as the road ahead.

I found a photo of this cabinet and could not stop thinking about it. And the more I dug, the more I realised: **nobody had ever gotten this working properly in MAME.** Not because it was impossible — because the chip responsible for stitching the three screens together had never been properly emulated. This is the story of chasing that cabinet down, through two dead ends left by other people, a lot of dead-end evenings of my own, and a discovery late in the process that I genuinely did not see coming.

## Act One: The Cabinet That Shouldn't Exist

### A chip called the C139

The obvious place to start was MAME — the emulator that's spent three decades documenting arcade hardware as software. Surely if any project could resurrect a triple-screen 1993 racer, it'd be this one.

It couldn't. Not out of the box, anyway.

The thing making Full Scale possible is a Namco custom chip called the **C139** — a serial interface controller used across two decades of Namco arcade boards, from Final Lap in 1987 through to Time Crisis a decade later. Its job is to let multiple PCBs talk to each other over a fast serial link, enabling both linked multiplayer cabinets and multi-screen setups like this one.

### A 113-line stub with a TODO in it

Mainline MAME's implementation of the C139 is 113 lines long and does almost nothing:

```cpp
uint16_t namco_c139_device::status_r()
{
    // STATUS bit?
    return 4;   // Hardcoded: just returns TXREADY to stop games hanging at boot
}
// TODO: Make this to actually work!
```

No register model. No networking. No interrupt handling. Just enough of a stub to stop the game hanging at boot. Every linked Namco title from 1987 to 1997 — Final Lap, Winning Run, Ridge Racer, Cyber Sled, Time Crisis, and around 40 others — has effectively zero linking support in official MAME. That `// TODO` comment had apparently been sitting there for years.

But "nobody's done it yet" is a very different proposition from "it can't be done." Somewhere out there, someone had presumably tried.

## Act Two: John Bennett's Proof of Concept

### Finding the thread

They had. Buried in a long-running <a href="https://forum.arcadecontrols.com/index.php?topic=165638.0" target="_blank">arcadecontrols.com forum thread</a>, I found the trail of **John Bennett**, an arcade hardware collector who'd built a working proof-of-concept years earlier — hacking C139 support directly into a MAME build using the emulator's own LAN socket system, the same plumbing Sega Model 1/2 games use for their linked cabinets.

### A genuine win

I built his code, wired up three MAME instances, pointed them at Ridge Racer Full Scale — and got three linked screens actually talking to each other. This was a real moment. John's approach worked. Three separate processes, three PCBs' worth of emulated hardware, successfully exchanging data over a serial protocol nobody outside a handful of forum threads had ever documented. Credit where it's due: he'd done the hard, unglamorous work of establishing that this was even possible in the first place, and got there before anyone else did.

### But the code told its own story

His own header comment for the device was refreshingly honest about what it was: *"Hacky Proof of Concept (TM)."* And reading through it, the label fit. Game-specific code branches were scattered everywhere rather than living behind a clean interface. Networking ran directly on MAME's built-in LAN sockets rather than a dedicated thread, so it competed with the emulation loop for CPU time. A custom packet framing format had been bolted on top, undocumented beyond the code itself. And his own notes called out exactly what you'd expect from those choices: frame synchronisation not fully reliable, transmission rate insufficient for a solid 60Hz once three or more players were linked, packet drops on some games. It was never built for mainline submission — it was built to prove the idea worked, and by that measure, it had already succeeded.

### The graphics problem

There was a second problem, and this one had nothing to do with John's code at all:

![Ridge Racer Full Scale running with corrupted, static-like road textures in MAME](/img/ridge-racer-full-scale-corrupted-graphics-mame.jpg)

That static-y, corrupted road surface is a ROM problem. Full Scale's program ROM has been dumped and is freely available — you can grab `ridgeracf.zip` from any standard MAME 0.260+ set. But its **graphics ROMs have never been publicly dumped.** The available set quietly substitutes graphics from the ordinary, single-screen Ridge Racer, and Full Scale's program code doesn't agree with that substitution — hence the "WRONG WAY" bitmap and static wherever the game expects data that simply isn't there.

### Why the good dump can't be released

I went looking for why, and found the answer in a separate <a href="https://www.ukvac.com/forum/threads/ridge-racer-full-scale-3-screens.66044/" target="_blank">UKVAC forum thread</a> that's been running for over a decade, alongside an earlier <a href="https://www.ukvac.com/forum/threads/in-depth-look-at-ridge-racer-full-scale.59223/" target="_blank">in-depth look at the cabinet</a> on the same forum. It turns out someone — John Bennett again, as far as the threads suggest — *did* get access to a real Full Scale board and successfully dumped the correct graphics ROMs. But he hasn't been able to release them publicly. The specifics get into the murky territory of who owns what when it comes to decades-old arcade ROMs and the goodwill required to get physical access to increasingly rare hardware in the first place — the kind of quiet politics that stalls preservation efforts more often than technical difficulty does.

So: a real win — three screens, actually linking — undercut by a hacky implementation on one side and a graphics dump stuck in limbo on the other.

## Act Three: SailorSat's Rewrite

### A second attempt, and some hope

John's code wasn't the only attempt. A more serious rewrite had been done by **Ariane Fugmann**, working under the handle SailorSat, with contributions from Angelo Salese and John Bennett himself — visible in <a href="https://github.com/SailorSat/cabmame" target="_blank">SailorSat/cabmame</a>, with the C139-specific changes isolated in <a href="https://github.com/SailorSat/C139" target="_blank">SailorSat/C139</a>. There was even an attempt to get it merged into mainline MAME, visible in <a href="https://github.com/mamedev/mame/commit/c729acf5613522e1b44bdbd4534ded655753db1d" target="_blank">this commit</a>. Finding it felt like the problem might already be solved — a more mature codebase, actively maintained, with real engineering behind it. Maybe Full Scale was closer than I thought.

### What was actually better

The architectural upgrade was real. Where John's version used MAME's LAN sockets directly on the emulation thread, Ariane moved networking onto a dedicated ASIO TCP thread — lower latency, cleaner separation from the emulation loop, per-instance port configuration via command-line options. She replaced John's game-specific register handling with something much closer to a proper unified register model across all eight of the C139's registers. And critically, she moved ring-forwarding logic into the network layer itself: when one PCB needed to relay data to the next screen in the chain, it happened directly in the network callback, without ever bothering the emulated CPU. It's a genuinely elegant piece of engineering, and by a wide margin the most mature C139 implementation that existed anywhere before I started.

### Still not quite there

But reading through it carefully turned up real problems too. Community hardware testing against a real C139 — probing the chip directly with an Arduino jig rather than guessing from ROM behaviour, documented across the same arcadecontrols.com thread — had established a specific, confirmed hardware quirk: register 6 (the RX buffer offset) has a hardware floor of `0x1000`. Write anything lower and the real chip silently ORs in `0x1000` anyway; write `0x0800` and `0x1800` is what actually gets stored. SailorSat's implementation initialised that register to `0` and never enforced the floor on read — a subtle thing, but the kind that causes RX buffer placement to quietly drift wrong under the right conditions.

There was a second, gnarlier problem that affected both implementations equally: on the side screens of a three-screen setup, the road would visibly clip at the *center* camera's field of view instead of its own. All three Full Scale PCBs run identical ROM code, so the side-screen CPU calls exactly the same rendering trigger function as the center screen does — but if that trigger fires before this screen's own camera data has actually arrived over the link, it renders with whatever stale viewport happened to be sitting in memory already. Both John's code and Ariane's code hit this. Neither had fully diagnosed why.

### Why I decided to build my own

Two implementations, two philosophies, neither fully solving the problem, and a growing punch list of specific, well-understood defects in both. At that point the sensible move stopped being "patch someone else's proof of concept" and became "build a canonical version from the hardware up" — treating the C139 the way MAME treats any well-documented custom chip, not as a bag of workarounds for one game.

## Act Four: Building a Canonical C139

### Standing on other people's research

Worth being upfront about something here: I didn't personally reverse-engineer this chip at the register level. The hard, patient work of establishing the C139's actual register map, power-on defaults, mode semantics, and quirks like the REG_6 floor was already done by the community before I ever got involved — documented piecemeal across that same <a href="https://forum.arcadecontrols.com/index.php?topic=165638.0" target="_blank">arcadecontrols.com thread</a>, cross-referenced against direct hardware probing and both John's and Ariane's existing code. What I did was pull that scattered, hard-won knowledge together into one clean, hardware-accurate device model — the part nobody had gotten around to yet.

### What I actually built

- **A full 8-register model** with correct hardware masks and confirmed power-on defaults, not approximated ones
- **ASIO TCP networking** on a background thread with lock-free FIFOs between the network and emulation threads — taking the architectural lesson from SailorSat's version and building it fresh against the current MAME codebase
- **A clean topology system** — `CENTER`, `FORWARDER`, and `SLAVE` roles, configured by the game driver at reset time rather than hard-coded port-number detection buried inside the device itself

That last point mattered more than it sounds. Both prior implementations inferred a PCB's role in the ring from which port it happened to be listening on — functional, but it meant the device itself had to know things about specific games. I wanted the C139 device to be a generic serial chip with no idea what game was plugged into it, with the *driver* telling it what role to play.

### The Y-split trick

The three-screen topology needed one conceptual workaround. On real Full Scale hardware, the center PCB's serial output is physically Y-split — a soldered junction feeding both side screens the same signal simultaneously. MAME can't replicate a hardware broadcast; it only does point-to-point TCP. So the emulated ring approximates it as a relay chain instead: the center screen sends to the right screen, and the right screen immediately forwards what it receives to the left screen, entirely within the network thread, without its own CPU ever touching the data. From the game's perspective — and the player's — the result is indistinguishable from the real Y-split.

### Chasing glitches

Development was not a straight line. Working through the problem alongside Codex and Claude Code, early attempts got three linked instances up and *technically* talking, but the connection would glitch and drop out continuously — the kind of intermittent failure that eats an entire evening before you find the actual cause. Chasing it down meant genuinely deep log inspection, port by port, packet by packet.

### Cracking the clipping bug

The side-screen clipping bug that had beaten both prior implementations turned out to have a satisfying answer. Rather than patch around it, I traced the actual SCI interrupt service routine on real ROM using MAME's built-in debugger, instruction by instruction, from ISR entry to return. The trace showed something neither prior implementation had established: the ISR *does* correctly trigger the render path, but indirectly — it copies received data into polygon RAM, then writes a trigger word that the master DSP polls, which is what actually fires the render trigger. The rendering architecture was never broken. It had just never been fed data in the right order to prove it. Once the C139 device delivered data to RX RAM *before* asserting its interrupt — properly, not as an approximation — the existing rendering chain turned out to already be correct. No driver-level workaround needed, just a chip that behaved the way real hardware does.

### One last bug

One issue did survive into a later test run: the right-screen forwarder was relaying every frame twice — once as data physically passed through the network callback, and again through a redundant path in the higher-level receive handler — slowly flooding the left screen's buffer and causing a progressive, worsening lag the longer a session ran. That one got caught and fixed shortly before what came next.

## Act Five: A Win

With the register model solid, the networking clean, and the relay bug fixed, three linked MAME instances came up talking cleanly for the first time — properly, not as a fragile proof of concept. No game-specific branching cluttering the device, no unenforced hardware floors, no side-screen clipping. Compared to where John's version and SailorSat's version had each landed, this was a genuine step forward: a chip emulation that behaved like a chip, not like a workaround for one specific game's quirks.

### This would be perfect, if we had proper ROMs

And then the lament, because it wouldn't have been an honest story without one: all that engineering, and Full Scale itself was still rendering with substituted, wrong graphics. The chip worked. The link worked. The registers, the topology, the timing — all of it worked. And it didn't matter, because the one thing I couldn't engineer my way around was a graphics ROM dump sitting in someone's private collection, unable to be released. This would be perfect, if we had proper ROMs.

## Act Six: A Discovery I Wasn't Expecting

### Wait — there's another cabinet?

Here's the thing I didn't know when I started any of this: Ridge Racer Full Scale wasn't the only three-screen cabinet Namco built for this game. There's a second, less flamboyant sibling — no roadster shell, just a standard sit-down cabinet — called **Ridge Racer Three Monitor Version**. Same three-PCB C139 trick under the hood. I'd never come across it in any of the research so far. It genuinely caught me off guard.

### Fully dumped, and it's been sitting in MAME

Better still: unlike Full Scale, Three Monitor Version's ROMs have actually been properly dumped and submitted to mainline MAME — credited in the commit history to <a href="https://github.com/mamedev/mame/commit/90749e5205a4d26ec503b5fc9bc11403f4e3c819" target="_blank">John Bennett and Keith Heathcote</a>. The same John Bennett from earlier in this story, who couldn't release Full Scale's graphics ROMs, had — together with Keith Heathcote — gotten a complete, working dump of its sibling cabinet into the official MAME romset. And crucially, in MAME's driver, Three Monitor Version is declared a clone of the *standard*, single-screen Ridge Racer ROM set. It uses the ordinary, completely and correctly dumped Ridge Racer graphics, sound, and 3D model ROMs. Only four small program ROMs are unique to it, and those had been fully and cleanly dumped too.

No corruption. No BAD_DUMP flags. No graphics gap to fall into. The one thing standing between my working chip emulation and a genuinely correct three-screen Ridge Racer had, this whole time, a side door.

## Act Seven: Does My Code Work Against It?

I checksummed all four of Three Monitor Version's program ROMs against MAME's expected values byte for byte — exact match on every one. Then I pointed my own C139 implementation at it and ran three linked instances: left, center, right.

**Yes. It does.**

All three connected over TCP cleanly. DIP-switch role selection worked exactly as documented. The forwarder relayed thousands of frames with zero errors, zero overflows, zero disconnects. And it rendered *correctly*:

![Three linked MAME windows running Ridge Racer Three Monitor Version, showing distinct camera angles per screen](/img/ridge-racer-three-monitor-version-mame-3-screen.jpg)

That's not three copies of the same frame stitched together — look closely and you can see it's not even trying to be. The center screen shows a full attract-mode scene with the HUD intact. The left and right monitors show tight, close-up canyon-wall views, consistent with a wraparound side-camera perspective mid-corner, hugging a rock face the center camera can't even see. Each PCB is receiving the same broadcast scene state over the link and computing its *own* distinct camera viewport from it — genuinely doing what the real, three-PCB cabinet does, not faking it.

It's not quite the cabinet I set out chasing. A real Full Scale, with the actual roadster-shell graphics rendering correctly, is still waiting on a ROM dump that exists but can't yet see daylight. But getting a three-screen, C139-linked Ridge Racer running cleanly, with correct per-screen graphics and not a hint of the corruption or clipping bugs that dogged both earlier attempts, is the moment this whole quest was actually about. Full Scale was the cabinet that started it. Three Monitor Version is the one that proved the chip — and the emulation of it — actually works.

## What's Next

Sustained sync through an actual race — credits inserted, laps driven, not just an attract-mode demo — is still unverified, and it's the obvious next test. Beyond that, the same C139 device should eventually cover the other linked modes: Final Lap's ring-network multiplayer, Winning Run, Ace Driver, Cyber Cycles, and the roughly 40 other Namco titles currently locked out of linking entirely in mainline MAME.

And somewhere out there, a Full Scale cabinet or its ROMs are still waiting to properly see daylight. When that happens, the code is ready for it.

The code and the full technical writeup — register maps, wire formats, ROM traces, and the implementation plan — are <a href="https://github.com/jamesfmackenzie/mame" target="_blank">on GitHub</a>, including <a href="https://github.com/jamesfmackenzie/mame/blob/master/C139_TECHNICAL_REFERENCE.md" target="_blank">C139_TECHNICAL_REFERENCE.md</a> if you want to go deeper than even this post did.

Further reading, for anyone who wants to fall down the same rabbit hole: <a href="https://arcadeblogger.com/2022/11/20/the-last-ridge-racer/" target="_blank">Arcade Blogger's history of the Full Scale cabinet</a>, and John Bennett's own Ridge Racer site, preserved on the <a href="http://web.archive.org/web/20190615000000*/Ridgeracer.co.uk" target="_blank">Wayback Machine</a>.
