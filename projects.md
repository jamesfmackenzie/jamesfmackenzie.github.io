---
layout: nocomments
title: Projects
---

## Porting Commander Keen to PlayStation Vita 

Status | In Progress
Goal | Bring the DOS classic <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> to <a href="https://en.wikipedia.org/wiki/PlayStation_Vita" target="_blank">PlayStation Vita</a>

I'm using the <a href="https://vitasdk.org/" target="_blank">Vita SDK</a> homebrew framework to port <a href="https://github.com/jamesfmackenzie/clonekeen" target="_blank">CloneKeen</a> (which is a C/C++ code base) to Vita. Will require a hacked Vita to run

Posts:
- <a href="https://twitter.com/jamesfmackenzie/status/1193643306850369536">Game engine successfully running on a real Vita</a> - 10 Nov 2019

<br />

## Porting Commander Keen to WebAssembly 

Status | Completed November 2019
Goal | Port <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> to <a href="https://en.wikipedia.org/wiki/WebAssembly" target="_blank">WebAssembly</a>, making it playable in the Browser

I used <a href="https://emscripten.org/" target="_blank">Emscripten</a> to port <a href="https://github.com/jamesfmackenzie/chocolatekeen" target="_blank">Chocolate Keen</a> to WebAssembly. The initial goal was to refactor the entire code base to [Emscripten Loops]({% post_url 2019-12-03-webassembly-emscripten-loops %}) but this proved too much effort. In the end I found a working (but slower) solution using <a href="https://github.com/emscripten-core/emscripten/wiki/Emterpreter" target="_blank">Emterpreter</a>

Links:
- Play Commander Keen in the browser right <a href="http://jamesfmackenzie.com/chocolatekeen">here</a>!
- Find instructions [here]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %})
- Source code available <a href="https://github.com/jamesfmackenzie/chocolatekeen">on GitHub</a>

Posts:
- <a href="https://twitter.com/jamesfmackenzie/status/1190604121717592064?s=21" target="_blank">The Commander Keen WebAssembly port is done!</a> - 02 Nov 2019
- [Commander Keen in a Web Browser?]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %}) - 28 Oct 2019
- <a href="https://twitter.com/jamesfmackenzie/status/1186034903294644224?s=21" target="_blank">Porting Commander Keen / CloneKeen to the web browser with #Emscripten. Great progress so far!</a> - 20 Oct 2019

<br />

## Learning about WebAssembly

Status | Completed November 2019
Goal | Learn about <a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a>. Understand how to make C/C++ code run in the Browser. Code some "Hello World" examples and document my findings

Findings:
- [Lesson 1: WebAssembly Hello World]({% post_url 2019-11-30-whats-is-webassembly-hello-world %}) - 30 Nov 2019
- [Lesson 2: Graphics with SDL]({% post_url 2019-12-01-webassembly-graphics-with-sdl %}) - 01 Dec 2019
- [Lesson 3: Emscripten Loops]({% post_url 2019-12-03-webassembly-emscripten-loops %}) - 03 Dec 2019
- [Lesson 4: File System Access]({% post_url 2019-12-08-webassembly-loading-files %}) - 08 Dec 2019

<br />

## Ultimate Retrogaming Machine

Status | Completed October 2018
Goal | Build a cheap, small and light device to retrogame on the big screen

I selected the <a href="https://www.raspberrypi.org/" target="_blank">Raspberry Pi</a> and <a href="https://retropie.org.uk/" target="_blank">RetroPie</a> as the base for my build. After a week-or-so of on/off tweaking, I found optimal settings and documented the full setup [here]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}). For Phase 2, I [configured Moonlight Game Streaming]({% post_url 2018-11-17-gamestream-moonlight-on-retropie %}) to allow low latency streaming of more demanding titles from my gaming PC

Posts:
- [RetroPie Ultimate Setup Guide]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}) - 08 Oct 2018
- [Stream PC Games to your RetroPie with GameStream and Moonlight]({% post_url 2018-11-17-gamestream-moonlight-on-retropie %}) - 08 Oct 2018

<br />

## Atari ST on the Web

Status | Completed June 2018
Goal | Connect my venerable [Atari ST]({% post_url 2015-08-15-atari-in-the-attic %}) to the World Wide Web. Browse some sites!

Starting with a <a href="https://lotharek.pl/productdetail.php?id=46" target="_blank">NetUSBee</a> Ethernet adapter, I <a href="http://hardware.atari.org/manuals/netsting.htm" target="_blank">installed TOS drivers and the STinG TCP/IP stack</a>. With those (and succesful TCP/IP ping) in place, I <a href="https://breakintochat.com/blog/2017/09/05/web-browsing-on-the-atari-st-with-a-cosmosex/" target="_blank">downloaded and configured Crystal Atari Browser (CAB)</a>. <a href="https://twitter.com/jamesfmackenzie/status/1004495104885886978" target="_blank">Hey presto!</a>

<br />

## VR panoramas

Status | Completed November 2016
Goal | Learn how to shoot, display and share VR panoramas

Pending

<br />

## Transferring files from PC to ST and vice versa

Status | Completed March 2016
Goal | Can my Atari ST interoperate with modern PCs? What are the best ways to send files back and forth?

Pending

<br />

## Playing downloaded games on real ST hardware (Sep 2015)

Status | Completed September 2015
Goal | My old ST disks are dead! Can I download a replacement image from the web and play on my physical ST?

Pending

<br />

## Watch mobile content on the go

Status | Completed December 2014
Goal | Download video content to my mobile device so I can watch it on the go

Pending

<br />

## Ghost blogging

Status | Completed June 2014
Goal | Learn how to use the Ghost blogging platform

Pending
