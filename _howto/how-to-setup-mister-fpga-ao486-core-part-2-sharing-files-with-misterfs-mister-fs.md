---
layout: post
title: "MiSTer AO486 Core Part 2 – Sharing Files With MiSTerFS"
date: '2021-02-14 22:55:00:00'
summary: Sharing files with MiSTerFS ...
tags: [DOS, Emulation, MiSTer FPGA, MiSTer FPGA Cores]
---

You have the [ao486 core setup and DOS installed]({% post_url 2021-02-06-mister-ao486-core-part-1-dos-quick-start %}), but what’s next?

One super-convenient ao486 feature is MiSTerFS – a file transfer solution that allows you to share files directly into ao486's DOS file system. Traditionally you'd use <a href="https://en.wikipedia.org/wiki/Disk_image" target="_blank">mounted disk images</a> to transfer files, but with MiSTerFS it's just drag and drop! Way easier. Here's how to get started.


### Step 1 – Download and Install MiSTerFS

To install MiSTerFS:

1. Download <a href="https://misterfpga.org/download/file.php?id=676" target="_blank">this MiSTerFS floppy image</a> (hosted on <a href="https://misterfpga.org/" target="_blank">MiSTer Forum</a>) and extract it

2. Use a file transfer tool like FileZilla to copy the floppy image to <code>/media/fat/games/AO486</code> on your MiSTer (reminder on how to do that [here]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %})). You should have a single file name <code>misterfs.img</code>:

![](/img/posts/mister-ao486-misterfs-floppy-image.png)

{:start="3"}
3. Still in FileZilla, create a new folder: <code>/media/fat/games/AO486/shared</code> (if it doesn't exist already). This is the "drop" folder you'll use to transfer files to ao486:

![](/img/posts/mister-ao486-misterfs-create-shared-folder-using-filezilla.png)

{:start="4"}
4. Power up the ao486 core and mount the MiSTerFS floppy image (*Windows Key* + *F12* for ao486 core options, set *Floppy A:* to <code>misterfs.img</code>)

![](/img/posts/mister-ao486-mount-misterfs-floppy-image-in-ao486.png)

{:start="5"}
5. Run the following commands to copy the MiSTerFS executable to your hard disk:

```
md c:\utils
md c:\utils\misterfs
copy a:\misterfs.exe c:\utils\misterfs
```

![](/img/posts/mister-ao486-copy-misterfs-files-to-ao486-dos.png)

{:start="5"}
6. Still on your MiSTer, type <code>edit c:\autoexec.bat</code>. An editor application will open. Add the following line:

```
LH C:\UTILS\MISTERFS\MISTERFS.EXE E /Q
```

<blockquote>This quiet-loads MiSTerFS into upper memory with drive letter <code>E:</code>. Hit <i>Alt+F,S</i> to save the file and then <i>Alt+F,X</i> to exit</blockquote>

That's the setup done. Unmount <code>misterfs.img</code>, reboot the ao486 core and get ready to transfer files! 


### A Note on Memory Managers

If you're using a DOS Memory Manager like <a href="https://en.wikipedia.org/wiki/EMM386" target="_blank">EMM386</a> or <a href="https://en.wikipedia.org/wiki/QEMM" target="_blank">QEMM</a>, there are some extra steps you need to take.

The ao486 core reserves memory segments between <code>CE00</code> and <code>CFFF</code> for MiSTerFS and other system features. If you don't protect this memory range, the system may hang or crash. 

See [MiSTer AO486 Core Part 3 – Managing Memory]({% post_url 2021-03-13-mister-ao486-core-part-3-managing-memory %}) to learn more.


### Step 2 – Using MiSTerFS

File transfer between PC and ao486 works in both directions. To copy files from PC to ao486:

1. Open a file transfer tool (e.g. FileZilla) on your PC

2. Navigate to <code>/media/fat/games/AO486</code>

3. Drag-and-drop files into the <code>shared</code> folder. Filenames must fit the <a href="https://en.wikipedia.org/wiki/8.3_filename" target="_blank">8.3 filename standard</a>

![](/img/posts/mister-ao486-misterfs-copy-files-to-shared-folder-using-filezilla.png)

{:start="4"}
4. In ao486, verify that the files appear under the <code>E:</code> drive:

![](/img/posts/mister-ao486-misterfs-files-copied-to-dos-using-filezilla.png)

To transfer files from ao486 to PC, simply do the reverse.

That's it for MiSTerFS. You'll come to rely on this a lot for file transfer.


### Next Post

* [MiSTer AO486 Core Part 3 – Managing Memory]({% post_url 2021-03-13-mister-ao486-core-part-3-managing-memory %})


### Other Posts in this Series

{% include mister-fpga-series.md %}

