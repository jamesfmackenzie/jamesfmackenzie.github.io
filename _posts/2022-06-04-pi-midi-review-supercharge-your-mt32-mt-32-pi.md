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

The PI-MIDI attaches to the Raspberry Pi's GPIO pins and allows you to connect MIDI input devices, for sending MIDI data to the Pi. In terms of connectivity we have:

* MIDI DIN – input connector. Connect MIDI devices
* RCA audio out – two jacks for stereo audio output. The PI-MIDI provides much improved audio quality vs native Pi audio
* 2.5mm stereo jack – for audio input. This will be mixed with MIDI audio to create combined output
* User port – looks like a USB port, but this is actually an IO port specifically for connection to the MiSTer FPGA

For controls and buttons you've got a couple of wheels and buttons so you've got some buttons to change various features. you've got a rotary dial on top here this is for volume and you've got another jog wheel here

Lastly we've got a display do you can view equalizers and you can view some selection options as you're using it


### MIDI Connectivity

![](/img/posts/windows-11-pc-health-check-app-tool.png)

let's get this hooked up and try it out

okay so we're connected we've got a dos gaming pc hooked up by the midi Input

we've got our audio output running off to our audio capture. we're not using the audio input here, this is useful if you want to mix in say the sound coming out of your your gaming pc (I.e. the sound blaster sound) then you can get midi and your regular sound mixed together 


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


