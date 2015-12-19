
###1. Find the right floppy disks

The ST and PC have shared compatibility with 3.5" Double Density ("DD") disks, so in the vast majority of cases, this is what you'll need.

Manufacturing stopped years ago, so your best option is eBay or specialist ST providers.

If you can't find any at all, it is possible to repurpose modern High Density ("HD") disks, albeit at a cost to reliability.

Compared to DD disks, HD disks have an extra hole on the right side, across from the write-protect slider. Put some opaque sticky tape over the extra hole on the right (both front and back) to fool the detector into thinking the HD disk is an ST-compatible DD floppy.

INSERT PIC OF REPURPOSED HD DISK HERE

In very rare cases, your ST drive unit may have been upgraded to support 3.5" HD disks natively. If this is the case, congratulations! You can forget about DD disks and purchase HD disks instead.

INSERT PICTURE OF HD MODIFIED ST HERE 

###2. Find the right drive

Most modern PC's don't ship with a floppy drive, so you'll need to buy one.

Your best bet is an internal "ATA" model as they have the greatest compatibility with the various Atari ST disk formats.

INSERT PICTURE OF ATA FLOPPY HERE

If you use a laptop or your PC motherboard doesn't have an ATA connector, you're stuck with a (less compatible) USB floppy drive. Many don't support DD floppies, so be sure to pick one that specifically mentions "720KB" compatibility.

INSERT PICTURE OF USB FLOPPY DRIVE HERE

###3. Format Floppy Disk

You need to prepare a floppy disk that is readable by both PC and ST.

Luckily, the standard MS-DOS/Windows floppy formats work on both machines. So the recommended (and easiest) way is to prepare the floppy disk on your PC.

In any modern version of Windows:

format a: /T:80 /N:9

This will create a formatted 720KB floppy, ready for transferring files.

INSERT IMAGE OF FORMAT COMMAND HERE

If you're lucky enough to have a ST with the aforementioned upgraded HD drive, you can use the built-in Windows format utility to quickly create formatted 1.44MB floppies, useful for transferring larger files.

INSERT PICTURE OF STANDARD WINDOWS FORMAT UTILITY

Some very early STs (specifically older 520STF and SF354 units) only feature a 3.5" *Single Sided*, Double Density ("SS/DD") drive, with a standard formatted capacity of 360KB. If you have one of these, it's not good news! Modern PC's can no longer read or write these - so you should consider swapping the drive out for a newer model.

Lastly, if you want to prepare the disk on your ST (I'm not sure why you'd want to do this), you can. But there are some restrictions:

* TOS <= 1.02 will not create a PC-readable floppy disk
* TOS >= 1.04 should work OK
* If you're not sure, you can use a special formatting program like Kobold or FastCopy Pro

###4. Copy files onto floppy disk

Use Windows explorer or the command line to copy files onto the disk

###5. Load files on ST

Pop the disk into your ST, power on and browse to the files. You're all done!

INSERT PICTURE OF FILES LOADING ON ST

###Splitting large files

If you have a hard drive attached to your ST, you might want to transfer files bigger than what can fit on a single floppy.

You can achieve this using the ARJ utility.

Firstly, use your PC split the large file into 720KB (or, if your drive supports it, 1440KB) chunks:

ARJ a -jm -r -v720 archive.arj *.*

INSERT SCREENSHOT OF ARJ COMMAND

You'll get multiple files, starting with archive.arj, followed by archive.a01, archive.a02 etc.

Use floppies to shuffle the files across to your ST one-by-one.

Once you've moved all the files across, use UnARJ to extract the original large file. The easiest way is to drag archieve.arj onto unarj.ttp, after which UnARJ will work its magic automatically.

INSERT SCREENSHOT OF UNARJ COMMAND
