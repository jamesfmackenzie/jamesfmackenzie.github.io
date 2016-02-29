---
layout: post
title: Using Ethernet to Transfer Files from PC to ST
date: '2015-12-26 10:13:10'
categories: transferring_files_from_pc_to_st
---

 
 
 
 
So I'm going to talk about probably the fastest and most convenient way of transfering files between your PC to ST ... and that's using Ethernet
 
What do you need?
 
Well first you need an Atari ST ethernet adapter - here I have one called the NetUSBee which you can pick up for about 60 euros
That plugs into the Atari ST cartridge interface which is normally on the left side
 
Once you've got that plugged in, you need to plug in a standard CAT5 or CAT6 ethernet cable - you've probably got loads of these lying around
 
Lastly you need some ethernet drivers and a TCP/IP stack for your Atari ST so it can talk to your Mac, Windows or Linux machine
Luckily for us, there's a super easy click-and-run solution out there called uiptool.
 
I've downloaded it and put it on this ST-compatible floppy disk just here - I'll put a download link for that below.
 
OK, that's the setup. Now I'll wire everything up for real and join you again when we're ready to transfer files!
 
 
 
 
OK, so we've got everything wired up for real.
* Over here in the top right we have the ST, with a copy of the uip-tool in the floppy drive
* Down in the bottom right here we have the file we want to copy across to our ST ... demo.prg
* And finally over here on the left, we have a web browser - which we'll get to in a minute
 
So, to get started, we run the uip-tool, and it says:
* Great, I've been assigned an IP address via DHCP, and it's 192.168.1.168
* Make a note of this IP address, it's important
 
So now on my PC, I open up a web browser, any will do, and I put in this IP address as the URL:
* http://192.168.1.168 <Enter>
* And what you can ST is the uip-tool running on our ST responds - it's actually running a mini web server
* So now, back in the browser on my PC, I can navigate my ST's file system
 
So to transfer a file, I select the drive - in this case A: drive and then I just drag and drop
uipTool come to life and you can see my ST is receiving the file over here
 
 