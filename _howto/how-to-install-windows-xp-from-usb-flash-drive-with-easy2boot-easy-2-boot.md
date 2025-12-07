---
layout: post
title: "How To Install Windows XP from USB Flash Drive with Easy2Boot"
date: '2023-01-08 10:17:00:00'
summary: How can you install Windows XP with no CD drive?
image: windows-xp-wallpaper-bliss.jpg
tags: [How To, PC, Retrocomputing, Windows XP]
---

Can you install Windows XP on a retro system with no CD drive?

Easy2Boot is super useful tool that can prepare a USB flash drive to install almost any version of Windows. Here's how to use it!

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/ozEF3McmWfM?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div> 


### What you need

* 16GB (or larger) USB stick
* <a href="https://easy2boot.xyz/download/" target="_blank">Easy2Boot</a>
* Windows XP SP3 ISO
 

### Step 1 - Download and extract Easy2Boot

First download and extract <a href="https://www.fosshub.com/Easy2Boot.html" target="_blank">Easy2Boot+DPMS</a>. This is a special version of Easy2Boot with the mass storage drivers required for Windows XP install:

![](/img/posts/download-easy2boot-dpms-for-windows-xp-install.jpg)

With the files extracted, run <code>MAKE_E2B_USB_DRIVE.cmd</code> as Administrator:

![](/img/posts/create-easy2boot-usb-stick.jpg)


### Step 2 - Prepare USB drive

In the command window, select your target USB drive (in this case it's <code>3 - 119.0GiB Generic STORAGE DEVICE</code>). Then hit <code>Y</code> to format the drive and <code>0</code> to set the default partition options. You’ll get one last warning. Hit <code>OK</code> to start the partition and format process:

![](/img/posts/windows-xp-easy2boot-usb-stick.jpg)

Once the format is done, repeatedly hit Enter to accept the default options (we don’t need to do anything special here). When the process is complete the command window will turn green. Just hit Enter to close:

![](/img/posts/windows-xp-easy2boot-usb-stick-ready.jpg)

With the USB stick prepared, you should have two partitions:

![](/img/posts/easy2boot-usb-e2b-e2b_ptn2-partitions.png)

1. <code>E2B</code> aka “Easy2Boot” partition. Any ISOs or images you copy in here will be bootable via the Easy2Boot menu system
2. <code>E2B_PTN2</code> aka “Easy2Boot Data” partition. A simple FAT partition, any files you copy here will be mounted on the host operating system when you boot via Easy2Boot


### Step 3 - Copy Windows XP ISO

Copy your Windows XP ISO over to the <code>\_ISO\WINDOWS\XP</code> folder on your Easy2Boot (<code>E2B</code>) partition:

![](/img/posts/copy-windows-xp-install-files-iso-easy2boot-usb-stick.jpg)


### Step 4 - Boot from USB stick, install Windows XP

Insert the Easy2Boot USB stick and power on your retro PC. The system will recognize the USB drive and load the Easy2Boot menu system.

The Windows XP install has two phases:

* Text mode install (for disk preparation, copying installation files etc)
* Graphics mode setup (for OS install, configuration etc)
 
Select *WINDOWS INSTALL Menu*, then *Install XP - Step 1* to start the first phase:

![](/img/posts/install-windows-xp-from-usb-stick-easy2boot-step-1.jpg)


### Step 5 - Prepare disks, copy install files

Windows will boot into the text mode installation menu.

Follow the on-screen prompts to partition/format your hard disk and copy Windows installation files.

![](/img/posts/windows-xp-text-mode-install-2.png)


### Step 6 - Configure Windows XP

After some time, your PC will reboot to the Easy2Boot menu. This time, select *Install XP - Step 2* to start the graphics mode setup:

![](/img/posts/install-windows-xp-from-usb-stick-easy2boot-step-2.jpg)

Follow the on-screen prompts to configure Windows. The default options are suitable for most installations.

![](/img/posts/windows-xp-graphics-mode-setup-and-configuration.png)


### Setup 7 - Boot Windows XP

After one last reboot, Windows XP will load for the first time. Enjoy!

![](/img/posts/windows-xp-wallpaper-bliss.jpg)


### More Windows articles

{% include windows.md %}

