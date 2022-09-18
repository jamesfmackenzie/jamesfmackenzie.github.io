---
layout: post
title: "PI-MIDI Review – Supercharge your mt32-pi"
date: '2022-06-04 16:41:00:00'
summary: PI-MIDI is fantastic companion for mt32-pi and a great way to boost for your DOS MIDI setup ...
image: pi-midi-connected.jpg
tags: [DOS, MIDI, Posts, Retrocomputing, Retrogaming]
---

The PI-MIDI is a MIDI hat for Raspberry Pi, granting your Pi extended MIDI capabilities like GPIO MIDI input, Stereo RCA output and a dedicated user port connection for MiSTer FPGA.

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/vnVbw3OV3N4?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 


### Hardware Overview

![](/img/posts/pi-midi-mt32-connectivity.jpg)

The PI-MIDI attaches to the Raspberry Pi's GPIO pins and allows you to connect MIDI input devices, for sending MIDI data to the Pi.

Once you’ve got MIDI messages flowing to the Pi, you can do a lot with it. For example, run a software synthesizer like <a href="https://sourceforge.net/projects/munt/" target="_blank">Munt</a> or <a href="https://www.fluidsynth.org/" target="_blank">FluidSynth</a> to generate high quality digital audio.

In terms of connectivity we have:

* MIDI DIN – input connector; to connect MIDI devices
* RCA audio out – two jacks for stereo audio output. The PI-MIDI provides much improved audio quality vs native Pi output
* 2.5mm stereo jack – for audio input. Can be mixed with synthesized MIDI audio for combined output
* User port – looks like a USB port, but is actually an IO port specifically for MIDI connection to [MiSTer FPGA]({% post_url 2020-08-22-mister-fpga-introduction-and-hardware-overview %})

For physical controls, we have a rotary dial, jog wheel and two push buttons. Useful for changing e.g. volume, synth selection or other MIDI options without the need for a keyboard or additional input device.

Lastly we have a 1.3” OLED screen to display selection options and visualise playback levels/equalisers.


### Enter mt32-pi

![](/img/posts/mt32-pi-logo.jpg)

<a href="https://github.com/dwhinham/mt32-pi" target="_blank">mt32-pi</a> is a baremetal kernel that turns your Raspberry Pi 3 or later into a <a href="https://en.wikipedia.org/wiki/Roland_MT-32" target="_blank">Roland MT-32</a> emulator and <a href="https://en.wikipedia.org/wiki/SoundFont" target="_blank">SoundFont</a> synthesizer. Behind the scenes it uses Circle (a C++ baremetal environment for Pi) and Munt/FluidSynth for MIDI synthesis.

It natively supports GPIO MIDI interfaces like the PI-MIDI, together a perfect match to create a DIY MIDI synthesiser with similar sound and features to classic synths like the Roland MT-32 or SC-88. A great combo for DOS gaming!


### MIDI Connectivity

![](/img/posts/pi-midi-connected.jpg)

To setup PI-MIDI for DOS gaming:

1. Connect DOS PC MIDI output to the MIDI input DIN (you’ll need a gameport MIDI cable)

2. Connect DOS PC audio output to the 2.5mm stereo input jack. Sound Blaster sound effects from your PC will be automatically mixed with MIDI audio generated on the Pi to create a combined audio track

3. Connect RCA output audio to your speakers
 
4. Configure your DOS games to use Roland MT-32, Roland Sound Canvas or General MIDI audio on Port 330

With setup out the way, we’re ready to explore some features!


### Feature Exploration 

Powering on the Pi and PI-MIDI, you’ll see the mt32-pi logo. As mentioned above, this software will receive MIDI messages and route them to the configured software synth (either Munt or FluidSynth) to generate digital audio. 

The rotary dial adjusts volume, and the push buttons toggle between MT-32 operating mode and SoundFont mode.

MT-32 mode is the primary feature of mt32-pi. It will use Munt soft synth to playback Roland MT-32 compatible MIDI. Many early DOS games support MT-32 MIDI and the sound quality is great.

In SoundFont mode, the Pi will use FluidSynth to synthesise SoundFont-compatible General MIDI into digital audio.  This is useful for later DOS games with General MIDI or native Sound Canvas support.


### MiSTer User Port

The [MiSTer FPGA platform]({% post_url 2020-08-22-mister-fpga-introduction-and-hardware-overview %}) is an open-source project that can emulate retro computing and gaming systems. The FPGA approach has the potential for greater accuracy and lower latency vs traditional software-based emulation, and many console and computer cores are available.

Some of those cores (PC, Atari ST, Amiga, X68000) are able to use external MIDI hardware, and the mt32-pi and MiSTer projects have collaborated to create a direct cabling solution. Here's how it works:

* The <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki/IO-Board" target="_blank">MiSTer IO board</a> provides "User port" with direct access to the FGPA's GPIO pins
* The PI-MIDI also has a physical User port, and the two can be connected via a USB A-to-A cable

This single cable will both power the Pi/PI-MIDI *and* receive MIDI data. Super convenient!


### Conclusion

If you can’t get your hands on a real Roland MT-32 or Sound Canvas synth, I’d strongly recommend a Pi + PI-MIDI as a great DIY option. It’s plug-and-play, simple to use, and (at least to my ear) produces very authentic sound. Look forward to trying it with more DOS games!


### Useful Links

* <a href="https://github.com/dwhinham/mt32-pi/wiki" target="_blank">mt32-pi Wiki</a>


