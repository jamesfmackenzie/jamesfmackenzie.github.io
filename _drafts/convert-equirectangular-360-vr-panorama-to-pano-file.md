---
layout: post
title: Convert Equirectangular Projection to .Pano File
date: '2016-10-22 19:03:00'
tags: [Photography, 360 Photo, VR Panorama, How To]
---

INSERT 

VR panoramas (aka "360" photos) are super cool. And if you're on the Windows platform, there's native support in the form of  [.pano files]({% post_url what-are-pano-files-sluggified %}).

But what if your VR image is in another common format, like <a href="https://en.wikipedia.org/wiki/Equirectangular_projection" target="_blank">equirectangular projection</a>? Can you convert it to a .pano? Well yes, you can! Here's how.

### Option 1. Use Photosynth

Definitely the quickest and easiest way. You need to:

1. Publish your equirectangular projection to Photosynth

You can keep them private if you like ("Unlisted"?)
LINK TO MY EXISTING ARTICLE ON THIS

2. Download the image from Photosynth as a .pano

INSERT SCREENSHOT OF PHOTOSYNTH DOWNLOAD OPTION

### Option 2. Direct conversion

Don't trust Photosynth with your data? Or just intellectually curious? If you'd prefer to build the .pano file yourself, you can. The process is much more convoluted than the above; here are some resources to get you started:

* The .pano file is just an OPC container with the images stored as cube faces + some metadata

LINK TO MY EXISTING ARTICLE ON PANO FILES

* You can convert your image to cube faces using Hugin and Panotools

LINK TO MY EXISTING ARTICLE ON CUBE FACE CONVERSION

* I was able to get this working in a simple fashion by:

1. Taking an existing .pano file
2. Renaming as .zip
3. Generating cube face data of different sizes
4. Replacing the old images with the new cube face data
5. Zipping it back up (no compression)
6. Renaming back to .pano

I SHOULD PUT THIS IN A SEPARATE FILE / EXPLORATION

* There is an official tool available to generate .pano files from cube face data

LINK TO BENEDICT HURKETT BLOG

* This is covered in much more detail by Benedict Hurkett

