---
layout: post
title: Lessons Learnt: Porting C code to WebAssembly
date: '2019-11-17 23:20:00:00'
summary: I recently finished work on my first WebAssembly project. Here are the things I learned ...
tags: [GameDev, Programming, Retrogaming, Videogames, Web Development, Emscripten, WebAssembly]
---

I recently undertook my first WebAssembly project: porting a C video game to the web browser. Learnings written up below


### What is WebAssembly?

WebAssembly is a new type of code that can be run in modern web browsers. It is a low-level assembly-like language with a compact binary format that runs with near-native performance

Users may use Emscripten SDK to compile C++ (or other LLVM-supported languages such as D or Rust) into a binary file which runs in the same sandbox as regular JavaScript code

WebAssembly cannot currently directly access the DOM. However it can call JavaScript, which can make Web API calls on its behalf 


### What is Emscripten?

Emscripten is a toolchain for compiling to asm.js and WebAssembly. With Emscripten you can:

- Compile C and C++ code into asm.js or WebAssembly
- Do the same for any any other code that can be translated into LLVM bitcode (e.g. D or Rust)

To get started you need the Emscripten SDK

Emscripten is accessed using the Emscripten Compiler Frontend (emcc). This script invokes all the other tools needed to build your code. Think of this as a drop-in replacement for a standard compiler like gcc or clang. It is called on the command line using ./emcc or ./em++.


### What is asm.js?

asm.js is a strict subset of JavaScript, to which code written in statically-typed languages with manual memory management (such as C) can be translated by e.g. Emscripten

Emscripten takes in C/C++ code, passes it through LLVM, and converts the LLVM-generated bitcode into asm.js

Since asm.js is just JavaScript, it can run in any browser. Performance can also be heavily optimised vs standard JavaScript. Today, most browsers can execute asm.js within a factor of ~2 slowdown vs native compilation (this is very fast!!)

With more browsers implementing direct support for WebAssembly, asm.js investment is dwindling


### WebAssembly Hello World

First, install the Emscripten SDK. Find instructions here: https://emscripten.org/docs/getting_started/downloads.html

Next, copy paste the following C code and save it as hello.c:

```
#include <stdio.h>
int main()
{
   printf("Hello, World!");
   return 0;
}
```

Open a shell / command prompt and build using emcc:

```
insert build commands here
```

All going well, you should see something like this:

Insert screenshot of successful build process




### File system and preloading files

Because the browser is sandboxed, you can't access the host file system

For this reason WebAssembly apps use a virtual file system. There are useful "pre-load" features you can use at build time to populate this virtual file system

- Expand on hello world article above to fopen a simple text file and show the string. Also have this is GitHub with a makefile

### Simulate main loop is your friend

On real hardware, things work in parallel. Even inside a tight for loop, you can still render graphics to the screen and listen for input

This is especially common in video games, where the "main loop" typically looks like this:

while(true) {
  - read input
  - perform calculation 
  - render frame
  - sleep
}

I'm WebAssembly this is a no-no. It will block the main thread and never draw anything

- include or link to broken WebAssembly loop that never draws to the screen

You need to release the main thread to do things like render graphics output - or you will disappear down the tight loop forever

Emscripten has a convenient way to do this:

emscripten simulate main loop

- include a fixed example that works fine
- note that we can use IFDEFs to make code compatible across WebAssembly and native builds

Emscripten will take control of the loop and invoke the loop method on a timer. You can choose how often this happens, or set to XXX if you want to match the display refresh rate (useful for games)

Note: you cannot run a main loop inside a main loop!

To remember: never block the main loop

### Emscripten loops are not real loops

Unlike real loops, Emscripten loops will not resume from where they left off when you break the loop. The app has totally lost the state of the stack and will not re-enter from where you invoked the loop from 

- include broken code snippet

You have two choices on how this will work:

- if you pass in 0 param the code will setup your loop and then keep running - so the loop will be called on your desired frequency but the main code will continue to run also

- if you pass in 1 param emscripten will stop running the main code (it actually forces an exception to do this) and only run your loop

But neither of these options behaves like a "true" loop

### Emterpreter to the rescue - but at a cost!

Because it's painful to rewrite traditional apps towards emscripten loops, Emscripten provides the "Emterpreter" feature. In this mode, you just use traditional infinite loops in your code. Emterpreter auto replaces these with Emscripten loops (I think) and keeps track of the call stack for you. When the loop breaks, Empterpreter will reassemble the stack for you and carry on from exactly where you left off

Note that you still need to emscripten_sleep to give the browser a chance to render to the screen. Otherwise there is no window (hohoho) of opportunity

- include and link to Emterpreter example

Is this a magic bullet? No, not really. Because it taxes performance very heavily

The advice is to rewrite to Emscripten loops wherever you can and only use Emterpreter very sparingly

Note: since latest version of emsdk, Emterpreter support was dropped. If you want to use Emterpreter you have to use the "Fastcomp" version as follows:

- details on now to use fastcomp

Extra notes below:

Generally this just isn’t well documented anywhere:
The final param of emscripten_set_main_loop will behave as follows:
0: program continues as normal but env will also call your loop function
1: program halts and loop function gets executed
Unfortunately code does not resume from where it left off when you cancel the main loop so some extra function calls or hacks will have to be made to accommodate. In the extreme nasty case you could use a goto
Use emscripten functions:
emscripten_set_main_loop(CVort_scroll_up_logo_loop, 0, 1);
emscripten_cancel_main_loop();


