---
layout: post
title: DOS Gaming on MiSTer FPGA
date: '2021-03-01 12:00:00'
tags: [Emulation, MiSTer FPGA, MS-DOS, PC, Projects, Retrocomputing, Retrogaming]
status: completed
---

Having acquired a <a href="https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046" target="_blank">Terasic DE10-Nano FGPA Development Kit</a>, I was very keen to install the [MiSTer software distribution]({% post_url  2020-08-22-mister-fpga-introduction-and-hardware-overview %}) and try some retro computing cores.

First on the list: the 80486 PC. I've many fond memories of DOS and Windows 95 gaming, messing with IRQ settings, tuning <code>config.sys</code> and <code>autoexec.bat</code> to get things working "just so".

Luckily for me, DOS gaming is very well served on MiSTer via the <a href="https://github.com/MiSTer-devel/ao486_MiSTer" target="_blank">ao486 core</a>.


### Project Notes

Status | Completed
Goal | Play DOS and Windows 95 games on the MiSTer FPGA platform

After a lot of tinkering, I was able to [setup file sharing]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}), [install a Memory Manager]({% post_url 2021-03-13-mister-ao486-core-part-3-managing-memory %}), [configure the Sound Blaster]({% post_url 2021-03-13-mister-ao486-core-part-4-sound-blaster-and-adlib-opl2-opl3-music %}), add [CD-ROM]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %}) and [Mouse]({% post_url 2021-03-13-mister-ao486-core-part-6-mouse-support %}) support, [configure Roland MIDI]({% post_url 2021-03-28-mister-ao486-core-part-8-midilink-midi-roland-mt-32-sound-canvas %}) and [install Windows 95]({% post_url 2021-03-28-mister-ao486-core-part-9-windows-95-install %}).

I chronicled the whole thing via a series of blog posts (see below).

A great result!


### Project Updates

- [MiSTer AO486 Core Part 1 – Getting Started]({% post_url 2021-02-06-mister-ao486-core-part-1-dos-quick-start %}) - 06 Feb 2021
- [MiSTer AO486 Core Part 2 – Sharing Files With MiSTerFS]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}) - 14 Feb 2021
- [MiSTer AO486 Core Part 3 – Managing Memory]({% post_url 2021-03-13-mister-ao486-core-part-3-managing-memory %}) - 13 Mar 2021
- [MiSTer AO486 Core Part 4 – Sound and Music Setup]({% post_url 2021-03-13-mister-ao486-core-part-4-sound-blaster-and-adlib-opl2-opl3-music %}) - 13 Mar 2021
- [MiSTer AO486 Core Part 5 – Adding CD-ROM Support]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %}) - 13 Mar 2021
- [MiSTer AO486 Core Part 6 – Mouse Support]({% post_url 2021-03-13-mister-ao486-core-part-6-mouse-support %}) - 13 Mar 2021
- [MiSTer AO486 Core Part 7 – Quick Start DOS Image]({% post_url 2021-03-18-mister-ao486-core-part-7-dos-quick-start-hard-disk-image %}) - 18 Mar 2021
- [MiSTer AO486 Core Part 8 – Roland MT-32, Sound Canvas Audio via MidiLink]({% post_url 2021-03-28-mister-ao486-core-part-8-midilink-midi-roland-mt-32-sound-canvas %}) - 28 Mar 2021
- [MiSTer AO486 Core Part 9 – Installing Windows 95]({% post_url 2021-03-28-mister-ao486-core-part-9-windows-95-install %}) - 28 Mar 2021

<br />