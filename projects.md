---
layout: nocomments
title: Projects
---

Project summaries for completed and in-progress projects below. Enjoy!

<br />


## Projects

<!--

Projects to add:

* Building the ultimate Windows 98 machine
* Dedicated Wi-Fi network for Oculus Quest 2
* Face and Body tracking

-->

* <a href="#Framerate Analysis Tooling">Framerate Analysis Tooling</a> - Apr 2022
* <a href="#HP Thin Client DOS Gaming PC">HP Thin Client DOS Gaming PC</a> - Feb 2021 
* <a href="#DOS Gaming on MiSTer FPGA">DOS Gaming on MiSTer FPGA</a> - Feb 2021 
* <a href="#Remote Play Xbox Series S/X Games on PC">Remote Play Xbox Series S/X Games on PC</a> - Jan 2021 
* <a href="#Lenovo Tiny Series Emulation Station">Lenovo Tiny Series Emulation Station</a> - May 2020 
* <a href="#Porting Commander Keen to PlayStation Vita">Porting Commander Keen to PlayStation Vita</a> - In Progress
* <a href="#Porting Commander Keen to WebAssembly">Porting Commander Keen to WebAssembly</a> - Nov 2019
* <a href="#Learning about Webassembly">Learning About Webassembly</a> - Nov 2019
* <a href="#Raspberry Pi Retrogaming">Raspberry Pi Retrogaming</a> - Oct 2018
* <a href="#Atari ST on the Web">Atari ST on the Web</a> - Jun 2018
* <a href="#Shooting and Sharing VR Photos">Shooting and Sharing VR Photos</a> - Nov 2016
* <a href="#Transferring Files Between PC and ST">Transferring Files Between PC and ST</a> - Mar 2016
* <a href="#Playing Downloaded Games on Real ST Hardware">Playing Downloaded Games on Real ST Hardware</a> - Sep 2015
* <a href="#Watch Mobile Content on the Go">Watch Mobile Content on the Go</a> - Dec 2014
* <a href="#Ghost Blogging">Ghost Blogging</a> - Jun 2014

<br />


<a name="Framerate Analysis Tooling">
## Framerate Analysis Tooling

Status | In-Progress
Goal | Build my own "Digital Foundry" style tooling to analyze videogame performance

Inspired by <a href="https://www.youtube.com/user/DigitalFoundry" target="_blank">Digital Foundry</a>, <a href="https://www.youtube.com/c/VGTech" target="_blank">VG Tech</a> and <a href="https://www.youtube.com/c/NXGamer" target="_blank">NX Gamer</a>, I wanted to deep-dive on videogame technical analysis. I set myself the following goals:

1. **Write my own performance analysis tooling**. Look at captured videogame footage and analyze framerate, torn frames, resolution etc
2. **Run some real performance comparisons** (e.g. Xbox Series X vs PS5 performance)
3. **Technical learning!** Build some proficiency in videogame technical analysis and machine vision

After some background research, I selected <a href="https://opencv.org/" target="_blank">OpenCV</a> as the foundational project library. As a specialised framework for computer vision and image analysis, it's a great project fit.

First, I worked on <a href="https://twitter.com/jamesfmackenzie/status/1516036998947028992" target="_blank">difference detection between video frames</a>. If two frames show zero difference, that means we have a duplicate frame (i.e. a frame drop vs the target frame rate).

With diff detection in place, I was able to <a href="https://twitter.com/jamesfmackenzie/status/1515344348313002000" target="_blank">do some rudimentary framerate analysis on The Legend of Zelda: Breath of the Wild</a> and (after some more iteration) <a href="https://twitter.com/jamesfmackenzie/status/1519647506254254080" target="_blank">add performance monitoring and graphing</a>.

