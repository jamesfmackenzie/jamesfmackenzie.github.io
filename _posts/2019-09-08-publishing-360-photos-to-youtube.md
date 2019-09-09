---
layout: post
title: Publishing VR Panoramas to YouTube
date: '2019-09-08 21:43:00'
tags: [Photography, 360 Photo, VR Panorama, YouTube, How To]
---

YouTube has built-in support for <a href="https://support.google.com/youtube/answer/6178631?hl=en" target="_blank">360° videos</a>, allowing you to tilt and pan around a scene, creating the fully immersive experience of "really being there"

With a little coercion, VR panoramas or 360° photos can be uploaded too. Here's how:

### 1. Source or shoot your own VR panorama

Either <a href="https://www.google.co.uk/search?q=equirectangular+vr+photo&rlz=1CDGOYI_enGB653GB654&hl=en-GB&prmd=ivn&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiMi6_uptLPAhXFECwKHYiRDOAQ_AUIBygB&biw=414&bih=660" target="_blank">head to Google</a> or shoot your own VR panorama. The stipulations are:

* The image must use an <a href="https://en.wikipedia.org/wiki/Equirectangular_projection" target="_blank">equirectangular</a> projection
* The image must have a 2:1 aspect ratio (i.e. twice as wide as it is high)
* The higher resolution, the better. YouTube recommends at least 7168x3584 or higher, up to 8192x4096

For more details see Google's official documentation <a href="https://support.google.com/youtube/answer/6178631?hl=en" target="_blank">here</a>

### 2. Convert the VR panorama to video

You need to convert the image to video. FFmpeg is the recommended tool. Head <a href="https://ffmpeg.org/download.html" target="_blank">here</a> to download a copy for your system

These resolutions we're working with exceed the max resolution for H.264, so you'll need to use the H.265/HEVC codec. To start the encode run, invoke:

{% highlight bash %}
{% raw %}
ffmpeg -loop 1 -i c:\temp\nasa.jpg -t 300 -vcodec libx265 -crf 15 -pix_fmt yuv420p c:\temp\out.mp4
{% endraw %}
{% endhighlight %}

The parameters:

* t = Length of the video in seconds
* vcodec = The video codec (H.265)
* crf = Video quality. Lower is better. 15 is very high quality 

More more advanced syntax, see the <a href="https://ffmpeg.org/ffmpeg-all.html#image2-1" target="_blank">official FFmpeg documentation</a>

### 3. Add 360° video metadata 
	
You'll need to add special metadata so that YouTube recognises the 360° video and enables the pan/tilt controls. Luckily Google provides a special tool for this:

1. Download and extract the <a href="https://github.com/google/spatial-media/releases/tag/v2.1" target="_blank">Spatial Media Metadata Injector</a>
2. Run `gui.py` (it's inside the spatialmedia directory)

![](/img/posts/spatial_media_metadata_injector_1.png)

![](/img/posts/spatial_media_metadata_injector_1.png)

### 4. Upload to YouTube

No special guidance required here. Just upload as a regular video. After some extended processing time YouTube will enable the 360° features

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/W1rKkSokIXU?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

Notes:

* Chrome was slow for me
* Edge and Firefox much faster but did not support 8K video


