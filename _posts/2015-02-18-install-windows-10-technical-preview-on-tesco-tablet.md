---
layout: post
title: Install Windows 10 on a £99 Tesco Tablet
date: '2015-02-18 16:53:30'
tags: [Windows 10, How To, Tech]
permalink: /install-windows-10-technical-preview-on-tesco-tablet/
---

### Article updated 2015-08-01 to reflect Windows 10 retail launch

### Introduction

I spotted <a href="http://www.tesco.com/direct/connect-7-tablet-with-windows-81-office-365-personal-32gb-wifi-black/182-3108.prd" target="_blank">this amazingly cheap Windows 8.1 tablet</a> on a recent Tesco grocery trip. At £99, I've no idea how they turn a profit, but with the recent launch of <del><a href="http://arstechnica.com/information-technology/2015/01/new-windows-10-preview-comes-to-pc-next-week-to-phones-in-february/" target="_blank">Windows 10 Technical Preview</a></del> <a href="http://blogs.windows.com/launch/" target="_blank">Windows 10</a>, I thought it'd make a nice experiment. 

### What you need

* USB keyboard
* USB memory stick (at least 8GB)
* USB splitter cable or hub (you'll need to plug in the memory stick and keyboard simultaneously)
* <a href="http://www.tesco.com/direct/connect-7-tablet-with-windows-81-office-365-personal-32gb-wifi-black/182-3108.prd" target="_blank">Tesco Connect 7" Tablet with Windows 8.1</a> (only £99)

### Step 1. Download the Windows 10 ISO

Head on over to the <a href="https://www.microsoft.com/en-us/software-download/windows10" target="_blank">Windows 10 Download Page</a> or <a href="https://msdn.microsoft.com/en-us/default.aspx" target="_blank">MSDN</a> to download the ISO. Make sure you download the 32-bit/x86 flavour - the Tesco tablet doesn't support 64-bit/x64.

### Step 2. Prepare a Windows 10 UEFI bootable using Rufus

To install Windows 10, you'll need to prepare a bootable USB stick. There's already a nice guide over <a href="http://www.intowindows.com/create-uefi-bootable-usb-of-windows-10/" target="_blank">here</a>. Make sure to create the UEFI bootable - it's the only method that'll work on the Tesco device.

![](/img/posts/2015-01-24-12_22_20-Mail.png)

### Step 3. Copy network and touchscreen drivers onto the USB stick

Windows 10 doesn't ship with the network, sound and touchscreen drivers you'll need.

<strong style="color: red;">Before you do anything:</strong>

1. Boot the tablet into Windows 8.1
2. Mount the USB stick 
3. Copy <code>C:\Windows\System32\DriverStore</code> across. It contains all the drivers you'll need

### Step 4. Boot to EFI Shell

Before you start, make sure both the USB memory stick and USB keyboard are connected.

From Windows 8.1 Desktop, swipe from the right to open the Charms Bar, then hit "Settings":

![](/img/posts/2015-01-24-13_00_18-Greenshot.png)

From the Settings panel, hit "Change PC settings":

![](/img/posts/2015-01-24-13_00_51-Greenshot-2.png)

Inside PC settings, click "Update and recovery":

![](/img/posts/2015-01-24-13_01_03-Greenshot.png)

Under "Advanced start-up" hit "Restart now":

![](/img/posts/2015-01-24-13_01_29-Greenshot.png)

### Step 5. Start Windows 10 install

Once inside the EFI Shell, select "Use a device":

![](/img/posts/File-18-02-2015-21-04-40.jpeg)

Choose "UEFI: Removable Device". After a short delay, the Windows 10 installation will begin.

![](/img/posts/File-18-02-2015-21-05-11.jpeg)

### Step 6. Follow Windows 10 installation steps

From here on in, the touchscreen won't work. You'll need to use your attached keyboard (and optionally, a mouse) for all input.

On the first screen, set your Language and Keyboard Preferences. The values don't matter.

![](/img/posts/File-18-02-2015-21-06-43.jpeg)

<strong>You're nearly at the point of no return! If you follow the next step, you won't be able to restore your original Windows 8.1 installation without performing an OS restore from installation media</strong>.

To continue, you'll need to delete all existing partitions. Select each partition in turn and hit Delete.

Once you're done deleting partitions, you'll have 29.1GB of unallocated space:

![](/img/posts/File-18-02-2015-21-08-17.jpeg)

Highlight the unallocated space and hit "New". Assign all available space to the partition (29,823MB) and hit "Apply":

![](/img/posts/File-18-02-2015-21-12-11.jpeg)

The Windows 10 installer will actually create *four* new partitions. Highlight the largest one (Partition 4) and hit "Next". The Windows 10 installation will begin.

![](/img/posts/File-18-02-2015-21-13-24.jpeg)

![](/img/posts/File-18-02-2015-21-15-21.jpeg)

After 15 minutes or-so, you'll see the screen below. You can choose custom options if you like, but I chose to "Use express settings".

![](/img/posts/File-18-02-2015-21-17-47.jpeg)

Not long after, the installer will deliver you to the Windows 10 Start screen. Nice!

![](/img/posts/Untitled.png)

### Step 7. Install drivers

You'll notice pretty quickly that sound, networking and the touchscreen don't work. To fix this, head inside the Control Panel. Find "System and Security" and click the "Device Manager" icon:

![](/img/posts/Untitled2-2.png)

Where Windows doesn't have the right drivers, you'll find a bunch of erroring devices, indicated by exclamation points:

![](/img/posts/Untitled4-2.png)

For each of these erroring devices, follow these same steps:

* Right-click on the device, select "Properties" and then "Update Driver":

![](/img/posts/Untitled3-1.png)

* When asked "How do you want to search for driver software?", select "Browse my computer for driver software":

![](/img/posts/Untitled7-1.png)

* Choose "Search for driver software in this location" and specificy the backup driver location you created in Step 3 (hint: it'll be on your USB memory stick). Check "Include subfolders" and click "Next".

![](/img/posts/Untitled8-1.png)

* Windows will whirr away for a while and install your missing driver.

Repeat the above process for all the erroring devices. Don't forget "System devices" - there are a bunch in there too.

**That's it! You now have a fully working Windows 10 tablet! Enjoy!**

![](/img/posts/Untitled.png)