Next, I investigated detection of torn frames. This is when the renderer doesn't have enough time to complete an entire frame, so a partial frame is rendered to the screen instead (with the remaining row gaps filled in with data from the last frame). I <a href="https://twitter.com/jamesfmackenzie/status/1520448444074188800" target="_blank">enhanced diff detection</a> and was able to <a href="https://twitter.com/jamesfmackenzie/status/1520807871549779970" target="_blank">reliably detect torn frames in Gran Turismo 5</a> (a game known for significant image tearing).

My next focus was resolution counting. Videogames often dynamically reduce rendering solution to keep frames "within budget" (i.e. rendered fast enough to hit the desired 30fps or 60fps target). This is known as Dynamic Resolution Scaling (DRS). The frame is then upscaled back to the target resolution (e.g. 1080p or 4K). It's an effective approach, but reduces image quality vs "native resolution" rendering. Artifacts (such as jagged edges) appear in the image, and it's possible to exploit these to identify the original render resolution of the frame.  

As a first pass, I was able to <a href="https://twitter.com/jamesfmackenzie/status/1531623625702400000" target="_blank">find all edges in each frame</a>. I was then able <a href="https://twitter.com/jamesfmackenzie/status/1532721445222158336" target="_blank">find "countable edges"</a> - straight line edges that can be <a href="https://www.youtube.com/watch?v=3ra-P3gH7Dg" target="_blank">pixel counted</a> to identify the original render resolution of the frame.

