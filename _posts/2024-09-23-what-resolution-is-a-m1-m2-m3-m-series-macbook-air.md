---
layout: post
title: "What is the M1 MacBook Air Resolution?"
date: '2034-09-23 15:55:00:00'
summary: I recently picked up a MacBook Air, and got thoroughy confused by the screen resolution.
image: macbook-air-resolution-system-info.png
tags: [Posts]
---

I recently picked up a MacBook Air, and got thoroughy confused by the screen resolution.

Apple's marketing literature and system settings indicate a screen resolution of 2560x1664:

![MacBook Air Resolution](/img/posts/macbook-air-resolution-system-info.png)

However other applications identify the resolution as 2940x1912 or even 1470x956. To understand why, why need to understand HiDPI.

### What is HiDPI?

Insert blurb here


### Why does HiDPI exist?

It didn't used to, but screen resolution went really high so scaling needed to be introduced



### What does it all mean?

So with HiDPI, we have two resolutions:

* The actual resolution
* The "looks like" resolution

Apple's "default" solution is usually to render twice the amount of pixels from the "looks like" resolution.

So with the M2 MacBook Pro, we have:

* Actual resolution: 3024x1964 (254ppi)
* Looks like resolution: 1512x982 (half)

Following this approach with the M2 MacBook Air, we *should* have:

* Actual resolution: 2560x1664 (227ppi)
* "Looks like" resolution: 1280x832 (half)

(consider doing the above as a table)

*However*, 1280x832 is relatively low, and would make everything look huge.

Apple's solution is to "pretend" the resolution is higher, and use a frame buffer resolution of 2940x1912.

When we half this, we get a default "looks like" resolution of 1470x956 - which gives us enough space.

*However* of course this doesn't match the native resolution of 2560x1664. So ultimate the resolution is downscaled to 2560x1664 for display.

CONFUSING!

(tidy this article up)
