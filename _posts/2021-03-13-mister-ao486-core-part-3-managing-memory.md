---
layout: post
title: "MiSTer AO486 Core Part 3 – Managing Memory"
date: '2021-03-13 11:57:00:00'
summary: Configuring the MiSTer ao486 core to use Extended/Expanded memory ...
image: mister-ao486-emm386-expanded-extended-conventional-memory-choice.png
tags: [How To, MiSTer FPGA, MS-DOS, Posts, Retrocomputing, Retrogaming, Single-Board Computing]
---

You've [installed DOS]({% post_url 2021-02-06-mister-ao486-core-part-1-dos-quick-start %}) and [MiSTerFS]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}). Next we need to look at memory management.

Some DOS games require <a href="https://en.wikipedia.org/wiki/Extended_memory" target="_blank">Extended Memory</a> to be configured. Some take advantage of <a href="https://en.m.wikipedia.org/wiki/Expanded_memory" target="_blank">Expanded Memory (EMS)</a> and some only need the original 640kB of DOS <a href="https://en.wikipedia.org/wiki/Conventional_memory" target="_blank">Conventional Memory</a>. Others still do their own memory management.

There's no "one size fits all" – DOS needs to be configured differently for different software. Here's how.


### Update CONFIG.SYS

**Quick setup (if you have [MiSTerFS installed]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}))**

Copy/Paste the code below and save it as <code>CONFIG.SYS</code>. Use [MiSTerFS]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %}) to transfer it to ao486 and copy to <code>C:\CONFIG.SYS</code> (overwrite the existing file with this new one). Reboot ao486.

**Without MiSTerFS**:

Type <code>edit c:\config.sys</code>. An editor application will open. Update <code>config.sys</code> to the following:

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

[E]
DEVICE=C:\DOS\HIMEM.SYS /TESTMEM:OFF
DOS=HIGH,UMB
DEVICE=C:\DOS\EMM386.EXE RAM 8192 FRAME=D000 D=256 I=C800-CDFF X=CE00-CFFF I=D000-EFFF

[C]
````

Hit *Alt+F,S* to save the file, then *Alt+F,X* to exit the editor. Reboot ao486.


### A Note on Included/Excluded Memory Ranges

You might have noticed the <code>I=</code> ("Include") and <code>X=</code> ("Exclude") parameters above. These are used tell EMM386 which memory segements it can/can't use for Extended/Expanded memory.

The ao486 core reserves memory segments between <code>CE00</code> and <code>CFFF</code> for system features (including [MiSTerFS]({% post_url 2021-02-14-mister-ao486-core-part-2-transferring-files-with-misterfs %})). The code above prevents EMM386 from using segments in this range – otherwise the system may hang/crash.


### Making a Memory Choice

When DOS starts again, you'll have a choice of memory configurations:

![](/img/posts/mister-ao486-emm386-expanded-extended-conventional-memory-choice.png)

For most software and games, the default option 1 (<code>Extended memory</code>) will work. This is also a good choice for booting windows.

Some games (e.g. Wing Commander 1 and 2) make use of Expanded memory. Use option 2.

Lastly, some games (e.g. Ultima VII) use their own memory manager and won't work with either Expanded or Extended memory. For these use option 3.


### Next Posts

* [MiSTer AO486 Core Part 4 – Sound and Music Setup]({% post_url 2021-03-13-mister-ao486-core-part-4-sound-blaster-and-adlib-opl2-opl3-music %})
* [MiSTer AO486 Core Part 5 – Adding CD-ROM Support]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %})
* [MiSTer AO486 Core Part 6 – Mouse Support]({% post_url 2021-03-13-mister-ao486-core-part-6-mouse-support %})


### Other Posts in this Series

{% include mister-fpga-series.md %}

