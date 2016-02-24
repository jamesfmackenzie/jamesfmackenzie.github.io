---
layout: post
title: Using PARCP-USB to Transfer Files from PC to ST
date: '2016-02-24 21:19:00'
categories: transferring_files_from_pc_to_st
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/-xNCRaiEHG0?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

If you want to quickly transfer files between your PC and ST, PARCP-USB is a great option.

### What is PARCP-USB?

From the <a href="http://joy.sophics.cz/parcp/parcpusb.html" target="_blank">official site</a>:

> *<a href="http://joy.sophics.cz/parcp/index.html" target="_blank">PARCP</a> (a short name for PARallel CoPy) has been used widely and successfully since 1996 for copying files between two computers connected via their parallel ports. However, nowadays PC computers do not have parallel ports anymore. Instead, USB is everywhere. That's why I have developed an unique hardware adapter that basically converts the PARCP data stream from parallel port to USB port and vice-versa. Since it's developed specifically for PARCP it is called PARCP-USB. This allows you to connect two computers, one having old parallel port and the other one with USB, using a plain USB cable. And you can continue using the PARCP software for copying/moving files and folders from one computer to another*

![](/img/posts/parcp-usb_adapter_dongle.jpg "The PARCP-USB adapter")

### What do I need to transfer files?

* A PARCP-USB adapter. You can pick one up <a href="http://joy.sophics.cz/parcp/parcp-usb.html" target="_blank">here</a> for EUR40 or USD43
* A <a href="http://www.amazon.co.uk/AmazonBasics-A-Male-Mini-B-Cable-Feet/dp/B00NH11N5A/ref=dp_ob_title_ce" target="_blank">mini USB cable</a>
* A downloaded copy of the <a href="http://joy.sophics.cz/parcp/download.htm" target="_blank">PARCP binaries</a>
* A copy of the ST PARCP binaries on [ST-compatible floppy disk ]({% post_url 2016-01-30-use-floppy-disk-to-transfer-files-from-pc-to-st %})

### Step 1. Connect your PC and ST together

1. Plug the parallel side of your PARCP-USB directly into your Atari ST's parallel port
2. Using a mini USB cable, connect the mini USB side of your PARCP-USB directly into your PC's USB port 

![](/img/posts/parcp-usb_parallel_port.jpg "PARCP-USB parallel connector")

![](/img/posts/parcp-usb_mini_usb_port.jpg "PARCP-USB mini USB connector")

### Step 2. Start PARCP server on your Atari ST

Take the disk with your Atari ST PARCP binaries on it, pop it in the ST and power on. Open the floppy drive and fire up <code>PARSERVE.TOS</code>

![](/img/posts/parcp_parserve_tos.png "Launch PARSERVE.TOS")

### Step 3. Start PARCP client on your PC

Back on your PC, navigate to your downloaded copy of the <a href="http://joy.sophics.cz/parcp/download.htm" target="_blank">PARCP binaries</a>. Find the appropriate folder for your OS (in my case <code>PC -> Windows</code>) and launch <code>PARCP.exe</code>

![](/img/posts/parcp_exe.png "Launch parcp.exe")

With any luck, the PARCP server running on your ST will pick up the connection. On your PC, you'll be presented with a shell-type interface.

![](/img/posts/parcp_server.png "PARCP server received connection")

![](/img/posts/parcp_client.png "PARCP client")

### Step 4. Copy Files

Within the PARCP shell, use the arrow keys and enter to navigate the system and find the file you want to transfer. Once you've found it, hit space bar to select, and use F5 to initiate the transfer.

![](/img/posts/parcp_client_file_selected.png "PARCP client - press spacebar to select a file")

Upon hitting F5, you'll be prompted with a "<code>Copy file(s)?</code>" confirmation dialog. By default, "<code>Yes</code>" is selected - so hit the Enter key to begin copying files.

![](/img/posts/parcp_confirmation_dialog.png "Copy file(s)? Yes / No")

![](/img/posts/parcp_progress_bar.png "A progress bar will report on your file transfer")

### Step 5. Shut down the PARCP server, verify file has been transferred

Owing to the (relative) high bandwidth of your ST's parallel port, the file transfer should complete fairly quickly.

Back on the ST, hit <code>Ctrl+Alt+Shift</code> to shut down the PARCP server. You'll drop back to the GEM desktop and (all things going well) your transferred file should be staring you in the face. Easy peasy!

![](/img/posts/parcp_transferred_file.png "File Transfer Success!")
