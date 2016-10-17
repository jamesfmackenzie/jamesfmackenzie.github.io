---
layout: post
title: Publishing VR Panoramas to Photosynth
date: '2016-10-12 07:54:00'
tags: [Photography, 360 Photo, VR Panorama, Facebook]
---

You've shot a 360 photo or VR panorama, and now you'd like to share it with your friends using Photosynth's excellent sharing features. How do you do that?

### Easy mode

Download and use the Photoshop plugin to upload the image to Photosynth

Use the Photosynth Photoshop plugin to upload to Photosynth, then download as .pano (actually, I don't even need the cube faces to do this! Move this to the top as the "easy way"!
http://research.microsoft.com/en-us/um/redmond/groups/ivm/PSPlugin/

### Hard mode (aka the free way)
 
This is for Windows. If you want a guide for Linux go and checkout this guy:
what am I trying to do?
http://www.reallyslick.com/blog/2015/09/making-cubemaps-from-overlapping-photos/

### Step 1. Download and Install Required Tooling

### Software Required

* Panotools
* Hugin
* MY HACKER PROGRAM TO GENERATE .SPJ FILE (probably fork the panoconverter and re-use their code)
* ICE

Panotools and Hugin require a bit of setup. LINK TO MY OTHER DOCUMENT
 
CONSIDER MOVING STEP 1 AND 2 TO A SEPARATE POST - CONVERTING EQUIRECTANGULAR PROJECTION TO CUBE FACES. OR MAYBE JUST DUPLICATE THE CONTENT

### Step 2. Convert your equirectangular image to cube faces

Use panotools to generate a convert script
---
erect2cubic --erect=your_equirectangular_image.jpeg --ptofile=convert_to_cubefaces.pto --face=face_size
erect2cubic --erect=fullpano.jpg --ptofile=convert.pto --face=1024
 
Use Hugin to execute convert and generate cube faces
---
nona -o convert convert.pto
 
This will produce 6 sequential images. For a horizontal cross, they are ordered as bottom, front, right, back, left, top (you can rename them to this if you prefer) ARE THEY REALLY THIS WAY ROUND EVERY TIME?
 
### Step 3. Use my hacker program to generate .SPJ file

MY HACKER PROGRAM TO GENERATE .SPJ FILE (probably fork the panoconverter and re-use their code)

### Step 4. Open SPJ file in ICE, publish to Photosynth
 
i. Create the ICE project file (hack this together) based on the File Format created by SynthExport (maybe write my own program for this)
ii. Import into ICE, then upload to Photosynth
iii. Download as pano