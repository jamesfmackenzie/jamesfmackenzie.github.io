---
layout: post
title: Convert Equirectangular Projection to .Pano File
date: '2016-10-30 13:17:00'
summary: With native support in the form of .pano files, the VR Photography experience in Windows is great ...
tags: [Photography, 360 Photo, VR Panorama, How To]
---

With native support in the form of [.pano files]({% post_url 2016-10-29-what-are-pano-files %}), the <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">VR Photography</a> experience in Windows is great. 

But how can you bring other VR images into the ecosystem? For example those shot and stored as <a href="https://en.wikipedia.org/wiki/Equirectangular_projection" target="_blank">equirectangular projections</a>? Can you convert them to .pano?

The answer is yes! Here's how.

### Option 1. Use Photosynth

Definitely the quickest and easiest way. You need to:

1. [Publish your equirectangular projection to Photosynth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %}). If you're worried about privacy, you can mark it as <i>Unlisted</i> and delete afterwards.
2. From your published Synth, select the <i>Export</i> option. After a minute-or-two (you may need to refresh the page), you'll see see a <i>Download</i> option. Click to download your .pano!

![Export from Photosynth](/img/posts/export-from-photosynth.png)

### Option 2. Direct conversion

Don't trust Photosynth with your data? Or just intellectually curious? If you'd prefer to build the .pano file yourself, you can. The process is much more convoluted than the above; here are some resources to get you started:

* The .pano file is just an <a href="https://en.wikipedia.org/wiki/Open_Packaging_Conventions" target="_blank">OPC container</a>. You can <a href="{% post_url 2016-10-29-what-are-pano-files %}#panoarchive">rename it to a .zip and extract the contents into a folder</a>
* If you look inside, you'll see the VR image stored as <a href="{% post_url 2016-10-29-what-are-pano-files %}#cubefaces">cube faces plus some metadata</a>
* You can [generate your own cube faces from an existing equirectangular panorama]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %})
* <a href="{% post_url 2016-10-29-what-are-pano-files %}#cubedetail">Several versions of each cube face are stored at increasing levels of detail</a>
* Each cube face is <a href="{% post_url 2016-10-29-what-are-pano-files %}#cubetiles">divided into tiles of a set size</a>
* You can generate these tiles using <a href="https://github.com/bdhurkett/PanoConverter" target="_blank">Ben Hurkett's PanoConverter</a>
* Once you're done, you can <a href="{% post_url 2016-10-29-what-are-pano-files %}#cubezip">use 7-zip to reassemble your work back into a .pano file</a>

### References

* <a href="https://bdhurkett.wordpress.com/2015/02/12/making-pano-files-the-hard-way/" target="_blank">Making .pano files the hard way</a>
