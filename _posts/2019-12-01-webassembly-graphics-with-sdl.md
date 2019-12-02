---
layout: post
title: WebAssembly Lesson 1: Graphics with SDL
date: '2019-12-01 19:18:00:00'
summary: Using Simple DirectMedia Layer (SDL) to render graphics in the browser
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

Yes! Emscripten (which we'll use to compile for WebAssembly) has a simple implementation of SDL 1.2's API built in. This is hand-written in JavaScript and unrelated to the SDL codebase - but with compatibility high enough for most simple use cases

SDL 2.0 support is also included via <a href="https://github.com/emscripten-ports" target="_blank">Emscripten Ports</a> - a collection of useful libraries, ported to Emscripten and integrated with the Emscripten compiler (emcc)

We'll take a look at both of these below 


### Running SDL 1.2 code in the browser

First, install and configure the Emscripten SDK (instructions <a href="https://emscripten.org/docs/getting_started/downloads.html" target="_blank">here</a>)

Next, copy-paste the C code below and save it on your local machine as `sdl_1_2_sample.c`. It's a tiny SDL program that renders random pixel data to the screen - it'll look like white noise

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
    
    emscripten_set_main_loop(drawRandomPixels, 60, 1);
}
{% endraw %}
{% endhighlight %}

Take special note of the `emscripten_set_main_loop` call

Games and other graphical apps often contain infinite loops to sequentially render animation frames to the screen

This infinite loop is a problem in the browser environment because control is never returned to the browser to render graphics. The app will appear to hang - and after some time the browser will notify the user that the page is stuck and offer to halt or close it

Emscripten's solution is `emscripten_set_main_loop`. This *simulates* an infinite loop, but in actuality just calls the loop function (in our case `drawRandomPixels()`

The JavaScript environment will call that function at a specified number of frames per second. After each call completes, control is returned to the browser for rendering and other housekeeping

Find more info <a href="https://emscripten.org/docs/porting/emscripten-runtime-environment.html#browser-main-loop" target="_blank">here</a>. We'll explore this more in the next Lesson

#### Build and Run

Still in the same directory, open a shell / command prompt. Invoke the following Emscripten build commands:

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


### Upgrading to SDL 2.0

Next, let's upgrade our sample code to SDL 2.0

Copy-paste the modified C code below and save it on your local machine as `sdl_2_0_sample.c`. It's a modified version of the above code - but targeting SDL 2.0 instead of SDL 1.2

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

The main change here is that you can no longer Flip pixels directly to the screen. You need to push pixels into a texture (in GPU RAM) and issue rendering calls to update the screen. More info <a href="https://wiki.libsdl.org/MigrationGuide#Video" target="_blank">here</a>


#### Build and Run

To build this SDL 2.0 sample you'll need a slightly different build command: 

{% highlight bash %}
{% raw %}
emcc -c sdl_2_0_sample.c -o sdl_2_0_sample.o -s USE_SDL=2
emcc sdl_2_0_sample.o -o sdl_2_0_sample.html -s USE_SDL=2
{% endraw %}
{% endhighlight %}

This time we're passing in the `USE_SDL=2` codegen option. This instructs Emscripten to switch off the built-in SDL 1.2 implementation and compile with the SDL 2.0 port

Similar to before, `emcc` will generate three files: `sdl_2_0_sample.wasm`, `sdl_2_0_sample.js` and `sdl_2_0_sample.html`

Serve `sdl_2_0_sample.html` and open it in a Web Browser. You'll see the same white noise animation, but this time powered by SDL 2.0:

![](/img/posts/emscripten_sdl_2_0_sample.png)


### Cross-platform capability

Our examples have hardcodings for Emscripten/WebAssembly - hardcodings that will break a traditional C compilation with gcc. With some adjustments we can use the same source code to target multiple platforms:

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

Here we've used `#ifdef` statements to change compilation behaviour under native build scenarios:

* Avoid loading the `emscripten.h` headers
* Replace `emscripten_set_main_loop` with a traditional infinite loop

We can now compile the above code into WebAssembly with Emscripten/emcc *and* native executables with regular gcc. Here's what it looks like running as a Windows app:

![](/img/posts/emscripten_sdl_2_0_mingw_sample.png)


 