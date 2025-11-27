---
layout: post
title: "WebAssembly Lesson 1: Hello World"
date: '2019-11-30 19:18:00:00'
summary: What is WebAssembly? Emscripten? asm.js? Find out how to get started with WebAssembly and run some Hello World examples
tags: [How To, Programming, Posts, WebAssembly]
---

I recently undertook my first WebAssembly project: [porting a C video game to the web browser]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %}). I plan to record my learnings as a series of Lessons - each covering a major WebAssembly topic. Find Lesson 1 below


### What is WebAssembly?

WebAssembly is a new type of code that can be run in modern web browsers. It is a low-level assembly-like language with a compact binary format that runs with near-native performance

You can use Emscripten to compile C++ (or other LLVM-supported languages such as D or Rust) into a WebAssembly binary which runs in the same sandbox as regular JavaScript code

WebAssembly cannot directly access the DOM. However it can call JavaScript, which can make Web API calls on its behalf 


### What is Emscripten?

Emscripten is a toolchain for compiling to asm.js and WebAssembly. With Emscripten you can:

- Compile C and C++ code into asm.js or WebAssembly
- Do the same for any any other code that can be translated into LLVM bitcode (e.g. D or Rust)

To get started you need the <a href="https://emscripten.org/docs/getting_started/downloads.html" target="_blank">Emscripten SDK</a>

Emscripten is accessed using the Emscripten Compiler Frontend (emcc). This invokes all the other tools needed to build your code. Think of this as a drop-in replacement for a standard compiler like gcc or clang. It is called on the command line using `./emcc` or `./em++`


### What is asm.js?

asm.js is a strict subset of JavaScript, to which code written in statically-typed languages with manual memory management (such as C) can be translated by special asm.js compiler - e.g. Emscripten

Emscripten takes in C/C++ code, passes it through LLVM, and converts the LLVM-generated bitcode into asm.js

Since asm.js is just JavaScript, it can run in any browser. Performance can also be heavily optimised vs standard JavaScript. Today, most browsers can execute asm.js within a factor of ~2 slowdown vs native compilation (this is very fast!!)

WebAssembly offers all the benefits of asm.js with even faster performance. With more browsers implementing direct support for WebAssembly - and with Emscripten able to output both - asm.js investment is dwindling


### Hello World

First, install and configure the Emscripten SDK. Find instructions <a href="https://emscripten.org/docs/getting_started/downloads.html" target="_blank">here</a> 

Next, copy-paste the following C code and save it on your local machine as `hello.c`:

{% highlight c %}
{% raw %}
#include <stdio.h>

int main() {
  printf("hello, world!\n");
  return 0;
}
{% endraw %}
{% endhighlight %}

### Build

At the same folder location, open a shell / command prompt. Invoke the following Emscripten build commands:

{% highlight bash %}
{% raw %}
emcc -c hello.c -o hello.o
emcc hello.o -o hello.html
{% endraw %}
{% endhighlight %}

You'll see three new files once the build completes:

* `hello.wasm` - the WebAssembly output
* `hello.js` - the asm.js output
* `hello.html` - a shell / wrapper file so you can launch your WebAssembly app in the browser

![](/img/posts/emscripten_hello_world_build.png)

### Run

For a quick and simple test, run `hello.js` with Node JS. It should output "hello, world!":

![](/img/posts/emscripten_node_js_test.png)

Alternatively use lightweight Web Server software such as <a href="https://www.npmjs.com/package/http-server" target="_blank">http-server</a> to serve `hello.html` and open it in a Web Browser. It should output "hello, world!" to the Browser window and console:

![](/img/posts/emscripten_browser_test.png)

![](/img/posts/emscripten_browser_test_console.png)

Congratulations! You're up and running with WebAssembly!

Next time we'll look at [WebAssembly graphics with SDL]({% post_url 2019-12-01-webassembly-graphics-with-sdl %})


### Other Posts in this Series

{% include webassembly-learning-series.md %}
