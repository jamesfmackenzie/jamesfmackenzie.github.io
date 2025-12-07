---
layout: post
title: Porting Commander Keen to PlayStation Vita 
date: '2020-02-01 12:00:00'
tags: [Programming, Projects, Retrogaming, Sony PlayStation, Videogames]
status: in progress
---

I've wanted to explore <a href="https://en.wikipedia.org/wiki/Cross_compiler" target="_blank">cross-compilation</a> (i.e. building code on one platform for execution on another) for a while. I'm also passionate about bringing classic retro games to a new audience.

With the advent of <a href="https://vita.hacks.guide/installing-h-encore.html" target="_blank">h-encore</a>, pretty much any <a href="https://en.wikipedia.org/wiki/PlayStation_Vita" target="_blank">PlayStation Vita</a> can now be unlocked to run <a href="https://en.wikipedia.org/wiki/Homebrew_(video_gaming)" target="_blank">homebrew</a> code. There's also the <a href="https://vitasdk.org/" target="_blank">Vita SDK</a> development framework available to help create working binaries. So the Vita seems like a great target platform.


### Project Notes

Status | In Progress
Goal | Bring the DOS classic <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> to <a href="https://en.wikipedia.org/wiki/PlayStation_Vita" target="_blank">PlayStation Vita</a>.



I'm aiming to bring <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> (in the form of <a href="https://github.com/jamesfmackenzie/clonekeen" target="_blank">CloneKeen</a>) to the Vita. The source code is C/C++ and uses the multiplatform <a href="https://www.libsdl.org/" target="_blank">SDL</a> development library, so should be relatively portable. I'm also looking for improvement opportunities over the orignal release (e.g. level editor, increased resolution).

So far I have the <a href="https://twitter.com/jamesfmackenzie/status/1193643306850369536">game engine running</a>, but need to add controller support.

More to come!


### Project Updates

- [I’m porting Commander Keen to PSVita. Should I continue with it?]({% post_url 2025-04-06-porting-commander-keen-to-ps-vita-playstation-vita %}) - May 6, 2025
- [Hack day! Commander Keen now running on PSVita]({% post_url 2019-11-10-commander-keen-clonekeen-ps-vita-psvita %}) - Nov 10, 2019

<br />