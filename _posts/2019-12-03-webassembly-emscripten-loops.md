---
layout: post
title: "WebAssembly Lesson 3: Emscripten Loops"
date: '2019-12-03 21:06:00:00'
summary: A deep-dive on Emscripten loops and Emterpreter
tags: [Programming, Web Development, Emscripten, WebAssembly, GameDev]
---

Games and other graphical apps often contain infinite loops to sequentially render animation frames to the screen:

{% highlight c %}
{% raw %}
int main(int argc, char* argv[]) {
    while(1) {        
        renderFrame();
        SDL_Delay(time_to_next_frame());
    }
}
{% endraw %}
{% endhighlight %}

This infinite loop is a problem in the browser environment because control is never returned to the browser. There's no opportunity to render graphics and the app will appear to hang - and after some time the browser will notify the user that the page is stuck and offer to halt or close it


### Emscripten Loops

Emscripten’s solution is `emscripten_set_main_loop`. This simulates an infinite loop, but in actuality just calls the loop function - in our case `renderFrame()` - at a specified number of frames per second. After each call completes, control is returned to the browser for rendering and other housekeeping. The adjusted code will look like this:

{% highlight c %}
{% raw %}
int main(int argc, char* argv[]) {
    emscripten_set_main_loop(renderFrame, 0, 1);
}
{% endraw %}
{% endhighlight %}

Remember to never block inside the loop function - doing so will prevent your app from drawing to the screen. Also you can only have one Emscripten loop running - no nesting!


#### emscripten_set_main_loop arguments

The function signature is:

{% highlight c %}
{% raw %}
void emscripten_set_main_loop(em_callback_func func, int fps, int simulate_infinite_loop)
{% endraw %}
{% endhighlight %}

Where:

* `func` = the loop function to invoke
<br /><br />
* `fps` = the number of times per second to invoke the loop function 
  * It's strongly recommended to set `fps` to `0`. This will use the browser's requestAnimatiomFrame mechanism to call the loop function - ensuring a smooth frame rate that lines up with the browser and monitor refresh rate
<br /><br />
* `simulate_infinite_loop` = the loop behaviour
  * If `simulate_infinite_loop` is set to `true`, the function will throw an exception to stop execution of the caller. This will lead to the main loop being entered instead of code after the call to `emscripten_set_main_loop()` being run - which is the closest we can get to simulating an infinite loop
  * If `simulate_infinite_loop` is set `false`, execution of the caller will continue after the call to `emscripten_set_main_loop()`

At any point we can cancel the Emscripten main loop by issuing `emscripten_cancel_main_loop()`. This will stop execution of the main loop function and prevent any further iterations

If you need to pass arguments to the loop function there is <a href="https://emscripten.org/docs/api_reference/emscripten.h.html#c.emscripten_set_main_loop_arg" target="_blank">emscripten_set_main_loop_arg</a>

You can find more info in the <a href="https://emscripten.org/docs/porting/emscripten-runtime-environment.html#browser-main-loop" target="_blank">official Emscripten documentation</a>


### Emscripten loops are not real loops

{% highlight c %}
{% raw %}
int main(int argc, char* argv[]) {
    while(1) {
        break();
    }

    /* 
    With a traditional loop, program will resume execuction from here once the loop is broken
    */
}
{% endraw %}
{% endhighlight %}

Unlike traditional loops, Emscripten loops will not resume execution of code beneath the `emscripten_set_main_loop` call when the loop is broken/cancelled. Here's how it works:
 
{% highlight c %}
{% raw %}
void loopFunction() {
    emscripten_cancel_main_loop();
}

int main(int argc, char* argv[]) {
    int simulate_infinite_loop = ?

    emscripten_set_main_loop(loopFunction, 0, simulate_infinite_loop);

    /* 
    * If simulate_infinite_loop = 0:
    *    - code here will execute straight away (even before loopFunction is called)
    *
    * If simulate_infinite_loop = 1:
    *    - code here will never execute
    *    (as emscripten_set_main_loop triggers an exception to prevent further code execution)
    */
}
{% endraw %}
{% endhighlight %}

Neither scenario works like a traditional loop, which means that code often requires significant refactoring to accomodate Emscripten loops. For a large code base the effort required might be prohibitive


#### Emterpreter to the rescue?
 
Because of the high effort required to rewrite traditional apps towards Emscripten loops, Emscripten provides the Emterpreter feature

In this mode, you can keep traditional infinite loops. You just need to replace your existing sleep/delay calls with `emscripten_sleep` calls: 

{% highlight c %}
{% raw %}
int main(int argc, char* argv[]) {
    while(1) {        
        renderFrame();
        // SDL_Delay(time_to_next_frame());
        emscripten_sleep(time_to_next_frame());
    }
}
{% endraw %}
{% endhighlight %}

During `emscripten_sleep`, your browser has the opportunity to render graphics to the screen and perform other actions it would normally be blocked from doing inside the infinite loop. Here's a real, working example you can try yourself:

{% highlight c %}
{% raw %}
#include <SDL.h>
#include <emscripten.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Surface *screen = SDL_SetVideoMode(512, 512, 32, SDL_SWSURFACE);
    
    while(1) {
        if (SDL_MUSTLOCK(screen)) SDL_LockSurface(screen);

        Uint8 * pixels = screen->pixels;
    
        for (int i=0; i < 1048576; i++) {
            char randomByte = rand() % 255;
            pixels[i] = randomByte;
        }

        if (SDL_MUSTLOCK(screen)) SDL_UnlockSurface(screen);

        SDL_Flip(screen);

        emscripten_sleep(16);
    }
}
{% endraw %}
{% endhighlight %}

You can build with the following commands. Then serve `<filename>.html` and open it in your browser

{% highlight bash %}
{% raw %}
emcc -c <filename>.c -o <filename>.o -s EMTERPRETIFY=1 -s EMTERPRETIFY_ASYNC=1
emcc <filename>.o -o <filename>.html -s EMTERPRETIFY=1 -s EMTERPRETIFY_ASYNC=1
{% endraw %}
{% endhighlight %}

If the build fails, try downloading and activating the "fastcomp" version of the Emscripten SDK. There are plans to drop Emterpreter support from the default version of the SDK 

When you run this sample, you'll immediately see the issues with Emterpreter - it's incredibly slow. The stack has to be unwound and reassembled for every `emscripten_sleep()` call - an expensive operation. The recommendation is to use Emterpreter sparingly and refactor towards Emscripten loops wherever you can

That's the end of Lesson 3! Next time we'll look at FileIO