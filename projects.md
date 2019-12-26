---
layout: nocomments
title: Projects
---

## Porting Commander Keen to PlayStation Vita 

Status | In Progress
Goal | Bring the DOS classic <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> to <a href="https://en.wikipedia.org/wiki/PlayStation_Vita" target="_blank">PlayStation Vita</a>

I've wanted to explore cross-compilation (i.e. building code on one platform for execution on another) for a while. I'm also passionate about bringing classic retro games to a new audience

With the advent of h-encore, pretty much any PlayStation Vita can now be unlocked to run homebrew code. There's also the <a href="https://vitasdk.org/" target="_blank">Vita SDK</a> homebrew framework available to help create working binaries. So the Vita seems like a great target platform

I'm aiming to bring Commander Keen (in the form of <a href="https://github.com/jamesfmackenzie/clonekeen" target="_blank">CloneKeen</a>) to the Vita. The source code is C/C++ and uses the SDL development library, so should be relatively portable

I'm also looking for improvement opportunities over the orignal release (e.g. level editor, take advantage of Vita's increased resolution)

So far I have the <a href="https://twitter.com/jamesfmackenzie/status/1193643306850369536">game engine running</a>, but need to add controller support

Posts:
- <a href="https://twitter.com/jamesfmackenzie/status/1193643306850369536">Game engine successfully running on a real Vita</a> - 10 Nov 2019

<br />

## Porting Commander Keen to WebAssembly 

Status | Completed November 2019
Goal | Port <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> to <a href="https://en.wikipedia.org/wiki/WebAssembly" target="_blank">WebAssembly</a>, making it playable in the Browser

I've wanted to find a creative outlet for my recently-acquired WebAssembly skills. I'm also passionate about bringing classic retro games to a new audience

I used <a href="https://emscripten.org/" target="_blank">Emscripten</a> to port <a href="https://github.com/jamesfmackenzie/chocolatekeen" target="_blank">Chocolate Keen</a> to WebAssembly. The initial goal was to refactor the entire code base to [Emscripten Loops]({% post_url 2019-12-03-webassembly-emscripten-loops %}) but this proved too much effort. In the end I found a working (but slower) solution using <a href="https://github.com/emscripten-core/emscripten/wiki/Emterpreter" target="_blank">Emterpreter</a>

I'm happy with the end result. Play Commander Keen in the browser right <a href="http://jamesfmackenzie.com/chocolatekeen">here</a>, instructions [here]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %}) and source code <a href="https://github.com/jamesfmackenzie/chocolatekeen">on GitHub</a>

In future, I could refactor towards Emscripten Loops to improve performance and add on-screen controls for mobile devices

Posts:
- <a href="https://twitter.com/jamesfmackenzie/status/1190604121717592064?s=21" target="_blank">The Commander Keen WebAssembly port is done!</a> - 02 Nov 2019
- [Commander Keen in a Web Browser?]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %}) - 28 Oct 2019
- <a href="https://twitter.com/jamesfmackenzie/status/1186034903294644224?s=21" target="_blank">Porting Commander Keen / CloneKeen to the web browser with #Emscripten. Great progress so far!</a> - 20 Oct 2019

<br />

## Learning about WebAssembly

Status | Completed November 2019
Goal | Learn about <a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a>. Understand how to make C/C++ code run in the Browser. Code some "Hello World" examples and document my findings

I've wanted to explore the WebAssembly ecosystem for a while. I learn best by sharing what I learn, so I've written up my findings as WebAssembly Lessons:

- [Lesson 1: WebAssembly Hello World]({% post_url 2019-11-30-whats-is-webassembly-hello-world %}) - 30 Nov 2019
- [Lesson 2: Graphics with SDL]({% post_url 2019-12-01-webassembly-graphics-with-sdl %}) - 01 Dec 2019
- [Lesson 3: Emscripten Loops]({% post_url 2019-12-03-webassembly-emscripten-loops %}) - 03 Dec 2019
- [Lesson 4: File System Access]({% post_url 2019-12-08-webassembly-loading-files %}) - 08 Dec 2019

<br />

## Ultimate Retrogaming Machine

Status | Completed October 2018
Goal | Build a cheap, small and light device to retrogame on the big screen

I'm a big fan of retro games, with many fond memories of the 8 and 16-bit years. Looking for a way to relive those memories on the big screen

I selected the <a href="https://www.raspberrypi.org/" target="_blank">Raspberry Pi</a> and <a href="https://retropie.org.uk/" target="_blank">RetroPie</a> as the base for my build. After a week-or-so of on/off tweaking, I found optimal settings and documented the full setup [here]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}). For Phase 2, I [configured Moonlight Game Streaming]({% post_url 2018-11-17-gamestream-moonlight-on-retropie %}) to allow low latency streaming of more demanding titles from my gaming PC

Overall pleased with the result, and pleasantly surprised by how well Moonlight Game Streaming works

Posts:
- [RetroPie Ultimate Setup Guide]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}) - 08 Oct 2018
- [Stream PC Games to your RetroPie with GameStream and Moonlight]({% post_url 2018-11-17-gamestream-moonlight-on-retropie %}) - 08 Oct 2018

<br />

## Atari ST on the Web

