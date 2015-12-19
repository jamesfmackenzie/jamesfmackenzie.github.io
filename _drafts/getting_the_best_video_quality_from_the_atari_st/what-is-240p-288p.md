---
layout: post
title: What is 240/288p?
date:
categories:
---

What is 240p/288p?

For broadcast television, odd and even fields of 288 lines each are displayed alternately. The fields are offset from one another by one line, providing a full 576 lines of detail 25 times per second (hence "25fps"). This is interlaced video - "576i".

Computers like the ST (and also old video game consoles) behave differently. They ask the CRT to draw the odd and even fields on top of each other (no offset). Instead of 576 lines of detail once every two fields, you get 288 lines of detail (and 288 black lines*) - i.e. a full frame - for every single field (hence "50fps"). This is progressive video - "288p".

*ironically, we call these black lines "scanlines". They should probably be called "unscanned lines" :-)

Some retro hardware/software does really interesting/inventive stuff with 240p/288p. For example:

* Draw your scene as normal for all the even fields
* Draw a dark colour over some of it for all the odd fields
* You've just drawn a transparent shadow for free! (doing this transparency in software is expensive and usually beyond the old hardware)

Unfortunately a lot of modern LCD screens misterpret 240p/288p as 480i/576i. They apply redundant deinterlacing techniques to the signal (i.e. wait for 2 frames, merge them in some fashion, and then draw onto the screen at 30/25fps). This results in choppier motion, and in the example above, might cause either the shadowed portion of the image to be displayed permanently (no transparency at all) or missing entirely.

It's for this reason that expensive upscaling hardware like the XRGB series exists. They understand the quirks of 240p/288p properly.

If you're interested, you can find more detail over here: http://www.hdretrovision.com/240p/ 


