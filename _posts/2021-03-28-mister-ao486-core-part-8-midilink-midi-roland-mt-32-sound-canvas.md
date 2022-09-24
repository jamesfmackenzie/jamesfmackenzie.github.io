---
layout: post
title: "MiSTer AO486 Core Part 8 – Roland MT-32, Sound Canvas Audio via MidiLink"
date: '2021-03-28 15:12:00:00'
summary: Thanks to fantastic work in the MiSTer community, you can get Roland MT-32 and Sound Canvas audio working in ao486. Here's how ...
image: roland-um-one_mk2_usb-midi-interface-adapter.jpg
tags: [DOS, FPGA, How To, MIDI, MiSTer, Posts, Retrocomputing, Retrogaming, Single-Board Computing]
---

<a href="https://en.wikipedia.org/wiki/Ad_Lib,_Inc." target="_blank">AdLib</a> is the de facto synth standard for DOS-gaming. Almost all games support AdLib music, and popular cards like the Sound Blaster include the same <a href="https://en.wikipedia.org/wiki/Yamaha_YM3812" target="_blank">Yamaha YM3812 (OPL2) chip</a> for AdLib-compatibility.

But true DOS gamers can do better. Games from the late 80s onwards often feature vastly superior <a href="https://en.wikipedia.org/wiki/MIDI" target="_blank">MIDI audio</a> – with strong support for the <a href="https://en.wikipedia.org/wiki/Roland_MT-32" target="_blank">Roland MT-32 synthesiser</a> and (for later games) the <a href="https://en.wikipedia.org/wiki/General_MIDI" target="_blank">General MIDI standard</a>. Give this a listen:

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/PMYKSwTa2cY?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div> 

Sounds glorious, no? Especially when compared to the (rather drab) <a href="https://www.youtube.com/watch?v=U4R_--__fjE" target="_blank">AdLib audio version</a>.

Thanks to fantastic work in the MiSTer community, you can get this working on your own MiSTer. Here's how.


### Step 1 – Install MidiLink

On real PCs, the Sound Blaster and other audio cards often include a MIDI interface for connecting MIDI devices. MiSTer provides a connectivity solution too via "MidiLink" – a daemon that runs on the ARM CPU, interfacing with running FPGA cores to pipe MIDI traffic downstream for playback. To get MidiLink installed:

1. Power on your MiSTer and hit *F12* to open the System Settings menu

2. Run `Scripts → Yes → midilink_updater`. This will install the latest version of MidiLink

3. After the forced reboot, hit *F12* once again to open the System Settings menu

4. This time, run `Scripts → Yes → soundfont_install`. This will download the <a href="https://en.wikipedia.org/wiki/SoundFont" target="_blank">SoundFonts</a> necessary for MIDI playback.

![](/img/posts/mister-ao486-midilink-updater.png)


### Step 2 – Enable MIDI Connection

With MidiLink installed, we're almost ready to play! But first we need to enable the MIDI connection:

1. Boot the MiSTer ao486 core (*F12* brings up the MiSTer main menu, browse to *Computer → ao486*)

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
* *USB* is for physically connecting a MIDI playback device (the menu option is hidden otherwise)
* *UDP* sends MIDI data over the network to another software synthesiser

We'll explore each of these below.

Whichever option you pick, the MIDI port is always <code>330</code> (for use during game setup).


### Roland MT-32 Playback via MUNT

Configure MidiLink as follows. Then hit *Save*:

![](/img/posts/mister-ao486-midilink-uart-mode-local-munt.png)

In this mode, MiSTer runs the <a href="https://sourceforge.net/projects/munt/" target="_blank">Munt</a> software synthesizer to emulate a real Roland MT-32. This is a super neat "ready to go" solution, with sound piped directly to your TV via the HDMI port. Give it a listen:

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/H9dU5CjoCDw?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div> 

Unfortunately, MiSTer's onboard ARM CPU isn't *quite* powerful enough to run MUNT at full speed. You might hear some smooshed, delayed or off-pitch notes compared to <a href="https://youtu.be/PMYKSwTa2cY" target="_blank">authentic playback</a>. If this is an issue for you, don't worry – there are other options.


### General MIDI Playback via FluidSynth

Configure MidiLink as follows:

![](/img/posts/mister-ao486-midilink-uart-mode-local-fsynth-fluidsynth.png)

