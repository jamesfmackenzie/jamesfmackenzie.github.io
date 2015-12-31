---
layout: post
title: Using Serial Cable and ZMODEM to Transfer Files from PC to ST
date: '2015-12-26 10:13:00'
categories: transferring_files_from_pc_to_st
---

###What is ZMODEM?

From Wikipedia:

"ZMODEM is a file transfer protocol developed by Chuck Forsberg in 1986, in a project funded by Telenet in order to improve file transfers on their X.25 network. In addition to dramatically improved performance compared to older protocols, ZMODEM also offered restartable transfers, auto-start by the sender, an expanded 32-bit CRC, and control character quoting, allowing it to be used on networks that might "eat" control characters. ZMODEM became extremely popular on bulletin board systems (BBS) in the early 1990s, displacing earlier protocols such as XMODEM and YMODEM."

Luckily for us, there are ZMODEM implementations available for both ST and Windows PC.

If we connect the machines together via a serial or null modem cable, we'll be able to push files back and forth.

###1. Choosing the right cable

The Atari ST serial port uses a 25-pin D-SUB male connector. The serial ports traditionally found on PCs use a 9-pin D-SUB male connector (if there's one there at all).

So to connect the two, you need a 25-pin D-SUB female to 9-pin D-SUB female cable. Or, using insider lingo, DB25F-DB9F.

INSERT PICTURE OF ATARI ST SERIAL PORT 

INSERT PICTURE NULL MODEM CABLE

If your PC doesn't have a serial port at all (many modern PCs don't), you can get away with using a serial to USB adapter cable (DB25F-USB).

INSERT PICTURE OF USB TO SERIAL ADAPTER CABLE 

###2. Download ZMODEM software for PC

The easiest software I've found is Teraterm. You can download it here:
https://en.osdn.jp/projects/ttssh2/

INSTRUCTIONS ON HOW TO DOWNLOAD TERATERM.

###3. Download ZMODEM software for ST

On the ST, I'd recommend Flash 1.60. Find it over here:
http://www.chebucto.ns.ca/Services/PDA/AtariSTComm.shtml

###4. Connect the machines together

Should be pretty obvious!

###5. Transfer files!

Initiate a new transfer on the PC side and watch it zip across. Easy!

###6. Crank up the speed

How fast can you go??