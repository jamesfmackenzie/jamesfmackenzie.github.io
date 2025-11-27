---
layout: post
title: "MiSTer AO486 Core Part 9 – Installing Windows 95"
date: '2021-03-28 15:12:00:00'
summary: You've installed DOS on ao486, but what about Windows 95? Find out how ...
image: mister-ao486-welcome-to-windows-95.png
tags: [Emulation, MiSTer FPGA]
---

You've [installed DOS on ao486]({% post_url 2021-02-06-mister-ao486-core-part-1-dos-quick-start %}), but what about <a href="https://en.wikipedia.org/wiki/Windows_95" target="_blank">Windows 95</a>? Here's how to do it.


### Step 1 – Download and Copy Install Media

Download, extract and [copy]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}) the following floppy disk images to <code>/media/fat/games/AO486</code> on your MiSTer:

* <a href="https://winworldpc.com/download/db57f85a-f039-11e7-a562-fa163e9022f0" target="_blank">Windows 95 OSR2 Boot Disk</a>
* <a href="https://winworldpc.com/download/411cc38b-1518-c39a-11c3-a4e284a2c3a5" target="_blank">Windows 95 OSR2.1 Install CD</a>

Once you're done, you should have:

* <code>disk01.img</code> – Windows 95 Boot disk
* <code>win95_full_ar.osr2_en.iso</code> – Windows 95 Install CD

![](/img/posts/mister-ao486-windows-95-install-media-cd-boot-floppy.png)


### Step 2 – Copy Boot ROMs

Next you need to install the ao486 <a href="https://en.wikipedia.org/wiki/BIOS" target="_blank">BIOS</a>:

1. Visit <a href="https://github.com/MiSTer-devel/ao486_MiSTer/tree/master/releases/bios" target="_blank">this Releases page</a> on GitHub

2. Download and [copy]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}) boot0.rom and boot1.rom to <code>/media/fat/games/AO486</code> on your MiSTer:

![](/img/posts/mister-ao486-file-copy-transfer-boot-roms.png)


### Step 3 – Create Hard Disk

1. <a href="https://en.wikipedia.org/wiki/Secure_Shell_Protocol" target="_blank">SSH</a> into your MiSTer and navigate to <code>/media/fat/games/AO486</code> (see "Shell Access" on [this page]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}) to learn how)

2. Invoke the following command to create a 2GB file (*Win95.vhd*) filled with zeros. We'll use this for our primary hard disk:

````
dd if=/dev/zero of=Win95.vhd bs=1M count=2048
````

![](/img/posts/mister-ao486-windows-95-hard-disk-image-vhd.png)


### Step 4 – Partition Hard Disk

Next we need to partition the hard disk. On the MiSTer:

1. Press *F12* to bring up the MiSTer main menu. Browse to *Computer -> ao486* to start the ao486 core:
   
![](/img/posts/mister-start-ao486-core.png)

{:start="2"}
2. Hit *Windows Key* + *F12* for ao486 core options. Set *Floppy A:* to the Windows 95 <code>disk01.img</code>, *IDE 0-0* to <code>Win95.vhd</code> and *IDE 1-0* to <code>win95_full_ar.osr2_en.iso</code>:

![](/img/posts/mister-ao486-windows-95-mount-floppy-vhd-install-cd-rom.png)

{:start="3"}
3. Hit *Reset and apply HDD*. ao486 will reboot into the Windows 95 Startup Menu. Select option 5 ("No CDROM support") and hit *Enter*:

![](/img/posts/mister-ao486-windows-95-boot-disk-no-cd-rom-support.png)

{:start="4"}
4. Run <code>A:\FDISK.EXE</code> to launch the <a href="https://en.wikipedia.org/wiki/Disk_partitioning" target="_blank">disk partitioner</a>. Choose the following (default) options to partition the disk:

* <code>Y</code> to enable *large disk support*
* <code>1</code> to *Create DOS Partition or Logical Drive*
* <code>1</code> to *Create Primary DOS Partition*
* <code>Y</code> to use the *maximum available size* and *make the partition active*
* <code>Esc</code> to go back to the FDISK options menu
* <code>Esc</code> twice again to exit FDISK

