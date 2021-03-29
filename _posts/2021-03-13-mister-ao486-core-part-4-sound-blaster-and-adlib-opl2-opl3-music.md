---
layout: post
title: "MiSTer AO486 Core Part 4 – Sound and Music Setup"
date: '2021-03-13 17:32:00:00'
summary: Configuring the sound and music capabilities of the MiSTer ao486 core ...
tags: [Retrocomputing, Retrogaming, FPGA, MiSTer, Single-Board Computing]
---

The MiSTer ao486 core is feature-packed when it comes to sound and music.

For sound, it has built-in <a href="https://en.wikipedia.org/wiki/Sound_Blaster">Sound Blaster</a> Pro and Sound Blaster 16 capability – the industry-standard for DOS gaming. On the music side, you have a choice of <a href="https://en.wikipedia.org/wiki/Yamaha_YM3812" target="_blank">OPL2</a>, <a href="https://en.wikipedia.org/wiki/Yamaha_YMF262" target="_blank">OPL3</a> and <a href="https://en.wikipedia.org/wiki/Sound_Blaster#Creative_Music_System" target="_blank">CM/S</a> synth.


### Sound Blaster Settings

The default settings are:

Port/Address | 220
IRQ | 5
DMA (Low/8-bit) | 1
DMA (High/16-bit) | 5

Many games can auto-detect these settings, but others read resource information from the <a href="https://retronn.de/imports/soundblaster_config_guide.html" target="_blank">BLASTER environment variable</a>. To get this configured:

1. From the DOS command prompt, type <code>edit C:\AUTOEXEC.BAT</code>. An editor application will open. Add the following line to your <code>AUTOEXEC.BAT</code>:

````
SET BLASTER=A220 I5 D1 H5 T6
````

{:start="2"}
2. Hit <i>Alt+F,S</i> to save the file, then <i>Alt+F,X</i> to exit


### Music and Synth

ao486 supports the following synths:

* <a href="https://en.wikipedia.org/wiki/Yamaha_YM3812" target="_blank">OPL2</a>/<a href="https://en.wikipedia.org/wiki/Yamaha_YMF262" target="_blank">OPL3</a> (aka <a href="https://en.wikipedia.org/wiki/Ad_Lib,_Inc." target="_blank">AdLib audio</a>)
* <a href="https://en.wikipedia.org/wiki/Sound_Blaster#Creative_Music_System" target="_blank">Creative Music System</a> (aka CM/S)

AdLib was the de facto synth standard in the DOS-gaming era. By comparison very few games support CM/S audio – you can leave it disabled.

Settings are configured in the MiSTer *Audio & Video* menu, which you can access by hitting *Windows Key* + *F12*, then selecting *Audio & Video*:

![](/img/posts/mister-ao486-audio-and-video-opl2-opl3-cms-synth.png)

For game setup:

* OPL2/3 *can* be accessed on the Sound Blaster ports (220-223 and 228-229 for OPL2 only), but it's recommended to use the AdLib ports 388-38B instead
* If CM/S audio is enabled, it *prevents* OPL2/3 access on ports 220-223. However 388-38B still work

That's it for sound setup.

Next:

* [MiSTer AO486 – Roland MT-32, Sound Canvas Audio via MidiLink]({% post_url 2021-03-28-mister-ao486-core-part-8-midilink-midi-roland-mt-32-sound-canvas %})
* [MiSTer AO486 Core Part 5 – Adding CD-ROM Support]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %})
* [MiSTer AO486 Core Part 6 – Mouse Support]({% post_url 2021-03-13-mister-ao486-core-part-6-mouse-support %})


### Other Posts in this Series

{% include mister-fpga-series.md %}

