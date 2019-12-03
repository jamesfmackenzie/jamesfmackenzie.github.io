---
layout: post
title: "WebAssembly Lesson 5: JavaScript Interop"
date: '2019-12-02 19:18:00:00'
summary: Understanding Emscripten Loops and Emterpreter
tags: [Programming, Web Development, Emscripten, WebAssembly, GameDev]
---
 
### File system and preloading files
 
Because the browser is sandboxed, you can't access the host file system
 
For this reason WebAssembly apps use a virtual file system. There are useful "pre-load" features you can use at build time to populate this virtual file system
 
- Expand on hello world article above to fopen a simple text file and show the string. Also have this is GitHub with a makefile