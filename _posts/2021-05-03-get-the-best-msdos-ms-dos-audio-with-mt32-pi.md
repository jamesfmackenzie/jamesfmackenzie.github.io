---
layout: post
title: "Get the Best MS-DOS Audio With mt32-pi"
date: '2021-05-03 18:24:00:00'
summary: A huge upgrade vs AdLib audio, mt32-pi is a cheap way to upgrade the gaming audio on your MS-DOS PC ...
image: mt32-pi-setup.jpg
tags: [DOS, How To, MIDI, Posts, Retrocomputing, Retrogaming]
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/9TI6cYEtwLE?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

Although <a href="https://www.youtube.com/watch?v=U4R_--__fjE" target="_blank">AdLib audio</a> is the synth standard for DOS-gaming, many games include support for vastly superior <a href="https://www.youtube.com/watch?v=PMYKSwTa2cY" target="_blank">MIDI audio</a>.

In 2021, it's cheap and easy to add MIDI music to your DOS gaming PC. Here's how.


### What you need

We'll use a <a href="https://en.wikipedia.org/wiki/Raspberry_Pi" target="_blank">Rasberry Pi</a> and the <a href="https://github.com/dwhinham/mt32-pi">mt32-pi software synthesizer</a> to build a cheap MIDI applicance – which we'll hook up to our DOS gaming PC via the <a href="https://en.wikipedia.org/wiki/Serial_port" target="_blank">serial port</a>.

Hardware and software you need:

* <a href="https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/" target="_blank">Raspberry Pi 3</a>
* <a href="https://simple.wikipedia.org/wiki/MicroSD" target="_blank">microSD card</a>
* RS232 to TTL converter module (e.g. <a href="https://ebay.us/ro4O3C" target="_blank">this one</a>)
* <a href="http://bjt42.github.io/softmpu/" target="_blank">SoftMPU</a>
* <a href="https://github.com/gmcn42/mt32-pi-control" target="_blank">mt32-pi control</a> (optional)


### Step 1 – Install mt32-pi

Follow <a href="https://github.com/dwhinham/mt32-pi#-quick-start-guide" target="_blank">these quick steps</a> to install and configure mt32-pi on your Pi.


### Step 2 – Update port settings

Mount your microSD card to edit the <a href="https://github.com/dwhinham/mt32-pi/wiki/Configuration-file" target="_blank">mt32-pi configration file</a> (<code>mt32-pi.cfg</code>). Replace the following line:

````
gpio_baud_rate = 31250
```` 

With this:

````
gpio_baud_rate = 38400
```` 

<i>Our PC serial port can't run at the standard <a href="https://en.wikipedia.org/wiki/MIDI" target="_blank">
MIDI</a> baud rate of 31250bps. Instead we tell our mt32-pi to use 38400bps – the closest "PC standard" baud rate.</i>

Save <code>mt32-pi.cfg</code> and insert the microSD card back into your Pi once complete.


### Step 3 – Connect hardware

Wire the serial converter module to the GPIO pins on your Raspberry Pi:

<strong>Converter pin</strong> | <strong>Raspberry Pi GPIO pin</strong>
VCC	| 1 (3.3V)
GND	| 6 (GND) - or any other GND pin
RXD	| 10 (UART RXD)
TXD	| 8 (UART TXD)

<i>Find more detail on the mt32-pi wiki <a href="https://github.com/dwhinham/mt32-pi/wiki/MIDI-via-RS-232-or-USB-to-serial#real-rs-232-ports-vintage-computers" target="_blank">here</a>.</i>

Once you're fully-wired:

1. Connect the converter module to your DOS PC serial port
2. Connect speakers / headphones to the Pi audio jack
3. Power-on the Pi and PC


### Step 4 – Start SoftMPU

Copy <a href="http://bjt42.github.io/softmpu/" target="_blank">SoftMPU</a> to your DOS PC and run it with the following parameters:

````
SOFTMPU.EXE /MPU:330 /SB:<Your Sound Blaster Port> /IRQ:<Your Sound Blaster IRQ> /OUTPUT:COM1
````

For example:

````
SOFTMPU.EXE /MPU:330 /SB:220 /IRQ:7 /OUTPUT:COM1
````

SoftMPU will detect your PC serial port and create a "Soft" MIDI interface that your games use for MIDI playback:

![](/img/posts/mt32-pi-softmpu-serial-mode-rs232-mpu-401.png)


#### Step 5 – Switching Modes

mt32-pi has two synth modes:

1. MT-32 mode (for games that support <a href="https://en.wikipedia.org/wiki/Roland_MT-32" target="_blank">Roland MT-32</a> audio)
2. <a href="https://en.wikipedia.org/wiki/SoundFont" target="_blank">Soundfont</a> mode (for games that support <a href="https://en.wikipedia.org/wiki/General_MIDI" target="_blank">General MIDI</a> or <a href="https://en.wikipedia.org/wiki/Roland_Sound_Canvas" target="_blank">Roland Sound Canvas</a> audio)

MT-32 support was common in the early 90s, but was gradually superseded by General MIDI. With both together the mt32-pi supports a very wide range of games.

Which mode your Pi boots into is controlled via the <a href="https://github.com/dwhinham/mt32-pi/wiki/Configuration-file" target="_blank">mt32-pi configration file</a> (<code>mt32-pi.cfg</code>). Amend the following line:

````
default_synth = mt32 (for Roland MT-32)
````

````
default_synth = soundfont (for General MIDI / Roland Sound Canvas)
````

To change modes "on the fly", use <a href="https://github.com/gmcn42/mt32-pi-control" target="_blank">mt32-pi control</a>.


### Step 5 – Play games!

You're ready to play!

For beautiful music, configure your games to use Roland MT-32, Roland Sound Canvas or General MIDI audio on <i>Port 330</i>.


### Notes

* Games that use <a href="https://en.wikipedia.org/wiki/DOS_extender" target="_blank">DOS extenders</a> (e.g. <a href="https://en.wikipedia.org/wiki/DOS/4G" target="_blank">DOS/4GW</a>) *will not work* with this "Serial MIDI" approach. <a href="https://en.wikipedia.org/wiki/Doom_(1993_video_game)" target="_blank">Doom</a> is a notable example. This is a limitation of <a href="http://bjt42.github.io/softmpu/" target="_blank">SoftMPU</a>. 
* To increase compatibility you'll need a hardware <a href="https://en.wikipedia.org/wiki/MPU-401" target="_blank">MPU-401 interface</a>, usually provided by your PC Sound Card or dedicated hardware like <a href="http://pcmidi.eu/" target="_blank">PCMIDI</a>. You'll also need a MIDI interface for your Pi – learn more <a href="https://github.com/dwhinham/mt32-pi/wiki/MIDI-connectivity" target="_blank">here</a>.
* The Raspberry Pi audio jack is not designed for high quality. If you want better quality audio output, consider <a href="https://github.com/dwhinham/mt32-pi/wiki/I%C2%B2S-DACs" target="_blank">adding your own DAC</a>.


### More MIDI articles

{% include midi.md %}






