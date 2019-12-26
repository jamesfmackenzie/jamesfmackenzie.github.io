---
layout: nocomments
title: Projects
---

## Projects

* <a href="#Porting Commander Keen to PlayStation Vita">Porting Commander Keen to PlayStation Vita</a> - In Progress
* <a href="#Porting Commander Keen to WebAssembly">Porting Commander Keen to WebAssembly</a> - Nov 2019
* <a href="#Learning about Webassembly">Learning About Webassembly</a> - Nov 2019
* <a href="#Ultimate Retrogaming Machine">Ultimate Retrogaming Machine</a> - Oct 2018
* <a href="#Atari ST on the Web">Atari ST on the Web</a> - Jun 2018
* <a href="#Shooting and Sharing VR Photos">Shooting and Sharing VR Photos</a> - Nov 2016
* <a href="#Transferring Files Between PC and ST">Transferring Files Between PC and ST</a> - Mar 2016
* <a href="#Playing Downloaded Games on Real ST Hardware">Playing Downloaded Games on Real ST Hardware</a> - Sep 2015
* <a href="#Watch Mobile Content on the Go">Watch Mobile Content on the Go</a> - Dec 2014
* <a href="#Ghost Blogging">Ghost Blogging</a> - Jun 2014

<br />

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

<a name="Porting Commander Keen to WebAssembly">
## Porting Commander Keen to WebAssembly 

Status | Completed November 2019
Goal | Port <a href="https://en.wikipedia.org/wiki/Commander_Keen" target="_blank">Commander Keen</a> to <a href="https://en.wikipedia.org/wiki/WebAssembly" target="_blank">WebAssembly</a>, making it playable in the Browser

I've wanted to find a creative outlet for my <a href="#Learning about Webassembly">recently-acquired WebAssembly skills</a>. I'm also passionate about bringing classic retro games to a new audience.

I used <a href="https://emscripten.org/" target="_blank">Emscripten</a> to port <a href="https://github.com/jamesfmackenzie/chocolatekeen" target="_blank">Chocolate Keen</a> to WebAssembly. The initial goal was to refactor the entire code base to [Emscripten Loops]({% post_url 2019-12-03-webassembly-emscripten-loops %}) but this proved too much effort. In the end I found a working (but slower) solution using <a href="https://github.com/emscripten-core/emscripten/wiki/Emterpreter" target="_blank">Emterpreter</a>.

I'm happy with the end result. Play Commander Keen in the browser right <a href="http://jamesfmackenzie.com/chocolatekeen" target="_blank">here</a>, find instructions [here]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %}) and source code <a href="https://github.com/jamesfmackenzie/chocolatekeen" target="_blank">on GitHub</a>.

In future, I could refactor towards Emscripten Loops to improve performance and add on-screen controls for mobile devices.

Posts:
- <a href="https://twitter.com/jamesfmackenzie/status/1190604121717592064?s=21" target="_blank">The Commander Keen WebAssembly port is done!</a> - 02 Nov 2019
- [Commander Keen in a Web Browser?]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %}) - 28 Oct 2019
- <a href="https://twitter.com/jamesfmackenzie/status/1186034903294644224?s=21" target="_blank">Porting Commander Keen / CloneKeen to the web browser with #Emscripten. Great progress so far!</a> - 20 Oct 2019

<br />

<a name="Learning about Webassembly">
## Learning About WebAssembly

Status | Completed November 2019
Goal | Learn about <a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a>. Understand how to make C/C++ code run in the Browser. Code some "Hello World" examples and document my findings

I've wanted to explore the <a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a> ecosystem for a while. I learn best by sharing what I learn, so I've written up my findings as WebAssembly Lessons:

