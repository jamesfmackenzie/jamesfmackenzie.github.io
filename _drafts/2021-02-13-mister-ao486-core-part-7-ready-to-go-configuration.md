---
layout: post
title: "MiSTer AO486 Core Part 6 – \"Ready-to-Go\" DOS Quick Start"
date: '2021-03-17 06:44:00:00'
summary: A wrap-up of all sessions so far. Ready to go ao486 config set for DOS ...
tags: [Retrocomputing, Retrogaming, FPGA, MiSTer, Single-Board Computing]
---

Want to play classic DOS games on your MiSTer?

I've prepared a "Ready-to-Go" hard disk image for the AO486 (80486SX) core, complete with:

* MS-DOS 6.22 pre-installed
* Memory manager (EMM386) setup with boot configurations for Extended/Expanded memory. Choose your memory config on each boot
* Sound Blaster, CD-ROM and mouse drivers pre-loaded
* MiSTerFS sharing pre-configured. Allows easy file-sharing between PC and AO486

Setup takes ~10 minutes. Here's how to get started.


### Quick Start Steps

1.	Download it from archive.org
2.	Copy it to MiSTer (location)
3.	Start ao486
4.	Set IDE0 and reboot
5.	Enjoy!

<!-- TODO: add YouTube video and link here -->


### Playing games

Either insert floppy images/CD-ROMs, install the games and play as usual!

Use miSTerFS to transfer directly to DOS <link to misterfs doc>


### DIY Method

If you want to follow the full setup and learn along the way, here’s how:

1.	Install DOS 6.22
2.	Configure MiSTerFS for easy file transfer
3.	Install EMM386 memory manager. Required for games that require Expanded/Extended memory
4.	Set the BLaSTEr end variable so all games pickup sound
5.	Add CD-ROM and mouse support


### Autoexec.bat and Config.sys

For reference, here are the autoexec.bat and config.sys used in this setup. Feel free to copy/paste and use as your own inspiration for DOS builds:

<copy here>


### Other Posts in this Series

{% include mister-fpga-series.md %}

