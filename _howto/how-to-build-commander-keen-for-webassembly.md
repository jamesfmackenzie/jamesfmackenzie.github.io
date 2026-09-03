---
layout: post
title: "How to Build Commander Keen in WebAssembly"
summary: "Step-by-step: set up a dev environment and compile the Chocolate Keen source to WebAssembly so it runs in a browser."
date: '2024-06-07 08:00:00:00'
tags: [How To, Programming, Retrogaming, Videogames, WebAssembly]
---

This is a build-along guide to compiling <a href="https://github.com/jamesfmackenzie/chocolatekeen" target="_blank">Chocolate Keen</a> to WebAssembly with <a href="https://emscripten.org/" target="_blank">Emscripten</a>, doing everything from scratch. For the underlying concepts, see the [WebAssembly Lesson series]({% link _howto/getting-started-with-webassembly-part-1-hello-world.md %}); this post applies them to a real game.

### Dev environment

I'm on Windows 11 using **WSL** (Windows Subsystem for Linux) for the command line and **VS Code** as the editor. The steps work on any standard Linux distro too.

### Step 1 – Get the source and build it natively first

Download the Chocolate Keen source, extract it, and drop it in your Linux home directory. Before touching WebAssembly, prove it compiles as a normal Linux program:

```
sudo apt install build-essential libsdl2-dev
make
```

A few warnings are fine as long as you get a `chocolatekeen` executable. Run it to confirm the game works — this is a plain GCC build, no WebAssembly yet, but it means the code is sound.

### Step 2 – Install Emscripten

Follow the <a href="https://emscripten.org/docs/getting_started/downloads.html" target="_blank">Emscripten install instructions</a>:

```
git clone https://github.com/emscripten-core/emsdk.git
cd emsdk
./emsdk install latest
./emsdk activate latest
source ./emsdk_env.sh
```

That last line puts `emcc` and friends on your `PATH`.

### Step 3 – Point the Makefile at Emscripten

In the Chocolate Keen Makefile:

1. Change the compiler from `gcc` to **`emcc`**.
2. Building now fails, because Emscripten needs its own SDL. Find the SDL compiler/linker flags, comment them out, and replace them with Emscripten's bundled SDL2 port: **`-sUSE_SDL=2`**.
3. Change the output filename to end in **`.html`** — you're building for the web, not a native binary.

Run `make` again and you'll get three files: `.wasm`, `.js` and `.html`.

### Step 4 – The infinite-loop problem

Serve the output with a quick web server and open it in a browser:

```
python3 -m http.server
```

The browser freezes — one CPU core pegged. Chocolate Keen has a classic infinite game loop, and that doesn't work in a browser. Natively, the OS renders frames and reads input on separate hardware while your loop runs; in WebAssembly *you* have to hand control back to the browser so it can draw and read input. ([WebAssembly Lesson 3]({% link _howto/getting-started-with-webassembly-part-3-emscripten-loops.md %}) covers this in depth.)

### Step 5 – Fix it with Asyncify

Rewriting the whole loop is a lot of work. **Asyncify** is the shortcut: it transforms the compiled code so it can be paused and resumed, making a synchronous loop behave asynchronously without touching the source. Add the linker flag:

```
-sASYNCIFY
```

Clean, rebuild, reload. Now the game runs and stays responsive — but it can't find its level data.

### Step 6 – Package the game data

The program still thinks it's on a real PC, trying to read files from `C:`. You need to bundle the data into Emscripten's virtual file system. Add a linker flag pointing at the game data directory:

```
--preload-file path/to/keen/data
```

Rebuild one more time. This produces an extra `.data` file alongside the others, and now Commander Keen loads its levels and runs — in the browser.

### Watch on YouTube

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/in05zYjIIE4?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

### More on this project

- [Porting Commander Keen to WebAssembly]({% link _projects/porting-commander-keen-to-webassembly.md %})
- [WebAssembly Lesson series]({% link _howto/getting-started-with-webassembly-part-1-hello-world.md %})
