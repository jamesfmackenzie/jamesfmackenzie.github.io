---
layout: post
title: Shooting and Sharing VR Photos
date: '2016-11-01 12:00:00'
tags: [Projects, VR Photography]
status: completed
---

Ever seen one of <a href="https://flickr.com/photos/136386099@N02/21597873406/" target="_blank">these photos</a> where you can interactively zoom and pan around? They're known as <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">360° or VR photos</a>.

More formally, <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">VR photography</a> (Virtual Reality photography) is the art of capturing or creating a complete scene as a single image, as viewed when rotating about a single central position.

I want to learn how to shoot, interactively view and share my own VR photos.


### Project Notes

Status | Completed
Goal | Learn how to shoot, interactively view and share VR photos

After a deep dive over several weekends, here's what I learned:

* <a href="https://wiki.panotools.org/Equirectangular_Projection" target="_blank">Equirectangular Projection</a> is the most common VR image format. Another popular option is <a href="https://wiki.panotools.org/Cubic_Projection" target="_blank">Cubic Projection</a> and you can easily [convert between the two]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %}).
* The Google Street View mobile app (<a href="https://apps.apple.com/us/app/google-street-view/id904418768" target="_blank">iOS</a>, <a href="https://play.google.com/store/apps/details?id=com.google.android.street&hl=en_US" target="_blank">Android</a>) is a cheap and easy way to shoot Equirectangular projections.
* Since Equirectangular images are <a href="http://www.jamesfmackenzie.com/img/posts/cube-faces-guide.jpg" target="_blank">heavily distorted</a>, you need a <a href="https://wiki.panotools.org/Panorama_Viewers" target="_blank">"viewer"</a> program to interact with them.
* Windows has built-in support via the [.pano]({% post_url 2016-10-29-what-are-pano-files %}) file extension. It's relatively easy to [create your own]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %}).
* Web viewers are also popular. Here's how to publish VR photos to [Photosyth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %}), [Facebook]({% post_url 2016-10-12-publishing-equirectangular-360-vr-panorama-to-facebook %}) and [YouTube]({% post_url  2019-09-08-publishing-360-photos-to-youtube %}).


### Project Updates

- [Publishing VR Panoramas to Facebook]({% post_url 2016-10-12-publishing-equirectangular-360-vr-panorama-to-facebook %}) - 12 Oct 2016
- [Installing Hugin and Panotools on Windows]({% post_url 2016-10-17-installing-hugin-and-panotools-on-windows %}) - 17 Oct 2016
- [Convert Equirectangular Projection to Cube Faces]({% post_url 2016-10-18-convert-equirectangular-projection-to-cube-faces %}) - 18 Oct 2016
- [Publishing VR Panoramas to Photosynth]({% post_url 2016-10-28-publishing-equirectangular-360-vr-panorama-to-photosynth %}) - 28 Oct 2016
- [What are .pano files?]({% post_url 2016-10-29-what-are-pano-files %}) - 29 Oct 2016
- [Convert Equirectangular Projection to .Pano File]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %}) - 30 Oct 2016
- [All You Need to Know about 360 VR Photos]({% post_url 2016-11-02-shooting-storing-and-sharing-vr-panormas %}) - 02 Nov 2016
- [Publishing VR Panoramas to YouTube]({% post_url 2019-09-08-publishing-360-photos-to-youtube %}) - 08 Sep 2019

<br />