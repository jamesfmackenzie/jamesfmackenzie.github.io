---
layout: post
title: "MiSTer AO486 Core Part 6 – Mouse Support"
date: '2021-03-13 22:57:00:00'
summary: Adding mouse support to the MiSTer ao486 core ...
tags: [How To, MiSTer FPGA, MS-DOS, Posts, Retrocomputing, Retrogaming, Single-Board Computing]
---

Many DOS games and applications need mouse support. Here's how to get up and running.

### Step 1 – Download and Copy Mouse Driver

1. We'll use the Open Source CuteMouse driver. Download it from <a href="http://cutemouse.sourceforge.net/" target="_blank">here</a>
2. Extract the downloaded archive and find <code>ctmouse.exe</code>. That's all you need. It's in the <code>bin</code> folder
2. Use [MiSTerFS]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}) to transfer <code>ctmouse.exe</code> to ao486
3. In ao486, type the following commands to copy the driver to <code>C:\DRIVERS</code>:

```
mkdir C:\DRIVERS
copy E:\CTMOUSE.EXE C:\DRIVERS
```

![](/img/posts/mister-ao486-mouse-cutemouse-driver.png)


### Step 2 – Install Mouse Driver

To install and activate the mouse driver, you'll need to update your <code>AUTOEXEC.BAT</code>.

1. From the DOS command prompt, type <code>edit c:\AUTOEXEC.BAT</code>. An editor application will open. Add the following line to your <code>AUTOEXEC.BAT</code>:

````
LH C:\DRIVERS\CTMOUSE.EXE
````

<blockquote>This loads the CuteMouse driver into High memory with default settings. Hit <i>Alt+F,S</i> to save, then <i>Alt+F,X</i> to exit.</blockquote>

{:start="2"}
2. Hit *Windows Key* + *F12* for ao486 core options. Select *Reset and apply HDD* to reboot ao486 and load the mouse driver. The following indicates a succesful load:

![](/img/posts/mister-ao486-mouse-cutemouse-driver-autoexec-bat-load.png)

That's it – you're ready to play some games! Can I recommend Monkey Island?

![](/img/posts/mister-ao486-mouse-cutemouse-monkey-island-lucasarts.png)


### Related Posts

* [MiSTer AO486 Core Part 4 – Sound and Music Setup]({% post_url 2021-03-13-mister-ao486-core-part-4-sound-blaster-and-adlib-opl2-opl3-music %})
* [MiSTer AO486 Core Part 5 – Adding CD-ROM Support]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %})


### Other Posts in this Series

{% include mister-fpga-series.md %}

