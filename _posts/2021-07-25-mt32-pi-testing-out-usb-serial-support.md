---
layout: post
title: "mt32-pi – Testing out New USB Serial Support"
date: '2021-07-25 12:47:00:00'
summary: mt32-pi recently added support for USB serial devices. How does it work?
image: mt32-pi-serial-midi-hardware-connection.jpg
tags: [DOS, How To, MIDI, Retrocomputing, Retrogaming]
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/SxMjDsT9rEo?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

The <a href="https://github.com/dwhinham/mt32-pi/releases/tag/v0.10.0" target="_blank">latest mt32-pi release</a> has added support for USB serial devices - making it much easier to connect retro gaming PCs via serial cable. [Previously we had to use a clunky RS232 to TTL converter module]({% post_url 2021-05-03-get-the-best-msdos-ms-dos-audio-with-mt32-pi %}). The new setup is much cleaner.

### What you need

* USB to Serial cable (e.g. <a href="https://www.amazon.com/gp/product/B00IDSM6BW" target="_blank">this one</a>)
* Null modem serial port adapter (e.g. <a href="https://www.amazon.com/gp/product/B075XGRLXW" target="_blank">this one</a>)

A new configuration option <code>usb_serial_baud_rate</code> has been introduced. You'll need to edit the <a href="https://github.com/dwhinham/mt32-pi/wiki/Configuration-file" target="_blank">mt32-pi configration file</a> (<code>mt32-pi.cfg</code>). Replace the following line:

````
usb_serial_baud_rate = 31250
```` 

With this:

````
usb_serial_baud_rate = 38400
```` 

<i>The PC serial port can't run at the standard <a href="https://en.wikipedia.org/wiki/MIDI" target="_blank">
MIDI</a> baud rate of 31250bps. Instead we tell our mt32-pi to use 38400bps – the closest "PC standard" baud rate.</i>

Other than that, the setup is [identical to the previous guide]({% post_url 2021-05-03-get-the-best-msdos-ms-dos-audio-with-mt32-pi %}). Enjoy! 


### More MIDI articles

{% include midi.md %}