Unfortunately the automation didn't work. Despite hours or tuning, the edge detection algorithm wasn't able to distinguish between polygon edges (which are suitable for counting) and straight line edges found within filtered textures (which aren't). The counts are unreliable, **so I've parked this for now**.

Next, I looked at framerate counting for *compressed* video. Video compression is typically lossy <a href="https://en.wikipedia.org/wiki/Compression_artifact" target="_blank">and introduces image artifacts e.g. pixelation, macroblocking etc</a>. These artifacts make it very challenging to detect duplicate frames. 100% identical frames rendered by the game engine will appear different in compressed video.

In short, compressed video broke my diff detection. Every single frame is perceived as unique - no frame drops detected. To address this, I needed to adopt a more statistical approach. Instead of looking for *zero* difference between frames, I looked at *difference trend*:

* Hypothesis: because video frames from a 3D engine are temporally connected, we would *usually* expect frame difference trend to be relatively consistent between frames. Significant trend divergence is aberration - and might indicates a frame drop

To test the hypothesis, I created a time series of frame-to-frame difference (Euclidean difference) for compressed video with known frame drops:

<img src="https://pbs.twimg.com/media/FVdxbEFXsAEgcJn?format=png" />

See those downspikes in the graph above? Those are the frame drops. And they're easy to identify. This is great news!

A few updates later, I was able to <a href="https://youtu.be/aQsxzAXpaHk" target="_blank">complete framerate analysis for the Starfield Official Gameplay Reveal</a>.

Finally, I looked at high quality video export from OpenCV. Unfortunately the built-in OpenCV VideoWriter is not super configurable - and video output is relatively low bitrate and blocky. Instead I chose to output results as PNG and then re-assemble into video using <a href="https://ffmpeg.org/" target="_blank">ffmpeg</a>.

Challenges overcome:

- Sampling framerate from captured gameplay video
- Identifying duplicate frames and torn frames
- Graphics and performance graphing in OpenCV
- How to accommodate compression noise in captured video
- High quality video export from OpenCV

Upcoming goals:

- Side-by-side comparison of 2 (or 3) videos
- Resolution counting revisited

You can also find the journey chronicled on Twitter <a href="https://twitter.com/jamesfmackenzie/status/1515054433889144834" target="_blank">here</a>.

<br />


<a name="HP Thin Client DOS Gaming PC">
## HP Thin Client DOS Gaming PC

Status | Completed July 2021
Goal | Build a small and light gaming PC for DOS and Windows 98 gaming

After <a href="#DOS Gaming on MiSTer FPGA">DOS gaming on MiSTer</a>, I was left wanting for more. The MiSTer felt underpowered, I wanted something a little faster to play Half-Life, Unreal and other Windows 98 classics.

In search of a retro PC (but short on apartment space), [I purchased a HP Compaq t5710 thin client]({% post_url 2021-07-11-hp-compaq-t5710-review-great-for-dos-and-windows-98-gaming %}).

Despite the 2004 build, the hardware is very well suited to DOS and Windows 98 gaming. Sound Blaster and Ad-Lib audio works even in DOS mode, making this a great all-in-one unit.

After some trial and error, I was able to <a href="https://youtu.be/V4DIPffO-sI" target="_blank">succesfully install and game on Windows 98</a>. I was [also able to find a working PS/2 splitter]({% post_url 2021-11-13-using-monoprice-ps2-splitter-with-hp-compaq-t5710-review %}).

Next, I experimented with the PCI expansion slot. After some success with PCI sound hardware, I installed a <a href="https://en.wikipedia.org/wiki/Voodoo2" target="_blank">3dfx Voodoo2</a>. It <a href="https://twitter.com/jamesfmackenzie/status/1492922391223283714" target="_blank">worked fantastically too!</a>

I'm super happy with this build. The t5710 is now my go to retro PC – I don't need anything more!

Posts:

- [HP Compaq t5710 Review – Great for DOS and Windows 98 Gaming?]({% post_url 2021-07-11-hp-compaq-t5710-review-great-for-dos-and-windows-98-gaming %}) - 11 Jul 2021
- [HP Compaq t5710 – How To Install Windows 98 from USB Flash Drive with Easy2Boot]({% post_url 2021-07-11-install-windows-98-from-usb-stick-flash-drive-with-easy2boot-hp-compaq-t5710 %}) - 11 Jul 2021
- [HP Compaq t5710 – Using a PS/2 Splitter Cable]({% post_url 2021-11-13-using-monoprice-ps2-splitter-with-hp-compaq-t5710-review %}) - 13 Nov 2021

<br />


<a name="DOS Gaming on MiSTer FPGA">
## DOS Gaming on MiSTer FPGA

Status | Completed March 2021
Goal | Play DOS and Windows 95 games on the MiSTer FPGA platform

Having recently acquired a <a href="https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046" target="_blank">Terasic DE10-Nano FGPA Development Kit</a>, I was very keen to install the [MiSTer software distribution]({% post_url  2020-08-22-mister-fpga-introduction-and-hardware-overview %}) and try some retro computing cores.

First on the list: the 80486 PC. I've many fond memories of DOS and Windows 95 gaming, messing with IRQ settings, tuning <code>config.sys</code> and <code>autoexec.bat</code> to get things working "just so". Luckily for me, DOS gaming is very well served on MiSTer via the <a href="https://github.com/MiSTer-devel/ao486_MiSTer" target="_blank">ao486 core</a>.

After a lot of tinkering, I was able to [setup file sharing]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}), [install a Memory Manager]({% post_url 2021-03-13-mister-ao486-core-part-3-managing-memory %}), [configure the Sound Blaster]({% post_url 2021-03-13-mister-ao486-core-part-4-sound-blaster-and-adlib-opl2-opl3-music %}), add [CD-ROM]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %}) and [Mouse]({% post_url 2021-03-13-mister-ao486-core-part-6-mouse-support %}) support, [configure Roland MIDI]({% post_url 2021-03-28-mister-ao486-core-part-8-midilink-midi-roland-mt-32-sound-canvas %}) and [install Windows 95]({% post_url 2021-03-28-mister-ao486-core-part-9-windows-95-install %}). A great result!

Posts:

