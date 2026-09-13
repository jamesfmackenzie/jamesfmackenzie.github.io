---
layout: post
title: Commander Keen
summary: My go-to porting target — I've moved this one specific DOS game to WebAssembly and PlayStation Vita, mostly as an excuse to learn the platform doing the moving.
date: '2025-11-26 23:35:00'
tags: [MS-DOS, PC, Videogames]
---

Commander Keen is id Software's early DOS platformer, and it's become my standard test case whenever I want to learn a new porting target. It's small, well-understood, and — via the open-source [Chocolate Keen](https://github.com/jamesfmackenzie/chocolatekeen) source port — genuinely portable, which makes it a good stand-in for "can I get real DOS-era code running on this platform" without taking on a huge project.

I've ported it twice for exactly that reason: to [WebAssembly]({% link _software/emscripten.md %}), as a way into Emscripten and browser-based porting, and to the [PlayStation Vita]({% link _hardware/sony-playstation-vita.md %}), as a way into homebrew cross-compilation once the Vita's h-encore exploit made that practical.

### Related on this site

- [Porting Commander Keen to WebAssembly]({% link _projects/porting-commander-keen-to-webassembly.md %})
- [Porting Commander Keen to PlayStation Vita]({% link _projects/porting-commander-keen-to-playstation-vita.md %})
- [Emscripten]({% link _software/emscripten.md %})
