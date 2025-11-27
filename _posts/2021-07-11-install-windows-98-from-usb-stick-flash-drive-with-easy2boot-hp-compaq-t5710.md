---
layout: post
title: "HP Compaq t5710 – How To Install Windows 98 from USB Flash Drive with Easy2Boot"
date: '2021-07-11 12:22:00:00'
summary: The HP Compaq t5710 makes a great DOS and Windows 98 retro gaming machine. But how can you install Windows 98 with no CD drive? Here's how ...
image: t5000-t5710-windows-98-install-windows-98-install-2.png
tags: [How To, MS-DOS, Posts, Retrocomputing, Retrogaming, t5710, Windows 98]
---

The HP Compaq t5710 [makes a great DOS and Windows 98 retro gaming machine]({% post_url 2021-07-11-hp-compaq-t5710-review-great-for-dos-and-windows-98-gaming %}). But how can you install Windows 98 on a system with no CD drive? Can you install from USB? Here's how to do it.

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/GioiRupslkU?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div> 


### What you need

* 32GB (or larger) USB stick
* HP Compaq t5710 thin client
* <a href="https://easy2boot.xyz/download/" target="_blank">Easy2Boot</a>
* Windows 98 SE install media – <a href="https://winworldpc.com/product/windows-98/98-second-edition" target="_blank">ISO</a> and <a href="https://winworldpc.com/product/microsoft-windows-boot-disk/98-se" target="_blank">boot floppy</a>
* Windows 98 <a href="https://mega.nz/file/LgYDhKDA#7upam9AIguSzKWAvV_ENg7_SnWvWNCpYYwAnF94eUpU" target="_blank">driver package</a>
* Recommended utilities – <a href="https://www.7-zip.org/download.html" target="_blank">7-zip 9.20</a>, <a href="http://falconfly.3dfx.pl/directx.htm" target="_blank">DirectX 7.0a</a>, <a href="https://sourceforge.net/projects/winscp/files/WinSCP/4.3.9/" target="_blank">WinSCP 4.39</a> 

These instructions will also work for other driveless PCs (e.g. HP t5000 Series thin clients) with some minor adjustments.


### Step 1 - Download and install Easy2Boot

First download and install <a href="https://easy2boot.xyz/download/" target="_blank">Easy2Boot</a>. This is a super useful tool that can prepare a USB flash drive to boot almost any floppy or CD image - even when you don't actually have a physical floppy or CD drive on your system. Perfect for our thin client build.

Easy2Boot likes to work with contigious (not fragmented) files - this is why we want a 32GB or larger USB drive. With smaller drives, our images might get fragmented and we might run into weird install or boot issues.

When the install completes, the <code>Make_E2B</code> utility will launch. Just ignore and close this. Instead, open the install folder and find <code>MAKE_E2B_USB_DRIVE.cmd</code>. Run this batch script as Administrator:

![](/img/posts/easy2boot-make_e2b_usb_drive.png)


### Step 2 - Prepare USB install media

In the command window, select your target USB drive (in my case this is <code>5</code> - ADATA USB Flash Drive). Then hit <code>Y</code> to format the drive and <code>0</code> to set the default partition options. You'll get one last warning. Hit <code>OK</code> to start the partition and format process.

![](/img/posts/easy2boot-make-usb-drive-selection.png)