- [Lesson 1: WebAssembly Hello World]({% post_url 2019-11-30-whats-is-webassembly-hello-world %}) - 30 Nov 2019
- [Lesson 2: Graphics with SDL]({% post_url 2019-12-01-webassembly-graphics-with-sdl %}) - 01 Dec 2019
- [Lesson 3: Emscripten Loops]({% post_url 2019-12-03-webassembly-emscripten-loops %}) - 03 Dec 2019
- [Lesson 4: File System Access]({% post_url 2019-12-08-webassembly-loading-files %}) - 08 Dec 2019

<br />

<a name="Ultimate Retrogaming Machine">
## Ultimate Retrogaming Machine

Status | Completed October 2018
Goal | Build a cheap, small and light device to retrogame on the big screen

I'm a big fan of retro games, with many fond memories of the <a href="https://en.wikipedia.org/wiki/Third_generation_of_video_game_consoles" target="_blank">8-bit</a> and <a href="https://en.wikipedia.org/wiki/Fourth_generation_of_video_game_consoles" target="_blank">16-bit</a> years. Looking for a way to relive those memories on the big screen.

I selected the <a href="https://www.raspberrypi.org/" target="_blank">Raspberry Pi</a> and <a href="https://retropie.org.uk/" target="_blank">RetroPie</a> as the base for my build. After a week of on/off tweaking, I found optimal settings and documented the full setup [here]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}). For Phase 2, I [configured Moonlight Game Streaming]({% post_url 2018-11-17-gamestream-moonlight-on-retropie %}) to allow low latency streaming of more demanding titles from my gaming PC.

Overall very pleased with the result, and pleasantly surprised by how well Moonlight Game Streaming works.

Posts:
- [RetroPie Ultimate Setup Guide]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}) - 08 Oct 2018
- [Stream PC Games to your RetroPie with GameStream and Moonlight]({% post_url 2018-11-17-gamestream-moonlight-on-retropie %}) - 08 Oct 2018

<br />

<a name="Atari ST on the Web">
## Atari ST on the Web

Status | Completed June 2018
Goal | Connect my venerable [Atari ST]({% post_url 2015-08-15-atari-in-the-attic %}) to the World Wide Web. Browse some sites!

The Atari ST was released in 1985. Is it usable on the modern Web today? How far can I push the experience?

Starting with a <a href="https://lotharek.pl/productdetail.php?id=46" target="_blank">NetUSBee</a> Ethernet adapter, I <a href="http://hardware.atari.org/manuals/netsting.htm" target="_blank">installed TOS drivers and the STinG TCP/IP stack</a>. I also used an <a href="http://www.atari-wiki.com/index.php/Graphics_cards" target="_blank">ET4000 graphics card</a> to push the resolution to a (somewhat) modern 1024x768 in 256 colours.

With those (and a successful TCP/IP ping) in place, I <a href="https://breakintochat.com/blog/2017/09/05/web-browsing-on-the-atari-st-with-a-cosmosex/" target="_blank">downloaded and configured Crystal Atari Browser (CAB)</a>.

The Web experience is slow and doesn't support CSS - which rules out a lot of content. However I was able to make <a href="https://twitter.com/jamesfmackenzie/status/1004495104885886978" target="_blank">older sites work</a>.

In search of a better experience: it might be possible to use a <a href="https://en.wikipedia.org/wiki/Proxy_server" target="_blank">proxy server</a> to strip CSS and shrink images. Or use a text-based browser like <a href="http://lynx.browser.org/" target="_blank">Lynx</a>. <a href="https://www.brow.sh/" target="_blank">Browsh</a> also looks interesting. Lots of avenues for future investigation!

<br />

<a name="Shooting and Sharing VR Photos">
## Shooting and Sharing VR Photos

Status | Completed November 2016
Goal | Learn how to shoot, interactively view and share VR photos

Ever seen one of <a href="https://flickr.com/photos/136386099@N02/21597873406/" target="_blank">these photos</a> where you can interactively zoom and pan around? They're known as <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">360° or VR photos</a>.

More formally, <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">VR photography</a> (Virtual Reality photography) is the art of capturing or creating a complete scene as a single image, as viewed when rotating about a single central position

