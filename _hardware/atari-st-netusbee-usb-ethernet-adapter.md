---
layout: post
title: Atari ST NetUSBee
summary: My take on the NetUSBee, a cartridge-port adapter that gives the Atari ST Ethernet and USB — the quickest way to move files onto the machine, and enough to get it browsing the web.
date: '2024-08-29 11:33:00'
tags: [Atari ST, Peripherals]
---

![Connecting a NetUSBee to an Atari ST](/img/atari_st_netusbee.jpg){: width="680"}

The NetUSBee is an expansion adapter that plugs into the Atari ST's cartridge port and adds an Ethernet port (and USB). It is, in my experience, the quickest and most convenient way to get files onto an ST — and with the right software it will also put the machine on the network properly.

### What it is

The adapter sits in the cartridge port, usually on the left-hand side of the ST, and exposes an RJ45 socket. From there you can connect it to a switch or router, or directly to a PC's network card.

### File transfer

The easy route is a tool called **uip-tool** (`UIPV43.TOS`): a single click-and-run program that brings up the network stack and serves a small web interface from the ST itself. You note the IP address it reports, open that address in any browser on your PC, and drag and drop files straight onto the ST's drives. No separate drivers or TCP/IP stack to install.

### Web browsing

With a full setup — TOS Ethernet drivers plus the **STinG** TCP/IP stack — the ST can also browse the web using **Crystal Atari Browser (CAB)**. It is slow and there is no CSS support, so most of the modern web is out, but simple and older sites do load. Adding an ET4000 graphics card to reach 1024×768 in 256 colours makes the experience noticeably better.

### Why I rate it

For getting data onto the machine it is the fastest and least fussy option I have used — faster than a serial cable, and simpler to live with than partitioning an SD card. The fact that the same adapter also enables genuine networking and web access is a bonus that the [PARCP-USB]({% link _hardware/parcp-usb-adapter.md %}) and floppy routes cannot match.

### Related on this site

- [Using Ethernet / NetUSBee to Transfer Files from PC to ST]({% link _howto/how-to-use-ethernet-netusbee-to-transfer-files-from-pc-to-st.md %})
- [How to Browse the Web on Atari ST]({% link _howto/how-to-browse-the-web-on-atari-st.md %})
- [Atari ST]({% link _hardware/atari-st.md %})
- [PARCP-USB Adapter]({% link _hardware/parcp-usb-adapter.md %})
