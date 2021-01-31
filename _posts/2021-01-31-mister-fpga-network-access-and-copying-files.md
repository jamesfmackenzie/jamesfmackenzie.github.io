---
layout: post
title: "MiSTer FPGA – Network Access and Copying Files"
date: '2021-01-31 13:54:00:00'
summary: How to copy files to your MiSTer over the network ...
tags: [Retrocomputing, Retrogaming, FPGA, MiSTer, Single-Board Computing]
---

You’ve just followed the [setup guide]({% post_url 2020-09-20-mister-fpga-install-and-setup %}) and have a freshly updated MiSTer. Next, you'll want to enable network access so can copy games/files and remotely configure your MiSTer. Here's how

### Network Connection

Although the MiSTer <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki/WiFi-setup" target="_blank">supports some Wi-Fi USB modules</a>, the simplest option is wired Ethernet. Simply plug a network patch cable into the MiSTer's RJ45 socket and an IP address will be configured automatically 

#### Finding the IP Address

The assigned IP address will vary from network to network, and you'll need to navigate some menus to find it:

1. On power up, the MiSTer will display the "Cores" menu. 

2. From here, hit Esc the access System Setting and then Left Arrow to show Misc. Options

3. If networking is setup correctly, you’ll see the IP address (in this case 192.168.100.45):

INSERT IP ADDRESS SCREENSHOT

Make a note of this address. You'll need it below


### Shell access

For advanced MiSTer configuration, you’ll need remote console access. We'll use <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki/Network-access" target="_blank">Secure Shell (SSH)</a>, which MiSTer has enabled by default. Here's how:

1. Download <a href="https://www.putty.org/" target="_blank">PuTTY</a>, a popular and multiplatform SSH client

2. Setup an SSH connection with the following details:

INSERT PUTTY SCREENSHOT 

3. Hit Connect. When prompted for a username enter <code>root</code> and for the password enter <code>1</code>

Now you're succesfully logged in, you can navigate the MiSTer file system. Some useful locations:

LIST USEFUL MISTER LOCATIONS


### Copying files

You can use <a href="https://en.wikipedia.org/wiki/File_Transfer_Protocol" target="_blank">FTP</a> or <a href="https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol" target="_blank">SFTP</a> to remotely copy games and files to/from the MiSTer. Here’s how:

1. Download and install <a href="https://filezilla-project.org/" target="_blank">FileZilla</a>, a free and popular file transfer client

2. Choose File -> Site Manager. Setup a connection with the following details:

INSERT FILEZILLA FILE MANAGER SCREENSHOT

3. Navigate to /media/fat/. This is where MiSTer stores all games and other assets for each core. Drag and drop files to copy

4. Close FileZilla once done

That’s the basics! Now you're ready to use some cores




