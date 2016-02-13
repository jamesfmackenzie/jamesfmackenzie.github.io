---
layout: post
title: Using Play to Streaming With Xbox One
date: '2014-03-22 17:36:00'
categories: stream_video_from_pc_to_xbox_one
---

Earlier this week, I asked myself the question [Can I stream video from PC to Xbox One?]({% post_url 2014-03-19-can-i-stream-video-from-pc-to-the-xbox-one %})

After a fruitless 10 minutes hunting around the Xbox One UI for a System Video Player (or something like it), I took to the Internet. It turns out such a thing [doesn't exist](http://o.canada.com/technology/gaming/major-nelson-says-dlna-streaming-support-is-coming-to-the-xbox-one-eventually/). Oops.

I did, however, find and enable a promising "Allow Play To streaming" option tucked away inside the Preferences menu.

![Allow Play To streaming](/img/posts/allowplaytostreaming.jpg)

So what is "Play To streaming"? Here's what Microsoft [has to say about it](http://support.xbox.com/en-GB/xbox-one/system/change-console-preferences):

> "Enable this if you want to play video and music on your Xbox One from the Windows 8 and 8.1 Share charm and other Play To compatible devices."

Promising indeed! Time for a bit of background reading.

### Windows Play To streaming

So, it turns out both Windows 7 and Windows 8 allow you right click on media files and "Play To" another device on your home network.

![Play To in action](/img/posts/2014_03_18_00_20_19_Sample_Video.png)

In Microsoft's own words:

> "You can use the Play To feature to stream video, music, or picture files stored on your computer to a separate playback device on your home network. That device could be another computer, TV, or stereo connected to your network."

You [wouldn't know it](http://windows.microsoft.com/en-GB/windows7/using-the-play-to-feature-to-stream-media) from [their literature](http://windows.microsoft.com/en-gb/windows-8/use-play-to), but Play To actually conforms to the [Digital Living Network Alliance (DLNA)](http://www.dlna.org/) standard. Any device which meets the DLNA interoperability rules should be a capable target for Play To - in this case the Xbox One.

So I gave it a try.

### Testing out Play To

First, the good news. Most of the <code>.mp4</code>, <code>.avi</code> and <code>.wmv</code> files I threw at the Xbox One worked great. I was able to push them directly to the Xbox One without many hiccups.

Second, the bad. Unfortunately there are a few more of these:

* Some videos were choppy, stuttered badly or didn't play at all.
* Subtitles (if present) aren't displayed on the One and there's no way to enable them.
* The Play To context menu item doesn't appear for some file formats, notably <code>.mkv</code>.

![Play To missing for .mkv files](/img/posts/2014_03_18_00_21_20_Sample_Video.png)

I think some more reading on DLNA is required.