---
layout: post
title: "MiSTer AO486 Core Part 8 – Roland MT-32 and Sound Canvas Audio via MidiLink"
date: '2021-03-28 15:12:00:00'
summary: Using MiSTer MidiLink to enable Roland MT-32 and Sound Canvas audio in ao486 ...
tags: [Retrocomputing, Retrogaming, FPGA, MiSTer, Single-Board Computing]
---

<a href="https://en.wikipedia.org/wiki/Ad_Lib,_Inc." target="_blank">AdLib</a> is the de facto synth standard for DOS-gaming. Almost all games support AdLib music, and popular cards like the Sound Blaster include the same <a href="https://en.wikipedia.org/wiki/Yamaha_YM3812" target="_blank">Yamaha YM3812 (OPL2) chip</a> for AdLib-compatibility.

But true DOS gamers can do better. Games from the late 80s onwards often feature vastly superior <a href="https://en.wikipedia.org/wiki/MIDI" target="_blank">MIDI audio</a> – with strong support for the <a href="https://en.wikipedia.org/wiki/Roland_MT-32" target="_blank">Roland MT-32 synthesiser</a> and (for later games) the <a href="https://en.wikipedia.org/wiki/General_MIDI" target="_blank">General MIDI standard</a>. Give this a listen:

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/PMYKSwTa2cY?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

Sounds glorious, no? Especially when compared to the (rather drab) <a href="https://www.youtube.com/watch?v=U4R_--__fjE" target="_blank">AdLib audio version</a>.

Thanks to fantastic work in the MiSTer community, you can get this working on your own MiSTer. Here's how.


### Step 1 – Install MidiLink

On real PCs, the Sound Blaster and other audio cards often include a MIDI interface for connecting MIDI devices. MiSTer provides a connectivity solution too via "MidiLink" – a daemon that runs on the ARM CPU, interfacing with running FPGA cores to pipe MIDI traffic downstream for playback. To get MidiLink installed:

1. Power on your MiSTer and hit *F12* to open the System Settings menu
2. Run `Scripts → Yes → midilink_updater`. This will install the latest version of MidiLink, then reboot your MiSTer.
3. After reboot, hit *F12* once again to open the System Settings menu
4. This time, run `Scripts → Yes → soundfont_install`. This will download the <a href="https://en.wikipedia.org/wiki/SoundFont" target="_blank">SoundFonts</a> necessary for MIDI playback.

![](/img/posts/mister-ao486-midilink-updater.png)


### Step 2 – Enable MIDI Connection

With MidiLink installed, we're almost ready to play! But first we need to enable the MIDI connection:

1. Boot the MiSTer ao486 core (*F12* to bring up the MiSTer main menu, browse to *Computer -> ao486*)
2. Hit *Windows Key* + *F12* for ao486 core options. Hit the right arrow key for *System options*
3. Scroll to <code>UART mode</code>. Hit *Enter*
4. Set <code>Connection</code> to <code>MIDI</code>. Now we're ready for some MIDI playback!

![](/img/posts/mister-ao486-midilink-uart-mode-midi-connection.png)


### Step 3 – MidiLink Playback

Exploring the UART Mode menu, MidiLink has several playback options:

````
Connection: MIDI
│
├── MidiLink: Local
│   ├── Type: MUNT
│   └── Type: FSYNTH
│
├── MidiLink: USB
│
└── MidiLink: UDP
````

* *Local* uses real-time software synthesisers (MUNT and FluidSynth) to play MIDI audio directly on the MiSTer itself
* *USB* is for physically connecting a MIDI playback device via USB (the menu option is hidden otherwise)
* *UDP* sends MIDI data over the network to another software synthesiser

We'll explore each of these below.


### Roland MT-32 Playback via MUNT

Configure MidiLink as follows. Then hit *Save*:

![](/img/posts/mister-ao486-midilink-uart-mode-local-munt.png)

In this mode, MiSTer runs the <a href="https://sourceforge.net/projects/munt/" target="_blank">Munt</a> software synthesizer to emulate a real Roland MT-32. This is a super neat "ready to go" solution, with sound piped directly to your TV via the HDMI port. Give it a listen:

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/H9dU5CjoCDw?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

