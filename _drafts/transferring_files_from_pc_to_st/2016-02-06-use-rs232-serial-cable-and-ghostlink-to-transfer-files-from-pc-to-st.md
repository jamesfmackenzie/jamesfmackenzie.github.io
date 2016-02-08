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

The Atari ST serial port uses a 25-pin D-SUB male connector. The serial ports traditionally found on PCs use a 9-pin D-SUB male connector (if there's one there at all). So to connect the two, you need a 25-pin D-SUB female to 9-pin D-SUB female cable. Or, using insider lingo, DB25F-DB9F.

![](/img/posts/atari_st_rs232_serial_port_25pin_db25.jpg "Atari ST 25-pin serial/RS232 port")

![](/img/posts/atari_st_rs232_serial_cable_db25f-db9f.jpg "DB25F-DB9F serial/RS232 cable")

If your PC doesn't have a serial port at all (many modern PCs don't), you can get away with using a serial to USB adapter cable (DB25F-USB).

![](/img/posts/atari_st_rs232_serial_to_usb_adapter.jpg "Serial/RS232 to USB adapter cable")

Once you've gotten the right cable, connect your PC and ST together!

### 2. Download the Ghostlink software

You can download Ghostlink <a href="http://www.chebucto.ns.ca/Services/PDA/AtariSTMisc.shtml" target="_blank">here</a>. It comes as an archive with two files:

* STMASTER.PRG - The Ghostlink client. Run this on your ST.
* PCSLAVE.EXE - The Ghostlink file server. Run this on your PC.

### 3. Download DOSBox

Being an MS-DOS program, Ghostlink doesn't play nice with newer versions of Windows. To work around these issues, we'll make use of a DOS emulator - DOSBox. You can download it <a href="http://www.dosbox.com/download.php?main=1" target="_blank">here</a>. 

### 4. Configure DOSBox

To get our file transfer working, we need to properly configure the COM port and DOSBox's COM redirection.

Head to the Windows Device Manager, expand "Ports (COM & LPT)" and identity what COM port you're running on. In my case it's COM3:

![](/img/posts/device_manager_com_ports.png)

In addition, open the COM port Properties dialog (right click, Properties) and select the Port Settings tab. Configure settings as per the below:

![](/img/posts/device_manager_com_port_settings.png)

Once you've done this, use Windows Explorer to navigate to <code>%localappdata%\DOSBox</code>. Find and open a file named <code>DOSBox.conf</code> (or similar). Once you've done that, navigate down to the <code>[serial]</code> section and add the following line:

{% highlight bash %}
serial1=directserial realport:<MY REAL COM PORT>
{% endhighlight %}

For this example:
{% highlight bash %}
serial1=directserial realport:com3
{% endhighlight %}

This instructs DOSBox to configure a virtual port (COM1) and map it to the real/physical interface COM3.

### 5. Download XControl

XControl is a replacement Control Panel for the ST. Most importantly for us, it allows us to configure the ST's serial port. You can download it <a href="https://sites.google.com/site/stessential/control-panel-replacements/xcontrol" target="_blank">here</a>.

### 6. Transfer Ghostlink and XControl to the ST

Before we can transfer any files down the serial cable, we need to copy a few files across to the ST. On your PC, prepare an [ST-compatible floppy disk]({% post_url transferring_files_from_pc_to_st/2016-01-30-use-floppy-disk-to-transfer-files-from-pc-to-st %}) and copy the following onto it:

* <code>STMASTER.PRG</code> (from the downloaded Ghostlink archive)
* <code>XCONT_UK.ACC</code> (from the downloaded XControl archive)
* <code>MODEM.CPX</code> (from the downloaded XControl archive)

This is the bare minimum you need on the ST to get Ghostlink file transfer working.

### 6. Launch STMaster.prg

Back on the ST, launch STMaster.prg and configure as follows:

INSERT SCREENSHOT AND CONFIG OPTIONS HERE

TRY 19200 FIRST, BUT WHAT IS THE HIGHEST BAUD RATE?

Click on Save to save your settings for next time, then Install. The program will quit, but don't worry, Ghostlink is now memory resident and running.

### 7. Install drive icon on your ST

SCREENSHOT AND INSTRUCTIONS HERE

### 8. Launch PCSlave.exe

Back on the PC, launch PCSlave.exe. Use 1 and 2 to adjust the baud rate - it should match the rate that you chose on the ST.

SCREENSHOT HERE

### 9. Transfer files!

Open files on your ST and drag them across!

### 10. Crank up the speed

Start at 19200, try increasing the speed. How fast can you get before errors start cropping up?

### What isn't supported?

* renaming a folder on the mounted partition
* Launching a program (.PRG of course) on the slave. (maybe in the next version...)

### Wait! I got some weird COM error

Might need to build a special version of DOSBox

### More info

BITZ Computers c/o P. Van Malderen
Brusselsesteenweg, 107
B-1500 Halle / Belgium

Phone: (02) 361 10 89
Fax: (02) 361 25 52 
BITZ Atari BBS: (02) 361 14 08 (message to PIRRE KING)

So, enjoy this program...

(c)Bitz 1994 Pierrot Van Malderen.