<blockquote>Now reboot AO486 (<i>Windows Key</i> + <i>F12</i>, <i>Reset and apply HDD</i>).</blockquote>

![](/img/posts/mister-ao486-fdisk-partition-windows-95-hard-disk.png)


### Step 5 – Format Hard Disk

Next we need to format the hard disk:

1. ao486 will boot into the Windows 95 Startup Menu again. This time select option 1 ("Load NEC IDE CDROM driver"):

![](/img/posts/mister-ao486-windows-95-boot-disk-nec-ide-cdrom-cd-rom-driver.png)

{:start="2"}
2. Type <code>format c: /s</code> to format the hard disk, <code>Y</code> to *Proceed with Format*:

![](/img/posts/mister-ao486-format-windows-95-hard-disk.png)

<blockquote>Enter a <i>Volume label</i> (your choice) to finalize the format process.</blockquote>

<!--
{:start="3"}
3. Now we need to format the storage disk. This time type <code>format d:</code>, <code>Y</code> to *Proceed with Format*:

![](/img/posts/mister-ao486-format-windows-95-hard-disk.png)

<blockquote>Again enter a <code>Volume label</code> of your choice.</blockquote>
-->


### Step 5 – Install Windows 95

Run <code>D:\SETUP.EXE</code> to launch Windows 95 setup. Follow all the defaults to install Windows 95:

![](/img/posts/mister-ao486-windows-95-setup-exe.png)

As the Windows 95 install finalizes, you'll be prompted to remove the floppy disk. <strong>Don't do this!</strong>

Instead, keep the disk in and reboot ao486 (*Windows Key* + *F12*, <code>Reset and apply HDD</code>).

![](/img/posts/mister-ao486-windows-95-finishing-setup.png)


### Step 5 – Disable Hard Disk Driver

Due to a compatibility issue between AO486 and the Windows 95 disk driver, we need to (temporarily) disable it. Here's how: 

1. When ao486 reboots to the Windows 95 Startup Menu, select option 5 ("No CDROM support")

2. Type the following at the command prompt:

````
c:
cd WINDOWS\SYSTEM\IOSUBSYS
ren ESDI_506.PDR ESDI_506.BAK
````

![](/img/posts/mister-ao486-windows-95-rename-esdi-506-pdr-hard-disk-driver.png)

{:start="3"}
3. Unmount the floppy disk (*Windows Key* + *F12*, <code>Floppy A:</code>, *Enter*, *Backspace*)

4. Reboot ao486 (*Windows Key* + *F12*, <code>Reset and apply HDD</code>)


### Step 6 – Start Windows 95

Windows 95 will start for the first time. Follow the last few setup steps to set your username, password, timezone etc.

Once those are done, the Windows 95 desktop will load!

![](/img/posts/mister-ao486-welcome-to-windows-95.png)


### Step 7 – Re-enable Hard Disk Driver

To re-enable the Hard Disk Driver:

1. Navigate to <code>Start → Control Panel → System → Device Manager</code>. Remove the following 2 entries:

* <code>Standard IDE/ESDI Hard Disk Controller</code>
* <code>Standard IDE/ESDI Hard Disk Controller</code>

![](/img/posts/mister-ao486-windows-95-control-panel-device-manager-remove-hard-disk-controller.png)

{:start="2"}
2. Click *OK*, then navigate to <code>My Computer → C: → Windows → System → Iosubsys</code>. Rename <code>Esdi_506.bak</code> to <code>Esdi_506.pdr</code>:

![](/img/posts/mister-ao486-windows-95-rename-esdi-506-pdr-hard-disk-driver-windows.png)

{:start="3"}
3. Reboot Windows 95 (<code>Start → Shut Down → Restart the computer</code>)


### Wrap Up

That’s it! You now have a fully functional Windows 95 installation.

Next, you might consider adding [adding CD-ROM support]({% post_url 2021-03-13-mister-ao486-core-part-5-cd-rom-support %}).
 
 
### Other Posts in this Series
 
{% include mister-fpga-series.md %}






