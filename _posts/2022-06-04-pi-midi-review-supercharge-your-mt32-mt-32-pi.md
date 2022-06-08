---
layout: post
title: "PI-MIDI Review – Supercharge your mt32-pi"
date: '2022-06-04 16:41:00:00'
summary: PI-MIDI is fantastic companion for mt32-pi and a great way to boost for your DOS MIDI setup ...
tags: [DOS, MIDI, Retrocomputing, Retrogaming]
---

The PI-MIDI is a MIDI hat for Raspberry Pi, granting your Pi extended MIDI capabilities like GPIO MIDI input, Stereo RCA output and a dedicated user port connection for MiSTer FPGA.

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/vnVbw3OV3N4?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 


### Hardware Overview

The PI-MIDI attaches to the Raspberry Pi's GPIO pins and allows you to connect MIDI input devices, for sending MIDI data to the Pi.

Once you’ve got MIDI messages flowing to the Pi, you can do a lot with it. For example, run a software synthesizer like Munt or Fluidsynth to generate high quality digital audio.

In terms of connectivity we have:

* MIDI DIN – input connector; to connect MIDI devices
* RCA audio out – two jacks for stereo audio output. The PI-MIDI provides much improved audio quality vs native Pi output
* 2.5mm stereo jack – for audio input. Can be mixed with synthesized MIDI audio for combined output
* User port – looks like a USB port, but  is actually an IO port specifically for MIDI connection to the MiSTer FPGA

For physical controls, we have a rotary dial, jog wheel and two push buttons. Useful for changing e.g. volume, synth selection or other MIDI options without the need for a keyboard or additional input device.

Lastly we have a 1.3” OLED screen to display selection options and visualise  playback levels/equalisers.


### Enter mt32-pi

mt32-pi is a baremetal kernel that turns your Raspberry Pi 3 or later into a Roland MT-32 emulator and SoundFont synthesizer. Behind the scenes it uses Circle (A C++ baremetal environment for Pi) and Munt/FluidSynth for MIDI synthesis.

It natively supports GPIO MIDI interfaces like the PI-MIDI, a perfect match to create a DIY MIDI synthesiser with similar sound and features to classic synths like this Roland MT-32 or SC-88.


### MIDI Connectivity

![](/img/posts/windows-11-pc-health-check-app-tool.png)

The typical PI-MIDI setup is to:

1. Connect DOS PC MIDI output to the MIDI input DIN (you’ll need a gameport MIDI cable)

2. Connect DOS PC audio output to the 2.5mm stereo input jack. Sound Blaster sound effects from your PC will be automatically mixed with MIDI audio generate on the Pi to create combined audio

3. Connect RCA output audio to your speakers
 
4. Configure your DOS games to use Roland MT-32, Roland Sound Canvas or General MIDI audio on Port 330

With setup out the way, we’re ready to explore some features!


### Feature Exploration 

powering up, we see the mt-32 pi logo. This is the midi synthesizer software that we've got installed on the raspberry pi. this is what we're going to use to play back the midi data that's pumped in through the midi port 

okay let's try out some of the features:

first i'm going to go for this button on the left. i'll click that and you can see that instructs the mt-32
to switch between MT-32 and sound font mode. 

Sound font mode:

in this mode it can play back!sound font compatible general midi!using the fluid synth software so this is useful for some of the newer dos games that use general midi or maybe even have dedicated sound canvas support

mt-32 mode:

this is the primary feature of the mt-32 pi. this will playback roland mt-32 compatible midi and it's really good. i've tried it on a few games and the sound quality is very good

we can use the rotary dial to adjust the volume up and down


### Conclusion

i love this little thing look forward to trying it out with some more games i'll do a full showcase

insert showcase link


### Useful Links

* <a href="https://github.com/dwhinham/mt32-pi/wiki" target="_blank">mt32-pi Wiki</a>


