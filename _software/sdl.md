---
layout: post
title: SDL
summary: The cross-platform graphics library that got pixels on screen for my Commander Keen WebAssembly port — the same library a lot of emulators and classic game source ports lean on.
date: '2025-11-26 23:35:00'
tags: [Programming, WebAssembly]
---

SDL (Simple DirectMedia Layer) is a cross-platform, open-source C library that gives low-level access to graphics, input, and audio hardware. It's used by a huge range of video playback software, emulators, and classic game source ports — including [Chocolate Keen]({% link _software/commander-keen.md %}), the source port I used for my WebAssembly [Commander Keen]({% link _software/commander-keen.md %}) port.

Since [Emscripten]({% link _software/emscripten.md %}) has SDL support built in, getting the game's original SDL rendering calls working in a browser tab was mostly a matter of compiling against Emscripten's SDL implementation rather than rewriting the graphics layer from scratch.

### Related on this site

- [WebAssembly Lesson 2: Graphics with SDL]({% link _howto/getting-started-with-webassembly-part-2-graphics-with-sdl.md %})
- [Emscripten]({% link _software/emscripten.md %})
- [Commander Keen]({% link _software/commander-keen.md %})
