---
layout: post
title: Update: Sync Web Videos to Your Tablet or Phone, Watch Them Offline
date: '2015-08-30 21:43:56'
categories: syncing_web_video
---

6 months on from my [original solution](/sync-pocket-videos-to-your-phone-watch-them-offline/), I've evolved a much leaner process for watching web video offline. Here's the experience:

1. Browse the web, find a video you want to watch offline
2. Email the page URL or video URL to a special email address
3. The video is downloaded and synced to your phone

The implementation:

1. An instance of [EmailWatcher](/2015/08/01/email-watcher/) listens on a special email address
2. When an email arrives, it scrapes the email address for URLs
3. Any URLs found are handed off to (<a href="https://rg3.github.io/youtube-dl/" target="_blank">youtube-dl</a>) for downloading
4. Once downloaded, videos are synced to the phone using the free (and excellent) <a href="https://getsync.com/" target="_blank">BitTorrent Sync</a>

### To Get It Working

1. Download video downloader from GitHub here
<!--
todo:
Upload video downloader to GitHub, insert link here
-->
2. Download <a href="https://rg3.github.io/youtube-dl/" target="_blank">youtube-dl</a>. Unzip the executable to the same directory as the video-downloader
3. Configure the video downloader
<!--
todo: insert configuration instructions
-->

