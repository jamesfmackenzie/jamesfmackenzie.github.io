---
layout: post
title: "How To Install SBEMU on a Bootable USB Stick"
date: '2023-03-22 16:08:00:00'
summary: SBEMU allows you to play DOS games, with sound effects and FM audio <i>natively on modern hardware</i> – no Sound Blaster required!<br /><br />Here's how to get started.
image: duke-nukem-3d-running-on-sound-blaster-sbemu-4.jpg
tags: [DOS, PC, SBEMU, Sound]
---

SBEMU is an awesome new DOS program that emulates a Sound Blaster card.

It allows you to play DOS games, with sound effects and FM audio *natively on modern hardware* – no Sound Blaster required!

It's a true breakthrough for DOS gaming. Here's how to get started.

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/rg-ci97DDow?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div> 


### What you need

* USB stick
* <a href="https://rufus.ie/en/" target="_blank">Rufus</a>
* <a href="https://github.com/crazii/SBEMU/releases" target="_blank">SBEMU</a>
 

### Does SBEMU work on all PCs?

SBEMU works on a good variety of modern hardware. The supported sound cards:

* <a href="https://en.wikipedia.org/wiki/I/O_Controller_Hub" target="_blank">Intel ICH southbridge</a>
* <a href="https://en.wikipedia.org/wiki/List_of_VIA_chipsets" target="_blank">VIA VT82C686 or VT8233 southbrige</a>
* <a href="https://en.wikipedia.org/wiki/NForce" target="_blank">nForce chipsets</a>
* <a href="https://en.wikipedia.org/wiki/Intel_High_Definition_Audio" target="_blank">Intel High Definition Autio (HDA)</a>
* <a href="https://en.wikipedia.org/wiki/Sound_Blaster_Live!" target="_blank">Sound Blaster Live</a> or <a href="https://en.wikipedia.org/wiki/Sound_Blaster_Audigy" target="_blank">Audigy</a>


### Step 1 – Download and run Rufus

First download and run <a href="https://rufus.ie/en/" target="_blank">Rufus</a>. This utility helps create bootable USB flash drives.

Use Rufus to prepare the drive, make sure to select the FreeDOS option:

![](/img/posts/rufus-create-bootable-usb-stick-drive-with-freedos-dos.png)

When you're ready click START to create a bootable FreeDOS drive.



### Step 2 – Download and extract SBEMU

Download SBEMU from the <a href="https://github.com/crazii/SBEMU/releases" target="_blank">GitHub Releases page</a>.

Extract and copy the files to your bootable USB stick:

![](/img/posts/extra-copy-sbemu-files-to-bootable-freedos-usb-drive-stick.jpg)



### Step 3 – Create CONFIG.SYS

Create a new text file and add the following 2 lines:

{% highlight bash %}
{% raw %}
DOS=HIGH
DEVICE=jemmex.exe
{% endraw %}
{% endhighlight %}

Save it in the root of your USB stick as CONFIG.SYS. 


### Step 4 – Edit AUTOEXEC.BAT

Next, find AUTOEXEC.BAT in the root of your USB stick. Open in a text editor and add the following lines:

{% highlight bash %}
{% raw %}
jload qpiemu.dll
hdpmi32i -r -x
sbemu
{% endraw %}
{% endhighlight %}

Once saved, the full file should look like this:

![](/img/posts/sbemu-autoexec-bat-file.png)


### Step 5 – Copy DOS Games

Next, copy any software you want to the USB stick. These will be available when you start FreeDOS. I went with some shareware classics and demos:

![](/img/posts/dos-classic-video-games-for-freedos-and-sbemu.png)


### Step 6 – Boot FreeDOS

The USB stick is now ready! When you boot from it, you should see:

![](/img/posts/freedos-sbemu-first-boot.png)

This indicates a succesful boot.

Make a note of the Sound Blaster settings. I have:

* Port/Address: 220
* IRQ: 7
* DMA: 1


### Step 7 – Play Games!

Now we're ready to go! Configure some games and get ready to be Sound Blasted!

![](/img/posts/duke-nukem-3d-running-on-sound-blaster-sbemu-1.jpg)

![](/img/posts/duke-nukem-3d-running-on-sound-blaster-sbemu-2.png)

![](/img/posts/duke-nukem-3d-running-on-sound-blaster-sbemu-3.jpg)

![](/img/posts/duke-nukem-3d-running-on-sound-blaster-sbemu-4.jpg)


