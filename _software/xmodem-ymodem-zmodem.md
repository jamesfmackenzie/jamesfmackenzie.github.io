---
layout: post
title: XModem / YModem / ZModem
summary: The family of serial file-transfer protocols I've used to get files onto an Atari ST over a null-modem cable, XYZ on the ST side and TeraTerm on the PC side.
date: '2024-08-29 11:33:00'
tags: [Atari ST, PC, Utilities]
---

XModem, YModem, and ZModem are a lineage of serial file-transfer protocols — XModem first, then YModem and ZModem improving on it with better speed, error-correction, and (in ZModem's case) auto-start and restartable transfers. They were the standard way of pushing files down a modem or serial line in the BBS era, and that makes them just as useful for moving files onto an Atari ST over a plain null-modem cable today.

Of the three, ZModem is the one I actually use — it's the fastest and least fiddly to get working. On the ST side that means `XYZ.TTP`, and on the PC side, TeraTerm's built-in ZModem support.

### Sending files back to the PC

Going the other way — ST to PC — just swaps the roles. In TeraTerm, choose *Receive a file* instead of *Send a file*, then on the ST side launch `XYZ.TTP` with the `-u` upload flag and the file to send, e.g. `XYZ.TTP -u C:\MYFILE.TXT`.

### Related on this site

- [Using Serial Cable and ZMODEM to Transfer Files from PC to ST]({% post_url 2016-02-13-use-rs232-serial-cable-and-zmodem-to-transfer-files-from-pc-to-st %})
- [How to Transfer Files from PC to Atari ST]({% link _howto/how-to-transfer-files-from-pc-to-atari-st.md %})
- [Ghostlink]({% link _software/ghostlink.md %})
