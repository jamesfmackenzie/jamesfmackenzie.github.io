---
layout: post
title: Using PARCP-USB to Transfer Files from PC to ST
date: '2015-12-26 10:13:00'
categories: transferring_files_from_pc_to_st
---

![](/img/posts/parcp-usb_adapter_dongle.jpg)

![](/img/posts/parcp-usb_parallel_port.jpg)

![](/img/posts/mini_usb_cable.jpg)

![](/img/posts/parcp-usb_mini_usb_port.jpg)

OK, so we've got the the Atari ST and the PC wired together via USB
Over on the ST, as I mentioned before, we've got the PARCP software copied onto a floppy disk and I can show you that just here ...
And on the PC, we've got the PARCP software downloaded here ... and if I browse to PC, Windows ... this is what we're going to use
And we also have ... down here ... a file that we want to transfer
OK, so let's get started
First, we start the server process on the ST ... so we run PARSERVE.TOS
Once that's up, we go back to the PC and we run PARCP.EXE
You can see that the ST server has picked up the client connection and we're delivered to this shell interface right here
No we use arrow keys to browse and enter to browse the file system and find the file we want to transfer 
So ... back c:\temp\copy_files_via_parcp ... here we go
Once I've found the file, I press space bar to select it ... F5 ... 
Do you want to Copy file(s) ... yes I sure do ... Enter
Here we go ... it's transfering across and you can see a progress indicator on both sides ...
All done ... really quick of course ... because the parallel port has relatively high bandwidth
So now back on the ST I kit Ctrl+Alt+Shift ... I'm dropped back to the desktop and I can see my file here ... copied across!
Let's double check it's come across OK by running it ...
Yep ... everything looks good! Easy, right?





