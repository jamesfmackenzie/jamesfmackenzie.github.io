---
layout: post
title: Using Serial Cable and ZMODEM to Transfer Files from PC to ST
date: '2016-02-13 10:13:00'
categories: transferring_files_from_pc_to_st
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/ofhKCXVbu-0?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

At some point, you'll most likely want to transfer files from PC to ST. One approach is to use a serial cable (or null modem) connection and ZMODEM.

### What is ZMODEM?

From <a href="https://en.wikipedia.org/wiki/Main_Page" target="_blank">Wikipedia</a>:

*"ZMODEM is a file transfer protocol developed by Chuck Forsberg in 1986, in a project funded by Telenet in order to improve file transfers on their X.25 network. In addition to dramatically improved performance compared to older protocols, ZMODEM also offered restartable transfers, auto-start by the sender, an expanded 32-bit CRC, and control character quoting, allowing it to be used on networks that might "eat" control characters. ZMODEM became extremely popular on bulletin board systems (BBS) in the early 1990s, displacing earlier protocols such as XMODEM and YMODEM."*

Luckily for us, there are ZMODEM implementations available for both ST and Windows PC.

If we connect the machines together via a serial or null modem cable, we'll be able to push files back and forth.

### 1. Choose the right cable, connect your PC and ST together

The Atari ST serial port uses a 25-pin D-SUB male connector. The serial ports traditionally found on PCs use a 9-pin D-SUB male connector (if there's one there at all). So to connect the two, you need a 25-pin D-SUB female to 9-pin D-SUB female cable. Or, in insider lingo, DB25F-DB9F.

![](/img/posts/atari_st_rs232_serial_port_25pin_db25.jpg "Atari ST 25-pin serial/RS232 port")

![](/img/posts/atari_st_rs232_serial_cable_db25f-db9f.jpg "DB25F-DB9F serial/RS232 cable")

If your PC doesn't have a serial port at all (many modern PCs don't), you can get away with using a serial to USB adapter cable (DB25F-USB).

![](/img/posts/atari_st_rs232_serial_to_usb_adapter.jpg "Serial/RS232 to USB adapter cable")

Get the right cable, then connect your PC and ST together.

### 2. Download ZMODEM software for PC

For the PC, the easiest software I've found is Teraterm. It's an open source terminal emulator, but also happens to support ZMODEM file transfers. You can download and install it from <a href="https://en.osdn.jp/projects/ttssh2/" target="_blank">here</a>.

### 3. Download ZMODEM software for ST

For the ST, I'd recommend X Y Z V2.02. It's a small program that (amongst a few other things) allows you to do ZMODEM file transfer. You can download it <a href="http://www.chebucto.ns.ca/Services/PDA/AtariSTComm.shtml" target="_blank">here</a>. There are a few files in the archive but the only one you need is <code>XYZ.TTP</code>

### 4. Transfer XYZ to the ST

Before we can transfer any files down the serial cable, we need to copy XYZ across to the ST via conventional means. On your PC, prepare an [ST-compatible floppy disk]({% post_url 2016-01-30-use-floppy-disk-to-transfer-files-from-pc-to-st %}) and copy <code>XYZ.TTP</code> onto it.

### 5. Run XYZ.TTP

Pop your newly-created floppy into the ST drive and launch <code>XYZ.TTP</code>. No parameters required, just press "OK" and let the application start:

![](/img/posts/atari_st_launch_xyz_zmodem.gif "Launching X Y Z V2.02")

![](/img/posts/atari_st_xyz_zmodem.png "X Y Z V2.02")

### 6. Launch Teraterm, configure serial port

Back on the PC, launch Teraterm. The application should auto-detect the null modem connection to your ST. Hit the "Serial" radio button and press "OK":

![](/img/posts/teraterm_serial_port.png)

Next, browse to "Setup", "Serial port..." and verify the following settings before pressing "OK":

![](/img/posts/teraterm_serial_port_config.png)

### 7. Transfer files! 

You're ready to transfer files! Still within Teraterm, head over to "File" -> "Transfer" -> "ZMODEM" -> "Send...":

![](/img/posts/teraterm_zmodem_transfer.png)

Choose a file to transfer and click "Open". Teraterm will begin transferring the file across. You even get a progress bar:

![](/img/posts/teraterm_file_transfer.png)

All going well, the Atari ST will also report transfer progress:

![](/img/posts/atari_st_xyz_file_transfer.png)

Once the file transfer finishes, <code>XYZ.TTP</code> will automatically terminate. You should find your transferred file available on the ST file system. Job done!

![](/img/posts/atari_st_zmodem_transferred_file.png "DEMO.PRG successfully transferred via ZMODEM")

###Crank up the speed

9600 bits per second is a little slow. If you want to speed things up a little, try the following:

Download <a href="https://sites.google.com/site/stessential/control-panel-replacements/xcontrol" target="_blank">XControl</a> and copy it to your ST.

* To install, put <code>XCONT_UK.ACC</code> or <code>XCONTROL.ACC</code> into the main/root directory of your ST's startup disk (usually A: or C:).
* Launch XControl via "Desk" -> "Control Panel"

Once you've loaded XControl, head to "Modem Settings" and increase your ST's Baud Rate to 19200:

![](/img/posts/atari_st_xcontrol_19200_baud.png)

On your PC, navigate to "Control Panel" -> "Device Manager" -> "Ports (COM & LPT)" -> "Serial Port" -> "Port Settings". Increase the bits per second to 19200 and press "OK":

![](/img/posts/device_manager_com_port_settings.png)
 
In Teraterm, navigate to "Setup", "Serial port..." and increase the Baud rate to 19200:
 
![](/img/posts/teraterm_serial_port_19200.png)

With a bit of luck, you should now be able to push files down the serial cable twice as fast! If you're *really* lucky, you might be able to push the speeds to 28800bps, 38400bps or even higher! But 19200bps was the fastest that worked reliably for me.
