---
layout: post
title: "MiSTer AO486 Core Part 5 – Adding CD-ROM Support"
date: '2021-03-13 21:26:00:00'
summary: Installing CD-ROM drivers for the MiSTer ao486 core ...
tags: [Emulation, MiSTer FPGA, MiSTer FPGA Cores]
---

Did you know that ao486 has built-in CD-ROM support? You can mount either ISO or BIN/CUE files – ao486 will think it's a real CD-ROM! Here's how.


### Step 1 – Download and Copy CD-ROM Driver

1. We'll use the OAKCDROM.SYS driver. Download it from <a href="https://www.computerhope.com/download/hardware.htm" target="_blank">here</a>
2. Use [MiSTerFS]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}) to transfer it to ao486
3. In ao486, type the following commands to copy the driver to <code>C:\DRIVERS</code>:

```
mkdir C:\DRIVERS
copy E:\OAKCDROM.SYS C:\DRIVERS
```

![](/img/posts/mister-ao486-cdrom-oakcdrom-sys-driver.png)


### Step 2 – Install CD-ROM Driver

To install and activate the CD-ROM driver, you'll need to update both your <code>CONFIG.SYS</code> and <code>AUTOEXEC.BAT</code>.

1. From the DOS command prompt, type <code>edit c:\CONFIG.SYS</code>. An editor application will open. Add the following line to your <code>CONFIG.SYS</code>:

````
DEVICEHIGH=C:\DRIVERS\OAKCDROM.SYS /D:MSCD001
````

<blockquote>This will load the CD-ROM device driver into memory. Hit <i>Alt+F,S</i> to save the file, then <i>Alt+F,X</i> to exit.</blockquote>

{:start="2"}
2. Next, type <code>edit c:\AUTOEXEC.BAT</code>. An editor application will open. Add the following line to your <code>AUTOEXEC.BAT</code>:

````
LH C:\DOS\MSCDEX.EXE /D:MSCD001 /L:D
````

<blockquote>This mounts the CD-ROM as drive <code>D:</code> and allows DOS programs to recognize CDs. Again hit <i>Alt+F,S</i> to save, <i>Alt+F,X</i> to exit.</blockquote>

{:start="3"}
3. Hit *Windows Key* + *F12* for ao486 core options. Select *Reset and apply HDD* to reboot ao486. The CD-ROM driver should load as follows:

![](/img/posts/mister-ao486-cdrom-oakcdrom-sys-driver-2.png)


### Step 3 – Copy an ISO CD-ROM image to your MiSTer

Download a CD-ROM image in <a href="https://en.wikipedia.org/wiki/Optical_disc_image" target="_blank">ISO</a> format. I went for the <a href="https://archive.org/details/cdrom-ultimate-shareware-games-1" target="_blank">Ultimate Shareware Games Collection</a> from archive.org:

![](/img/posts/ultimate-shareware-games-collection.jpg)

Once downloaded, [copy your ISO]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}) to the <code>/media/fat/games/AO486</code> folder on your MiSTer.


### A Note on CD-ROM Formats

Currently ao486 only supports CD-ROM data. The best image format to use is <a href="https://en.wikipedia.org/wiki/Optical_disc_image" target="_blank">ISO</a>. <a href="https://en.wikipedia.org/wiki/Cue_sheet_(computing)" target="_blank">BIN/CUE</a> can also be mounted, but extra tracks or audio/video won't be recognized. 


### Step 3 – Mount a CD-ROM

Time to mount a CD-ROM! From the DOS prompt:

1. Hit *Windows Key* + *F12* for ao486 core options. Highlight *IDE 1-0* and hit *Enter*. Select your ISO file:

![](/img/posts/mister-ao486-cdrom-choose-ide1-0-cd-rom-iso-bin-cue-2.png)

{:start="2"}
2. Hit *Esc* to close the MiSTer menu and navigate to the CD-ROM by typing <code>D:</code>. Then type <code>dir</code> to view the contents of your CD:

![](/img/posts/mister-ao486-cdrom-list-cd-rom-contents.png)

<blockquote>All going well, you should see the CD contents. You're ready to play some games!</blockquote>

![](/img/posts/mister-ao486-spear-of-destiny.png)

That's it for this post. Consider looking at [sound]({% post_url 2021-03-13-mister-ao486-core-part-4-sound-blaster-and-adlib-opl2-opl3-music %}) and [mouse]({% post_url 2021-03-13-mister-ao486-core-part-6-mouse-support %}) setup if you haven't already.


### Other Posts in this Series

{% include mister-fpga-series.md %}

