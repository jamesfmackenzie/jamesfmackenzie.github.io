---
layout: post
title: Publishing VR Panoramas to Photosynth
date: '2016-10-28 07:54:00'
summary: You’ve shot a 360 photo or VR panorama, and now you’d like to share it with your friends using Photosynth’s excellent sharing features. Here’s how ...
tags: [How To, Photography, Photosynth, VR Photography]
---

You've shot a 360 photo or <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">VR panorama</a>, and now you'd like to share it with your friends using <a href="https://photosynth.net/" target="_blank">Photosynth</a>'s excellent sharing features. Here's how.

### If you have Photoshop or Photoshop Elements

If you have Photoshop or Photoshop Elements, there's a really easy way to do this:

1. Download and install the <a href="http://research.microsoft.com/en-us/um/redmond/groups/ivm/PSPlugin/" target="_blank">official Photosynth Export Plug-in for Photoshop</a>
2. Open your panoramic image
3. Select <i>Export -> Photosynth</i>
4. Select a projection. VR panoramas typically use <i><a href="https://en.wikipedia.org/wiki/Equirectangular_projection" target="_blank">Equirectangular</a> (Horizontal)</i>
5. Click <i>Publish</i>

![Export to PhotoSynth](/img/posts/photosynth-export.png)

### If you don't

If you don't have Photoshop or Photoshop Elements, get ready for hard mode! You can do this, but the process is a little convoluted.

### Step 1. Download and install required tooling

You'll need some panorama processing software. Hugin and Panotools are your best free options. You can [find my setup guide over here]({% post_url 2016-10-17-installing-hugin-and-panotools-on-windows %})

You'll also need software to do the Photosynth upload. <a href="http://research.microsoft.com/en-us/um/redmond/projects/ice/" target="_blank">Grab and install copy of Microsoft ICE</a>.

### Step 2. Convert your image to cube faces

Before you can upload your VR panorama to Photosynth, you'll need to convert it to <a href="https://en.wikipedia.org/wiki/Cube_mapping" target="_blank">cubic projection</a>. [Follow my guide]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %}) and you'll end up with 6 cube faces. Name them as follows:

* left.tif
* front.tif
* right.tif
* back.tif
* top.tif
* bottom.tif

If you're unsure which cube face is which, check my visual guide below:

![cube faces guide](/img/posts/cube-faces-guide.png)

### Step 3. Create ICE project file

In the same directory as your cube faces, create a new file called <code>pano.spj</code>. Copy and paste the following XML into it, then save and exit.

{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>
<stitchProject version="1.1">
  <stitchParams mapping="horizontalSpherical" motionModel="rotation3D" view3D="0 deg 0 deg 0 deg" />
  <sourceImages>
    <image src="front.tif">
      <camOrient3D eulerAngles="0 deg 0 deg 0 deg" focalLength="1" />
    </image>
    <image src="right.tif">
      <camOrient3D eulerAngles="0 deg 0 deg 90 deg" focalLength="1" />
    </image>
    <image src="back.tif">
      <camOrient3D eulerAngles="0 deg 0 deg 180 deg" focalLength="1" />
    </image>
    <image src="left.tif">
      <camOrient3D eulerAngles="0 deg 0 deg -90 deg" focalLength="1" />
    </image>
    <image src="top.tif">
      <camOrient3D eulerAngles="0 deg -90 deg 0 deg" focalLength="1" />
    </image>
    <image src="bottom.tif">
      <camOrient3D eulerAngles="0 deg 90 deg 0 deg" focalLength="1" />
    </image>
  </sourceImages>
</stitchProject>
{% endhighlight %}

### Step 4. Publish to Photosynth
 
Double click the .spj file to launch ICE. The panorama should load automatically, showing thumbnails of your cube faces:

![stitch a panorama](/img/posts/ice-1.png)

Ensure <i>Camera motion</i> is toggled to <i>Rotating motion</i> and hit <i>Next</i> three times to proceed to the <i>EXPORT</i> tab. Once there, expand the <i>Photosynth</i> panel:

![Publish to Photosynth](/img/posts/ice-publish-to-photosynth.png)

The very first time, you'll need to (possibly register and) login to Photosynth. After that, fill out some descriptive details and hit <i>Publish</i>. All going well, ICE will spawn a browser window and display your brand new, published VR panorama!

![Photosynth VR panorama](/img/posts/photosynth-published-panorama.png)

That's all there is to it! Pan around the image to your heart's content, then share the link with your friends!

### Other Posts in this Series
 
{% include vr-photography-series.md %}

### References

* <a href="http://www.reallyslick.com/blog/2015/09/making-cubemaps-from-overlapping-photos/" target="_blank">Making Cubemaps from Overlapping Photos</a>