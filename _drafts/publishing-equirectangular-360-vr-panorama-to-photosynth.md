---
layout: post
title: Publishing VR Panoramas to Photosynth
date: '2016-10-12 07:54:00'
tags: [photography, vr panorama, facebook]
---

You've shot a 360 photo or VR panorama, and now you'd like to share it with your friends using Photosynth's excellent shading features. How do you do that?

Pano notes
====
 
This is for Windows. If you want Linux go checkout this website:
 
What is a .pano?
---
Microsoft proprietry format
https://bdhurkett.wordpress.com/2013/11/06/windows-8-1-panorama-files/
 
 
Overall guide
---
what am I trying to do?
http://www.reallyslick.com/blog/2015/09/making-cubemaps-from-overlapping-photos/
 
 
Download ActivePerl
---
http://www.activestate.com/
Add c:\perl64\bin to your path (if necessary - the package didn't seem to do this for me)
Add C:\Perl64\site\bin to your path (if necessary - the package didn't seem to do this for me either)
 
Install panotools script on windows
---
ppm install Panotools::Script
 
 
Install Hugin on Windows
---
Download the binary and extract somewhere
Put Hugin bin directory in your path
 
Use panotools to generate a convert script
---
erect2cubic --erect=your_equirectangular_image.jpeg --ptofile=convert_to_cubefaces.pto --face=face_size
erect2cubic --erect=fullpano.jpg --ptofile=convert.pto --face=1024
 
Execute the convert action using Hugin
---
nona -o convert convert.pto
 
This will produce 6 sequential images. For a horizontal cross, they are ordered as bottom, front, right, back, left, top (you can rename them to this if you prefer)
 
Convert to .pano file
---
 
Option 1. Use panoconverter (hacks together a .pano file using the blog page)
C:\Users\James\Downloads\PanoConverter
It doesn’t actually work right now in Windows 10, so probably best to take an existing pano file and hack it
Compress everything as a zipfile with no compression (Store Only)
 
Option 2. Use the Photosynth Photoshop plugin to upload to Photosynth, then download as .pano (actually, I don't even need the cube faces to do this! Move this to the top as the "easy way"!
http://research.microsoft.com/en-us/um/redmond/groups/ivm/PSPlugin/
 
Option 3. Use ICE
i. Create the ICE project file (hack this together) based on the File Format created by SynthExport (maybe write my own program for this)
ii. Import into ICE, then upload to Photosynth
iii. Download as pano