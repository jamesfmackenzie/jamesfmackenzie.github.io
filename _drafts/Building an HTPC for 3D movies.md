I should write up this follow-up blog post to my original 3D projector blog post.

Notes below. Let’s form this into a new blog post and publish.

---


A follow up to [[I Accidentally Turned My Projector Into a 3D Cinema]], I wanted to go the whole hog and build an HTPC for 3D movies.

# Why do I need an HTPC for 3D movies?

Why do I need this? It’s because:

- Although many devices can play back the simple 3D movie formats (e.g. SBS / side-by-side)
- Very few devices can play back the optimal format: frame packing 3D


# More on 3D frame packing

For the uninitiated, frame packing is a special video mode where two full 1080p left and right eye images are packed into a larger 1920x2205 frame, along with some padding space and signaling metadata.

Compatible devices (like my projector) will recognise this as a frame packed resolution, and enable their 3D features to deliver the correct images to left and right eye.

![[Pasted image 20251217011415.jpg]]

Checking the specs for my projector, my projector does indeed support frame packing. Let’s do this!

![[IMG_3939.jpeg]]
https://esupportdownload.benq.com/esupport/PROJECTOR/UserManual/TH575/TH575_UM_EN_220830165100.pdf

# What are the steps to build a 3D HTPC?

At a super high level, the process is:

1. Acquiring 3D content — makemkv
2. Choosing playback software — vlc, stereoscopic player, MPC-BE + LAV filters + madvr
3. Get 3D frame packing working (this is where it gets tricky!)
4. Get sound working

# Acquiring 3D content

From the start, I wanted no-compromise on video quality. This means:

- Original 3D Blu ray quality
- No transcoding, recompression or other lossy solutions

Lucky for us, a great solution exists — MakeMKV.

It will rip the original H.264 video and DTS (?) audio streams from a Blu ray disc, and repackage them into an mkv file. It even has an option to extract the 3D content in its original multi view coding (MVC) format.

(expand on this, how I did it)

(I have to check the “MVC” box during extraction)

(to prove the show a screenshot or two of MediaInfo and that these videos have a multiview count = 2)


# Choosing playback software 

Although most video players (including the ever trusty VLC) will playback our frame packing videos as regular 2D, very few will understand the MVC coding and correctly enable 3D playback.

(Double check — does VLC understand MVC coding? I don’t think so)

After a *lot* of research, I found two good options for Windows:

1. Stereoscopic player
2. Media Player Classic: Black Edition

Both of these will detect the 3D video and enable side-by-side playback. Activating the corresponding side-by-side feature on the projector gives us a proper 3D movie! Nice!

(Double check — do I need the latest LAV filters to do this in MPC: BE?)

One caveat: with side-by-side video, you’re losing half the horizontal resolution.

Can we do better?


# Getting 3D Frame Packing working 

One problem:

Most PC graphics cards and drivers have long ago dropped support for frame packing. The latest AMD and Nvidia drivers do not have frame packing support, and most modern cards *never* had this feature.

There are *some experiments* where people worked with a custom resolution utilities to manually output a “frame packed like” resolution (i.e. correct resolution and framerate, but without the signalling data).

Unfortunately my projector won’t accept this and activate frame packing 3D mode.

So I did the obvious thing — built an old PC.

## Option 1. Building an old PC

(Talk about how I built an old PC - using Intel HD graphics - which are known to work with 3D support)

(Stereoscopic player does work, but without purchasing a license you’re restricted to only a few minutes of playback. I want something free and reliable).

(Go through the full setup process for MPC-BE, LAV filters, madvr)

(explain the challenges I had with MPC-BE crashing.)

(To fix the crashing, I had to enable Quicksync hardware decoding. But the hardware decoder itself breaks with Way of the Water — perhaps the bitrate is too high)

(Double confirm — is this fixed with madvrhdmeasure?)

(Luckily for me, I had an old graphics card — an Nvidia GTX 1060 3GB. This can *did* have 3D drivers once upon a time)

(I installed the newest drivers with 3D support — version 425.31. Because Windows is aggressive about installing its own drivers, I had to use DDU, restart the computer whilst disconnected from the internet, and then install the legacy drivers)

(With these in place the 3D mode worked OK and I was able to FINALLY enjoy 3D movies reliably)

# Using a Modern PC

It was at this point I learned there is a *possible* solution for modern PCs.

Even though Nvidia removed 3D support from their drivers, 3D Fix Manager can (amongst other things) restore this support and allow frame packing video modes to be enabled even with modern cards and drivers!

https://helixmod.blogspot.com/2017/05/3d-fix-manager.html