Status | Completed June 2018
Goal | Connect my venerable [Atari ST]({% post_url 2015-08-15-atari-in-the-attic %}) to the World Wide Web. Browse some sites!

The Atari ST was released in 1985. Is it usable on the modern Web today? How far can I push the experience?

Starting with a <a href="https://lotharek.pl/productdetail.php?id=46" target="_blank">NetUSBee</a> Ethernet adapter, I <a href="http://hardware.atari.org/manuals/netsting.htm" target="_blank">installed TOS drivers and the STinG TCP/IP stack</a>. I also used an ET4000 graphics card to push the resolution to a (somewhat) modern 1024x768 in 256 colours

With those (and a succesful TCP/IP ping) in place, I <a href="https://breakintochat.com/blog/2017/09/05/web-browsing-on-the-atari-st-with-a-cosmosex/" target="_blank">downloaded and configured Crystal Atari Browser (CAB)</a>

The Web experience is slow and doesn't support CSS - which rules out a lot of content. However I was able to make <a href="https://twitter.com/jamesfmackenzie/status/1004495104885886978" target="_blank">older sites work</a>

In search of a better experience: it might be possible to use a proxy server to strip CSS and shrink images. Or use a text-based browser like Lynx. Browsh also looks interesting. Lots of avenues for future investigation!

<br />

## Shooting and Sharing VR Photos

Status | Completed November 2016
Goal | Learn how to shoot, interactively view and share VR photos

Ever seen one of those photos you can zoon and pan around?

VR photography (after Virtual Reality photography) is the art of capturing or creating a complete scene as a single image, as viewed when rotating about a single central position

I want to know how to shoot, interactively view and share my own photos

I learned that the Google Street View app is a cheap and easy way to shoot images as equirectangar format. I then learned how to convert these imagss into to various formats other including cube-face and .pano files. Finally I learned how to share to Photosyth, Facebook and YouTube

Posts:
- Publishing VR Panoramas to YouTube - 08 Sep 2019
- All You Need to Know about 360 VR Photos - 02 Nov 2016
- Convert Equirectangular Projection to .Pano File - 30 Oct 2016
- What are .pano files? - 29 Oct 2016
- Publishing VR Panoramas to Photosynth - 28 Oct 2016
- Convert Equirectangular Projection to Cube Faces - 18 Oct 2016
- Publishing VR Panoramas to Facebook - 12 Oct 2016

<br />

## Transferring files between PC and ST

Status | Completed March 2016
Goal | Explore the various ways to share files between PC and Atari ST

Can my Atari ST interoperate with modern PCs? What are the best ways to send files back and forth?

I explored several ways to transfer files between PC and Atari ST, including:

- Using an SD card and Ultrasatan to Transfer Files from PC to ST - 08 Mar 2016
- Using Ethernet to Transfer Files from PC to ST - 07 Mar 2016
- Using PARCP-USB to Transfer Files from PC to ST - 24 Feb 2016
- Using Serial Cable and ZMODEM to Transfer Files from PC to ST - 13 Feb 2016
- Using Serial Cable and Ghostlink to Transfer Files from PC to ST - 06 Feb 2016
- Using Floppy Disk to Transfer Files from PC to ST - 30 Jan 2016

I also took a detour into file compression, and learned how to split large files into chunks that can be individually copied using (for example) floppy disks:

- How to Split and Copy Large Files to Your Atari ST in Chunks - 31 Jan 2016

<br />

## Playing downloaded games on real ST hardware (Sep 2015)

Status | Completed September 2015
Goal | Download an Atari ST game image from the web and play it on my real ST

My old ST disks are dead! Can I download a replacement image from the web and play on my physical ST?

I explored several options, including floppy disk images and hard disk adaptations:

- Use Your PC to Create a Bootable Atari ST Game Disk - 22 Sep 2015
- Playing Downloaded Games on a Real Atari ST - 18 Sep 2015

<br />

## Watch mobile content on the go

Status | Completed December 2014
Goal | Download video content to my mobile device so I can watch it on the go

The work commute is a great time to catch up on news, vlogs and other web videos. But cellphone signal is way too patchy for reliable streaming - especially in the subway.

I explored use of the Pocket API and PlexSync to download and push web videos to my phone:

- Sync Web Videos to Your Tablet or Phone, Watch Them Offline - 01 Feb 2015
- Download Pocket Videos to Your PC - 03 Jan 2015
- I Can't Stream Video on the Commute. How Can I Fix It? - 17 Dec 2014

<br />

## Ghost blogging

Status | Completed June 2014
Goal | Learn how to use the Ghost blogging platform

Note: today I use the Jekyll blog engine

I'm always interested in crisp, lightweight blogging platforms. I took some to learn about the Ghost blogging platform, setup my own developmemt environment and even write my own theme

Posts:
- Things I Wish I'd Known Before Creating My Own Ghost Theme - 23 Jun 2014
- It's Done! 8-Bit Memories Ghost Theme - 21 Jun 2014
- Create Your Own Ghost Theme in 5 Minutes - 10 Jun 2014
- Setting Up a Ghost Dev Environment - 17 May 2014
- Getting to Grips With Ghost Themes - 24 Apr 2014
