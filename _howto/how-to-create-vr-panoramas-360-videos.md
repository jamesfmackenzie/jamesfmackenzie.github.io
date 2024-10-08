---
layout: post
title: All You Need to Know about 360 VR Photos
date: '2016-11-02 08:25:00'
summary: Whether it’s a view from the highest holiday vista or showing off your new bathroom, no photo recreates the feeling of actually being there like a 360 VR panorama. Pan left, right, up, down, or even swivel right around to take in the whole view ...
image: church-pano-equirectangular.jpg
tags: [Photography, VR Photography]
---


<a name="Shooting and Sharing VR Photos">
## Shooting and Sharing VR Photos

Status | Completed November 2016
Goal | Learn how to shoot, interactively view and share VR photos

Ever seen one of <a href="https://flickr.com/photos/136386099@N02/21597873406/" target="_blank">these photos</a> where you can interactively zoom and pan around? They're known as <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">360° or VR photos</a>.

More formally, <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">VR photography</a> (Virtual Reality photography) is the art of capturing or creating a complete scene as a single image, as viewed when rotating about a single central position

I want to learn how to shoot, interactively view and share my own VR photos. Here's what I found:

* <a href="https://wiki.panotools.org/Equirectangular_Projection" target="_blank">Equirectangular Projection</a> is the most common VR image format. Another popular option is <a href="https://wiki.panotools.org/Cubic_Projection" target="_blank">Cubic Projection</a> and you can easily [convert between the two]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %}) 
* The Google Street View mobile app (<a href="https://apps.apple.com/us/app/google-street-view/id904418768" target="_blank">iOS</a>, <a href="https://play.google.com/store/apps/details?id=com.google.android.street&hl=en_US" target="_blank">Android</a>) is a cheap and easy way to shoot Equirectangular projections
* Since Equirectangular images are <a href="http://www.jamesfmackenzie.com/img/posts/cube-faces-guide.png" target="_blank">heavily distorted</a>, you need a <a href="https://wiki.panotools.org/Panorama_Viewers" target="_blank">"viewer"</a> program to interact with them
* Windows has built-in support via the [.pano]({% post_url 2016-10-29-what-are-pano-files %}) file extension. It's relatively easy to [create your own]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %})
* Web viewers are also popular. Here's how to publish VR photos to [Photosyth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %}), [Facebook]({% post_url 2016-10-12-publishing-equirectangular-360-vr-panorama-to-facebook %}) and [YouTube]({% post_url  2019-09-08-publishing-360-photos-to-youtube %})

Posts:

- [Publishing VR Panoramas to Facebook]({% post_url 2016-10-12-publishing-equirectangular-360-vr-panorama-to-facebook %}) - 12 Oct 2016
- [Installing Hugin and Panotools on Windows]({% post_url 2016-10-17-installing-hugin-and-panotools-on-windows %}) - 17 Oct 2016
- [Convert Equirectangular Projection to Cube Faces]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %}) - 18 Oct 2016
- [Publishing VR Panoramas to Photosynth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %}) - 28 Oct 2016
- [What are .pano files?]({% post_url 2016-10-29-what-are-pano-files %}) - 29 Oct 2016
- [Convert Equirectangular Projection to .Pano File]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %}) - 30 Oct 2016
- [All You Need to Know about 360 VR Photos]({% post_url 2016-11-02-shooting-storing-and-sharing-vr-panormas %}) - 02 Nov 2016
- [Publishing VR Panoramas to YouTube]({% post_url 2019-09-08-publishing-360-photos-to-youtube %}) - 08 Sep 2019



Whether it's a view from the highest holiday vista or showing off your new bathroom, no photo recreates the feeling of actually being there like a <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">360 VR panorama</a>. Pan left, right, up, down, or even swivel right around to take in the whole view.

With loads of choices out there, what are your best options for shooting, storing and sharing your inspiring pano's?

### Shooting