- [MiSTer AO486 Core Part 1 – Getting Started]({% post_url 2021-02-06-mister-ao486-core-part-1-dos-quick-start %}) - 06 Feb 2021
- [MiSTer AO486 Core Part 2 – Sharing Files With MiSTerFS]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}) - 14 Feb 2021
- [MiSTer AO486 Core Part 3 – Managing Memory]({% post_url 2021-03-13-mister-ao486-core-part-3-managing-memory %}) - 13 Mar 2021
- [MiSTer AO486 Core Part 4 – Sound and Music Setup]({% post_url 2021-03-13-mister-ao486-core-part-4-sound-blaster-and-adlib-opl2-opl3-music %}) - 13 Mar 2021
- [MiSTer AO486 Core Part 5 – Adding CD-ROM Support]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %}) - 13 Mar 2021
- [MiSTer AO486 Core Part 6 – Mouse Support]({% post_url 2021-03-13-mister-ao486-core-part-6-mouse-support %}) - 13 Mar 2021
- [MiSTer AO486 Core Part 7 – Quick Start DOS Image]({% post_url 2021-03-18-mister-ao486-core-part-7-dos-quick-start-hard-disk-image %}) - 18 Mar 2021
- [MiSTer AO486 Core Part 8 – Roland MT-32, Sound Canvas Audio via MidiLink]({% post_url 2021-03-28-mister-ao486-core-part-8-midilink-midi-roland-mt-32-sound-canvas %}) - 28 Mar 2021
- [MiSTer AO486 Core Part 9 – Installing Windows 95]({% post_url 2021-03-28-mister-ao486-core-part-9-windows-95-install %}) - 28 Mar 2021

<br />


<a name="Remote Play Xbox Series S/X Games on PC">
## Remote Play Xbox Series S/X Games on PC

Status | Completed January 2021
Goal | Stream / Remote Play Xbox Series S/X games from my Windows PC

With the Xbox One, <a href="https://support.xbox.com/en-US/help/games-apps/apps-help/how-to-use-game-streaming-in-xbox-console-companion-app" target="_blank">I often used the Xbox Console Companion app to remote play games on PC</a>. Frustratingly, this feature was silently dropped for Xbox Series S/X – the Console Companion app just doesn’t work for the new consoles.

Looking for a solution, I was able to install a hidden “Xbox Game Streaming (Test App)” from the Windows 10 Store, and start streaming again. Full details [here]({% post_url 2021-01-24-remote-play-how-to-xbox-series-x-s-game-streaming-to-windows-10-pc %}). Case closed!

Posts:

- [How To Remote Play Xbox Series S/X Games On Your PC]({% post_url 2021-01-24-remote-play-how-to-xbox-series-x-s-game-streaming-to-windows-10-pc %}) - 24 Jan 2021

<br />


<a name="Lenovo Tiny Series Emulation Station">
## Lenovo Tiny Series Emulation Station

Status | Completed May 2020
Goal | Repurpose a Lenovo Tiny Series business desktop as a small and quiet retrogaming PC 

For many years I've been on quest to find the perfect emulation station. Something small and quiet, hidden under the TV, with a wireless controller and enough horsepower for high quality retrogaming.

Two years ago I [built and custom-configured a Raspberry Pi with RetroPie]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}). A great device, but not really powerful enough for 32-bit consoles like PlayStation or Saturn. I need something with a bit more grunt, reasonable price (~$100) and good Wife-Acceptance-Factor (no tower PC!)

After some investigation, I purchased a <a href="https://www.lenovo.com/us/en/desktops/thinkcentre/m-series-tiny/m93-m93p/" target="_blank">Lenovo ThinkCenter M93p Tiny Desktop</a> from eBay for ~$100.

The form factor looks great under a TV and emulation performance is also great. Even Dreamcast and Gamecube run well, a significant step up from the Raspberry Pi. Full write up [here]({% post_url 2020-05-31-the-lenova-m93p-is-a-great-small-form-factor-emulation-pc %}).

Posts:

- [Lenovo M93p Tiny Review – The Best Mini PC for Emulation?]({% post_url 2020-05-31-the-lenova-m93p-is-a-great-small-form-factor-emulation-pc %}) - 31 May 2020

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