https://www.mtbs3d.com/forum/viewtopic.php?t=23397

https://web.archive.org/web/20190124211005/http://fixmanager.rentus.de/

https://web.archive.org/web/20220815195319/http://fixmanager.markus-guendert.de/download.php

(I installed 3D Fix Manager, and in the driver tab enabled 3D vision support)

(After toggling 3D slider, frame packing mode was enabled)

(Something to double confirm: do I need to set the graphics mode to 24hz first?)

After doing this, I was able to setup MPC-BE the same way as before and play 3D movies! The best of both worlds!



# A Bonus: 3D gaming

Notes about 3d gaming with geo 11 below

To be clear, 3D fix manager is responsible for downloading individual game fixes and overall patching the Nvidia driver with 3d vision support.

But geo 11 is the driver replacement that allows games to actually output 3d graphics using the geo 11 DLLs

The geo 11 driver is a full replacement for NVidia 3D Vision for DX11 games.  It will create 3D out of thin air.  We are calling it geo-11 as it does create geometric 3D for DX11


https://helixmod.blogspot.com/2022/06/announcing-new-geo-11-3d-driver.html

https://www.mtbs3d.com/forum/viewtopic.php?t=26264



There are *some experiments* where people made it work with a custom resolution



# Useful links

https://r-htpc.github.io/wiki/3d





![[IMG_3928.jpeg]]


every media player will understand our 3

With my original 3D Blu ray discs 




Alternative list (for reference)
1. Pick the right hardware
2. Install the 3D drivers (has to be the right version)
3. (do it with the network cable unplugged, or windows will install newer versions. I used 3D fix manager)
4. Rip the blu ray with Make MKV
5. Install MPC-BE, Lav filters, madvr (nightmare). Make sure it's 32-bit version

They say the best PC is the PC you have, so let’s start there:

# AMD AM5 with RTX 2060 Super

This is my active PC, so I decided to try it first.

First, we need to understand how to enable frame packed 3D output.

What is frame packing? (cover this briefly)

![[Pasted image 20251217011415.jpg]]

Using the custom resolution utility



(Try 1080p 23.XXX and 24.000fps - expect it to stay in regular mode)
(Try )

My first attempt was to just try running 3D playback on the most modern software.

Unsurprisingly none of these worked:

- Stereoscopic player — black screen when enabling 3D vision


# i7-4770k with GTX 1060







# Old notes

Some exploratory notes on getting 3D frame packaging output working on a PC

I bought a projector ... and even better, just found out it does 3D! Can I use this to watch 3D Blu Rays?

I want to try this out and chronicle it on twitter!



Unfortunately I no longer have any dedicated Blu-ray players. 😢

But I do have a trusty old PlayStation 3.

Time for a second attempt!




# tweet 1

I was setting up my new projector when I found something weird in the settings:

3D Mode: ON

I didn’t even know this thing could do 3D.

Now I have shutter glasses on order.

The journey begins… 🕶️👇


# tweet 2

Did I impulsively order shutter glasses at 1:30 AM?

Yes.

Did I order two pairs because I know I’ll want to show this off?

Also yes.


# tweet 3

After some research, turns out my projector — a BenQ TH575 — requires 3D glasses that are compatible with DLP-Link synchronisation technology.


# tweet 4?

DLP-Link works by embedding a white flash signal into projected video.

The shutter glasses use a sensor to detect this signal and rapidly switch their liquid crystal lenses, making one lens opaque and the other transparent. This ensures that each eye sees only the image intended for it, creating the illusion of a single, seamless 3D image.


# tweet 4 

OK, after reading 
After some research, I bought these AWOL VISION 3D glasses.

They’re relatively cheap and (I think!) decently comfortable for extended wear.

The battery life is decent too — XXX hours.

![[IMG_3824.jpeg]]


# tweet 5

With the glasses in hand, I do think they’re comfortable.

Perhaps there are better glasses out there, but I’m happy for the price.

Now it’s time to actually try out some 3D content!


# tweet 6

I was able to find a 3D trailer online and play it via the Apple TV. I just needed to activate my projectors side by side mode.

It’s impressive! 

One annoyance, however. The sound is not so great. The speakers on the projector are tinny, not much bass.

And the sound is also in the wrong place — with stereo audio coming from the back of the room, not the front (where the picture is)

# tweet 6

OK! Good news!

The Apple TV is able to connect to my TCL sound bar via Bluetooth - a BIG improvement vs the built-in speakers.

(And also in the right place - with stereo sound coming from the front of the room, not the back)


# tweet 7

