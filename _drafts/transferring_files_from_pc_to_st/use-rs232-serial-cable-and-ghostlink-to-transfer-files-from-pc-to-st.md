---
layout: post
title: Using Serial Cable and Ghostlink to Transfer Files from PC to ST
date: '2015-12-26 10:13:00'
categories: transferring_files_from_pc_to_st
---

### What is Ghostlink?

Ghostlink mounts a folder from your PC file system as an extra drive/partition on your STs GEM desktop, allowing you to copy files back and forth.

Connection is made via a serial or null modem cable.

INSERT SCREENSHOT HERE

Here's how to get started!

### 1. Choosing the right cable

The Atari ST serial port uses a 25-pin D-SUB male connector. The serial ports traditionally found on PCs use a 9-pin D-SUB male connector (if there's one there at all).

So to connect the two, you need a 25-pin D-SUB female to 9-pin D-SUB female cable. Or, using insider lingo, DB25F-DB9F.

INSERT PICTURE OF ATARI ST SERIAL PORT 

INSERT PICTURE NULL MODEM CABLE

If your PC doesn't have a serial port at all (many modern PCs don't), you can get away with using a serial to USB adapter cable (DB25F-USB).

INSERT PICTURE OF USB TO SERIAL ADAPTER CABLE 

### 2. Downloading the Ghostlink software

INSTRUCTIONS ON HOW TO DOWNLOAD GHOSTLINK

### 3. Download DOSBox

Being an MS-DOS program, Ghostlink doesn't play nice with newer versions of Windows.

To work around these issues, we'll make use of a DOS emulator - DOSBox.

You can download it here: http://www.dosbox.com/download.php?main=1

### 4. Configure DOSBox

To get our file transfer working, we need to properly configure the COM redirection.

Head to the Windows Control panel (Device Manager? more info needed here) and identity what COM port you're running on.

INSERT SCREENSHOT HERE

Once you know the COM port, head to DOSBox.conf (where is this?) and enter the following line

serial1=directserial realport:<MY REAL COM PORT>

e.g.
serial1=directserial realport:com1

Save DOSBox.conf and you're good to go.

### 5. Connect the machines together

Should be pretty self explanatory!

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