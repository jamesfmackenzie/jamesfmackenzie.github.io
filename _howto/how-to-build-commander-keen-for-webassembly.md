---
layout: youtube
title: "How to Build Commander Keen in WebAssembly"
summary: "<strong>A deep dive follow-up to last week's video on porting Commander Keen to WebAssembly</strong>. I'll go step by step on how to setup your dev environment and port Keen to run in the web browser."
date: '2024-06-07 08:00:00:00'
videoId: in05zYjIIE4
tags: [Programming, Videogames, WebAssembly]
---


CONSIDER TURNING THIS AND ALSO THE WEBASSEMBLY ARTICLE INTO GENERAL ARTICLES:

"HOW TO BUILD C++ CODE FOR WEBASSEMBLY / PS VITA"

I THINK THESE MAY BE MORE BLOG POSTS THAN HOW TO GUIDES

SO CONSIDER TAKING THE BELOW AND TURNING INTO A BLOG POST (to wrap up the existing posts that already exist)


<a name="Porting Commander Keen to WebAssembly">
## Porting Commander Keen to WebAssembly 

Status | Completed November 2019
Goal | Port <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> to <a href="https://en.wikipedia.org/wiki/WebAssembly" target="_blank">WebAssembly</a>, making it playable in the Browser

I've wanted to find a creative outlet for my <a href="#Learning about Webassembly">recently-acquired WebAssembly skills</a>. I'm also passionate about bringing classic retro games to a new audience.

I used <a href="https://emscripten.org/" target="_blank">Emscripten</a> to port <a href="https://github.com/jamesfmackenzie/chocolatekeen" target="_blank">Chocolate Keen</a> to WebAssembly. The initial goal was to refactor the entire code base to [Emscripten Loops]({% post_url 2019-12-03-webassembly-emscripten-loops %}) but this proved too much effort. In the end I found a working (but slower) solution using <a href="https://github.com/emscripten-core/emscripten/wiki/Emterpreter" target="_blank">Emterpreter</a>.

I'm happy with the end result. Play Commander Keen in the browser right <a href="http://jamesfmackenzie.com/chocolatekeen" target="_blank">here</a>, find instructions [here]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %}) and source code <a href="https://github.com/jamesfmackenzie/chocolatekeen" target="_blank">on GitHub</a>.

In future, I could refactor towards Emscripten Loops to improve performance and add on-screen controls for mobile devices.

Posts:

- <a href="https://twitter.com/jamesfmackenzie/status/1186034903294644224?s=21" target="_blank">Porting Commander Keen / CloneKeen to the web browser with #Emscripten. Great progress so far!</a> - 20 Oct 2019
- [Commander Keen in a Web Browser?]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %}) - 28 Oct 2019
- <a href="https://twitter.com/jamesfmackenzie/status/1190604121717592064?s=21" target="_blank">The Commander Keen WebAssembly port is done!</a> - 02 Nov 2019