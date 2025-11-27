---
layout: post
title: "How To Install Windows XP from USB Flash Drive with Win​Setup​From​USB"
date: '2022-09-17 18:10:00:00'
summary: How can you install Windows XP with no CD drive? Here's how ...
image: windows-xp-wallpaper-bliss.jpg
tags: [PC, Windows XP]
---

How can you install Windows XP on a retro system with no CD drive?

WinSetupFromUSB is a super useful tool that can prepare a USB flash drive to install any Windows versions since 2000/XP. Here's how to use it!

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/bMq0KfjOCpc?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div> 


### What you need

* 8GB (or larger) USB stick
* <a href="https://1drv.ms/f/s!Aqzdh9DilDnHhotsH2VDY5A9ZqwmrA" target="_blank">WinSetupFromUSB</a>
* Windows XP ISO 


### Step 1 - Format USB stick

First, insert the USB stick on a modern PC and format as NTFS.

![](/img/posts/usb-stick-flash-drive-formatted-ntfs.png)


### Step 2 - Extract Windows XP ISO

Using an archival tool like <a href="https://www.7-zip.org/" target="_blank">7-Zip</a>, extract your Windows XP ISO to a folder. 

![](/img/posts/extract-windows-xp-iso-using-7zip.png)


### Step 3 - Download and extract WinSetupFromUSB

Download and extract <a href="http://www.winsetupfromusb.com/downloads/" target="_blank">WinSetupFromUSB</a>. 

When the extract completes, run <code>WinSetupFromUSB_1-10_x64.exe</code>:

![](/img/posts/launch-winsetupfromusb-x64.png)


### Step 4 - Prepare USB install media

WinSetupFromUSB should auto detect your flash drive. If not, select it from the drop down menu under *USB disk selection and format tools*.

Under *Add to USB disk*, find *Windows 2000/XP/2003 Setup*. Check the checkbox and identify the Windows XP source folder from Step 2 above.

Accept the Microsoft EULA and click *GO* to create the bootable USB stick.

![](/img/posts/create-bootable-windows-xp-install-media-with-winsetupfromusb-win-setup-from-usb.png)


### Step 5 - Verify files

Once the install completes, verify the USB stick is readable with the following files in place:

![](/img/posts/verify-windows-xp-winsetupfromusb-stick-and-copy-drivers.png)

Also copy any *extra* files you want onto the USB stick (drivers/utilities/games etc). They will be available in Windows XP when the install completes.

Now you're ready to install Windows XP! Eject the USB stick and move to your retro PC.


### Step 6 - Boot from USB stick, install Windows XP

Insert the WinSetupFromUSB stick and power on your retro PC. The system will recognize the USB drive and load the WinSetupFromUSB menu system.

From the menu, select *Windows XP/2003/2003 Setup*:

![](/img/posts/windows-xp-2000-2003-setup-winsetupfromusb-win-setup-from-usb.png)

The Windows XP install has two phases:

1. Text mode install (for disk preparation, copying installation files etc)
2. Graphics mode setup (for OS install, configuration etc)

Select *First part of Windows XP Professional SP3 setup* to start the first phase.

![](/img/posts/windows-xp-text-mode-install-1.png)


### Step 7 - Prepare disks, copy install files

Windows will boot into the text mode installation menu.

Follow the on-screen prompts to partition/format your hard disk and copy Windows installation files.

![](/img/posts/windows-xp-text-mode-install-2.png)


### Step 8 - Configure Windows XP

After some time, your PC will reboot to the WinSetupFromUSB menu. This time, select *Second part of Windows XP Professional setup* to start the graphics mode setup:

![](/img/posts/windows-xp-graphics-mode-install.png)

Follow the on-screen prompts to configure Windows. The default options are suitable for most installations.

![](/img/posts/windows-xp-graphics-mode-setup-and-configuration.png)


### Setup 9 - Boot Windows XP

After one last reboot, Windows XP will load for the first time. This is your opportunity to install any necessary drivers and start using Windows XP.

Enjoy!

![](/img/posts/windows-xp-wallpaper-bliss.jpg)


### More Windows articles

{% include windows.md %}

