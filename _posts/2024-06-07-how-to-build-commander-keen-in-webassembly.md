---
layout: post
title: "How to Build Commander Keen in WebAssembly"
summary: "A deep-dive follow-up to porting Commander Keen to the browser — the approach, and the two gotchas that trip most people up."
date: '2024-06-07 10:00:00:00'
image: keen.png
tags: [MS-DOS, Posts, Programming, Retrocomputing, Retrogaming, Videogames, Videos, WebAssembly]
---

Last week I [ported Commander Keen to the browser]({% post_url 2024-06-01-i-ported-commander-keen-to-the-web-browser-webassembly %}). This is the deep-dive follow-up: how I set up the environment and compiled the <a href="https://github.com/jamesfmackenzie/chocolatekeen" target="_blank">Chocolate Keen</a> source to WebAssembly with <a href="https://emscripten.org/" target="_blank">Emscripten</a>, from scratch.

The exact build steps live in the <a href="https://github.com/jamesfmackenzie/chocolatekeen" target="_blank">repo README</a>. What's worth writing up here is the *approach* and the two problems that stump most people.

### Build it natively first

Before touching Emscripten I got Chocolate Keen compiling and running as a normal Linux program with `make`. If the code doesn't build natively, stacking a WebAssembly toolchain on top only makes debugging harder. Once it ran, swapping `gcc` for `emcc`, pointing the Makefile at Emscripten's bundled SDL, and setting the output to `.html` produced a `.wasm` / `.js` / `.html` set.

### Gotcha 1: the browser freezes

Chocolate Keen has a classic infinite game loop. Natively that's fine — the OS renders frames and reads input on separate hardware while your loop runs. In a browser it isn't: *you* have to hand control back so it can draw and read input, or the tab just locks up.

Rewriting the whole loop is a lot of work. **Asyncify** is the shortcut — it transforms the compiled code so it can be paused and resumed, making a synchronous loop behave asynchronously without changing the source. One linker flag (`-sASYNCIFY`) and the game runs, responsive.

### Gotcha 2: no level data

Now Keen runs but can't find its levels — it still thinks it's on a PC, reading from `C:`. The fix is to bundle the data files into Emscripten's virtual file system with `--preload-file`. Rebuild, and Keen loads its levels and plays — in the browser.

### Watch on YouTube

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/in05zYjIIE4?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

### More on this project

- [Porting Commander Keen to WebAssembly]({% link _projects/porting-commander-keen-to-webassembly.md %})
- [WebAssembly Lesson series]({% link _howto/getting-started-with-webassembly-part-1-hello-world.md %})
