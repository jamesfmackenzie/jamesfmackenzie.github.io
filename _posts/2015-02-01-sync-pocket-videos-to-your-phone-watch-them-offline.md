---
layout: post
title: Sync Web Videos to Your Tablet or Phone, Watch Them Offline
date: '2015-02-01 22:44:56'
summary: There’s so much good web content out there - hard hitting news, educational articles and insightful blogs. And services like Pocket sync this content to your mobile device, making it available wherever (and whenever) you like - even without cellular data ...
image: 2015-01-03-00_36_48-Downloaded-Videos.png
tags: [Automation, How To, Lifehacks, Productivity]
---

There's so much good web content out there - hard hitting news, educational articles and insightful blogs. And services like <a href="http://wwww.getpocket.com/" target="_blank">Pocket</a> sync this content to your mobile device, making it available wherever (and whenever) you like - even without cellular data.

But there's a big gap. Why can't you download and cache web ***videos*** for offline viewing? Wouldn't it be great to watch a webinar or conference talk on the plane?

Here's how.

### How it's going to work

For the avoidance of confusion:

* When you save a link to Pocket
* If the link contains a video
* The video will be synced to your mobile device

### Prerequisites

* **A PC** - we'll use this to stage and prepare the videos for syncing to the phone/tablet. These instructions are for Windows, but the tooling supports multiple platforms - Linux and OS X will work with minor tweaks.
* **A smartphone/tablet** - iPhone, iPad, Android, Windows Phone - all will work.
* **A Pocket account** - these are free. You can sign up over <a href="https://getpocket.com/" target="_blank">here</a>.
* **A Plex Pass membership** - we'll use the rather wonderful <a href="https://plex.tv/" target="_blank">Plex</a> to sync all the videos from PC to phone/tablet. The sync feature ("<a href="https://support.plex.tv/hc/en-us/articles/201082477-Quick-Guide-to-Plex-Sync" target="_blank">Plex Sync</a>") requires a <a href="https://plex.tv/subscription/about" target="_blank">Plex Pass</a> membership, which costs £3.99 per month, £31.99 per year or £119.99 lifetime.

### Step 1. Download Pocketed videos to your PC

Before you can sync videos to the phone you'll need to download them to your PC. Follow my previous guide: <a href="/download-pocket-videos-to-your-pc/">how to automatically download Pocketed videos to your PC</a>.

Make a note of your Downloaded Videos folder location (in my case <code>D:\Videos\Downloaded Videos</code>). You'll need this later.

![](/img/posts/2015-01-03-00_36_48-Downloaded-Videos.png)

### Step 2. Download and install Plex Media Server on your PC

Plex Media Server is available for Windows, OS X, Linux and even NAS. Full installation instructions are available <a href="https://support.plex.tv/hc/en-us/articles/200288586" target="_blank">here</a>.

### Step 3. Create a new Plex library, add your Downloaded Videos folder

* In the Plex Media Manager, click "Add Library". Set the media type to "Home Videos":

![](/img/posts/2015-02-01-21_51_24-Plex.png)

* Give the library a name. I chose "Downloaded Videos":

![](/img/posts/2015-02-01-21_51_49-Plex.png)

* Add your Downloaded Videos folder to the library (you made a note of the location in Step 2):

![](/img/posts/2015-02-01-21_52_35-Plex.png)

![](/img/posts/2015-02-01-21_53_10-Plex.png)

* Complete the library setup by clicking "Add Library":

![](/img/posts/2015-02-01-21_53_37-Plex.png)

### Step 4. Download and install the Plex client on your phone/tablet

Plex is available on multiple platforms:

* You can purchase the iOS version <a href="https://appsto.re/gb/jMX2w.i" target="_blank">here</a>. It costs £2.99
* You can find the Android version <a href="https://play.google.com/store/apps/details?id=com.plexapp.plex&hl=en_GB" target="_blank">here</a>. It's free for PlexPass members
* You can download for Windows Phone <a href="http://www.windowsphone.com/en-gb/store/app/plex/4854f786-ea4b-4db0-b67a-4645c04225d4" target="_blank">here</a>. It costs £3.49
* Surface users? Plex for Windows 8 is available <a href="http://apps.microsoft.com/webpdp/app/647bfcf7-7f87-4a72-ad86-2e6274f969e3" target="_blank">here</a>. It also costs £3.49, but is a cross-purchase with the Windows Phone edition (you only have to buy one to get both)

### Step 5. Configure Plex Sync to automatically sync your videos

Last step. We need to configure Plex to sync our Downloaded Videos from PC to the phone/tablet. This is easiest from the mobile device. Instructions for iOS below.

* From the Download Videos library, hit the Plex Sync button (downward-facing arrow, top right)

<img src="/img/posts/IMG_0174.PNG" style="width: 480px; display: block; margin: 0 auto 0 auto;" />

* Choose your Plex Sync parameters. I went with 10 Unwatched Videos, meaning I'll always have 10 fresh items to watch.

<img src="/img/posts/IMG_0175.PNG" style="width: 480px; display: block; margin: 0 auto 0 auto;" />

Plex will now automatically sync your Downloaded Videos whenever you're on a Wi-Fi network. To save bandwidth, cellular sync is disabled by default, but you can force it. More information available <a href="https://support.plex.tv/hc/en-us/articles/201053678-Sync-Media-to-a-Device" target="_blank">here</a>.

### Step 6. Enjoy your videos! Even with no cellular reception

That's it! Keep Pocket topped up and videos will trickle onto your mobile device, ready for consumption whenever you have a spare moment. Now back to that Airplane journey ...

![](/img/posts/IMG_0177.PNG)