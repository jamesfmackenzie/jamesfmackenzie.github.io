---
layout: post
title: Raspberry Pi Headless Install
date: '2017-01-02 17:23:00'
summary: Don’t have an extra keyboard or HDMI cable? Here’s how to do a headless Raspbian install on your Pi ...
image: raspberry-pi.jpg
tags: [How To, IoT, Raspberry Pi, Single-Board Computing]
overrideUrl: https://medium.com/hackernoon/raspberry-pi-headless-install-462ccabd75d0
--- 

Don't have an extra keyboard or HDMI cable? Here's how to do a headless <a href="https://www.raspbian.org/" target="_blank">Raspbian</a> install on your Pi.

### Step 1. Download Raspbian image

Head on over <a href="https://www.raspberrypi.org/downloads/raspbian/" target="_blank">here</a> to grab a copy of the Raspbian image. The "Lite" version will do.

![Download Rasbian](/img/posts/2017-01-02 17_28_22-Download Raspbian for Raspberry Pi.png)

### Step 2. Write image to SD card

Write the image to SD card. You can find detailed instructions <a href="https://www.raspberrypi.org/documentation/installation/installing-images/README.md" target="_blank">here</a>.

![Write the Rasbian image using Win32DiskImager](/img/posts/2017-01-02 14_22_43-Rasbian Win32 Disk Imager.png)

### Step 3. Add "ssh" file to the SD card root

Enable <a href="https://en.wikipedia.org/wiki/Secure_Shell" target="_blank">SSH</a> by placing a file named "ssh" (without any extension) onto the boot partition of the SD card.

![ssh file](/img/posts/2017-01-02 14_27_37-ssh-file.png)

### Step 4. Boot your Pi

Pop your prepared SD card, power and a network cable into the Pi.

![Raspberry Pi, powered up and ready to go](/img/posts/raspberry-pi.jpg)

### Step 5. Find your Pi's IP address

To configure your Pi, you need the IP address. You can find this in your Router's DHCP lease allocation table:

![DHCP lease allocation table](/img/posts/2017-01-02 14_40_16-raspberry-pi-ip-address.png)

### Step 6. SSH into your Pi

Use your favourite SSH client (I prefer <a href="http://www.putty.org/" target="_blank">PuTTY</a>) to access the Pi. The default credentials are:

<pre>
username: pi
password: raspberry
</pre>

![SSH into your Pi](/img/posts/2017-01-02 14_40_39-ssh-into-your-pi.png)

### Step 7. Configure your Pi

That's it! You can now <a href="https://www.raspberrypi.org/documentation/configuration/raspi-config.md" target="_target">configure your Pi</a> via <code>sudo raspi-config</code>

![Invoke raspi-config](/img/posts/2017-01-02 14_47_57-sudo-raspi-config.png)

![raspi-config](/img/posts/2017-01-02 14_48_05-raspi-config.png)