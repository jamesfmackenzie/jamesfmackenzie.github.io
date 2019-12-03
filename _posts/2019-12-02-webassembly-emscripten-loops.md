---
layout: post
title: WebAssembly Lesson 3: Emscripten Loops
date: '2019-12-02 19:18:00:00'
summary: Understanding Emscripten Loops and Emterpreter
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

Emscripten’s solution is `emscripten_set_main_loop`. This simulates an infinite loop, but in actuality just calls the loop function - in our case `renderFrame()` - at a specified number of frames per second. After each call completes, control is returned to the browser for rendering and other housekeeping:

{% highlight c %}
{% raw %}
int main(int argc, char* argv[]) {
    emscripten_set_main_loop(renderFrame, 0, 1);
}
{% endraw %}
{% endhighlight %}

Remember to never block inside the loop function - doing so will prevent your app from drawing to the screen. You can only have one Emscripten loop running - no nesting


### Cross-platform capability 

As we saw in the last lesson, we can use `#ifdef` statements to make code compatible with both Emscripten and native environments:

{% highlight c %}
{% raw %}
int main(int argc, char* argv[]) {

    #ifdef __EMSCRIPTEN__
    emscripten_set_main_loop(renderFrame, 0, 1);
    #else
    while(1) {        
        renderFrame();
        SDL_Delay(time_to_next_frame());
    }
    #endif
}
{% endraw %}
{% endhighlight %}


### emscripten_set_main_loop arguments

The function signature is `void emscripten_set_main_loop(em_callback_func func, int fps, int simulate_infinite_loop)`

Where:

* `func` = the loop function to invoke
* `fps` = the number of times per second to invoke the loop function
* `simulate_infinite_loop` = loop behaviour (see below)

It's strongly recommended to set `fps` to `0`. This will use the browser's requestAnimatiomFrame mechanism to call the loop function - ensuring a smooth frame rate that lines up with the browser and monitor refresh rate

If `simulate_infinite_loop` is true, the function will throw an exception to stop execution of the caller. This will lead to the main loop being entered instead of code after the call to `emscripten_set_main_loop()` being run - which is the closest we can get to simulating an infinite loop

If `simulate_infinite_loop` is false, execution of the caller will continue after the call to `emscripten_set_main_loop()`


 
### Breaking the loop

- placeholder 

### Passing arguments to an Emscripten Loop

- placeholder

 
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
 
