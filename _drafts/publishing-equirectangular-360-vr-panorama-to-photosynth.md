---
layout: post
title: Publishing VR Panoramas to Photosynth
date: '2016-10-12 07:54:00'
tags: [Photography, 360 Photo, VR Panorama, Facebook]
---

You've shot a 360 photo or VR panorama, and now you'd like to share it with your friends using Photosynth's excellent sharing features. Here's how.

### If you have Photoshop or Photoshop Elements

If you have Photoshop or Photoshop Elements, there's a really easy way to do this:

1. Download and install the <a href="http://research.microsoft.com/en-us/um/redmond/groups/ivm/PSPlugin/" target="_blank">official Photosynth Export Plug-in for Photoshop</a>
2. Open your panoramic image
3. Select <i>Export -> Photosynth</i>
4. Select a projection. VR panoramas typically use <i><a href="https://en.wikipedia.org/wiki/Equirectangular_projection" target="_blank">Equirectangular</a> (Horizontal)</i>
5. Click <i>Publish</i>

### If you don't

If you don't have Photoshop or Photoshop Elements, get ready for hard mode! You can do this, but the process is a little convoluted.

### Step 1. Download and install required tooling

You'll need some panorama processing software. Hugin and Panotools are your best free options. You can find my setup guide over here
INSERT LINK 2016/10/17/installing-hugin-and-panotools-on-windows/

You'll also need something to upload to Photosynth. <a href="http://research.microsoft.com/en-us/um/redmond/projects/ice/" target="_blank">Grab and install copy of Microsoft ICE</a>.

### Step 2. Convert your image to cube faces

Before you can upload your VR panorama to Photosynth, you'll need to convert it to <a href="http://wiki.panotools.org/Cubic_Projection" target="_blank">cubic projection</a>. Follow my guide over here, and you'll end up with 6 cube faces. Name them as follows:

INSERT LINK TO MY GUIDE

* left.tif
* front.tif
* right.tif
* back.tif
* top.tif
* bottom.tif

If you're unsure which cube face is which, check my visual guide below:

CREATE AND INSERT VISUAL GUIDE ON HOW EQUIRECTANGULAR PROJECTION MAPS TO CUBE FACES

ALSO SEE IF I CAN DO THIS WITHOUT CUBIC PROJECTION BY SPLITTING AN EQUIRECTANGULAR PROJECTION IN HALF

### Step 3. Create ICE project file

In the same directory as your cube faces, create a new file called <code>pano.spj</a>. Copy and paste the following code into it:

INSERT CODE READ OUT FOR PANO.SPJ. SHOULD I ALSO PUT IT IN GITHUB OR A GIST?

### Step 4. Publish to Photosynth
 
Double click the .spj file to launch ICE. The panorama should load automatically.

Click next, next and then export to Photosynth. The first time you do this you'll need to enter your Photosynth credentials.

INSERT SCREENSHOT OF ICE PHOTOSYNTH UPLOAD

### References
http://www.reallyslick.com/blog/2015/09/making-cubemaps-from-overlapping-photos/