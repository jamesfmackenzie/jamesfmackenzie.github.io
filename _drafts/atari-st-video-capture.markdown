---
layout: post
title: What cables should i use?
date:
categories: atari_st_video_quality
---

* The Micomsoft card - "Rolls-Royce" solution that supports 15khz
* RGB SCART and Sync Strike
* Atari ST is 320x240 but encodes onto a PAL signal which has vertical resolution of 576 lines ... And horizontal scanlines which output at around 720 lines (talk a bit about horizontal resolution)
* "Simple option - use OBS" at 720x288 and stretch to 720x576
* BUT stretching uses bilinear algorithm, which won't give you the best sharpness
* To get the best sharpness, capture with something like VirtualDub which can resize using a "nearest neighbour" algorithm and retain your sharpness
* VirtualDub mostly meant for conversion - the "live capture" window is laggy - you wouldn't be able to play a game from it
* So it's better to capture video in a high-end format from a tool with a good preview window. Enter AmarecTV
* Then once you have the file (keep it as high end as possible), you can resize in VirtualDub
* Preparing for the web - you'll want to go for 1080p and crop it a little
