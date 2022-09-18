---
layout: post
title: What are .pano files?
date: '2016-10-29 17:59:00'
summary: If you’re on the Windows platform, .pano files are probably the most convenient way to manage and share VR panoramas (aka “360 photos”) ...
image: altered-pano-file.png
tags: [Photography, VR Photography]
---

If you're on the Windows platform, .pano files are probably the most convenient way to manage and share <a href="https://en.wikipedia.org/wiki/VR_photography" target="_blank">VR panoramas</a> (aka "360 photos").

### The Experience

Built-in support for .pano files is available in Windows 8.1, Windows 10, Windows 10 Mobile and OneDrive. In Windows, simply double click to open the photo viewer, then tilt, pan and zoom your way around the VR image:

![Pan, zoom and tilt in Microsoft Photos](/img/posts/pan-and-tilit-the-microsoft-photos-panorama-experience.png)

Upload .pano files to OneDrive for an in-browser panoramic experience, and for easy sharing with your friends:

![The OneDrive pano experience](/img/posts/pan-and-tilt-the-onedrive-panorama-experience.png)

### Creating .pano files

If you have one of the following devices, the Windows Camera app will shoot .pano files natively:

* Surface Pro 4
* Surface Book
* Surface 3
* Lumia 950, 950XL, 650 and 550

If you have a VR panorama in another format (such as <a href="https://en.wikipedia.org/wiki/Equirectangular_projection" target="_blank">equirectangular projection</a>), you can [convert it]({% post_url 2016-10-30-convert-equirectangular-360-vr-panorama-to-pano-file %}).

### Details

* <a name="panoarchive"></a>.pano files are self-contained archives in the <a href="https://en.wikipedia.org/wiki/Open_Packaging_Conventions" target="_blank">Open Packaging Conventions (OPC) format</a>.  You can rename to a .zip and extract the contents:

{% highlight bash %}
C:\Temp\pano_example>copy building_site.pano building_site.zip
        1 file(s) copied.

C:\Temp\pano_example>7z x building_site.zip

7-Zip 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18

Processing archive: building_site.zip

Extracting  ...

Everything is Ok

Files: 720
Size:       5387132
Compressed: 5507134
{% endhighlight %}

* <a name="cubefaces"></a>Looking inside, you'll see the VR image stored as <a href="https://en.wikipedia.org/wiki/Cube_mapping" target="_blank">cube faces</a> plus some metadata.

{% highlight bash %}
C:\Temp\pano_example>tree
Folder PATH listing for volume OS
Volume serial number is 000000FF D06A:CE0C
C:.
├───formats
│   └───cubemap
│       ├───back
│       │   ├───10
│       │   ├───11
│       │   ├───8
│       │   └───9
│       ├───bottom
│       │   ├───10
│       │   ├───11
│       │   ├───8
│       │   └───9
│       ├───front
│       │   ├───10
│       │   ├───11
│       │   ├───8
│       │   └───9
│       ├───left
│       │   ├───10
│       │   ├───11
│       │   ├───8
│       │   └───9
│       ├───right
│       │   ├───10
│       │   ├───11
│       │   ├───8
│       │   └───9
│       └───top
│           ├───10
│           ├───11
│           ├───8
│           └───9
├───properties
└───_rels
{% endhighlight %}

* You'll find a folder for each side of the cube: <code>back, bottom, front, left, right, top</code>
* <a name="cubedetail"></a>Within these, you'll find several numbered folders: <code>8, 9, 10, 11</code>. These indicate increasing levels of detail for the cube face:

{% highlight bash %}
8:    = max cube face size of (2^8)*(2^8)    = 256*256 pixels
9:                                           = 512*512 pixels
10:                                          = 1024*1024 pixels
11:                                          = 2048*2048 pixels

... etc
{% endhighlight %}

* <a name="cubetiles"></a>The actual contents of these folders depends on the tile size defined in <code>cubemap.json</code>:

{% highlight bash %}
C:\Temp\pano_example>type formats\cubemap\cubemap.json
{"cubemap_json_version":1.0,"field_of_view_bounds":[0.0,360.0,-89.9,89.9],"initial_look_direction":[1.5707963267948966,0.0],"face_size":2048,"tile_size":254,"front":{},"back":{},"left":{},"right":{},"top":{},"bottom":{}}
{% endhighlight %}

In my example above, the tile size is 254. So I'd expect, for the <i>8</i> folder, to see:

* One tile of 254*254
* Two edge strips of 2\*254 and 254\*2
* One corner piece of 2*2
 
i.e. when these pieces are added together, they make up the full 256*256 cube face. Is this what I actually see? Well almost:

![.pano tile dimensions - 256 pixels](/img/posts/pano-tile-dimensions.png)

So it looks like each tile is padded by a few pixels, probably to avoid ugly seams in the final result. Extending this to the <i>9</i> folder, I expect to see:

* Four tiles of 256*256
* Two horizontal strips 256 pixels wide
* Two vertical strips 256 pixels high
* One square corner piece

Is this what I see? Yep:

![.pano tile dimensions - 512 pixels](/img/posts/pano-tile-dimensions-512.png)

This pattern of 256*256 tiling continues right the way up to the full face size defined in <code>cubemap.json</code>:

![.pano tile dimensions - 1024 pixels](/img/posts/pano-tile-dimensions-1024.png)

![.pano tile dimensions - 2048 pixels](/img/posts/pano-tile-dimensions-2048.png)

* <a name="cubezip"></a>You can easily adjust the tiles and zip them back up into a working .pano. *But be sure not accidentally add any compression*:

{% highlight bash %}
C:\Temp\pano_example>copy c:\temp\example-tile.jpg formats\cubemap\back\8\0_0.jpg
Overwrite formats\cubemap\back\8\0_0.jpg? (Yes/No/All): y
        1 file(s) copied.

C:\Temp\pano_example>copy c:\temp\example-tile.jpg formats\cubemap\back\9\0_0.jpg
Overwrite formats\cubemap\back\9\0_0.jpg? (Yes/No/All): y
        1 file(s) copied.

C:\Temp\pano_example>copy c:\temp\example-tile.jpg formats\cubemap\back\10\0_0.jpg
Overwrite formats\cubemap\back\10\0_0.jpg? (Yes/No/All): y
        1 file(s) copied.

C:\Temp\pano_example>copy c:\temp\example-tile.jpg formats\cubemap\back\11\0_0.jpg
Overwrite formats\cubemap\back\11\0_0.jpg? (Yes/No/All): y
        1 file(s) copied.

C:\Temp\pano_example>7z a new_pano.zip -r * -mx0

7-Zip 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
Scanning

Creating archive new_pano.zip

Compressing  ...

Everything is Ok

C:\Temp\pano_example>copy new_pano.zip new_pano.pano
        1 file(s) copied.
{% endhighlight %}

![Altered .pano file](/img/posts/altered-pano-file.png)

That's it!

### Other Posts in this Series
 
{% include vr-photography-series.md %}

### References

<a href="https://bdhurkett.wordpress.com/2013/11/06/windows-8-1-panorama-files/" target="_blank">Windows 8.1 Panorama Files</a>.