In this mode, MiSTer runs the <a href="https://www.fluidsynth.org/" target="_blank">FluidSynth</a> software synthesizer for <a href="https://en.wikipedia.org/wiki/General_MIDI" target="_blank">General MIDI</a> playback. By default, it uses <a href="https://en.wikipedia.org/wiki/Roland_SC-55" target="_blank">Roland SC-55</a> <a href="https://en.wikipedia.org/wiki/SoundFont" target="_blank">SoundFonts</a>, but any SoundFonts will work. FluidSynth is much lighter on the CPU vs Munt and playback is very authentic. Witness this awesome rendition of the Doom E1M1 theme:

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/tvr3GdtlhcI?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div> 


### Direct Playback via USB

If you're lucky enough to own real <a href="https://en.wikipedia.org/wiki/Roland_MT-32" target="_blank">MT-32</a> or <a href="https://en.wikipedia.org/wiki/Roland_Sound_Canvas" target="_blank">Sound Canvas hardware</a>, you can hook it up to the MiSTer directly. 

You'll need an <a href="https://en.wikipedia.org/wiki/Advanced_Linux_Sound_Architecture" target="_blank">ALSA</a>-supported USB MIDI adapter such as the <a href="https://www.roland.com/global/products/um-one_mk2/" target="_blank">Roland UM-ONE</a>. With an adapter connected, the <code>USB</code> menu option will appear. If you don't have a real synth, consider the <a href="https://github.com/dwhinham/mt32-pi" target="_blank">mt32-pi</a> project – a baremetal MIDI/MT-32 synthesizer for Raspberry Pi 3.

![](/img/posts/roland-um-one_mk2_usb-midi-interface-adapter.jpg)


### Network Playback over UDP

Configure MidiLink as follows:

![](/img/posts/mister-ao486-midilink-uart-mode-udp-udpmidi.png)

In this mode, MidiLink will transmit MIDI data onto the network as <a href="https://en.wikipedia.org/wiki/User_Datagram_Protocol" target="_blank">UDP packets</a> – for playback on a networked MIDI device. To get this working:

1. Download, install and run a software synthesizer on your home PC. <a href="https://sourceforge.net/projects/munt/" target="_blank">Munt</a> works well for MT-32 emulation and <a href="https://coolsoft.altervista.org/en/virtualmidisynth" target="_blank">VirtualMIDISynth</a> for General MIDI

2. [Copy]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}) the necessary MT-32 ROMS / SoundFonts from your MiSTer. Find them in <code>/media/fat/linux</code>

3. Download and run <a href="https://github.com/bbond007/UDPMIDI" target="_blank">UDPMIDI</a>. This small program will receive the UDP MIDI packets and forward them to your selected synth

4. Edit <code>/media/fat/linux/MidiLink.INI</code> on your MiSTer. Set <code>UDP_SERVER</code> to the IP address of your home PC:

![](/img/posts/mister-ao486-midilink-ini-udp-server.png)

{:start="5"}
5. When MIDI playback begins in ao486, UDPMIDI will start receiving packets and playback should start!

![](/img/posts/mister-ao486-midilink-udp-udpmidi.png)


#### UDP Troubleshooting 

If you have trouble receiving packets, check your personal firewall. I use <a href="https://en.wikipedia.org/wiki/Windows_Firewall" target="_blank">Windows Defender Firewall</a> and had to add an incoming rule to allow private network traffic on UDP port 1999:

![](/img/posts/mister-ao486-midilink-udp-udpmidi-incoming-firewall-rule.png)

As an alternative to UDPMIDI, it's also possible to build MidiLink <a href="https://github.com/bbond007/MiSTer_MidiLink" target="_blank">from source</a> and run in "listen" mode. The command line args are:

* <code>UDPMUNT</code> – to listen and forward to Munt 
* <code>UDPFSYNTH</code> – to listen and forward to FluidSynth

You can even run MidiLink on <a href="https://github.com/dwhinham/mt32-pi" target="_blank">mt32-pi</a> for an "appliance-like" solution. More details <a href="https://misterfpga.org/viewtopic.php?f=27&t=375" target="_blank">here</a>.


### Wrap Up

That’s it! We've explored all facets of MidiLink and MIDI playback options in ao486. Good luck with your own MIDI adventures!
 
 
### Other Posts in this Series
 
{% include mister-fpga-series.md %}


### More MIDI articles

{% include midi.md %}






