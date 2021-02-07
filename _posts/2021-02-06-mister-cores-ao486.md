---
layout: post
title: "MiSTer Cores – ao486 DOS Quick Start"
date: '2021-02-06 18:21:00:00'
summary: Deep dive on the MiSTer AO486 Core ...
tags: [Retrocomputing, Retrogaming, FPGA, MiSTer, Single-Board Computing]
---

You’ve followed the [setup guide]({% post_url 2020-09-20-mister-fpga-install-and-setup %}) and know how to [copy files to your MiSTer]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}). Now you're ready to try out some cores. Let's start with ao486.

### What is ao486?

ao486 is a <a href="https://en.wikipedia.org/wiki/X86" target="_blank">x86 PC-compatible</a> core implementing all features of an <a href="https://en.wikipedia.org/wiki/Intel_80486SX" target="_blank">80486SX</a> CPU. Together with the 486 core, the ao486 project also contains a <a href="https://en.wikipedia.org/wiki/System_on_a_chip" target="_blank">SoC</a> capable of booting <a href="https://en.wikipedia.org/wiki/MS-DOS" target="_blank">DOS</a>, <a href="https://en.wikipedia.org/wiki/Windows_3.1x" target="_blank">Windows 3.1</a>, <a href="https://en.wikipedia.org/wiki/Windows_95" target="_blank">Windows 95</a> and <a href="https://en.wikipedia.org/wiki/Linux_kernel" target="_blank">Linux kernel</a> 3.13.

Performance-wise, the core is in line with a <a href="https://en.wikichip.org/wiki/intel/80486/486dx-33" target="_blank">i486DX-33</a> CPU – only with a missing <a href="https://en.wikipedia.org/wiki/Floating-point_unit" target="_blank">FPU</a>. This makes it perfect for DOS gaming.


### Features

In addition to the CPU, the ao486 core also includes:

- 256MB RAM
- <a href="https://en.wikipedia.org/wiki/Super_VGA" target="_blank">SVGA</a> graphics (1280x1024 at 256 colours, 1024x768 at ~65,000 colours, 640x480 at ~16 million colours)
- <a href="https://en.wikipedia.org/wiki/Sound_Blaster">Sound Blaster</a> Pro and Sound Blaster 16 support. Choice of <a href="https://en.wikipedia.org/wiki/Yamaha_YM3812" target="_blank">OPL2</a>, <a href="https://en.wikipedia.org/wiki/Yamaha_YMF262" target="_blank">OPL3</a> and <a href="https://en.wikipedia.org/wiki/Sound_Blaster#Creative_Music_System" target="_blank">CM/S</a> synth
- High speed <a href="https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter" target="_blank">Serial/UART</a> (3Mbps)
- <a href="https://en.wikipedia.org/wiki/MIDI" target="_blank">MIDI</a> device support, built-in <a href="https://github.com/dwhinham/mt32-pi" target="_blank">Roland MT-32 emulation</a>
- 4 virtual HDDs, up to 137GB each
- 2 virtual CD-ROM drives


### DOS Quick Start

Some quick steps to get up and running with DOS and a copy of <a href="https://en.wikipedia.org/wiki/Doom_(1993_video_game)" target="_blank">Doom</a>.


#### Step 1 – Download and Copy Install Media

Download, extract and [copy]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}) the following floppy disk images to <code>/media/fat/games/AO486</code> on your MiSTer:

* <a href="https://archive.org/details/002962-MsDos622" target="_blank">DOS 6.22 Floppy Disk Images</a>
* <a href="https://archive.org/details/001258-Doom" target="_blank">Doom Floppy Disk Images</a>

Once you're done, you should have:

* <code>disk1.img, disk2.img, disk3.img</code> – DOS 6.22 install images
* <code>disk1.img, disk2.img</code> – Doom install images

![](/img/posts/mister-ao486-dos-622-doom-install-floppy-images.png)


#### Step 2 – Copy Boot ROMs

Next you need to install the ao486 <a href="https://en.wikipedia.org/wiki/BIOS" target="_blank">BIOS</a>:

