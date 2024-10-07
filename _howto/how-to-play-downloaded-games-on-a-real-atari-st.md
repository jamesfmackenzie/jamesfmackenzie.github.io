---
layout: post
title: Playing Downloaded Games on a Real Atari ST
date: '2015-09-18 22:33:00'
summary: As discussed before, I want to play some downloaded games on my Atari ST ...
tags: [Atari ST]
---


## Playing Downloaded Games on Real ST Hardware

Status | Completed September 2015
Goal | Download an Atari ST game image from the web and play it on my real ST

My old ST disks are dead! Can I download replacement disk images from the web and play on my physical ST?

I explored several options, including floppy disk images and hard disk adaptations:

- [Playing Downloaded Games on a Real Atari ST]({% post_url 2015-09-18-playing-downloaded-games-on-a-real-atari-st %}) - 18 Sep 2015
- [Use Your PC to Create a Bootable Atari ST Game Disk]({% post_url 2015-09-22-use-your-pc-to-create-a-bootable-atari-st-game-disk %}) - 22 Sep 2015



As discussed before, I want to [play some downloaded games on my Atari ST]({% post_url 2015-08-15-atari-in-the-attic %}).

But first we need to get them there. Here are the options:


### Option 1. Use Disk Images

<a href="https://en.wikipedia.org/wiki/Disk_image" target="_blank">Disk Images</a> are a software representation of the physical Atari ST game disk. Think the floppy equivalent of the .ISO files you use for CDs/DVDs. Common image formats are .ST, .MSA and .STX (aka Pasti). For our use case we prefer the first two as .STX is for emulators only and cannot be used on a physical Atari.

Disk images are freely available on the web (use Google). <a href="http://www.emuparadise.me/Atari_ST_ROMs/63" target="_blank">Emuparadise</a> is probably the best resource.

Once you have a disk image, you need to make it physically playable on the Atari ST. Your options:

1. [Use your PC to prepare a bootable game disk]({% post_url 2015-09-22-use-your-pc-to-create-a-bootable-atari-st-game-disk %}). Then put the game disk into your ST, power on and boot the game
2. [Transfer the disk image to your ST]({% post_url 2015-12-26-transferring-files-from-pc-to-st %}). Then use your ST to prepare a bootable game disk.
3. [Transfer the disk image to your ST]({% post_url 2015-12-26-transferring-files-from-pc-to-st %}). Then mount it as a <a href="https://en.wikipedia.org/wiki/RAM_drive" target="_blank">RAM disk</a> and run the game directly.
4. Purchase and use a <a href="https://en.wikipedia.org/wiki/Floppy_disk_hardware_emulator" target="_blank">floppy emulator</a>. Floppy emulators are a hardware solution that trick the ST into thinking a disk image is a real game disk


### Option 2. Use Hard Disk Adaptations

Most original ST games were designed to boot directly from floppy disk, bypassing the Desktop OS. This approach frees up more memory, allowing the game to be bigger and better.

Following the initial ST release, units with more memory arrived, opening up the possibility of launching games from within the Desktop UI - or even from an attached hard disk (if you had one). Way more convenient. This wasn't the intention of game developers, though, and games had to be hacked/adapted to run.

Over time, hard disk adaptations appeared for almost all popular titles. You can find some <a href="http://atari.8bitchip.info/fromhd.php" target="_blank">here</a>, <a href="http://www.klapauzius.net/Old_Games.html" target="_blank">here</a> and <a href="http://dbug.kicks-ass.net/patch.php" target="_blank">here</a>.

To play a hard disk adaptation, all you need to do is:

1. Download it
2. [Transfer it to your ST]({% post_url 2015-12-26-transferring-files-from-pc-to-st %})
3. Launch the file from within the Desktop UI


### How Do I Transfer Files From PC to ST?

Several of the solutions above rely on transferring files from PC to ST. I've already explored this and you [can find the details here]({% post_url 2015-12-26-transferring-files-from-pc-to-st %})

That's pretty much it. Happy retrogaming!


### More Atari ST Posts
 
{% include atari-st.md %}