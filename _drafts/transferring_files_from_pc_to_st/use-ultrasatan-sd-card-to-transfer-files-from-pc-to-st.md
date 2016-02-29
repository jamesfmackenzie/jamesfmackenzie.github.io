---
layout: post
title: Using an SD card and Ultrasatan to Transfer Files from PC to ST
date: '2015-12-26 10:13:00'
categories: transferring_files_from_pc_to_st
---

So another way to transfer files between PC and ST is to use one of these - an Ultrasatan device.
 
The name sounds like a boss out of Doom, but this is a hard disk replacement for your Atari ST that uses SD cards as the storage mechanism.
 
Is not intended for transferring files, but if you partition and format your SD card in the right way, you can mount the SD card on both your PC and your ST ... and hence use it to shuffle files back and forth
What are the advantages of this method?
1) It's definitely the fastest way to transfer files as you're only limited by the speed at which your PC can write to an SD card - i.e. very fast
2) Secondly, this method doesn't need any floppy drive at all - so if you don't have a floppy drive on your PC *or* your ST floppy drive it broken, you can still use this
 
The disadvantages?
* Well, it's a bit expensive - an Ultrasatan sets you back about 100 euros - but it's a worthy investment!
 
How do you hook it up?
* Well first you take a micro USB power adapter - this is the standard Android and BlackBerry connector and plug it in here.
* And secondly you plug the other side into the STs hard disk port
 
That's it! Now I'll wire everything up for real and join you again when we're ready to transfer files!
 
 
 
OK, so before we're able to transfer f iles, there's some setup we need to do.
Firstly, we need an SD card ... and I've gone one here 1GB - fresh out the packet
Secondly, we need some hard disk drivers and some partitioning software for our ST. I bought Peter Putnik's "PP" hard disk drivers because:
⦁              It's a two in one - I get both partitioning software and hard disk drivers
⦁              They're specially designed to facilitate the creation of GEMDOS drives - i.e. drives that work on both ST and PC
⦁              It features a "quick start" sd card image so you can get this all working without any floppy disks
Lastly, we need a disk imager program. I downloaded and installed Win32DiskImager from Sourceforge. There are alternative programs available for Mac and Linux.
OK, let's get started. First we need to  write the quick start image to our SD card:
⦁              load the Win32DiskImager, select the image file, select my SD card
⦁              ... be really careful here. If you pick the wrong drive letter you can corrupt your files or OS.
⦁              Press "Write" and we're done ... let's check that we can view the files on the PC ... yes we can.
OK, let's eject and put the file into our ST and reboot ... yep I can see the files OK ... but the disk is only 15MB ... that's no good - I want more than that!
So to fix that we run the partitioner - PP13U.PRG. Double click that - and I'm in the partitioning interface
⦁              First, press ASCI0 to display the topology of the SD card ... and we're reminded again that I only have a 14MB partition
⦁              So start changing this. I'll overwrite the 14MB partition with a much larger one ... 511MB. This is the max you can use - the ST operating system (TOS) can't address any more. Some older ST's which have TOS 1.02 or below can only addresss 256MB ... so be aware of that too.
⦁              Going onto the next disk, let's fill out the space that I have left ... OK that's done
⦁              The ST supports up to 14 drives ... so with 511MB each a 8GB SD card works quite well
⦁              Now I press "Partition and Initialize all" ... wait for that to tick through
⦁              Finally, I press "ACSI0" again to display the topology, looks good!
⦁              Now we're all done with the partitioning, press Exit
Next we exit and install the driver by clicking this USAB101.TOS. There is another flavour of this driver that polls the SD card to allow hot swaps ... but it's not recommended ... let's stick with this one.
⦁              So double click
⦁              Press I to install ... and then any key to quit
⦁              Reboot the ST ... and I can see that I have a bunch of drives ... C and D ... around 500MB each
⦁               
 
 
 
 