1. Visit <a href="https://github.com/MiSTer-devel/ao486_MiSTer/tree/master/releases/bios" target="_blank">this Releases page</a> on GitHub

2. Download, extract and [copy]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}) boot0.rom and boot1.rom to <code>/media/fat/games/AO486</code> on your MiSTer:

![](/img/posts/mister-ao486-bios-boot-roms.png)


#### Step 3 – Create a Hard Disk

1. SSH into your MiSTer and navigate to <code>/media/fat/games/AO486</code>

2. Invoke the following command to create a 2GB file (*DOS.vhd*) filled with zeros. We'll use this for our primary hard disk:

````
dd if=/dev/zero of=DOS.vhd bs=1M count=2048
````

![](/img/posts/mister-ao486-dos-622-hard-disk-vhd.png)


#### Step 4 – Install Operating System

Time to install the Operating System. On the MiSTer:

1. Press *F12* to bring up the MiSTer main menu. Browse to *Computer -> ao486* to start the ao486 core:
   
![](/img/posts/mister-start-ao486-core.png)

{:start="2"}
2. Hit *Windows Key* + *F12* for ao486 core options. Set *Floppy A:* to the DOS 6.22 <code>disk1.img</code> and *IDE 0-0* to <code>DOS.vhd</code>:

![](/img/posts/mister-ao486-core-settings.png)

{:start="3"}
3. Hit *Reset and apply HDD*. ao486 will reboot into MS-DOS 6.22 Setup. Hit *Enter* and follow the prompts to install DOS:

![](/img/posts/mister-ao486-dos-622-install-setup.png)

{:start="4"}
4. You'll be be asked to switch disk a few times. Hit *Windows Key* + *F12* for ao486 core options, set *Floppy A:* to <code>disk2.img</code> or <code>disk3.img</code> as prompted, then bit *Esc*:

![](/img/posts/mister-ao486-dos-622-install-switch-disk.png)

![](/img/posts/mister-ao486-dos-622-install-switch-disk-2.png)

{:start="5"}
5. At the final stage, you'll be asked to "Remove disks for all floppy disk drives". Follow the same disk switch steps as above, but this time hit *Backspace* to unmount the floppy:

![](/img/posts/mister-ao486-dos-622-install-remove-disk.png)

![](/img/posts/mister-ao486-dos-622-install-remove-disk-2.png)

{:start="6"}
6. Hit *Enter* to finalize the install. ao486 will restart and boot to DOS from your new hard disk:

![](/img/posts/mister-ao486-boot-from-dos-622.png)


#### Step 5 – Install Doom

Time to install Doom! From the DOS prompt:

1. Hit *Windows Key* + *F12* for ao486 core options, set *Floppy A:* to the Doom <code>disk1.img</code>

2. Navigate to the floppy drive by typing <code>A:</code>. Then type <code>INSTALL.BAT</code> to begin the Doom install:

![](/img/posts/mister-ao486-install-doom-1.png)

{:start="3"}
3. Follow the default install options. You'll be asked to switch disk a few times. Follow the same steps outlined above:

![](/img/posts/mister-ao486-install-doom-3.png)



#### Step 6 – Doom Sound Setup

After the install completes, Doom Setup will automatically launch. You'll need to configure sound hardware

1. When prompted to select *Music Playback Device* or *Sound FX Device*, choose <code>Sound Blaster</code>:

![](/img/posts/mister-ao486-doom-setup-1.png)

{:start="2"}
2. When prompted to select *PORTs*, *IRQs* or *DMA Channels*, take the pre-selected options (PORT = <code>220</code>, IRQ = <code>5</code>, DMA = <code>1</code>)

3. Once done, hit *Save Settings & Run Doom*:

![](/img/posts/mister-ao486-doom-setup-2.png)


#### Step 7 – Play Doom!

You're good to go! Doom runs relatively well, but is pushing the limits of what plays well on the ao486 core. Look for more deep dives in future!

![](/img/posts/mister-ao486-doom-1.png)

![](/img/posts/mister-ao486-doom-2.png)


### Other Posts in this Series

{% include mister-fpga-series.md %}

