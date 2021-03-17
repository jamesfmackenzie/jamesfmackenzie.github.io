---
layout: post
title: "MiSTer AO486 Core Part 6 – DOS Quick Start"
date: '2021-03-17 06:44:00:00'
summary: A wrap-up of all sessions so far. Ready to go ao486 config set for DOS ...
tags: [Retrocomputing, Retrogaming, FPGA, MiSTer, Single-Board Computing]
---

ao486 is a x86 FPGA core for MiSTer, implementing all features of an 80486SX CPU. Performance-wise, the core is in line with an i486DX-33 CPU, making it perfect for DOS gaming.

To get gaming fast, use this "quick start" hard disk image, complete with:

* DOS 6.22 pre-installed
* Memory manager (EMM386) with boot configurations for Extended/Expanded memory
* Sound Blaster, CD-ROM and mouse drivers
* MiSTerFS sharing. Allows easy file-sharing between PC and AO486

Setup takes ~10 minutes. Here's how to get started.


### Quick Start Steps

1. Download <a href="https://misterfpga.org/download/file.php?id=676" target="_blank">the hard disk image</a> (hosted on <a href="https://archive.org/" target="_blank">archive.org</a>) and extract it. It'll expand to 2GB

2. Use a file transfer tool like FileZilla to copy the floppy image to <code>/media/fat/games/AO486</code> on your MiSTer (learn how how to do that [here]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %})). You should have a single file name <code>DOS622.VHD</code>:

![](/img/posts/mister-ao486-misterfs-floppy-image.png)

{:start="3"}
3. Power up the ao486 core and mount the hard drive  (*Windows Key* + *F12* for ao486 core options, set *IDE 0* to <code>DOS622.VHD</code>)

![](/img/posts/mister-ao486-mount-misterfs-floppy-image-in-ao486.png)

{:start="4"}
4. Still in the core options menu, select *Reset and apply HDD*. The core will reboot and load DOS.  The following indicates a succesful load:

![](/img/posts/mister-ao486-mount-misterfs-floppy-image-in-ao486.png)

<!-- TODO: add YouTube video and link here -->


### Playing games

Floppy (.img) and CD-ROM (.iso/.bin/.cue) images can be mounted natively. 

You can also copy games files/executables directly into the DOS partition via MiSTerFS

Happy gaming!

To copy files directly into the DOS partition, use

Either insert floppy images/CD-ROMs, install the games and play as usual!

Use miSTerFS to transfer directly to DOS <link to misterfs doc>


### DIY Method

If you want to follow the full setup and learn along the way, here’s how:

1. Install DOS 6.22
2. Configure MiSTerFS for easy file transfer
3. Install EMM386 memory manager. Required for games that require Expanded/Extended memory
4. Set the BLaSTEr end variable so all games pickup sound
5. Add CD-ROM and mouse support


### Autoexec.bat and Config.sys

For reference, here are the autoexec.bat and config.sys used in this setup. Feel free to copy/paste and use as your own inspiration for DOS builds:

<copy here>


### Other Posts in this Series

{% include mister-fpga-series.md %}

