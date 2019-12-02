---
layout: post
title: SDL and WebAssembly
date: '2019-12-01 19:18:00:00'
summary: I recently finished work on my first WebAssembly project. Here are the things I learned ...
tags: [Programming, Web Development, Emscripten, WebAssembly, GameDev]
---

### What is SDL?

SDL (Simple DirectMedia Layer) is a cross-platform, Open Source development library designed to provide low level access to input and graphics hardware

Written in C, it is used by video playback software, emulators, and many popular games

It is not full game engine, but rather a wrapper around OS-specific functions that software might need to access. It's purpose is to add abstraction and help developers target multiple platforms with one code base

SDL officially supports Windows, Mac OS X, Linux, iOS, and Android - with unofficial support for many other platforms


### SDL 1.2 vs SDL 2.0

There are two flavours of SDL:

- v1.2 - original version licensed under <a href="http://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html" target="_blank">GNU LGPL</a>. Deprecated but still in popular use
- v2.0 - major update with a different, not backwards-compatible API. Improved support for hardware-accelerated 2D graphics


### Does SDL have WebAssembly support?

Yes! Emscripten (which we'll use to compile for WebAssembly) has a simple implementation of SDL 1.2's API built in. This is written by hand in JavaScript and unrelated to the SDL codebase - but with compatibility high enough for most simple use cases

SDL 2.0 support is also included via <a href="https://github.com/emscripten-ports" target="_blank">Emscripten Ports</a> - a collection of useful libraries, ported to Emscripten and integrated with the Emscripten compiler (emcc)

We'll take a look at both of these in this article


### Running SDL 1.2 code in the browser

First, install and configure the Emscripten SDK (instructions <a href="https://emscripten.org/docs/getting_started/downloads.html" target="_blank">here</a>) 

Next, copy-paste the C code below and save it on your local machine as `sdl_1_2_sample.c`. It's a tiny SDL program that renders random pixels data to the screen - it'll look like white noise

{% highlight c %}
{% raw %}
#include <SDL.h>
#include <emscripten.h>
#include <stdlib.h>

SDL_Surface *screen;

void drawRandomPixels() {
    if (SDL_MUSTLOCK(screen)) SDL_LockSurface(screen);

    Uint8 * pixels = screen->pixels;
    
    for (int i=0; i < 1048576; i++) {
        char randomByte = rand() % 255;
        pixels[i] = randomByte;
    }

    if (SDL_MUSTLOCK(screen)) SDL_UnlockSurface(screen);

    SDL_Flip(screen);
}

int main(int argc, char* argv[]) {
    SDL_Init(SDL_INIT_VIDEO);
    screen = SDL_SetVideoMode(512, 512, 32, SDL_SWSURFACE);
    
    emscripten_set_main_loop(drawRandomPixels, 0, 1);
}
{% endraw %}
{% endhighlight %}

Some things of note:

* emscripten_set_main_loop(drawRandomPixels, 0, 1);

#### Testing

At the same folder location, open a shell / command prompt. Invoke the following Emscripten build commands:

{% highlight bash %}
{% raw %}
emcc -c sdl_1_2_sample.c -o sdl_1_2_sample.o
emcc sdl_1_2_sample.o -o sdl_1_2_sample.html
{% endraw %}
{% endhighlight %}

You'll see three new files once the build completes:

* `sdl_1_2_sample.wasm` - the WebAssembly output
* `sdl_1_2_sample.js` - the asm.js output
* `sdl_1_2_sample.html` - a shell / wrapper file so you can launch your WebAssembly app in the browser

Use lightweight Web Server software like <a href="https://www.npmjs.com/package/http-server" target="_blank">http-server</a> to serve `sdl_1_2_sample.html` and open it in a Web Browser. You should see an animation - looks like white noise: 

![](/img/posts/emscripten_sdl_1_2_sample.png)

### SDL 2.0

Next, let's try the sample example, but this time with SDL 2.0.

Copy-paste the modified C code below and save it on your local machine as `sdl_2_0_sample.c`. It's a modified version of the above code for SDL 2.0

{% highlight c %}
{% raw %}
#include <SDL.h>
#include <emscripten.h>
#include <stdlib.h>

SDL_Window *window;
SDL_Renderer *renderer;
SDL_Surface *surface;

void drawRandomPixels() {
    if (SDL_MUSTLOCK(surface)) SDL_LockSurface(surface);

    Uint8 * pixels = surface->pixels;
    
    for (int i=0; i < 1048576; i++) {
        char randomByte = rand() % 255;
        pixels[i] = randomByte;
    }

    if (SDL_MUSTLOCK(surface)) SDL_UnlockSurface(surface);

    SDL_Texture *screenTexture = SDL_CreateTextureFromSurface(renderer, surface);

    SDL_RenderClear(renderer);
    SDL_RenderCopy(renderer, screenTexture, NULL, NULL);
    SDL_RenderPresent(renderer);

    SDL_DestroyTexture(screenTexture);
}

int main(int argc, char* argv[]) {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_CreateWindowAndRenderer(512, 512, 0, &window, &renderer);
    surface = SDL_CreateRGBSurface(0, 512, 512, 32, 0, 0, 0, 0);
    
    emscripten_set_main_loop(drawRandomPixels, 0, 1);
}
{% endraw %}
{% endhighlight %}

Some things of note:

* You can't blit directly to the screen surface in SDL 2.0 (+ some expansion on this)

#### Testing

At the same folder location, open a shell / command prompt. Invoke the following Emscripten build commands:

{% highlight bash %}
{% raw %}
emcc -c sdl_2_0_sample.c -o sdl_2_0_sample.o -s USE_SDL=2
emcc sdl_2_0_sample.o -o sdl_2_0_sample.html -s USE_SDL=2
{% endraw %}
{% endhighlight %}

Note that this time we're passing in `-s USE_SDL=2`. This instructs Emscripten to switch of the built-in SDL 1.2 implementation and instead use the SDL 2.0 port.

You'll see three new files once the build completes:

* `sdl_2_0_sample.wasm` - the WebAssembly output
* `sdl_2_0_sample.js` - the asm.js output
* `sdl_2_0_sample.html` - a shell / wrapper file so you can launch your WebAssembly app in the browser

Again, use lightweight Web Server software like <a href="https://www.npmjs.com/package/http-server" target="_blank">http-server</a> to serve `sdl_2_0_sample.html` and open it in a Web Browser. You'll see the same white noise animation:

![](/img/posts/emscripten_sdl_2_0_sample.png)


### Cross-platform capability

We mentioned cross-platform capability above. But these examples have hardcodings for Emscripten/WebAssembly alone. How could we make this compatible cross platform?

{% highlight c %}
{% raw %}
#include <SDL.h>
#ifdef __EMSCRIPTEN__
#include <emscripten.h>
#endif
#include <stdlib.h>

SDL_Window *window;
SDL_Renderer *renderer;
SDL_Surface *surface;

void drawRandomPixels() {
    if (SDL_MUSTLOCK(surface)) SDL_LockSurface(surface);

    Uint8 * pixels = surface->pixels;
    
    for (int i=0; i < 1048576; i++) {
        char randomByte = rand() % 255;
        pixels[i] = randomByte;
    }

    if (SDL_MUSTLOCK(surface)) SDL_UnlockSurface(surface);

    SDL_Texture *screenTexture = SDL_CreateTextureFromSurface(renderer, surface);

    SDL_RenderClear(renderer);
    SDL_RenderCopy(renderer, screenTexture, NULL, NULL);
    SDL_RenderPresent(renderer);

    SDL_DestroyTexture(screenTexture);
}

int main(int argc, char* argv[]) {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_CreateWindowAndRenderer(512, 512, 0, &window, &renderer);
    surface = SDL_CreateRGBSurface(0, 512, 512, 32, 0, 0, 0, 0);
    
    #ifdef __EMSCRIPTEN__
    emscripten_set_main_loop(drawRandomPixels, 0, 1);
    #else
    while(1) {        
        drawRandomPixels();
        SDL_Delay(16);
    }
    #endif 
}
{% endraw %}
{% endhighlight %}

Notes:
* IFDEF around include statements
* IFDEF around render loop

The above code can now be built both with Emscripten/emcc *and* regular gcc. Here's what it looks like for Windows:

![](/img/posts/emscripten_sdl_2_0_mingw_sample.png)







### SDL1 vs 2

### WebAssembly has built-in support for WebAssembly

 
### Building SDL apps in WebAssembly
 
Next up
 
### File system and preloading files
 
Because the browser is sandboxed, you can't access the host file system
 
For this reason WebAssembly apps use a virtual file system. There are useful "pre-load" features you can use at build time to populate this virtual file system
 
- Expand on hello world article above to fopen a simple text file and show the string. Also have this is GitHub with a makefile
 
### Simulate main  loop is your friend
 
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
 