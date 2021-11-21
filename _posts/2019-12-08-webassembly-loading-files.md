---
layout: post
title: "WebAssembly Lesson 4: File System Access"
date: '2019-12-08 00:00:02:00'
summary: How does File IO work in WebAssembly?
tags: [Emscripten, How To, Programming, WebAssembly, Web Development]
---
 
JavaScript and WebAssembly do not have access to the host file system when run inside the sandboxed Web Browser environment

So that File IO continues to work for WebAssembly apps, Emscripten provides a virtual file system that simulates the local file system. C/C++ code that uses traditional file APIs can then be compiled and run with little or no change
 
### Populating the Virtual File System

There are two alternatives for how files are packaged: *preloading* and *embedding*

Embedding puts the specified files inside the generated JavaScript, while preloading packages the files separately. Embedding files is much less efficient than preloading and should only be used when packaging small numbers of small files. Preloading also enables the option to separately host the data.

To package using preloading:

```
emcc myfile.c -o myfile.html --preload-file asset_dir
```

This will generate `myfile.html`, `myfile.js` and `myfile.data`. The .data file contains all the files in `asset_dir/`, and is loaded by `myfile.js`

Any file API calls made in `myfile.c` will work as if they had native access to the files stored under `asset_dir` - except they will operate on the preloaded copies of those files and not touch the original source files on the local file system 

To package using embedding:

```
emcc myfile.c -o myfile.html --embed-file asset_dir
```

This will work the same as preloading, except the files under `asset_dir/` will be serialised and included inside `myfile.js`. As mentioned above, this is less efficient than preloading and should only be used for simple cases with few files

Find more detail on packaging files and the Emscripten virtual file system <a href="https://emscripten.org/docs/porting/files/packaging_files.html#packaging-files" target="_blank">here</a>


### Other Posts in this Series

{% include webassembly-learning-series.md %}
