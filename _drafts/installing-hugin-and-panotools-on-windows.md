---
layout: post
title: Installing Hugin and Panotools on Windows
date: '2016-10-12 07:54:00'
tags: [Photography, Panorama, How To]
---

<a href="http://hugin.sourceforge.net/" target="_blank">Hugin</a> and <a href="http://panotools.sourceforge.net/" target="_blank">Panotools</a> are two hugely useful tools for image stitching and panorama processing in general.

Unfortunately getting them installed and configured on Windows is a bit fiddly. Here's how.
 
### Step 1. Install ActiveState Perl

Available either as .exe (guided install) or zipfile, you can always find the latest version of ActiveState Perl <a href="http://downloads.activestate.com/ActivePerl/releases" target="_blank">here</a>.

Whichever format you choose, ensure both the <code>perl\bin</code> and <code>perl\site\directories</code> are in your <a href="https://en.wikipedia.org/wiki/PATH_(variable)" target="_blank">PATH</a> post-install:
 
![Perl bin directories are in the Path](/img/posts/perl-env-vars.png)

![Perl bin directories are in the Path](/img/posts/perl-env-vars-2.png)

### Step 2. Test Perl is installed correctly

Open a command prompt type <code>perl -v</code>. You should see something similar to the following:

![A successful Perl test](/img/posts/perl-version-test.png)

### Step 3. Install Panotools Script

Back in the command prompt, type <code>ppm install Panotools::Script</code>. <a href="https://en.wikipedia.org/wiki/Perl_package_manager" target="_blank">Perl Package Manager</a> should download and Install Panotools Script:

![Installing Panotools Script](/img/posts/install-panotools.png)

### Step 4. Test Panotools Script is installed correctly

Still in the command prompt, type <code>panostart</code>. The following help text should be displayed:

![Panotools Script is installed correctly](/img/posts/panotools-test.png)
 
### Step 5. Install Hugin

Available either as a self-extracting .exe or archive, you can download Hugin from <a href="https://sourceforge.net/projects/hugin/files/hugin/hugin-2015.0/" target="_blank">here</a>.

After downloading and extracting, add the Hugin 

Download the binary and extract somewhere
Put Hugin bin directory in your path

### Step 4. Verify

Confirm perl is working correctly:

Add c:\perl64\bin to your path (if necessary - the package didn't seem to do this for me)
Add C:\Perl64\site\bin to your path (if necessary - the package didn't seem to do this for me either)
Why do I need both?

Confirm Panotools is working correctly by running the following command:

foo

Confirm Hugin is working correctly by running the following


Verify 
 
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