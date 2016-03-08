---
layout: post
title: Using Ethernet to Transfer Files from PC to ST
date: '2016-03-07 16:00:10'
categories: transferring_files_from_pc_to_st
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/m3Lk96knpI0?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

<a href="https://en.wikipedia.org/wiki/Ethernet" target="_blank">Ethernet</a> - probably the quickest and most convenient way to transfer files between your PC and ST.
 
### What do you need?
 
* An Atari ST Ethernet adapter. You can pick up the awesome NetUSBee <a href="http://www.lotharek.pl/product.php?pid=73" target="_blank">here</a> for EUR60.
* A <a href="https://en.wikipedia.org/wiki/Category_5_cable" target="_blank">Cat5</a> or <a href="https://en.wikipedia.org/wiki/Category_6_cable" target="_blank">Cat6</a> Ethernet cable
* An [ST-compatible floppy disk]({% post_url 2016-01-30-use-floppy-disk-to-transfer-files-from-pc-to-st %})

### Step 1. Connect your PC and ST together

1. Plug the NetUSBee into your ST's cartridge port (usually on the left-hand side)
2. Connect one end of the Ethernet cable into the NetUSBee. The other end should connect to your <a href="https://en.wikipedia.org/wiki/Network_switch" target="_blank">switch</a>/<a href="https://en.wikipedia.org/wiki/Router_(computing)" target="_blank">router</a> or (in advanced cases) to your PC's <a href="https://en.wikipedia.org/wiki/Network_interface_controller" target="_blank">NIC</a> directly. 

![](/img/posts/atari_st_netusbee.jpg "Connecting a NetUSBee")

### Step 2. Download and prepare uip-tool

Typically, you'll need some Ethernet drivers and a TCP/IP stack for your Atari ST before it can talk to your PC. But luckily for us, there's a super easy click-and-run solution out there called uip-tool. Here's how to get started:

1. Download a copy of uip-tool from <a href="https://bitbucket.org/sqward/uip-tools/downloads/" target="_blank">here</a>. The file you want is <code>UIPV43.TOS</code>.
2. Copy the file onto your [ST-compatible floppy]({% post_url 2016-01-30-use-floppy-disk-to-transfer-files-from-pc-to-st %})

### Step 3. Launch uip-tool

Pop the floppy disk in your ST and power on. Launch <code>UIPV43.TOS</code>. You should see something like this:

![](/img/posts/atari_st_uip_tool.png "uip-tool")

Make a note of the IP address (in this case <code>192.168.1.168</code>). You'll need this to transfer files. If you don't see an IP address, it might be that <a href="https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol" target="_blank">DHCP</a> isn't properly configured on your network.

### Step 4. Use your browser to connect to your ST

Back on the PC, launch a Web browser (any will do) and navigate to <code>http://[your.ip.address]</code> - for our example case it's <code>http://192.168.1.168</code>. All going well, you'll see the uip-tool web interface:

![](/img/posts/atari_st_uip_tool_file_copy.png "uip-tool File Copy")

Use the leftmost column to navigate through drives and folders in the ST's file system. Files are displayed in the main column. To upload a file, simply drag-and-drop (shown above). That's it! Easy peasy.