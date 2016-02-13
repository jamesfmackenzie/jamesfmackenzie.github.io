---
layout: post
title: Plex to the Rescue
date: '2014-04-03 17:49:00'
categories: stream_video_from_pc_to_xbox_one
---

Last time, I did some background research on the [DLNA Technology underlying Windows Play To]({% post_url 2014-03-28-delving-into-dlna %}), with the hopes of finding a general solution for Windows 7/8 to Xbox One streaming.

Unfortunately I hit a problem. Windows supports Play To streaming of some file formats (<code>.avi</code>, <code>.mp4</code>, <code>.wmv</code>) but not others (<code>.mkv</code>, <code>.vob</code>, <code>.divx</code>). **And it can't be changed**.

So the only solution is to use supported formats - i.e. convert your entire media library to (for example) <code>.mp4</code>. Ugh.

***But wait***. *What if we converted the unsupported files as needed, on-the-fly? That wouldn't be too bad, right?*

It turns out there's already software that does this.

### Switching Media Server

* Up til now, I've been using Windows' built-in media sharing capability, but there's [plenty of other Digital Media Server software out there](http://en.wikipedia.org/wiki/Comparison_of_UPnP_AV_MediaServers): Mezzmo, Plex Media Server, PS3 Media Server, Serviio, TVersity to name just a few.
* Even better, some of these Media Servers support real time [transcoding](http://en.wikipedia.org/wiki/Transcoding). *If I can convince the Media Server to convert our unsupported files to supported ones on-the-fly,* ***we'll be all set!***

### Plex to the rescue

I probably could've chosen any of the Media Servers mentioned above, but I chose to investigate Plex for two reasons:

1. I have some familiarity with it.
2. I know it supports [DLNA media profiles](https://forums.plex.tv/index.php/topic/42523-writing-profiles-for-dlna-devices/). These are essential for what we want to achieve.

### What are DLNA media profiles?

From Plex's website:

> "DLNA is a rather broad and flexible standard, and different devices interpret the standard in different ways. Some by design, some due to device bugs accident. This makes it impossible for a media server that supports DLNA to provide a one-size-fits-all implementation of the standard. Instead, the server [via media profiles] must adapt to different clients by recognizing them and changing its behavior accordingly."

So what next? My idea is to create two new client profiles:

* **One for the Windows Digital Media Controller.**
	* We'll tell Plex that this client only supports those file formats that Windows allows Play To for (i.e. <code>.mp4</code>, <code>.avi</code> etc). This means Plex will convert any other file formats (e.g. <code>.mkv</code>) to supported ones on-the-fly, in theory allowing us to use Play To with almost anything.

* **One for the Xbox One.**
	* Here we'll tell Plex which streaming parameters the Xbox One supports, so any files it doesn't handle will be converted ahead of time.