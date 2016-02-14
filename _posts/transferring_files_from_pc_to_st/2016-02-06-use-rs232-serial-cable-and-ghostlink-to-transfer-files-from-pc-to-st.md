---
layout: post
title: Using Serial Cable and Ghostlink to Transfer Files from PC to ST
date: '2016-02-06 17:32:00' 
categories: transferring_files_from_pc_to_st
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/N_l7VXHF9m0?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

At some point, you'll most likely want to transfer files from PC to ST. One common approach is to use the Ghostlink software along with the correct cabling.

### What is Ghostlink?

Ghostlink mounts a folder from your PC file system as an extra drive/partition on your ST's GEM desktop, allowing you to copy files back and forth. Connection is made via a serial or null modem cable.

Here's how to get started!

### 1. Choose the right cable, connect your PC and ST together

The Atari ST serial port uses a 25-pin D-SUB male connector. The serial ports traditionally found on PCs use a 9-pin D-SUB male connector (if there's one there at all). So to connect the two, you need a 25-pin D-SUB female to 9-pin D-SUB female cable. Or, in insider lingo, DB25F-DB9F.

![](/img/posts/atari_st_rs232_serial_port_25pin_db25.jpg "Atari ST 25-pin serial/RS232 port")

![](/img/posts/atari_st_rs232_serial_cable_db25f-db9f.jpg "DB25F-DB9F serial/RS232 cable")

If your PC doesn't have a serial port at all (many modern PCs don't), you can get away with using a serial to USB adapter cable (DB25F-USB).

![](/img/posts/atari_st_rs232_serial_to_usb_adapter.jpg "Serial/RS232 to USB adapter cable")

Get the right cable, then connect your PC and ST together.

### 2. Download the Ghostlink software

You can download Ghostlink <a href="http://www.chebucto.ns.ca/Services/PDA/AtariSTMisc.shtml" target="_blank">here</a>. It comes as an archive with two files:

* <code>STMASTER.PRG</code> - The Ghostlink client. Run this on your ST.
* <code>PCSLAVE.EXE</code> - The Ghostlink file server. Run this on your PC.

### 3. Download DOSBox

Being an MS-DOS program, Ghostlink doesn't play nice with newer versions of Windows. To work around these issues, we'll make use of a DOS emulator - DOSBox. You can download it <a href="http://www.dosbox.com/download.php?main=1" target="_blank">here</a>. 

### 4. Configure DOSBox

To get our file transfer working, we need to properly configure the COM port and DOSBox's COM redirection.

Head to the Windows Device Manager, expand "Ports (COM & LPT)" and identity what COM port you're running on. In my case it's COM3:

![](/img/posts/device_manager_com_ports.png)

Once you've done this, use Windows Explorer to navigate to <code>%localappdata%\DOSBox</code>. Locate a file named <code>DOSBox.conf</code> (or similar). You may need to start DOSBox just the once to make this file appear. 

When you've found the file, open it in your favourite text editor, navigate down to the <code>[serial]</code> section and add the following line:

{% highlight bash %}
serial1=directserial realport:<MY REAL COM PORT>
{% endhighlight %}

Or, for our example case:
{% highlight bash %}
serial1=directserial realport:com3
{% endhighlight %}

This instructs DOSBox to configure a virtual port (COM1) and map it to the real/physical interface COM3.

### 5. Transfer Ghostlink to the ST

Before we can transfer any files down the serial cable, we need to copy the Ghostlink program across to the ST via conventional means. On your PC, prepare an [ST-compatible floppy disk]({% post_url 2016-01-30-use-floppy-disk-to-transfer-files-from-pc-to-st %}) and copy <code>STMASTER.PRG</code> (from the downloaded Ghostlink archive) onto it.

### 6. Launch STMASTER.PRG

Switch your ST to medium resolution and launch <code>STMASTER.PRG</code>. When it loads up, select any/all of the preconfigured partitions and hit "Remove":

![](/img/posts/configuring_ghostlink_1.png "Remove existing Ghostlink partitions")

Once you've removed all the preconfigured partitions, hit "Add" and select the following:

![](/img/posts/configuring_ghostlink_2.png "Configuring Ghostlink")

This means "I want to map drive Z: on my Atari ST to drive C: on my PC". Once you're done with this, hit "OK" and then "Install":

![](/img/posts/configuring_ghostlink_3.png "Installing Ghostlink")

Ghostlink appears to quit without doing anything useful - but don't worry, it's now memory resident and ready to talk to your PC.

### 8. Prepare files for transfer

Back on the PC, create a new directory and copy the following files into it:

* <code>PCSLAVE.EXE</code> (this is part of the downloaded Ghostlink archive - see above)
* Any files you want to transfer to the ST

![](/img/posts/files_to_copy_st.png)

### 9. Launch DOSBox, mount file share

Launch DOSBox and type the following to mount your new directory as the C: drive:

{% highlight bash %}
mount C: <PATH TO FILE SHARE DIRECTORY>
{% endhighlight %}

Or, for our example case:
{% highlight doscon %}
mount c: c:\temp\copy_files_via_ghostlink\files_for_pc
{% endhighlight %}

![](/img/posts/dosbox_mount_file_share.gif)

### 10. Launch PCSLAVE.EXE

Still in DOSBox, navigate to the C: drive and launch <code>PCSLAVE.EXE</code>.

![](/img/posts/launch_pc_slave.png)

Once you've launched <code>PCSLAVE.EXE</code>, use the Function keys (F1-F10) to set the speed to 9600 Baud: 

![](/img/posts/ghostlink_9600_baud.png)

### 11. Map Ghostlink drive, start transferring files!

Back on the Atari ST Desktop, use the Options menu to map your Z: drive:

![](/img/posts/atari_st_map_drive.gif)

You're ready to transfer files! Back on the Atari ST's GEM Desktop, open up your new Z: drive and start copying files across! 

![](/img/posts/atari_st_transfer_files.gif)

If file transfer is working as expected, you'll see telemetry in the DOSBox window:

![](/img/posts/ghostlink_pc_slave_telemetry.png)

That's pretty much it! Happy file transferring!

###Crank up the speed

9600 bits per second is a little slow. If you want to speed things up a little, try the following:

Download <a href="https://sites.google.com/site/stessential/control-panel-replacements/xcontrol" target="_blank">XControl</a> and copy it to your ST.

* To install, put <code>XCONT_UK.ACC</code> or <code>XCONTROL.ACC</code> into the main/root directory of your ST's startup disk (usually A: or C:).
* Launch XControl via "Desk" -> "Control Panel"

Once you've loaded XControl, head to "Modem Settings" and increase your ST's Baud Rate to 19200:

![](/img/posts/atari_st_xcontrol_19200_baud.png)

On your PC, navigate to "Control Panel" -> "Device Manager" -> "Ports (COM & LPT)" -> "Serial Port" -> "Port Settings". Increase the bits per second to 19200 and press "OK":

![](/img/posts/device_manager_com_port_settings.png)
 
Whilst running <code>PCSLAVE.EXE</code> in DOSBox, press F4 to set the Baud rate to 19200:
 
![](/img/posts/ghostlink_19200_baud.png)

With a bit of luck, you should now be able to push files down the serial cable twice as fast! If you're *really* lucky, you might be able to push the speeds to 28800 bits per second or higher, but 19200 was the fastest that worked reliably for me.
