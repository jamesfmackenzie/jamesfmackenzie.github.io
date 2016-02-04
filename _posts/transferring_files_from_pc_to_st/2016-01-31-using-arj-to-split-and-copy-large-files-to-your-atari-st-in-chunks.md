---
layout: post
title: How to Split and Copy Large Files to Your Atari ST in Chunks
date: '2016-01-31 17:47:00'
categories: transferring_files_from_pc_to_st
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/UNkJJKaKd2w?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 


If you have a hard drive attached to your ST, you might want to transfer files bigger than what can fit on a single floppy. You can achieve this using ARJ compression software, available for PC <a href="http://www.arjsoftware.com/arj32.htm" target="_blank">here</a> and ST <a href="https://sites.google.com/site/stessential/archiver-tools" target="_blank">here</a>.

Once you have the software downloaded and extracted, use your PC split the large file into 720KB (or, if your drive supports it, 1440KB) chunks:

{% highlight bash %}
ARJ32 a -jm -r -v720 arc.arj largefile.jpg
{% endhighlight %}

![](/img/posts/arj_split_file_into_720kb_chunks.png)

You'll get multiple files, starting with <code>arc.arj</code>, followed by <code>arc.a01</code>, <code>arc.a02</code> etc.

Use floppies to shuffle the files across to your ST one-by-one.

Once you've moved all the files across, use UnARJ to extract the original large file. The easiest way is to drag <code>arc.arj</code> onto <code>unarj.ttp</code>, after which UnARJ will work its magic automatically:

![](/img/posts/atari_st_unarj_file.gif)

In older versions of TOS, drag-and-drop won't work - you'll need to double click <code>unarj.ttp</code> and type in the archive source path:

![](/img/posts/atari_st_unarj.png)

That's all there is to it! Easy when you know how.