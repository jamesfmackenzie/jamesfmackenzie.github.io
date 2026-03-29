

  

#blog/ideas  

  
 
Idea is to have one massive article with all my notes in it. Then I can do some separate blog posts on specific topics:

  

- How to prepare CF card
- Using Serial Drive (and how to find/download it) - [https://www.xtideuniversalbios.org/wiki/SerialDrives](https://www.xtideuniversalbios.org/wiki/SerialDrives)
- Common issues

  

But to start let’s just have the single big post

  

Take a look at minuszerodegrees blog posts. That might help me think about the structure and subheadings etc

  

[https://www.minuszerodegrees.net/xtide/Serial%20drive/Serial%20drive.htm](https://www.minuszerodegrees.net/xtide/Serial%20drive/Serial%20drive.htm)

  

  

  

  

I bought the tex elec version. BIOS comes pre-installed

  

Used Rufus to write a bootable OS image to a 64MB CF card. It did not work (stuck with Booting C>>C).

  

Instead a booted the PC with a DOS 3.3 floppy, and then used fdisk to partition the CF card and format /s to copy system files.

  

Because of DOS 3.3 file system limitations, I had to limit the numbers of cylinders to a low number (200).

  

Even after fdisk and formatting, unfortunately the PC still failed to boot (same error as before). But at least after booting from floppy, the hard drive was now mounted and usable.

  

Next I used serdrive to mount a floppy over COM1. Unfortunately this doesn’t seem to be included in the latest universal ide binaries. I had to get an old version (add link to this)

  

After booting a MSDOS 6.2 boot disk via serdrive, I ran fdisk /mbr

  

This did fix the “Booting C>>C” hang, but unfortunately I now run straight onto another issue “Boot sector not found”

  

I don’t really know what the issue is, so I got a larger CF card (16GB), and used serdrive to boot into DOS 6.22 floppy, and fdisk to create a 2GB primary partition.

  

Even though fdisk seems to work OK, DOS 6.22 format does not work, and fails to either format the partition or copy system files. Formatting the partition in windows 10 does work, but unfortunately that gives us a non-bootable partition.

  

As a next step, I have a few options.

  

1. Use a DOS 6.22 boot disk to prepare and format my 64MB CF card. Perhaps this will work fine with a smaller card
2. Use a DOS 5.0 boot disk to prepare both the 64MB and 16GB card. Perhaps this will just work better
3. Download full DOS 5.0 or DOS 3.3 install floppies, and use those instead to install DOS to CF

  

Next steps, try to boot a floppy image over serial and try fdisk /mbr

  

Finding: in the end, this is what worked:

  

1. Install XTIDE in PC1640 slot
2. Download serdrive
3. Use a USB to serial port cable, with a null modem adapter
4. Download DOS 5 floppy boost disk
5. Boot from serdrive
6. FDISK /mbr to proactively fix any master boot record / boot sector issues on thr CF card
7. FDISK to partition the CF card
8. Format c: /u /s
9. Reboot to verify all works OK (it should do!)

  

I could consider using the original Amstrad images, but that’s for another day!

  

**Useful hot keys**

  

Alt = search COM ports for mounted serial drives

Boot menu = ?

  

  

**Multi drives**

  

I was also unable to mount both the Amstrad MFM drive and XTIDE concurrently. The XTIDE BIOS does not load when the MFM controller card is connected. Seems like we can only have one of the other, perhaps whichever card is inserted in the first ISA slot