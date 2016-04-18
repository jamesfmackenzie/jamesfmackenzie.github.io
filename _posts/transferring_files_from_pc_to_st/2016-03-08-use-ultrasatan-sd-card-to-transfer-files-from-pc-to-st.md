---
layout: post
title: Using an SD card and Ultrasatan to Transfer Files from PC to ST
date: '2016-03-08 10:16:00'
categories: transferring_files_from_pc_to_st
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/ddwDJn8CV8I?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

If you want to make a large number of files available on your ST, <a href="http://www.lotharek.pl/product.php?pid=94" target="_blank">Ultrasatan</a> is the way to go.

### What is Ultrasatan?

The Ultrasatan is a hard disk replacement for your Atari ST - and it uses SD cards for storage. Whilst not specifically intended for file transfer, by partitioning and formatting the SD card in the right way, you can mount the SD card on both your PC and ST - and hence use it to transfer files.

* Pros
  * Definitely the fastest way to transfer files - you're only limited by the speed at which your PC can write data to the SD card (i.e. **really** fast)
  * Unlike [other methods]({% post_url 2015-12-26-transferring-files-from-pc-to-st %}), no floppy drive is required. So if you PC or ST floppy drive is broken (or you don't have one), you can still use this method
* Cons
  * Expensive (<a href="http://www.lotharek.pl/product.php?pid=94" target="_blank">EUR92</a> for the cased version) - but a worthy investment!

### What do you need?

* An <a href="http://www.lotharek.pl/product.php?pid=94" target="_blank">Ultrasatan device</a>
* A <a href="http://www.pcmag.com/encyclopedia/term/62117/micro-usb" target="_blank">micro-USB</a> power adapter (your Android or BlackBerry charger will do)
* An <a href="https://en.wikipedia.org/wiki/Secure_Digital" target="_blank">SD card</a> (8GB is ideal)
* Some hard disk drivers and partitioning software for your ST. I used <a href="http://atari.8bitchip.info/pphdr.php" target="_blank">Peter Putnik's "PP" drivers and partitioner</a> because:
  * It's a "two-in-one" - the package includes both partitioning software and hard disk drivers
  * The toolset facilitates the creation and use of GEMDOS drives that work on both ST and PC - **this is exactly what we need to do**
  * It features a "quick start" SD card image to get you up and running without using a floppy disk
* An SD card disk imager for your PC. I recommend <a href="https://sourceforge.net/projects/win32diskimager/" target="_blank">Win32DiskImager</a> (alternatives are available for Mac and Linux)

### Step 1. Write quick start image to SD card

Included in the <a href="http://atari.8bitchip.info/pphdr.php" target="_blank">PP driver distribution</a> is a "quick start" SD card image (<code>15MB.img</code>). You need to write this to your SD card.

* Open Win32DiskImager, hit "Select disk image" and pick the quick start image (<code>15MB.img</code>)

![](/img/posts/atari_st_win32diskimager_a.png "Select a disk image")

* Once you've selected the disk image, hit "Write". **Be very sure that you've selected the right volume to write to. Writing to the wrong volume can corrupt your data and/or Operating System**

![](/img/posts/atari_st_win32diskimager_b.png "Click 'Write'")

![](/img/posts/atari_st_win32diskimager_c.png "Ensure you have the correct volume")

* All things going well, your image is written to the SD card successfully and you'll be able to browse the new volume from Windows Explorer:

![](/img/posts/atari_st_win32diskimager_d.png "Write successful")

![](/img/posts/atari_st_win32diskimager_e.png "Files are readable using Windows Explorer")

### Step 2. Boot your ST from SD card

Pop your newly prepared SD card into the Ultrasatan and reboot your ST. The ST should boot from the SD card and you'll see something like this:

![](/img/posts/atari_st_ultrasatan_boot.png "Ultrasatan boot")

![](/img/posts/atari_st_ultrasatan_ramdisk.png "Ultrasatan ramdisk")

Breaking this down:

* The SD card is mounted as our <code>C:</code> drive - this is same volume we just browsed from Windows Explorer
* Rather helpfully, the quick start image has also provides some useful partitioning and formatting tools. These are available on the <code>D:</code> drive

So this is working well, right? Our SD card is readable by both PC and ST - and we *could* use it to copy files. But there's a problem - **the volume is only 14MB** - and we want more than that!

To get more space, we need to partition the SD card.

### Step 3. Partition the SD card

Still on your ST, launch <code>D:/PPP13U.PRG</code>. This is the partitioning software and will allow us to expand into the extra space available on the SD card. Once in the partitioner:

* Press "ASCI0" to display the topology of the SD card. This will remind us that we only have 1 partition of 14MB available to us on the <code>C:</code> drive:

![](/img/posts/atari_st_ultrasatan_partitioning_1.png "Ultrasatan partitioning 1")

* Increase the size of the <code>C:</code> drive from 14MB to 511MB (or 255MB if you're running TOS 1.02 or lower)

![](/img/posts/atari_st_ultrasatan_partitioning_2.png "Ultrasatan partitioning 2")

* Repeat the same for <code>D:</code>, <code>E:</code>, <code>F:</code> etc until you run out of space on your SD card. Remaining free space is always displayed in the top right. The ST can support a maximum of 14 partitions, making an 8GB SD card the perfect size.

![](/img/posts/atari_st_ultrasatan_partitioning_3.png "Ultrasatan partitioning 3")

* Once you're done, select "PARTIT. and INIT  all". Your ST will whirr for a little while as it partitions and initializes your new volumes.

* Lastly, press "ASCI0" one more time. This will display the SD card topology and confirm that partitioning has worked as expected. Press "EXIT" once you're happy.

### Step 4. Install drivers

The next step is to install hard disk drivers.

* Launch <code>D:\USAB101.TOS</code>

![](/img/posts/atari_st_ultrasatan_install_pp_drivers_1.png "Launch USAB101.TOS")

* You'll now be prompted with <code>Select target 0-7</code>. Press "0"

![](/img/posts/atari_st_ultrasatan_install_pp_drivers_2.png "Select target device")

* You'll now be asked to confirm the driver installation: <code>I installs, Space exits without install</code>. Press "I"

![](/img/posts/atari_st_ultrasatan_install_pp_drivers_3.png "Install PP driver")

* Once the drivers are installed succesfully (it should be very quick), you'll see a confirmation message: <code>Installed</code>

![](/img/posts/atari_st_ultrasatan_install_pp_drivers_4.png "PP drivers installed successfully")

* Press any key to exit the installer

* Reboot your ST

Take a look at the boot screen - you should now see your new drives letters available:

![](/img/posts/atari_st_ultrasatan_partitioning_drives.png "Partitioning drives")

### Step 5. Install missing drives

Once your ST reaches the GEM desktop, you'll notice that you only have the <code>C:</code> drive available. You need to install the other drives manually.

* Left click on your <code>C:</code> drive

* Navigate to <code>Options -> Install Disk Drive</code>

![](/img/posts/atari_st_ultrasatan_install_disk_drive_1.png "Installing a new drive")

* Set the <code>Drive identifier</code> to "D:"

![](/img/posts/atari_st_ultrasatan_install_disk_drive_2.png "Setting the new drive letter")

* Repeat the process for any other new drives you have

* Save the Desktop via <code>Options -> Save Desktop</code>

![](/img/posts/atari_st_ultrasatan_save_desktop.png "Save Desktop")

Now whenever you reboot, the ST will remember all your drive letters.

### Step 6. Copy files

Now that you have a working SD card, it's time to copy some files!

* Pull the SD card from your Ultrasatan and mount it on your PC

* You'll see a single volume of 510MB. This corresponds to the <code>C:</code> drive on your ST

![](/img/posts/atari_st_ultrasatan_sd_card_properties.png "Ultrasatan SD card")

* In Windows Explorer, Drag and drop some files onto the SD card

![](/img/posts/atari_st_ultrasatan_sd_card_copied_files.png "Drag & Drop some files onto the SD card")

* Pull the SD card from your PC and insert it back into the Ultrasatan

* Reboot your ST and open the <code>C:</code> drive. You'll find all the copied files ready and waiting!

![](/img/posts/atari_st_ultrasatan_atari_st_copied_files.png "Copied files, available on the ST!")

