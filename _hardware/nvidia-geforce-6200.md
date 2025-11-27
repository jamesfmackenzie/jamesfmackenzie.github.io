---
layout: post
title: Nvidia GeForce 6200
summary: 
date: '2024-08-29 11:33:00'
tags: [Graphics Cards, Nvidia Graphics, PC]
---


### Hardware

I have a GeForce 6200 PCI version. It's a nice passive card and one of the (relatively) rare PCI variants.

One observation from my experiments with a PCI backplane: although the card is keyed as both 3.3v and 5v PCI, the card will *not* work in a machine with only 3.3v. 

The card will not initialise and the machine will not post.

To get it working you need an ATX PSU that supplies 5v.


### Drivers

For Win9x (Win98SE in my case), I used the 81.98 December 2005 drivers from Phil's Computer lab:

https://www.philscomputerlab.com/nvidia-9x-graphics-drivers.html

Unfortunately performance was disappointing with big frame stutters.

For WinXP, I used two drivers:

93.71 October 2006 Forceware from Phil's Computer lab:

https://www.philscomputerlab.com/nvidia-xp-graphics-drivers.html

307.83 Feb 2013 GeForce Driver from nvidia:

https://www.nvidia.com/en-us/drivers/details/57493/

Both perform *significantly* better than the Windows 98 driver.