Unfortunately, MiSTer's onboard ARM CPU isn't *quite* powerful enough to run MUNT at full speed. You might hear some smooshed, delayed or off-pitch notes compared to <a href="https://youtu.be/PMYKSwTa2cY" target="_blank">authentic playback</a>. If this is an issue for you, don't worry – there are other options.


### General MIDI Playback via FluidSynth

Configure MidiLink as follows:

![](/img/posts/mister-ao486-midilink-uart-mode-local-fsynth-fluidsynth.png)

In this mode, MiSTer runs the <a href="https://www.fluidsynth.org/" target="_blank">FluidSynth</a> software synthesizer for <a href="https://en.wikipedia.org/wiki/General_MIDI" target="_blank">General MIDI</a> playback. By default, it uses <a href="https://en.wikipedia.org/wiki/Roland_SC-55" target="_blank">Roland SC-55</a> <a href="https://en.wikipedia.org/wiki/SoundFont" target="_blank">SoundFonts</a>, but anything that uses the SoundFont 2 specification will work. FluidSynth is much easier on the CPU, and playback is very authentic. Witness this awesome rendition of the iconic Doom E1M1 theme:

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/tvr3GdtlhcI?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 


### Direct Playback via USB

If you're lucky enough to own a <a href="https://en.wikipedia.org/wiki/Roland_MT-32" target="_blank">real MT-32</a> or <a href="https://en.wikipedia.org/wiki/Roland_Sound_Canvas" target="_blank">Sound Canvas hardware</a>, you can hook it up to the MiSTer directly. 

You'll need an <a href="https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture" target="_blank">ALSA</a>-supported USB MIDI adapter such as the <a href="https://www.roland.com/global/products/um-one_mk2/" target="_blank">Roland UM-ONE</a>. Once you plug it in, this menu option will appear. Good to go!

![](/img/posts/roland-um-one_mk2_usb-midi-interface-adapter.jpg)

If you don't have a real synth, consider looking at the <a href="https://github.com/dwhinham/mt32-pi" target="_blank">mt32-pi</a> project – a baremetal MIDI/MT-32 synthesizer for Raspberry Pi 3.


### Network Playback over UDP

Configure MidiLink as follows:

![](/img/posts/mister-ao486-midilink-uart-mode-udp-udpmidi.png)

In this mode, MidiLink will transmit MIDI data onto the network as <a href="https://en.wikipedia.org/wiki/User_Datagram_Protocol" target="_blank">UDP packets</a> – for playback on a networked MIDI device. The simplest possible setup:

1. Download, install and run a software synthesizer like <a href="https://sourceforge.net/projects/munt/" target="_blank">Munt</a>, <a href="https://www.fluidsynth.org/" target="_blank">FluidSynth</a> or <a href="https://coolsoft.altervista.org/en/virtualmidisynth" target="_blank">VirtualMIDISynth</a> on your home PC
2. Download the necessary <a href="https://en.wikipedia.org/wiki/SoundFont" target="_blank">SoundFonts</a>
3. Download and run <a href="https://github.com/bbond007/UDPMIDI" target="_blank">UDPMIDI</a>. This small program will receive the UDP MIDI packets and send to your software synth
4. Edit <code>/media/fat/linux/MidiLink.INI</code> on your MiSTer. Set <code>UDP_SERVER</code> to the IP address of your home PC:

![](/img/posts/mister-ao486-midilink-ini-udp-server.png)

{:start="5"}
5. When MIDI playback begins in ao486, UDPMIDI will start receiving packets and playback should start!

![](/img/posts/mister-ao486-midilink-udp-udpmidi.png)

If you have trouble receiving packets, check your personal firewall. I use Windows Defender and added the following rule to allow incoming private network traffic on UDP 1999:

![](/img/posts/mister-ao486-midilink-udp-udpmidi-incoming-firewall-rule.png)


That's it! Hope you find this useful for your own MIDI adventures!
 
 
### Other Posts in this Series
 
{% include mister-fpga-series.md %}






