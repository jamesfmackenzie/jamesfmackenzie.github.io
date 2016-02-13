---
layout: post
title: Use Your PC to Create a Bootable Atari ST Game Disk
date: '2015-09-22 11:37:00'
categories: playing_downloaded_atari_st_games
---

As [discussed before]({% post_url 2015-09-18-playing-downloaded-games-on-a-real-atari-st %}), Atari ST disk images are freely available on the web, <a href="http://www.emuparadise.me/Atari_ST_ROMs/63" target="_blank">Emuparadise</a> probably being the best resource.

But how can you play these games on physical Atari ST hardware?

One way is to use your Windows PC to prepare a bootable game disk. Once it's done, pop the disk into your ST floppy drive, power-on and you're good to go!

Here's how.

### What you need

#### Internal 3.5" floppy drive

![](/img/posts/floppy2.png)

You'll need a 3.5", 1.44MB PC floppy drive that uses the <a href="http://www.computerhope.com/jargon/f/flopcabl.htm" target="_blank">old 34-pin connector</a>. Unfortunately, for our purposes, a USB floppy drive won't do as:

* Some of them don't support the standard 720KB Atari ST disk format
* None of them support the "special" 800KB+ disk formats that many ST games use

A few notes to help with your search:

* 34-pin floppy drives are difficult to find new nowadays, so you might <a href="http://www.ebay.co.uk/bhp/internal-floppy-drive" target="_blank">go to eBay and pick up a used one</a>
* A lot of modern motherboards are missing the old 34-pin connector. You can add this support via something like the <a href="https://en.wikipedia.org/wiki/Individual_Computers_Catweasel" target="_blank">Catweasel</a>, but it's an expensive option
* All things considered, it might be easier and cheaper to purchase an old PC from eBay with a built in floppy drive. **This is what I chose to do**:

![](/img/posts/dell_laptop.jpg)

#### Makedisk

For writing the images to disk, we'll use a tool called Makedisk. Written by Darren Birks back in 1997, it's still the most reliable tool I've found. A few facts:

* Makedisk can write both .ST and .MSA images to disk. Sorry, no .STX
* For best compatibility, use <a href="https://en.wikipedia.org/wiki/DOS" target="_blank">DOS</a>. Win98/ME may work, but all newer Windows releases are a no-go due to incompatible floppy drivers
* You can download Makedisk <a href="http://emulatari.free.fr/zip/makedisk_v15.zip" target="_blank">here</a>
* More information at the <a href="http://www.atari-wiki.com/?title=Make_disk_Tutorial" target="_blank">Makedisk wiki</a>

#### Some 3.5" floppy disks

Clearly, you need some 3.5" floppy disks to write the images onto.

The ST takes 3.5" Double-Sided, Double-Density floppies, with a regular capacity of 720KB. These are little hard to come by nowadays, but you can occasionally <a href="http://www.ebay.co.uk/sch/i.html?_odkw=1.44MB&_osacat=80136&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.X720kb.TRS0&_nkw=720kb&_sacat=80136" target="_blank">find them on eBay</a>. If 720KB disks prove too hard to find, you can buy <a href="http://www.ebay.co.uk/sch/i.html?_odkw=720kb&_osacat=80136&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.X1.44MB.TRS0&_nkw=1.44MB&_sacat=80136" target="_blank">1.44MB Double-Sided High-Density disks</a> and <a href="http://borislegradic.blogspot.co.uk/2009/03/obsolete-hardware.html" target="_blank">cover the corner over with tape</a> - at a slight reliability cost. 

If you're interested in the official floppy specs, you can <a href="https://en.wikipedia.org/wiki/List_of_floppy_disk_formats#Known_disk_logical_formats" target="_blank">find them over on Wikipedia</a>.

#### A bootable DOS USB drive

As I mentioned earlier, Makedisk works best in <a href="https://en.wikipedia.org/wiki/DOS" target="_blank">DOS</a>. By far-and-away the easiest way to get a DOS environment is via bootable USB media. How-To Geek <a href="http://www.howtogeek.com/136987/how-to-create-a-bootable-dos-usb-drive/" target="_blank">has an excellent guide you can follow</a>.

### How to create the bootable game disk

#### 1. Copy data onto USB media

Take your bootable DOS USB drive and copy the following onto it:

1. The Makedisk program executable
2. The disk image (.MSA or .ST file) you wish to play on your Atari ST

![](/img/posts/copy_files.gif)

#### 2. Boot from your USB media

Restart your machine and boot from your DOS USB drive. You might have to hit F12 to access the boot menu and then select "USB Drive".

#### 3. Use Makedisk to prepare game disk

Once you're at the DOS prompt, invoke Makedisk with the following params to write your disk image:

{% highlight bat %}
{% raw %}
C:\>makedisk /write <disk image name> /auto
{% endraw %}
{% endhighlight %}

![](/img/posts/makedisk_command_line.png)

After a couple of prompts (for which the answers are suggested and you should always answer Yes), Makedisk will whirr away and prepare your disk image:

![](/img/posts/makedisk.gif)

#### 4. Play the game

That's it! You should now have a working game disk. Put it in your ST and play!

![](/img/posts/rick_dangerous.png)

### On YouTube

I've put together a video copy of this guide too. Find it embedded below.

<iframe width="853" height="480" src="https://www.youtube.com/embed/Tu52dALu6lQ" frameborder="0" allowfullscreen></iframe>