One thing I did notice was the 3D image was a little fuzzy.

# tweet 

After some research, it turn out there are four different ways to display 3D content:

Top bottom
Side by side
Frame sequential
Frame packing

My projector supports all four!




# tweet 7

In terms of quality:

Top bottom and side by side are the worst. You lose half of the vertical or horizontal resolution

Frame sequential is much better, but you need to support high refresh rates — since video must be sent at double the target frame rate (all the left eye frames, all the right eye frames)


# tweet 8

Frame Packing is a special format.

Frame packing a special formats

Left and right I are packaged into a single frame, for 1080p video this will be 1920x2205

(Show the picture)






Good news, I have this copy of desolation of Smaug! I no longer have a 3D Blu Ray player, but can I get this working from an Xbox


OK, bad news. Neither Xbox Series or PS5 support 3D Blu ray any longer ... that's a no go



Luckily for me, I still have the trusty PS3. Does this work?



Yes it does! (trust me it looks great)



But unfortunately think sound only comes out the tiny speakers on the projector. How do I get it out my bluetooth soundbar and subwoofer setup?



No-go! It turns out PS3 can't talk to Bluetooth audio devices. And there doesn't seem to be a super good way around it



But I do have a Blu ray drive on the PC. Can I use that?


OK! Bluetooth audio is go! (Test this out)


Let’s try the blu ray
OK! Not as easy at it seems! I got an instant error in VLC. AACS looks like something with decryption


I looked online and I can use makemkv to decrypt a blu ray disc. So I downloaded and installed that, and extracted the blue ray (don’t forget to use the backup option)


Was I able to play it in VLC? Yes!
(should work according to the link below. Test it out!)
https://forum.makemkv.com/forum/viewtopic.php?t=37698


But was I able to get it working in 3D? no!
I can’t seem to make the projector recognize a 3d image at all


After some more searching, I found the stereoscopic player - a player specially intended for 3d movies.

It takes tons of input formats
(Side by side, over under, frame sequential)


I downloaded a short movies trailer to try it out 
(Just try out a side by side video, with side by side output )


OK! That works!
But I’m losing half the resolution!


So, what’s the best 3D format? I think time to look at my projector support formats



My projector is the benq th575

Looking at the docs, looks like it suppprts three 3d formats

Top bottom
Side by side
Frame sequential
Frame packing

Clearly the first two are not good. With those I’m losing resolution.

Looking at the frame sequential mode, the supported resolutions are blah … that doesn’t work optimally either

Seems like the best is really frame packing at 1080p 24hz

(Show a picture of what frame packing is)



the best 3d format is 1080p 24hz

Or if I want a higher frame rate it’s 720p 60hz

https://esupportdownload.benq.com/esupport/PROJECTOR/UserManual/TH575/TH575_UM_EN_220830165100.pdf




Maybe it can do anaglyph 3d? Check it out)





And I wasn’t able to install 425.31
Got a gosh darn error “not compatible with this version of windows"


I downloaded and run the Display Driver Uninstaller (DDU) … did it work?


Nope! It seems like windows was too busy installing its own Microsoft drivers - it wouldn’t let me keep the old drivers 

Luckily I was able to fix that with some settings:

Step-by-step instructions

1. **Open System Settings:** Right-click the Start button and select "System," or search for and open "Settings".
2. **Access advanced system settings:** Scroll down in the System settings and click "About." In the "Related settings" section, click "Advanced system settings".
3. **Open Device Installation Settings:** In the System Properties window that appears, go to the "Hardware" tab and click the "Device Installation Settings" button.
- **Disable automatic driver installation:** Choose the "No" option with the text "your device might not work as expected," then click "Save Changes" and "OK".- **Restart your PC:** A restart is required to apply the changes effectively.


Ok! Another try to install nvidia 425.31


Did it work? Fuck no! Microsoft still installs its own GeForce display driver

But this time, I went to device manager and rolled back that bastared. Now I am back to Microsoft default displays driver


This time, I tried 391.35 … did this work? Fuck no!



Next up, I ran DDU again and restarted windows into safe mode. Let’s try installing 425.31 from there? Nope!


After reading some forums, I came across this tidbit:

![[Pasted image 20251102224946.png]]

https://www.mtbs3d.com/phpbb/viewtopic.php?t=25481

It seems like this German version of 425.31 installs OK - no idea why!








After looking on Nvidia forums, looks like I can downgrade even further and then retry. Will this crazy work?

https://www.nvidia.com/en-us/geforce/forums/3d-vision/41/407687/42531-drivers-wont-install-anymore/?topicPage=9


After all this FUCK, here is the summary:

