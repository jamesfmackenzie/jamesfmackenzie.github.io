---
layout: post
title: "MiSTer FPGA Part 2 – Install and Setup"
date: '2020-09-20 09:25:00:00'
summary: How to install and configure your MiSTer to play the latest arcade, computer and game console cores ...
tags: [Retrocomputing, Retrogaming, FPGA, MiSTer, Single-Board Computing]
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/X77hmWYz9VM?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

Following on from the [hardware overview]({% post_url 2020-08-22-mister-fpga-introduction-and-hardware-overview %}), here's how to install and configure your MiSTer to play the latest arcade, computer and game console cores.


### What you'll need

Hardware:

* <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki/How-to-start-with-MiSTer#1-de10-nano-board" target="_blank">DE10-Nano Board</a> and power supply
* microSD card (at least 2GB) and reader
* USB keyboard – to navigate the MiSTer menus and configure the device
* <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki/How-to-start-with-MiSTer#2-usb-connection" target="_blank">USB "On-The-Go" (OTG) connector or hub</a> – to connect your keyboard and other peripherals
* Ethernet connection – to update the MiSTer and download cores
* HDMI Monitor/TV and HDMI cable

Software:

* <a href="https://github.com/MiSTer-devel/mr-fusion/releases" target="_blank">MiSTer SD card image</a> – you'll write this to the microSD card
* Software to write the SD card image – I recommend <a href="https://www.balena.io/etcher/" target="_blank">BalenaEtcher</a>


### Setup guide


#### Step 1. Flash the downloaded image onto microSD

Flash the downloaded image onto your microSD card. Follow the BalenaEtcher instructions <a href="https://www.balena.io/etcher/" target="_blank">here</a>. Make sure you pick the right drive!


#### Step 2. Put the microSD card into the DE10-Nano and power on

Put the microSD card into the DE10-Nano and power on. After a few seconds the orange LED on the board should light up. If you have a TV or monitor connected, you should see the installation splash screen:

![](/img/posts/mister-fpga-install.jpg)

The installer will automatically re-partition and resize your SD card and copy all the necessary MiSTer files onto it. Once complete the DE10-Nano will reboot and you'll be greeted with an (empty) MiSTer menu:

![](/img/posts/mister-fpga-install-2.jpg)


#### Step 3. Run MiSTer update script

Connect a keyboard to your DE10-Nano and hit F12 to open the menu. Make sure you have an (Internet-enabled) Ethernet cable connected and navigate to `Scripts → Yes → update`. This will trigger the <a href="https://github.com/MiSTer-devel/Updater_script_MiSTer" target="_blank">update script</a> which will download:

1. All MiSTer cores
2. Video scaler filters
3. GameBoy palettes
4. Cheat codes
5. Scripts

Once complete the DE10-Nano will reboot. When it loads again, you'll see a fully-populated menu with all cores. Good to go!

![](/img/posts/mister-fpga-install-3.jpg)

That completes the MiSTer setup. Next up: [Network Access and Copying Files]({% post_url 2021-01-31-mister-fpga-network-access-and-copying-files %}).


### Other Posts in this Series

{% include mister-fpga-series.md %}