I want to learn now how to shoot, interactively view and share my own VR photos. Here's what I found:

* <a href="https://wiki.panotools.org/Equirectangular_Projection" target="_blank">Equirectangular Projection</a> is the most common VR image format. Another popular option is <a href="https://wiki.panotools.org/Cubic_Projection" target="_blank">Cubic Projection</a> and you can easily [convert between the two]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %}) 
* The Google Street View mobile app (<a href="https://apps.apple.com/us/app/google-street-view/id904418768" target="_blank">iOS</a>, <a href="https://play.google.com/store/apps/details?id=com.google.android.street&hl=en_US" target="_blank">Android</a>) is a cheap and easy way to shoot Equirectangular projections
* Since Equirectangular images are <a href="http://www.jamesfmackenzie.com/img/posts/cube-faces-guide.png" target="_blank">heavily distorted</a>, you need a <a href="https://wiki.panotools.org/Panorama_Viewers" target="_blank">"viewer"</a> program to interact with them
* Windows has built-in support via the [.pano]({% post_url 2016-10-29-what-are-pano-files %}) file extension. It's relatively easy to [create your own]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %})
* Web viewers are also popular. Here's how to publish VR photos to [Photosyth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %}), [Facebook]({% post_url 2016-10-12-publishing-equirectangular-360-vr-panorama-to-facebook %}) and [YouTube]({% post_url  2019-09-08-publishing-360-photos-to-youtube %})

Posts:
- [Publishing VR Panoramas to YouTube]({% post_url 2019-09-08-publishing-360-photos-to-youtube %}) - 08 Sep 2019
- <a href="https://medium.com/vantage/all-you-need-to-know-about-360-vr-photos-d180aa25d8de" target="_blank">All You Need to Know about 360 VR Photos</a>  - 02 Nov 2016
- [Convert Equirectangular Projection to .Pano File]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %}) - 30 Oct 2016
- [What are .pano files?]({% post_url 2016-10-29-what-are-pano-files %}) - 29 Oct 2016
- [Publishing VR Panoramas to Photosynth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %}) - 28 Oct 2016
- [Convert Equirectangular Projection to Cube Faces]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %}) - 18 Oct 2016
- [Installing Hugin and Panotools on Windows]({% post_url 2016-10-17-installing-hugin-and-panotools-on-windows %}) - 17 Oct 2016
- [Publishing VR Panoramas to Facebook]({% post_url 2016-10-12-publishing-equirectangular-360-vr-panorama-to-facebook %}) - 12 Oct 2016

<br />

<a name="Transferring Files Between PC and ST">
## Transferring Files Between PC and ST

Status | Completed March 2016
Goal | Explore the various ways to share files between PC and Atari ST

Can my Atari ST interoperate with modern PCs? What are the best ways to send files back and forth?

I explored several ways to transfer files between PC and Atari ST, including:

- [Using an SD card and Ultrasatan to Transfer Files from PC to ST]({% post_url 2016-03-08-use-ultrasatan-sd-card-to-transfer-files-from-pc-to-st %}) - 08 Mar 2016
- [Using Ethernet to Transfer Files from PC to ST]({% post_url 2016-03-08-use-ethernet-to-transfer-files-from-pc-to-st %}) - 07 Mar 2016
- [Using PARCP-USB to Transfer Files from PC to ST]({% post_url 2016-02-24-use-parcp-usb-to-transfer-files-from-pc-to-atari-st %}) - 24 Feb 2016
- [Using Serial Cable and ZMODEM to Transfer Files from PC to ST]({% post_url 2016-02-13-use-rs232-serial-cable-and-zmodem-to-transfer-files-from-pc-to-st %}) - 13 Feb 2016
- [Using Serial Cable and Ghostlink to Transfer Files from PC to ST]({% post_url 2016-02-06-use-rs232-serial-cable-and-ghostlink-to-transfer-files-from-pc-to-st %}) - 06 Feb 2016
- [Using Floppy Disk to Transfer Files from PC to ST]({% post_url 2016-01-30-use-floppy-disk-to-transfer-files-from-pc-to-st %}) - 30 Jan 2016