The best camera is the one you already have - and for most of us that's our smartphone. Modern smartphones are already equipped with all everything they need to take VR panoramas - namely accelerometer, gyroscope and CCD. The only remaining question is what software to use.

After some trial and error I settled on <a href="https://www.google.co.uk/streetview/apps/">Google Street View</a>. Intended as a data entry point for Google Maps, it also renders beautiful panoramas to your phone's Camera Roll in JPEG format. The experience is super simple. Simply point your phone at a series of orange dots and Street View will snap the panorama for you: 

![VR shooting via Google Street View app (iOS and Android)](/img/posts/google_street_view.jpg)

If you need better results, Street View is also <a href="https://support.google.com/maps/answer/6281877?hl=en" target="_blank">compatible with the following 360 degree cameras</a>.:

* Ricoh Theta S
* Samsung Gear 360
* NCTech iris360
* LG 360 CAM

If you want more control, you can shoot panoramas the old way:

1. Use your camera or DSLR to shoot lots of overlapping photos. Make sure you always shoot from the same point. A tripod helps here.
2. Stitch them in post-processing. Some good free options are <a href="http://hugin.sourceforge.net/" target="_blank">Hugin</a> and <a href="http://research.microsoft.com/en-us/um/redmond/projects/ice/" target="_blank">Microsoft ICE</a>.

### Storing

Stay away from the proprietary "walled garden" services out there. You want to store your panoramas in a plain, portable, future-proofed format.

My recommendation: stick with JPEG images in <a href="https://en.wikipedia.org/wiki/Equirectangular_projection" target="_blank">equirectangular</a> (or sometimes, "spherical") projection:

* Google's Street View already exports in this format
* Supported by most photo-stitching software
* Accepted as input by most panorama-sharing sites and apps too 

Take these and store them with your preferred photo backup service. 

![A 360 VR photo in Equirectangular projection](/img/posts/church-pano-equirectangular.jpg)

If you spend lots of time in the Windows ecosystem, also consider the [.pano file format]({% post_url 2016-10-29-what-are-pano-files %}). The Desktop, Tablet, Phone and OneDrive have built in support for it. Just double click to get panning:

<!-- 

ADD THESE NOTES LATER ON ONCE THE ARTICLES ARE FINISHED
It's relatively easy to convert from one to the other: 

* Converting from equirectangular projection to .pano
* Converting from .pano to equirectangular projection
-->

![The 360 VR experience - check out the ceiling!](/img/posts/church-pano.jpg)

### Viewing 

Aside from the Windows support mentioned above, there's no native OS capability out there. You'll need custom apps (or "Players") to tilt and pan through your 360 VR photos.

In addition to the Google Street View app, the free <a href="https://appsto.re/gb/2CTBbb.i" target="_blank">VR Camera app</a> for iOS is worth a look. Most of the other iOS options are either paid, walled gardens or total junk.

For other platforms, check out <a href="http://wiki.panotools.org/Panorama_Viewers" target="_blank">this comprehensive list</a>.

### Sharing

With no convergence around a popular, cross-platform Player, your best option is to share panoramas via the web. 

With this in mind, <a href="https://photosynth.net/" target="_blank">Photosynth</a> and <a href="http://www.facebook.com" target="_blank">Facebook</a> are great options. Both feature slick viewers in the browser and allow easy sharing with your friends. To get started, see:

* [Publishing VR Panoramas to Facebook]({% post_url 2016-10-12-publishing-equirectangular-360-vr-panorama-to-facebook %})
* [Publishing VR Panoramas to Photosynth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %})

If you shoot (or [convert to]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %})) [.pano files]({% post_url 2016-10-29-what-are-pano-files %}), your best option is definitely <a href="https://onedrive.live.com/about/en-gb/" target="_blank">OneDrive</a>. Simply upload the .pano and the share the link:

![OneDrive 360 VR viewer. Click and drag to pan around the scene](/img/posts/church-pano-onedrive.jpg)

Happy shooting!

### Other Posts in this Series
 
{% include vr-photography-series.md %}