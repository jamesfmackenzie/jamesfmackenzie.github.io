---
layout: post
title: Convert Equirectangular Projection to Cube Faces
date: '2016-10-18 10:13:00'
summary: Equirectangular and cube face projections are commonly used in 360 photo / VR panorama processing. Here’s how to convert from one to the other ...
image: cubefaces.png
tags: [How To, Photography, Posts, VR Photography]
---

![Equirectangular source image](/img/posts/equirectangular-pano.png)

Equirectangular and cube face projections are commonly used in 360 photo / VR panorama processing. Here's how to convert from one to the other.

### Step 1. Install tooling

You'll need Panotools and Hugin to perform the photo transformation. Follow [this guide]({% post_url 2016-10-17-installing-hugin-and-panotools-on-windows %}) to get them installed and setup.

### Step 2. Generate parameters

Open a command line and invoke the following:

{% highlight bash %}
erect2cubic --erect=<equirectangular_image_to_convert> --ptofile=<output_parameters_file> --face=<desired_face_size>
{% endhighlight %}

This will generate a .pto file, containing all the parameters needed for the transformation from equirectangular to cube faces.

A real world example:

{% highlight bash %}
erect2cubic --erect=equirectangular-pano.png --ptofile=convert_to_cubefaces.pto --face=1024
{% endhighlight %}

![Specify transformation parameters](/img/posts/2016-10-17-erect2cubic-command.png)

### Step 3. Execute convert

Still in the command line, invoke the following:
 
{% highlight bash %}
nona -o convert <parameters_file_generated_in_previous_step>
{% endhighlight %}

Or, continuing my example:

{% highlight bash %}
nona -o convert convert_to_cubefaces.pto
{% endhighlight %}

This will produce 6 images, one for each cube face:

![Execute transformation](/img/posts/2016-10-17-nona-command.png)

![Output cubefaces](/img/posts/cubefaces.png)

Job done!

### Other Posts in this Series
 
{% include vr-photography-series.md %}