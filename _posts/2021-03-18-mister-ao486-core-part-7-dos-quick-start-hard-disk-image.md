---
layout: post
title: "MiSTer AO486 Core Part 7 – Quick Start DOS Image"
date: '2021-03-18 00:59:00:00'
summary: To get gaming fast, download this quick start DOS image ...
tags: [How To, MiSTer FPGA, MS-DOS, Posts, Retrocomputing, Retrogaming, Single-Board Computing]
---

<a href="https://github.com/MiSTer-devel/ao486_MiSTer" target="_blank">ao486</a> is an x86 FPGA core for MiSTer, implementing all features of an 80486SX CPU. Performance-wise, the core is in line with an i486DX-33 CPU, making it perfect for DOS gaming.

To get gaming fast, use this "quick start" hard disk image, complete with:

* DOS 6.22 pre-installed
* Memory manager (<a href="https://en.wikipedia.org/wiki/EMM386" target="_blank">EMM386</a>) with boot configurations for Extended/Expanded memory
* Sound Blaster, CD-ROM and mouse drivers
* MiSTerFS sharing (allows easy file-sharing between PC and ao486)

Setup takes ~10 minutes. Here's how to get started.


### Quick Start Steps

1. Download <a href="https://1drv.ms/u/s!AhPM2FpzJ_ovgSdQMvoD_BlPvMJe?e=VVoRq5" target="_blank">this hard disk image</a> and extract it. It'll expand to ~2GB in size

2. Use a file transfer tool like FileZilla to copy the image to <code>/media/fat/games/AO486</code> on your MiSTer (learn how to do that [here]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %})). You should have a single file named <code>DOS622.vhd</code>:

![](/img/posts/mister-ao486-dos-quick-start-dos622-copy-vhd-hard-disk-drive-image.png)

{:start="3"}
3. Download boot0.rom and boot1.rom from <a href="https://github.com/MiSTer-devel/ao486_MiSTer/tree/master/releases/bios" target="_blank">this Releases page</a>. [Copy]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}) them to <code>/media/fat/games/AO486</code> on your MiSTer:

![](/img/posts/mister-ao486-dos-quick-start-dos622-copy-boot-roms.png)

{:start="4"}
4. Power up the ao486 core and mount the hard drive  (*Windows Key* + *F12* for ao486 core options, set *IDE 0-0* to <code>DOS622.vhd</code>):

![](/img/posts/mister-ao486-dos-quick-start-dos622-mount-vhd-hard-disk-drive-image.png)

{:start="5"}
5. Still in the core options menu, select *Reset and apply HDD*. The core will reboot and load DOS.  The following indicates a succesful load:

![](/img/posts/mister-ao486-dos-quick-start-first-boot.png)

<!-- TODO: add YouTube video and link here -->


### Mounting Floppy and CD-ROM Images

Both floppy images (<a href="https://en.wikipedia.org/wiki/IMG_(file_format)" target="_blank">IMG</a> format) and CD-ROM images (<a href="https://en.wikipedia.org/wiki/Optical_disc_image" target="_blank">ISO</a> and <a href="https://en.wikipedia.org/wiki/Cue_sheet_(computing)" target="_blank">BIN/CUE</a> formats) can be mounted natively. 

To mount a floppy image, first [transfer it to your MiSTer]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}), then:

1. Hit *Windows Key* + *F12* for ao486 core options.
2. Select *Floppy A:* and hit *Enter*. Select your image file and hit *Enter* again
3. Hit *Esc* to exit the core options menu. Your floppy image is now mounted and available in DOS at <code>A:</code>

![](/img/posts/mister-ao486-dos-quick-start-mount-floppy.png)

To mount a CD-ROM image, again [transfer it to your MiSTer]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}), then:

1. Hit *Windows Key* + *F12* for ao486 core options.
2. Select *IDE 1-0* and hit *Enter*. Select your image file and hit *Enter* again
3. Hit *Esc* to exit the core options menu. Your CD-ROM image is now mounted and available in DOS at <code>D:</code>

![](/img/posts/mister-ao486-dos-quick-start-mount-cd-rom.png)

You can learn more about CD-ROM support [here]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %}).


### Copying Files

You can copy games files/executables directly into the DOS partition via MiSTerFS. Learn more about transferring files [here]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}).


### Build Your Own ao486 Hard Disk Image

If you want to build and customize your own hard disk image (and learn along the way), here's how:

1. [Create a blank hard disk image and install DOS 6.22]({% post_url 2021-02-06-mister-ao486-core-part-1-dos-quick-start %})
2. [Configure MiSTerFS for easy file transfer]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %})
3. [Install EMM386 memory manager]({% post_url 2021-03-13-mister-ao486-core-part-3-managing-memory %}) (required for games that require Expanded/Extended memory)
4. [Set the BLASTER environment variable]({% post_url 2021-03-13-mister-ao486-core-part-4-sound-blaster-and-adlib-opl2-opl3-music %}). Some games use this for sound/music setup
5. Add [CD-ROM]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %}) and [mouse]({% post_url 2021-03-13-mister-ao486-core-part-6-mouse-support %}) support


### Autoexec.bat and Config.sys

For reference. Here are the AUTOEXEC.BAT and CONFIG.SYS used in this setup. Feel free to copy/paste and use as your own inspiration for DOS builds:

#### AUTOEXEC.BAT

````
@ECHO OFF
PROMPT $p$g
PATH C:\DOS

LH C:\UTILS\MISTERFS\MISTERFS.EXE E /Q
LH C:\DOS\MSCDEX.EXE /D:MSCD001 /L:D
LH C:\DRIVERS\CTMOUSE.EXE

SET TEMP=C:\DOS
SET BLASTER=A220 I5 D1 H5 T6
````

#### CONFIG.SYS

````
[COMMON]
FILES=30
LASTDRIVE=Z

[menu]  
menuitem=X, Extended memory (default)
menuitem=E, Extended + Expanded memory
menuitem=C, Conventional memory only

menudefault=X,10

[X]
DEVICE=C:\DOS\HIMEM.SYS /TESTMEM:OFF
DOS=HIGH,UMB
DEVICE=C:\DOS\EMM386.EXE NOEMS I=C800-CDFF X=CE00-CFFF I=D000-EFFF
DEVICEHIGH=C:\DRIVERS\OAKCDROM.SYS /D:MSCD001

[E]
DEVICE=C:\DOS\HIMEM.SYS /TESTMEM:OFF
DOS=HIGH,UMB
DEVICE=C:\DOS\EMM386.EXE RAM 8192 FRAME=D000 D=256 I=C800-CDFF X=CE00-CFFF I=D000-EFFF
DEVICEHIGH=C:\DRIVERS\OAKCDROM.SYS /D:MSCD001

[C]
DEVICEHIGH=C:\DRIVERS\OAKCDROM.SYS /D:MSCD001
````


### Other Posts in this Series

{% include mister-fpga-series.md %}