Once the format is done, repeatedly hit Enter to accept the default options (we don't need to do anything special here). When the process is complete the command window will turn green. Just hit Enter to close:

![](/img/posts/easy2boot-usb-preparation-complete.png)

With the USB stick prepared, you should have two partitions:

![](/img/posts/easy2boot-usb-e2b-e2b_ptn2-partitions.png)

1. <code>E2B</code> aka "Easy2Boot" partition. Any ISOs or images you copy in here will be bootable via the Easy2Boot menu system
2. <code>E2B_PTN2</code> aka "Easy2Boot data partition". Any files you copy here will be mounted on the host operating system when we launch via Easy2Boot


### Step 3 - Copy Windows install files

We'll plan to install Windows 98 from hard drive. This will make the install much faster and it's also super useful to have the install files on our hard drive so we don't have to keep mounting the Windows 98 CD in future.

First, download the <a href="https://winworldpc.com/product/windows-98/98-second-edition" target="_blank">Windows 98 SE ISO</a>. Double-click to mount it as a new drive.

Copy the win98 folder over to the Easy2Boot data partition (<code>E2B_PTN2</code>):

![](/img/posts/easy2boot-copy-windows98-install-iso-setup-files.png)

Next we need boot media. Download the <a href="https://winworldpc.com/product/microsoft-windows-boot-disk/98-se" target="_blank">Windows 98 boot floppy</a> and copy it to the <code>\_ISO\WIN</code> folder on your Easy2Boot (<code>E2B</code>) partition:

![](/img/posts/easy2boot-copy-windows98-boot-floppy-disk-image.png)

Once the copy is done, we need to change the file extension. Rename the file, and change the extension to <code>imgfdhd01</code>. This tells Easy2Boot that this is a floppy image, and to mount the thin client internal drive as drive C - which is what we need for Windows 98 install:

![](/img/posts/easy2boot-rename-windows98-boot-floppy-disk-image.png)


### Step 4 - Copy drivers and utilities

Lastly, download and copy the <a href="https://mega.nz/file/LgYDhKDA#7upam9AIguSzKWAvV_ENg7_SnWvWNCpYYwAnF94eUpU" target="_blank">Windows 98 driver package</a> to the Easy2Boot data partition (<code>E2B_PTN2</code>). This contains the chipset, graphics and audio drivers for our thin client hardware:

![](/img/posts/easy2boot-copy-drivers.png)

You'll also need a zip utility to extract the drivers. I recommend <a href="https://www.7-zip.org/download.html" target="_blank">7-zip 9.20</a>. <a href="http://falconfly.3dfx.pl/directx.htm" target="_blank">DirectX 7.0a</a> and <a href="https://sourceforge.net/projects/winscp/files/WinSCP/4.3.9/" target="_blank">WinSCP 4.39</a> (an FTP client) are also useful. Copy them all to the Easy2Boot data partition:

![](/img/posts/easy2boot-copy-utils-utilities.png)

That's our USB setup done. Remove the USB stick and switch over to the thin client.


### Step 5 - Partition thin client internal hard disk

Next we need to prepare the thin client internal hard drive for Windows 98 install. Insert the Easy2Boot USB stick and power on the thin client. The system will recognize the USB drive and load the Easy2Boot menu system.

From the menu, select <code>Windows Boot</code> - this will load the Windows boot menu - and then select <code>Windows 98 Second Edition Boot</code>. This will boot from our Windows 98 floppy image:

![](/img/posts/easy2boot-windows-boot-menu.png)

On succesful boot, you should be at the DOS with the Windows 98 floppy image mounted as <code>A:</code>. Type <code>fdisk</code> to launch the Microsoft Fixed Disk Partition Tool:

![](/img/posts/t5000-t5710-windows-98-install-fdisk.png)

This is not a guide on how to use FDISK (there are plenty of others out there). Also the steps required here will vary depending on your hardware and disk setup. For my build, I did the following:

1. <code>Y</code> to enable FAT32 support
2. <code>3</code> to delete partitions and then <code>1</code> to delete the Primary DOS partition
3. <code>1</code> to create a new partition, and then <code>1</code> again to create a Primary DOS partition
4. <code>Y</code> to use the maximum available parition size
5. <code>2</code> to activate our new partition</code>
6. Hit <code>Esc</code> a few times to exit

Once you've made partition changes, restart the system and boot from the Windows 98 floppy again:

![](/img/posts/t5000-t5710-windows-98-install-fdisk-restart.png)


### Step 6 - Format thin client internal hard disk

Back at the DOS prompt. Before we install Windows 98, we need to format the internal hard disk. Type <code>format c:</code> and then <code>Y</code> to start the format process:

![](/img/posts/t5000-t5710-windows-98-install-format-internal-hard-drive-disk.png)


### Step 7 - Copy Windows install files, drivers and utilities to hard disk

With the format complete, it's time to copy the Windows 98 install files (from Step 3 above) and drivers/utilities (from Step 4) to the thin client internal hard disk. You'll find them mounted and available on drive <code>D:</code>:

![](/img/posts/t5000-t5710-windows-98-install-show-easy2boot-mounted-file-system.png)

Use the DOS <code>copy</code> command to bring them across to drive <code>C:</code>

```
md C:\WIN98
copy D:\WIN98\*.* C:\WIN98

md C:\DRIVERS
copy D:\DRIVERS\*.* C:\DRIVERS

md C:\UTILS
copy D:\UTILS\*.* C:\UTILS
```

![](/img/posts/t5000-t5710-windows-98-install-copy-windows-98-install-setup-files.png)

With everything safely on our internal hard disk, we're ready to start the Windows 98 install process.


### Step 8 - Install Windows 98

Run <code>C:\WIN98\SETUP.EXE</code> to launch Windows 98 setup. Follow all the defaults to install Windows 98:

![](/img/posts/t5000-t5710-windows-98-install-windows-98-install-1.png)

![](/img/posts/t5000-t5710-windows-98-install-windows-98-install-2.png)


### Step 9 - Install 7-Zip

When Windows 98 loads, first install 7-Zip. We need this to extract the drivers. Double click to install:

![](/img/posts/t5000-t5710-windows-98-install-windows-98-install-7zip-7-zip.png)


### Step 10 - Install drivers

![](/img/posts/t5000-t5710-windows-98-install-windows-98-install-drivers.png)

With 7-Zip installed, extract and then install drivers in the following order. The sequencing is important here. If you do this out of order, it won't work:

1. IDE Hotfix (<code>IDE Hotfix - q245682.exe</code>). This is required to make the thin client IDE controller work correctly in Windows 98
2. Chipset drivers (<code>Chipset - 4in1435v\Setup.exe</code>)

With these two installed, you can install the following in any order:

* GPU drivers (<code>GPU - 6-2_wme_dd_cp_30314.exe</code>)
* Audio drivers (<code>Audio - vinyl_v700b\SETUP.EXE</code>)
* Network drivers (<code>Network - via_rhine_ndis5_v384a\​WinSetup.exe</code>)

You'll need to reboot after each driver install - it'll take a while. But once complete you'll have a fully working Windows 98 install. Enjoy!


### More t5710 articles

{% include t5710.md %}

