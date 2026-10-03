---
layout: post
title: "Disassembly vs Decomp vs Recomp vs Port: What's the Difference?"
date: '2026-10-03 09:00:00'
summary: "Four words that get used almost interchangeably for the projects bringing old games back to life — what each one actually means, where they overlap, and how to tell them apart."
tags: [Emulation, Posts, Programming, Retrogaming, Videogames]
image: disassembly-decomp-recomp-port-diagram.svg
---

Lately I've been working on a [native PC port of SNES Star Fox]({% post_url 2026-09-26-im-building-my-own-native-pc-port-of-star-fox %}), and along the way I noticed how loosely four words get used: disassembly, decomp, recomp and port. One [headline](https://www.androidauthority.com/majoras-mask-decomp-finished-3508633/) about the finished Majora's Mask decomp said goodbye to emulators. A [Hacker News thread](https://news.ycombinator.com/item?id=43503807) described the game as "dissembled and then recompiled to native", and a reply called Ship of Harkinian a decompilation, which it isn't.

They're easy to mix up. All four usually start from a game that only exists as shipped machine code, and three of them can end with that game running natively on a PC. But they're different things, and the difference tells you what a project can do, how much work went into it, and how far to trust it.

These are the definitions I use. Two questions sort out almost every case: what did the project start from, and what did it produce?

![Diagram: a shipped game can be disassembled into assembly or decompiled into C, both of which rebuild the original game; recompiled into intermediate generated C, which compiles with a runtime into a port; or emulated as-is. Decompiled C and original source code can also be ported.](/img/disassembly-decomp-recomp-port-diagram.svg)

## Disassembly

A disassembly turns a game's machine code back into assembly language: the original CPU instructions, written out as text, one for one. A disassembler does the mechanical part. The slow part is people working out what each routine does and giving it names and comments.

The serious projects are buildable. [pret's pokered](https://github.com/pret/pokered) describes itself as "a disassembly of Pokémon Red and Blue", and it reassembles into ROMs that match the originals' SHA1 hashes.

A disassembly is still code for the original CPU, though. On its own it rebuilds the original game for the original console, and nothing else. It's a map of the game, not a way of running it anywhere new.

## Decompilation

A decompilation goes a level higher. It reconstructs source code in a high-level language, usually C, that compiles back into the original game. The same group draws the line itself: pret calls [pokeemerald](https://github.com/pret/pokeemerald) "a decompilation of Pokémon Emerald".

The gold standard is a matching decompilation. The [Perfect Dark project](https://github.com/n64decomp/perfect_dark) defines it well: "When a matching decompilation is compiled with the same compiler that the original developers used, the output will be exactly the same as the retail game, byte for byte."

That's what makes a decomp trustworthy, and also what makes it slow. Traditionally it's been written by hand, function by function, with each one checked against the original, which is why decomps take years. AI coding tools are increasingly part of the work now, but they don't change what the result has to be: readable, maintainable C that still matches the original, byte for byte. The [Super Mario 64 decomp](https://github.com/n64decomp/sm64) appeared in 2019. Ocarina of Time's [reached 100%](https://www.videogameschronicle.com/news/zelda-64-has-been-fully-decompiled-potentially-opening-the-door-for-mods-and-ports/) in November 2021 after 21 months, and Majora's Mask [got there](https://www.nintendolife.com/news/2024/12/zelda-majoras-mask-decompilation-project-now-at-100percent) in December 2024.

What a decomp isn't is a port. The [Ocarina of Time project](https://github.com/zeldaret/oot) says so plainly: "It is not producing a PC port." What it builds is the N64 ROM.

## Static recompilation

Static recompilation is easiest to explain next to something emulator users already know: dynamic recompilation, or [dynarec](https://en.wikipedia.org/wiki/Dynamic_recompilation). Many emulators speed themselves up by translating the game's machine code into the host computer's machine code while the game runs, and caching the result.

A static recompilation, or recomp, does the same kind of translation ahead of time, once, before the game ever runs. The goal is a native program for a new platform. Binary in, program out, and there's no emulator underneath when you play it.

Most current tools get there by way of C. [N64Recomp](https://github.com/N64Recomp/N64Recomp) describes itself as a tool to "statically recompile N64 binaries into C code that can be compiled for any platform". The C is a portable middle step: it lets ordinary compilers build the final program for whatever platform you like, while a runtime stands in for the original console's hardware. The runtime is where the platform-specific work happens.

The C isn't meant to be read. The [XenonRecomp](https://github.com/hedge-dev/XenonRecomp) README says its output is "not very human-readable", and that it's "not going to function correctly without a runtime backing it". It isn't throwaway either, because it's a place where a port can be patched and extended. But it's an intermediate, not the product, and that's the clearest line between the two techniques: a decomp's C is written to be read and maintained, while a recomp's C is generated by a tool on the way to a program.

The big advantage is that no source code is needed. In the [Zelda64Recomp](https://github.com/Zelda64Recomp/Zelda64Recomp) FAQ's words, static recompilation "bypasses the need for decompiled source code when making a port, allowing ports to be made without source code". In practice the two approaches help each other — Zelda64Recomp still borrows headers and some function definitions from the Majora's Mask decomp — but the game code itself comes from the recompiler. Zelda64Recomp (Majora's Mask, May 2024), [Unleashed Recompiled](https://github.com/hedge-dev/UnleashedRecomp) (the Xbox 360 Sonic Unleashed, March 2025) and [Starfox 64: Recompiled](https://github.com/sonicdcer/Starfox64Recomp) (December 2025) are all built this way.

## Port

A port is an outcome, not a method: the game running natively on a platform it wasn't originally released on. To make one you need code you can build for the new target, and there are several ways to get it.

- **Official source.** id released the [Doom source](https://github.com/id-Software/DOOM) in December 1997, and the projects built on it are called source ports. [Chocolate Doom](https://github.com/chocolate-doom/chocolate-doom) is one, and it "aims to accurately reproduce the original DOS version".
- **A decomp.** [sm64-port](https://github.com/sm64-port/sm64-port) is "a port of n64decomp/sm64 for modern devices", and [Ship of Harkinian](https://github.com/HarbourMasters/Shipwright) is built on the Ocarina of Time decomp.
- **A recomp.** Unleashed Recompiled calls itself "an unofficial PC port of the Xbox 360 version of Sonic Unleashed created through the process of static recompilation".
- **Leaked source.** wipEout's source leaked in 2022, and phoboslab [used it](https://phoboslab.org/log/2023/08/rewriting-wipeout) as the basis for a near-total rewrite that runs on Windows, Linux, macOS and the web.

So "is it a port?" and "is it a decomp?" are separate questions. Ship of Harkinian is a port built on a decomp. The decomp itself isn't a port.

## The words they get confused with

- **Emulation** runs the original, unmodified game on a simulated console. Nothing gets rebuilt, and the emulator does all the work while the game runs.
- **Non-matching decompilation** is C that behaves like the original but doesn't compile to the same bytes. It's useful, but harder to trust.
- **Leaked source** is the developers' own code, released without permission. It isn't a decomp, because nobody had to reconstruct it. wipEout's 2022 leak, above, is one example.
- **Reimplementation** is a new engine that runs the original game's data without using its code. [OpenMW](https://openmw.org/faq/) "does not use the original executable file in any way", and needs your own copy of Morrowind.

## The short version

| | Starts from | Produces | Runs on | Example |
| --- | --- | --- | --- | --- |
| **Disassembly** | The shipped machine code | Assembly, named and documented | The original console | pokered |
| **Decompilation** | The shipped machine code | Readable C that rebuilds the original game | The original console, until someone ports it | Super Mario 64, Ocarina of Time |
| **Static recompilation** | The shipped machine code | A native build of the game, via generated C and a hardware runtime | A new platform | Zelda64Recomp, Unleashed Recompiled |
| **Port** | Any code you can compile: source, a decomp or a recomp | The game, running natively | A new platform | Chocolate Doom, Ship of Harkinian |
| **Emulation** | The shipped machine code, untouched | Nothing new | An emulator | — |

One thing nearly all of these projects have in common is that none of them include the game. The Super Mario 64 decomp, Zelda64Recomp, Unleashed Recompiled and Ship of Harkinian all need your own copy for the assets.

### Related on this site

- [I'm building my own native PC port of Star Fox]({% post_url 2026-09-26-im-building-my-own-native-pc-port-of-star-fox %})
- [Commander Keen]({% link _software/commander-keen.md %}) — the source port I keep porting to new platforms
- [A native Super Mario 64 port on the PS Vita]({% post_url 2020-09-16-super-mario-64-on-ps-vita %})
