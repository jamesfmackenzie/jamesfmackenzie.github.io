---
layout: post
title: Emscripten
summary: The compiler toolchain that got a DOS-era C codebase running in a web browser — my way into WebAssembly.
date: '2025-11-26 23:35:00'
tags: [Programming, WebAssembly]
---

Emscripten is a compiler toolchain that takes C/C++ code and compiles it to WebAssembly, so it can run inside a web browser at close to native speed. It's what I used to port [Commander Keen]({% link _software/commander-keen.md %}) — specifically the open-source Chocolate Keen source port — into something playable directly in a browser tab.

The original plan was to refactor the whole codebase around Emscripten's cooperative main-loop model, but that turned out to be more effort than it was worth. What actually shipped uses Emscripten's [Emterpreter](https://github.com/emscripten-core/emscripten/wiki/Emterpreter) instead — slower, but a working solution without a full rewrite. Getting graphics on screen alongside it meant learning [SDL]({% link _software/sdl.md %}), which Emscripten has built-in support for.

### Related on this site

- [Porting Commander Keen to WebAssembly]({% link _projects/porting-commander-keen-to-webassembly.md %})
- [WebAssembly Lesson 1: Hello World]({% link _howto/getting-started-with-webassembly-part-1-hello-world.md %})
- [Commander Keen]({% link _software/commander-keen.md %})
- [SDL]({% link _software/sdl.md %})
