---
layout: post
title: Convert Equirectangular Projection to Cube Faces
date: '2016-10-12 07:54:00'
tags: [Photography, 360 Photo, VR Panorama]
---

### Software Required

* Panotools
* Hugin

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