1. I can’t install the old updates over the new ones

2. If I uninstall the old ones, the new one just gets reinstalled

3. If I use DDU, the new one still gets reinstalled

4. I had to disable windows updates and hardware updates … (see below)

5. Then I had to install via fix manager (452.06 first, then 425.31)

6. Finally with all that done, the new driver seemed to stay off


here is what actually worked:

1. Turn off Microsoft updates (do not install vendor drivers)

https://youtu.be/npJy_0gnm7c?si=mCuFA4YYK3ZF2fzG

2. Use DDU to uninstall display nvidia drivers

3. Use use fix manager to install intermediate drivers

4. Use fix manager to downgrade to original drivers 













(This is where i fire up the Blu Ray and try to play it, but it doesn’t work - lets try )
(I probably need to find a player first … what is a good one to do that?)



Good news! I have an NVidia GPU, and it should support Nvidia 3D vision. This is NVidia's way to do 3d video



Downloaded and tried out the Medusa demo. No go! (ugh!)
It only displays in 2D
[3D Vision Drivers and Downloads|NVIDIA](https://www.nvidia.com/en-in/drivers/GeForce-3D-Drivers-Downloads/)





OK, turns out getting a PC to output 3D video is a lot harder than it used to be
Nvidia used to have 3D Vision. But it was discontinued in 2019


So in 2025, it looks like there’s no way to get your GPU to output a 



If you have a 20-series or earlier GPU, you can make it work.
Luckily for me! I have a 2060 Super.
Turns out the newest drivers that support 3D Vision are 425.31. Let's download those and give it a spin!
[GeForce Game Ready Driver 425.31 | Windows 10 64-bit | NVIDIA](https://www.nvidia.com/en-us/drivers/details/145872/)


OK, crap! I can't install on Windows 11 (show the error)


Let's try manually via Device Manager
OK! That didn't work either. Looks like these drivers pre-date my 2060 super. BAHA
The NVIDIA RTX 2060 Super was released on ==July 9, 2019==. It was announced alongside the RTX 2070 Super and was available for purchase on that date, with the RTX 2080 Super launching later in July.
|   |   |
|---|---|
|Driver Version:|425.31 \| WHQL|
|Release Date:|Thu Apr 11, 2019|
|Operating System:|Windows 10 64-bit|
|Language:|English (US)|
|File Size:|579.98 MB|

So! I need to find another way.







What about 3d games!

thankfully some guy has made 3dfixmanager
It has a feature to install the Nvidia graphics driver directly (452.06) -- I assume it does some special stuff? Or maybe not? Why does it use 452.06??

Here's what Gemini says:

1. **Install the driver:** Download the **GeForce Game Ready Driver 452.06** from the [NVIDIA website](https://www.nvidia.com/en-gb/drivers/details/163082/).
2. **Perform a clean installation:** During the driver installation, select "Custom" and check the box for **"Perform a clean installation"** to ensure no conflicting files remain.
3. **Install 3D Fix Manager:** Download and install 3D Fix Manager from the [Helix Mod website](https://helixmod.blogspot.com/2017/05/3d-fix-manager.html).
4. **Restore 3D Vision:** Once 3D Fix Manager is installed, it should automatically detect your games and allow you to download and install fixes to restore 3D Vision compatibility with the 452.06 driver.
- **Troubleshoot if needed:** If you encounter errors or issues, try the following:
    - Make sure your operating system is compatible with both the driver and 3D Fix Manager.
    - Check your graphics hardware compatibility with the driver.
    - Disable your antivirus software temporarily to avoid any conflicts during the installation.
    - Ensure your drivers are installed correctly before attempting to use 3D Fix Manager.
    - Consider backing up your system configuration before making any major changes, especially when using older drivers.

I tried installing the drivers via the 3d fix manager. It used the nvidia installer but it majorly fucked up and sent me back to Microsoft Basic Display Driver.

However I was able to extra the archive and install via Device Manager

After that I was able to install the Stereoscopic 3d driver via 3d fix manager.

NEXT!
I tried out Final Fantasy X. It did not work
I had to override it to use side by side ... suboptimal in my opinion.

Turns out that my projector just doesn't support 1920x1080 at 120hz needed for frame packing. I needed to lower the resolution.

Luckily for me 3D fix can use RTSS to force a lower reoslution

I downloaded RTSS from guru3d and installed it
[Guru3D RTSS Rivatuner Statistics Server Download 7.3.7](https://www.guru3d.com/download/rtss-rivatuner-statistics-server-download)




To get frame packing on a PC ... you need to do some clever things

Originally