- <a href="https://twitter.com/jamesfmackenzie/status/1186034903294644224?s=21" target="_blank">Porting Commander Keen / CloneKeen to the web browser with #Emscripten. Great progress so far!</a> - 20 Oct 2019
- [Commander Keen in a Web Browser?]({% post_url 2019-10-28-commander-keen-ported-to-webassembly %}) - 28 Oct 2019
- <a href="https://twitter.com/jamesfmackenzie/status/1190604121717592064?s=21" target="_blank">The Commander Keen WebAssembly port is done!</a> - 02 Nov 2019

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


<a name="Raspberry Pi Retrogaming">
## Raspberry Pi Retrogaming

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

Starting with a <a href="https://lotharek.pl/productdetail.php?id=46" target="_blank">NetUSBee</a> Ethernet adapter, <a href="http://hardware.atari.org/manuals/netsting.htm" target="_blank">I installed TOS drivers and the STinG TCP/IP stack</a>. I also used an <a href="http://www.atari-wiki.com/index.php/Graphics_cards" target="_blank">ET4000 graphics card</a> to push the resolution to a (somewhat) modern 1024x768 in 256 colours.

With those (and a successful TCP/IP ping) in place, <a href="https://breakintochat.com/blog/2017/09/05/web-browsing-on-the-atari-st-with-a-cosmosex/" target="_blank">I downloaded and configured Crystal Atari Browser (CAB)</a>.

The Web experience is slow and doesn't support CSS - which rules out a lot of content. However I was able to make <a href="https://twitter.com/jamesfmackenzie/status/1004495104885886978" target="_blank">older sites work</a>.

In search of a better experience: it might be possible to use a <a href="https://en.wikipedia.org/wiki/Proxy_server" target="_blank">proxy server</a> to strip CSS and shrink images. Or use a text-based browser like <a href="http://lynx.browser.org/" target="_blank">Lynx</a>. <a href="https://www.brow.sh/" target="_blank">Browsh</a> also looks interesting. Lots of avenues for future investigation!

<br />


<a name="Shooting and Sharing VR Photos">
## Shooting and Sharing VR Photos

Status | Completed November 2016
Goal | Learn how to shoot, interactively view and share VR photos

Ever seen one of <a href="https://flickr.com/photos/136386099@N02/21597873406/" target="_blank">these photos</a> where you can interactively zoom and pan around? They're known as <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">360° or VR photos</a>.

More formally, <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">VR photography</a> (Virtual Reality photography) is the art of capturing or creating a complete scene as a single image, as viewed when rotating about a single central position

I want to learn how to shoot, interactively view and share my own VR photos. Here's what I found:

* <a href="https://wiki.panotools.org/Equirectangular_Projection" target="_blank">Equirectangular Projection</a> is the most common VR image format. Another popular option is <a href="https://wiki.panotools.org/Cubic_Projection" target="_blank">Cubic Projection</a> and you can easily [convert between the two]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %}) 
* The Google Street View mobile app (<a href="https://apps.apple.com/us/app/google-street-view/id904418768" target="_blank">iOS</a>, <a href="https://play.google.com/store/apps/details?id=com.google.android.street&hl=en_US" target="_blank">Android</a>) is a cheap and easy way to shoot Equirectangular projections
* Since Equirectangular images are <a href="http://www.jamesfmackenzie.com/img/posts/cube-faces-guide.png" target="_blank">heavily distorted</a>, you need a <a href="https://wiki.panotools.org/Panorama_Viewers" target="_blank">"viewer"</a> program to interact with them
* Windows has built-in support via the [.pano]({% post_url 2016-10-29-what-are-pano-files %}) file extension. It's relatively easy to [create your own]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %})
* Web viewers are also popular. Here's how to publish VR photos to [Photosyth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %}), [Facebook]({% post_url 2016-10-12-publishing-equirectangular-360-vr-panorama-to-facebook %}) and [YouTube]({% post_url  2019-09-08-publishing-360-photos-to-youtube %})

Posts:

