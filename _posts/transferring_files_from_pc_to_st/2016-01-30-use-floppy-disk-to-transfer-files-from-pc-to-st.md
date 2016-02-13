---
layout: post
title: Using Floppy Disk to Transfer Files from PC to ST
date: '2016-01-30 22:30:00'
categories: transferring_files_from_pc_to_st
---

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/HwcleHTcZr8?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

### 1. Choosing the right floppy disks

For the vast majority of cases, you'll want 3.5" Double-Sided, Double-Density ("DD") floppy disks - they're the only variety supported by both PC and ST drives. They're also known as "720KB" floppy disks due to their standard formatted capacity. Unfortunately, manufacturing stopped years ago, so your best option is <a href="http://www.ebay.co.uk/itm/3-5-in-DSDD-720k-DS-formatted-floppy-disks-Double-sided-double-density-2DD-new-/291572499546?hash=item43e313445a:g:tHUAAOSwWnFWA6lR" target="_blank">eBay</a> or <a href="http://www.st-freakz.co.uk/page8.html" target="_blank">specialist ST providers</a>.

If you can't find any DD disks, it is *possible* to repurpose modern 1.44MB High Density ("HD") disks - albeit at a cost to reliability. HD disks have an extra hole on the right side (across from the write-protect slider), and if you cover this over with some opaque sticky tape (front and back), it'll fool the detector into thinking the HD disk is an ST-compatible DD floppy:

![](/img/posts/taped_corner_high_density_floppy_disk_front.jpg)

![](/img/posts/taped_corner_high_density_floppy_disk_back.jpg)

In very rare cases, your ST drive unit <a href="http://www.atari-wiki.com/index.php/Replace_internal_720k_DD_Floppy_Drive_with_1.44MB_HD_Floppy_Drive" target="_blank">may have been upgraded to support 3.5" HD disks natively</a>. If this is the case, congratulations! You can forget about DD disks and purchase higher capacity HD disks instead.

### 2. Choosing the right PC floppy drive

Most modern PC's don't ship with a floppy drive, so you'll need to buy one. Your best bet is an internal "ATA" model as they have the greatest compatibility with the various Atari ST disk formats:

![](/img/posts/floppy2.png)

If you use a laptop or your PC motherboard doesn't have a floppy connector, you're stuck with a (less compatible) USB drive. Many don't support DD floppies, so be sure to pick one that specifically mentions "720KB" compatibility (like <a href="http://www.floppydisk.com/usb.htm" target="_blank">this one</a>).

### 3. Format floppy disk

You have disks and a drive - now it's time to prepare the floppy. You need use a disk format compatible with both PC and ST - and luckily the standard MS-DOS/Windows floppy formats are suitable. So the recommended (and easiest) approach is to prepare the floppy disk on your PC. In any modern version of Windows:

{% highlight bash %}
format a: /T:80 /N:9
{% endhighlight %}

![](/img/posts/format_disk_720kb.png)

This will create a formatted 720KB floppy, ready for transferring files.

If you're lucky enough to have a ST with the aforementioned HD drive upgrade, you can <a href="http://windows.microsoft.com/en-gb/windows-vista/format-a-floppy-disk" target="_blank">use the built-in Windows format utility</a> to quickly create formatted 1.44MB floppies, useful for transferring larger files.

Lastly, if you want to prepare the disk on your ST (I'm not sure why you'd want to do this), you can. But there are some restrictions:

* TOS <= 1.02 will not create a PC-readable floppy disk
* TOS >= 1.04 should work OK
* If you're not sure, you can use a special formatting program like <a href="http://milan.kovac.cc/atari/software/index.php?search_word=kobold" target="_blank">Kobold</a> or <a href="https://sites.google.com/site/stessential/disks-tools" target="_blank">FastCopy</a>

#### A note on (very) old ST units

Some very early STs (specifically older 520STF models) only feature a 3.5" *Single Sided*, Double Density ("SS/DD") drive, supporting disks with a standard formatted capacity of 360KB. If you have one of these, it's not good news! Modern PC's can no longer read or write these - so you should consider swapping your ST drive out for a newer model. Find more info <a href="http://www.atari-forum.com/viewtopic.php?t=11250" target="_blank">here</a>.

### 4. Copy files onto floppy disk

Pop your formatted disk into the PC drive and use Windows Explorer (or Command prompt) to copy files. Easy peasy!

![](/img/posts/copy_atari_st_files.gif)

### 5. Load files on ST

Pop the disk into your ST, power on and browse to the files. You're all done!

![](/img/posts/atari_st_open_a_drive.gif)

### Splitting large files

If you have a hard drive attached to your ST, you might want to transfer files bigger than what can fit on a single floppy. You can achieve this using ARJ compression software. Find more details [here]({% post_url 2016-01-31-using-arj-to-split-and-copy-large-files-to-your-atari-st-in-chunks %}).
