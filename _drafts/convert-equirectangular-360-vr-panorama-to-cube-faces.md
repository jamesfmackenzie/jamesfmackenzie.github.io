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


C:\Temp\pano>erect2cubic --erect=equirectangular-pano.png --ptofile=convert_to_c
ubefaces.pto --face=1024

C:\Temp\pano>dir /b *.pto
convert_to_cubefaces.pto



C:\Temp\pano>nona -convert convert_to_cubefaces.pto

C:\Temp\pano>dir /b *.tif
nvert0000.tif
nvert0000_x.tif
nvert0000_y.tif
nvert0001.tif
nvert0001_x.tif
nvert0001_y.tif
nvert0002.tif
nvert0002_x.tif
nvert0002_y.tif
nvert0003.tif
nvert0003_x.tif
nvert0003_y.tif
nvert0004.tif
nvert0004_x.tif
nvert0004_y.tif
nvert0005.tif
nvert0005_x.tif
nvert0005_y.tif


![Output cubefaces](/img/posts/cubefaces.png)
![Execute transformation](/img/posts/2016-10-17-nona-command.png)
![Specify transformation parameters](/img/posts/2016-10-17-erect2cubic-command.png)
![Equirectangular source image](/img/posts/equirectangular-pano.png)