- [Publishing VR Panoramas to Facebook]({% post_url 2016-10-12-publishing-equirectangular-360-vr-panorama-to-facebook %}) - 12 Oct 2016
- [Installing Hugin and Panotools on Windows]({% post_url 2016-10-17-installing-hugin-and-panotools-on-windows %}) - 17 Oct 2016
- [Convert Equirectangular Projection to Cube Faces]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %}) - 18 Oct 2016
- [Publishing VR Panoramas to Photosynth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %}) - 28 Oct 2016
- [What are .pano files?]({% post_url 2016-10-29-what-are-pano-files %}) - 29 Oct 2016
- [Convert Equirectangular Projection to .Pano File]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %}) - 30 Oct 2016
- [All You Need to Know about 360 VR Photos]({% post_url 2016-11-02-shooting-storing-and-sharing-vr-panormas %}) - 02 Nov 2016
- [Publishing VR Panoramas to YouTube]({% post_url 2019-09-08-publishing-360-photos-to-youtube %}) - 08 Sep 2019

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

- [Playing Downloaded Games on a Real Atari ST]({% post_url 2015-09-18-playing-downloaded-games-on-a-real-atari-st %}) - 18 Sep 2015
- [Use Your PC to Create a Bootable Atari ST Game Disk]({% post_url 2015-09-22-use-your-pc-to-create-a-bootable-atari-st-game-disk %}) - 22 Sep 2015

<br />


<a name="Watch Mobile Content on the Go">
## Watch Mobile Content on the Go

Status | Completed December 2014
Goal | Download video content to my mobile device so I can watch it on the go

<strong>Update Dec 2019:</strong> <em>YouTube has emerged as the dominant platform for Web video. In future, it makes sense to look at the YouTube API. Can I automatically download every video tagged to the "Watch Later" playlist for offline consumption?</em>

The work commute is a great time to catch up on news, vlogs and other Web videos. But cellphone signal is way too patchy for reliable streaming - especially in the subway.

I explored use of the Pocket API and PlexSync to download and push web videos to my phone:

- [I Can't Stream Video on the Commute. How Can I Fix It?]({% post_url 2014-12-17-i-cant-stream-video-on-the-commute-how-can-i-fix-it %}) - 17 Dec 2014
- [Download Pocket Videos to Your PC]({% post_url 2015-01-03-download-pocket-videos-to-your-pc %}) - 03 Jan 2015
- [Sync Web Videos to Your Tablet or Phone, Watch Them Offline]({% post_url 2015-02-01-sync-pocket-videos-to-your-phone-watch-them-offline %}) - 01 Feb 2015

<br />


<a name="Ghost Blogging">
## Ghost Blogging

Status | Completed June 2014
Goal | Learn how to use the Ghost blogging platform

<strong>Update Jun 2018:</strong> <em>I now use <a href="https://jekyllrb.com/" target="_blank">Jekyll</a> and <a href="https://pages.github.com/" target="_blank">GitHub Pages</a> as my blogging platform.</em>

I'm interested in <a href="https://ghost.org/" target="_blank">Ghost</a> as a crisp, clean, lightweight blogging platform. I took some time to learn about the platform, setup my own developmemt environment and even write my own theme. Findings below.

Posts:

- [Getting to Grips With Ghost Themes]({% post_url 2014-04-24-getting-to-grips-with-ghost-themes %}) - 24 Apr 2014
- [Setting Up a Ghost Dev Environment]({% post_url 2014-05-17-setting-up-a-ghost-dev-environment %}) - 17 May 2014
- [Create Your Own Ghost Theme in 5 Minutes]({% post_url 2014-06-10-create-your-own-ghost-theme-in-5-minutes %}) - 10 Jun 2014
- [It's Done! 8-Bit Memories Ghost Theme]({% post_url 2014-06-21-its-done-8-bit-memories-ghost-theme %}) - 21 Jun 2014
- [Things I Wish I'd Known Before Creating My Own Ghost Theme]({% post_url 2014-06-23-things-i-wish-id-known-before-creating-my-ghost-theme %}) - 23 Jun 2014
