---
layout: post
title: "How to Build Commander Keen for PlayStation Vita"
summary: "<strong>A deep dive follow-up to last week's video on porting Commander Keen to WebAssembly</strong>. I'll go step by step on how to setup your dev environment and port Keen to run in the web browser."
date: '2024-06-07 08:00:00:00'
tags: [Programming, Sony PlayStation, Sony PlayStation Vita, Videogames]
---

CONSIDER TURNING THIS AND ALSO THE WEBASSEMBLY ARTICLE INTO GENERAL ARTICLES:

"HOW TO BUILD C++ CODE FOR WEBASSEMBLY / PS VITA"

I THINK THESE MAY BE MORE BLOG POSTS THAN HOW TO GUIDES

SO CONSIDER TAKING THE BELOW AND TURNING INTO A BLOG POST (to wrap up the existing posts that already exist)


<a name="Porting Commander Keen to PlayStation Vita">
## Porting Commander Keen to PlayStation Vita 

Status | In Progress
Goal | Bring the DOS classic <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> to <a href="https://en.wikipedia.org/wiki/PlayStation_Vita" target="_blank">PlayStation Vita</a>.

I've wanted to explore <a href="https://en.wikipedia.org/wiki/Cross_compiler" target="_blank">cross-compilation</a> (i.e. building code on one platform for execution on another) for a while. I'm also passionate about bringing classic retro games to a new audience.

With the advent of <a href="https://vita.hacks.guide/installing-h-encore.html" target="_blank">h-encore</a>, pretty much any <a href="https://en.wikipedia.org/wiki/PlayStation_Vita" target="_blank">PlayStation Vita</a> can now be unlocked to run <a href="https://en.wikipedia.org/wiki/Homebrew_(video_gaming)" target="_blank">homebrew</a> code. There's also the <a href="https://vitasdk.org/" target="_blank">Vita SDK</a> development framework available to help create working binaries. So the Vita seems like a great target platform.

I'm aiming to bring <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> (in the form of <a href="https://github.com/jamesfmackenzie/clonekeen" target="_blank">CloneKeen</a>) to the Vita. The source code is C/C++ and uses the multiplatform <a href="https://www.libsdl.org/" target="_blank">SDL</a> development library, so should be relatively portable. I'm also looking for improvement opportunities over the orignal release (e.g. level editor, increased resolution).

So far I have the <a href="https://twitter.com/jamesfmackenzie/status/1193643306850369536">game engine running</a>, but need to add controller support.

Posts:

- <a href="https://twitter.com/jamesfmackenzie/status/1193643306850369536">Game engine successfully running on a real Vita</a> - 10 Nov 2019

<br />