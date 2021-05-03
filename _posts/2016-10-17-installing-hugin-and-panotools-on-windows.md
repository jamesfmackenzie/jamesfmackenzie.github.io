---
layout: post
title: Installing Hugin and Panotools on Windows
date: '2016-10-17 20:36:00'
summary: Hugin and Panotools are two hugely useful tools for image stitching and panorama processing in general ...
tags: [Photography, VR Photography, How To]
---

<a href="http://hugin.sourceforge.net/" target="_blank">Hugin</a> and <a href="http://panotools.sourceforge.net/" target="_blank">Panotools</a> are two hugely useful tools for image stitching and panorama processing in general.

Unfortunately getting them installed and configured on Windows is a bit fiddly. Here's how.
 
### Step 1. Install ActiveState Perl

Available either as .exe (guided install) or zipfile, you can always find the latest version of ActiveState Perl <a href="http://downloads.activestate.com/ActivePerl/releases" target="_blank">here</a>.

Whichever format you choose, ensure both the <code>perl\bin</code> and <code>perl\site\bin</code> directories are in your <a href="https://en.wikipedia.org/wiki/PATH_(variable)" target="_blank">PATH</a> post-install:
 
![Perl bin directories are in the Path](/img/posts/perl-env-vars.png)

### Step 2. Test Perl is installed correctly

Open a command prompt type <code>perl -v</code>. You should see something similar to the following:

![A successful Perl test](/img/posts/perl-version-test.png)

### Step 3. Install Panotools Script

Back in the command prompt, type <code>ppm install Panotools::Script</code>. <a href="https://en.wikipedia.org/wiki/Perl_package_manager" target="_blank">Perl Package Manager</a> should download and Install Panotools Script:

![Installing Panotools Script](/img/posts/install-panotools.png)

### Step 4. Test Panotools Script is installed correctly

Still in the command prompt, type <code>panostart</code>. The following help text should be displayed:

![Panotools Script is installed correctly](/img/posts/panotools-test.png)
 
### Step 5. Install and configure Hugin

Hugin is available as an .msi. You can download the latest version <a href="https://sourceforge.net/projects/hugin/files/hugin/hugin-2016.2/" target="_blank">here</a>. Download the version appropriate for your platform and double-click to install.

Once installation completes, add the Hugin bin directory to your PATH:

![Hugin bin directory is in the Path](/img/posts/hugin-env-vars.png)

### Step 6. Test Hugin command line is working correctly

Open a command prompt and type <code>nona</code>. You should see the following help text:

![Hugin bin directory is in the Path](/img/posts/nona-test.png)

That's it!

### Other Posts in this Series
 
{% include vr-photography-series.md %}