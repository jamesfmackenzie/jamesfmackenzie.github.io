---
layout: post
title: Delving Into DLNA
date: '2014-03-28 17:58:00'
summary: Last time, Play To allowed me to stream some (but crucially not all) of my media collection from PC to Xbox One ...
tags: [DLNA, Media, Streaming]
---

Last time, [Play To allowed me to stream some (but crucially not all) of my media collection from PC to Xbox One]({% post_url 2014-03-22-using-play-to-streaming-with-xbox-one %}).

In the hopes of a more comprehensive solution, I did some background reading on the underlying [DLNA technology](http://www.dlna.org/).

DLNA was formed back in 2003 with the stated goal of "using standard-based technology to make it easier for consumers to use, share and enjoy their digital photos, music and videos".

The Alliance is now more than 250 companies strong, with most major consumer electronics companies (minus Apple) as members. Thousands of "DLNA Certified" devices have been produced, falling into four broad categories:

* **Digital Media Server**. These store media and make it available on the home network.
* **Digital Media Players**. These can play content pulled from a Digital Media Server.
	* Unfortunately, this is exactly what the Xbox One *isn't*, due to the [lack of a System Video Player](http://o.canada.com/technology/gaming/major-nelson-says-dlna-streaming-support-is-coming-to-the-xbox-one-eventually/).
* **Digital Media Controllers**. These can find content on a Digital Media Server and push it to a Digital Media Renderer (see below).
* **Digital Media Renderers**. These can play content pushed from a Digital Media Controller.

In my case, I have:

* A **Digital Media Server** (my Windows 8 PC) which stores media and makes it available on the home network.
* A **Digital Media Controller** (also the PC) which finds the content and pushes it to a **Digital Media Renderer** (the Xbox One) via Play To.

### So what's the problem? Why doesn't Play To just work?

For reasons unknown, Microsoft Windows 8, in it's capacity as a Digital Media Controller:

* Doesn't support subtitles.
* Supports enumeration of some file formats (<code>.avi</code>, <code>.mp4</code>, <code>.wmv</code>) but not others (<code>.mkv</code>, <code>.vob</code>, <code>.divx</code>).

None of this seems to be changeable, so we're left with a streaming solution which works in some cases but not others.

### What next? How do we fix it?

One solution is to use a tool like [Handbrake](http://handbrake.fr/) to convert your TV/movie collection to a supported format. Handbrake even allows you to burn-in the subtitles if you need.

However, this solution is definitely sub-optimal for me. I've spent hours (days?) ripping my DVD collection to <code>.mkv</code> and don't want to convert it all again. In addition, I don't want to hard-burn the subtitles or suffer the quality loss inherent in transcoding.

We need another solution.