I also took a detour into file compression, and learned how to split large files into chunks that can be individually copied using (for example) floppy disks:

- [How to Split and Copy Large Files to Your Atari ST in Chunks]({% post_url 2016-01-31-using-arj-to-split-and-copy-large-files-to-your-atari-st-in-chunks %}) - 31 Jan 2016

<br />

<a name="Playing Downloaded Games on Real ST Hardware">
## Playing Downloaded Games on Real ST Hardware

Status | Completed September 2015
Goal | Download an Atari ST game image from the web and play it on my real ST

My old ST disks are dead! Can I download replacement disk images from the web and play on my physical ST?

I explored several options, including floppy disk images and hard disk adaptations:

- [Use Your PC to Create a Bootable Atari ST Game Disk]({% post_url 2015-09-22-use-your-pc-to-create-a-bootable-atari-st-game-disk %}) - 22 Sep 2015
- [Playing Downloaded Games on a Real Atari ST]({% post_url 2015-09-18-playing-downloaded-games-on-a-real-atari-st %}) - 18 Sep 2015

<br />

<a name="Watch Mobile Content on the Go">
## Watch Mobile Content on the Go

Status | Completed December 2014
Goal | Download video content to my mobile device so I can watch it on the go

<strong>Update Dec 2019:</strong> <em>YouTube has emerged as the dominant platform for Web video. In future, it makes sense to look at the YouTube API. Can I automatically download every video tagged to the "Watch Later" playlist for offline consumption?</em>

The work commute is a great time to catch up on news, vlogs and other Web videos. But cellphone signal is way too patchy for reliable streaming - especially in the subway.

I explored use of the Pocket API and PlexSync to download and push web videos to my phone:

- [Sync Web Videos to Your Tablet or Phone, Watch Them Offline]({% post_url 2015-02-01-sync-pocket-videos-to-your-phone-watch-them-offline %}) - 01 Feb 2015
- [Download Pocket Videos to Your PC]({% post_url 2015-01-03-download-pocket-videos-to-your-pc %}) - 03 Jan 2015
- [I Can't Stream Video on the Commute. How Can I Fix It?]({% post_url 2014-12-17-i-cant-stream-video-on-the-commute-how-can-i-fix-it %}) - 17 Dec 2014

<br />

<a name="Ghost Blogging">
## Ghost Blogging

Status | Completed June 2014
Goal | Learn how to use the Ghost blogging platform

<strong>Update Jun 2018:</strong> <em>I now use <a href="https://jekyllrb.com/" target="_blank">Jekyll</a> and <a href="https://pages.github.com/" target="_blank">GitHub Pages</a> as my blogging platform.</em>

I'm interested in <a href="https://ghost.org/" target="_blank">Ghost</a> as a crisp, clean, lightweight blogging platform. I took some time to learn about the platform, setup my own developmemt environment and even write my own theme. Findings below.

Posts:
- [Things I Wish I'd Known Before Creating My Own Ghost Theme]({% post_url 2014-06-23-things-i-wish-id-known-before-creating-my-ghost-theme %}) - 23 Jun 2014
- [It's Done! 8-Bit Memories Ghost Theme]({% post_url 2014-06-21-its-done-8-bit-memories-ghost-theme %}) - 21 Jun 2014
- [Create Your Own Ghost Theme in 5 Minutes]({% post_url 2014-06-10-create-your-own-ghost-theme-in-5-minutes %}) - 10 Jun 2014
- [Setting Up a Ghost Dev Environment]({% post_url 2014-05-17-setting-up-a-ghost-dev-environment %}) - 17 May 2014
- [Getting to Grips With Ghost Themes]({% post_url 2014-04-24-getting-to-grips-with-ghost-themes %}) - 24 Apr 2014
