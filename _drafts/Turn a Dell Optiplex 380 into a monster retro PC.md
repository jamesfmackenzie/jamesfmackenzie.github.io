
#blog/ideas #projects 

Update: the video is now posted, so removing the YouTube tag. But still needs to be posted to the blog


# Hardware Overview

The Dell OptiPlex 380 is an unassuming late-2000s business desktop — but for retro PC builders, it sits in a *very* interesting sweet spot. Cheap, widely available, and just old enough to retain key legacy features, it can be turned into a surprisingly capable **DOS, Windows 98, and Windows XP** gaming machine with the right approach.

## Why the OptiPlex 380 is interesting for retro builds

On paper, the OptiPlex 380 doesn’t look like a retro machine at all. But dig a little deeper and several useful traits emerge:

- Core 2–era performance that **obliterates late DOS and Win9x games**
- Real legacy I/O still present (VGA, serial, parallel)
- PCI *and* PCIe expansion
- A BIOS feature that can **limit RAM to 256MB** for Windows 98 installs
- SATA support that can be made Win98-friendly with patches
- Extremely low cost and easy availability on the second-hand market

It’s a classic example of a machine that makes more sense when judged by **capability**, not appearance.

### Core specifications (typical)

Exact specs vary by configuration, but most OptiPlex 380 systems share the following baseline:

- **CPU:** Intel Core 2 Duo (commonly E7xxx / E8xxx)
- **Chipset:** Intel G41 + ICH7 southbridge
- **Memory:** DDR3 (officially up to 4GB)
- **Storage:** SATA (HDD or SSD via SATA)
- **Optical:** DVD-ROM or DVD-RW
- **Graphics:** Intel GMA X4500 (onboard)

Form factors include desktop and small-form-factor (SFF).

The desktop version offers the best expansion flexibility for retro builds.

## Expansion slots (important for retro use)

One of the OptiPlex 380’s biggest strengths is its slot layout:

- **1× PCI Express x16**
- **2× PCI**

This allows for:

- A fast **PCIe GPU** for Windows 98 / XP
- A **PCI sound card** with better DOS compatibility than onboard audio

Despite common myths, **PCIe graphics *can* work in Windows 98** on this system with the right card and drivers.

## Rear I/O and legacy ports

Unlike many later systems, the OptiPlex 380 still includes genuinely useful legacy connectivity:

- VGA output
- Serial (COM) port
- Parallel (LPT) port
- USB 2.0
- Ethernet
- PS/2 support (via motherboard header + bracket)

For DOS and early Windows installs, this is a *big* advantage — especially when USB input proves unreliable.

## BIOS features that matter

The BIOS is unusually friendly for retro experimentation.

### OS Install mode (RAM limiting)

A standout feature is the **“OS Install”** option, which temporarily limits available system memory to **256MB**.

This is ideal for:

- Installing **Windows 98**
- Avoiding early setup crashes or hangs
- Simplifying Win9x compatibility on a system with 4GB installed

Once Windows is installed, you can choose whether to stay capped or apply RAM patches.

### SATA visibility

The BIOS exposes SATA drives in a way that *can* work with Windows 98 once appropriate patches are applied — something many newer systems fail at entirely.

## Windows 98 compatibility overview

**Out of the box:** ❌
**With patches and add-in cards:** ✅ very good

Key points:

- No official Intel G41 Windows 98 drivers (expected)

Requires:

- SATA patch (e.g. rloew’s)
- Third-party chipset INF files
- Onboard graphics are not suitable — **add a supported PCIe GPU**
- Excellent results with Radeon X6xx / X8xx-era cards
- Strong Win98 gaming performance once configured

In practice, Windows 98 is very usable on this system if you treat it like a *retro platform* rather than a stock PC.

## DOS compatibility (the reality)

DOS on post-ICH5 systems is always a compromise, and the OptiPlex 380 is no exception.

### What works well

DOS games that rely on:

- CPU speed
- VESA graphics
- FM music (OPL3)
- Late DOS titles that struggle in DOSBox often shine here

### Sound considerations

The ICH7 southbridge **does not support DDMA or PC/PCI**, which rules out many PCI sound cards for native DOS sound effects.

**What *does* work:**

Yamaha YMF7x4 cards (724 / 744 / 754)

- Real OPL3
- DSDMA support
- Excellent FM and MIDI

ISA sound cards are not an option on this platform.

## Windows XP compatibility

Windows XP is where the OptiPlex 380 feels completely at home:

- Full chipset driver support
- Excellent GPU compatibility
- Stable audio
- Strong performance for early-to-mid 2000s games

It comfortably handles titles like:

- Return to Castle Wolfenstein
- Half-Life 2
- Doom 3

…and can even stretch to famously demanding games with reduced settings.

## Known quirks and gotchas

- USB keyboards and mice can be laggy or unstable in DOS (PS/2 input is **strongly recommended**)
- Some PCIe GPUs (notably certain Radeon X600 variants) appear incompatible
- Native DOS sound support is limited by chipset design
- Small-form-factor cases restrict GPU and cooling options

None of these are deal-breakers — just things to plan around.
  
## Who is the OptiPlex 380 *for*?

This machine is ideal if you want:

- A **cheap, widely available** retro base system
- Strong **late DOS + Windows 98** performance
- A single box that also excels at **Windows XP**
- A platform that encourages experimentation without fear

It’s *not* ideal if you need:

- ISA expansion
- Perfect SB16-style DOS compatibility
- Zero configuration effort

## Summary

The Dell OptiPlex 380 is a great example of an overlooked system that becomes interesting once you stop judging it by its intended purpose. With a few smart upgrades, it can span nearly **two decades of PC gaming**, all while costing less than many single “retro” components.

Ugly? Absolutely.

Capable? Shockingly so.




# Installing Windows 98

## How I Prepared the Hard Disk

I have a 500GB laptop hard drive, and a USB caddy. This'll allow me to connect it to a modern PC and prep the disk, then take the case off connect to the Optiplex via these SATA connectors 

## High Level Install Sequence

**Hardware setup**

- partition disk

**install windows 98**

- patches
- finalize win 98
- install directx
- install gfx drivers (need to manually disable onboard gfx in device manager)
- install sound drivers
- test direct3d

**install xp**

- easy2boot
- install xp
- chipset drivers
- directx
- install gfx
- sound?

**last thing - DOS setup**

- install sound drivers and make surethey work

**performance**

- under 98
- under xp
- under dos

## Detailed Instructions

First I got the Windows 98 ISO and key from here:
- [https://winworldpc.com/product/windows-98/98-second-edition](https://winworldpc.com/product/windows-98/98-second-edition)
- PRDDH-83JD9-G6PK4-684GF-6Y73B

Then, get the patches. What patches did I have?

1. rloew SATA patch
2. Unofficial Intel Chipset INF files
3. [http://lonecrusader.x10host.com/intel_inf.html](http://lonecrusader.x10host.com/intel_inf.html)
4. And optionally, if I want to run Win98 with more than 256MB RAM, rloew PATCHMEM

Get the necessary drivers (e.g. Radeon catalyst drivers, FastVoodoo drivers and also DirectX 7 or 9.0c):

http://falconfly.3dfx.pl/directx.htm 

VBEMP graphics drivers:
- [https://bearwindows.zcm.com.au/vbe9x.htm](https://bearwindows.zcm.com.au/vbe9x.htm)

Then, prepare the hard disk. Partion to 32GB FAT32, and copy across the Windows 98 install files and everything else  

Start up the PC, go to BIOS and turned on "OS install" feature. This restricts the memory to 256MB - Windows 98 install won't play nice with the 4GB RAM I have on this thing

 Also disable all the integrated features - as I didn't have the drivers and I don't need them

Then I booted from Windows 98 floppy and started Windows 98 install

Once the first reboot was complete, next step was to slipstream the Win98 patches:

- first, copy Intel INF files. manually copy MACHINE3.INF, MACHINE4.INF, and MACHINE5.INF from your SETUP folder to the \INF folder of you new installation, (usually WINDOWS\INF).

Second, install SATA patch:

-> Run PTCHSATA.

-> Copy the SATA.INF file to the C:\WINDOWS\INF Folder

Lastly, run PATCHMEM  

Then reboot and continue Windows setup

Product key: PRDDH-83JD9-G6PK4-684GF-6Y73B


Once Windows 98 is installed, first do a reboot 

Then, boot back into Windows and:

1. Check Device Manager, make sure those INF files are good

2. Install DirectX. I got the latest Windows 98 SE version from here:

http://falconfly.3dfx.pl/directx.htm 

3. Radeon 6.2 Drivers -> for X800 

4. Yamaha DSXG driver -> for sound  

5. Then try out some games and 3dmark!

## Other Install Notes

- I started up the PC, went to BIOS and turned on "OS install" feature. This restricts the memory to 256MB - Windows 98 install won't play nice with the 4GB RAM I have on this thing
- I also disabled all the integrated features - as I didn't have the drivers and I don't need them
- Then I booted from Windows 98 floppy and attempted to install Windows 98
- The keyboard didn't work properly (very slow) and was causing crashes in the Windows setup. So I installed the serial/PS2 adapter from Dell and used PS2 mouse and keyboarsd
- Second time I installed Windows 98, then slipstreamed the SATA drivers [if I don't do this, Windows hangs on boot!]
- Windows booted up great, almost all the hardware was detected correctly inside the Device Manager and Windows seemed very stable
- Then I install DirectX. I got the latest Windows 98 SE version from here:
- [http://falconfly.3dfx.pl/directx.htm](http://falconfly.3dfx.pl/directx.htm)
- Then I installed some better drivers for the on board graphics. They are called the "VBEMP" drivers and you can find them here:
- [https://bearwindows.zcm.com.au/vbe9x.htm](https://bearwindows.zcm.com.au/vbe9x.htm)
- Then I went to installed the Sound Card. I was using a Sound Blaster Live SB0100

The first drivers I used were the VxD drivers from Phil:

[https://www.philscomputerlab.com/sound-blaster-live.html](https://www.philscomputerlab.com/sound-blaster-live.html)

Unfortunately the SB 16 Emulation always gave me a BSOD. This guy has the same issue:

[https://www.vogons.org/viewtopic.php?t=71049](https://www.vogons.org/viewtopic.php?t=71049)

So I was unable to get SB16 Emulation working

Aiming to do better, I installed the WDM drivers instead using this guide:

[https://www.vogons.org/viewtopic.php?p=352199](https://www.vogons.org/viewtopic.php?p=352199)

These are a special version of the WDM drivers, _just_ old enough to support SB Pro emulation for old games, but also support the cool new feature of the SB Live in Win98

In Windows, this works great. Sound is awesome (I didn't try EAX out yet).

I also get to use Sound Blaster Pro emulation - although this only works in Windows. I belive this is using sbemul.sys

Performance (often a criticism of WDM drivers) seems good when I compare side-by-side with sound disabled

As a bonus, I also get the amazing Sound Canvas / Soundfont support. Awesome! Some more reading here:

[https://www.vogons.org/viewtopic.php?t=57717](https://www.vogons.org/viewtopic.php?t=57717)

[https://www.vogons.org/viewtopic.php?t=51263](https://www.vogons.org/viewtopic.php?t=51263)
[https://www.manualslib.com/download/350430/Creative-Sb0100.html](https://www.manualslib.com/download/350430/Creative-Sb0100.html)

I _could_ try using the Audigy drivers, but since everything is working so well I don't see a need to change or try this yet:

[https://www.vogons.org/viewtopic.php?t=74361](https://www.vogons.org/viewtopic.php?t=74361)

- Next I tried to get DOS audio working with Phil's Livedos drivers
- After a lot of headbanging I gave up on this. It turns out that my hardware is just too new. The southbridge (ICH7) does not have PC-PCI or DDMA support - which means I can never get DOS SFX working (the best hope is Music, which I was able to get working)

A lot of further reading on this topic is available here:

[https://www.vogons.org/viewtopic.php?t=24769](https://www.vogons.org/viewtopic.php?t=24769)

[https://www.vogons.org/viewtopic.php?t=59696](https://www.vogons.org/viewtopic.php?t=59696)

[http://www.bttr-software.de/forum/mix_entry.php?id=4200](http://www.bttr-software.de/forum/mix_entry.php?id=4200)

[http://www.bttr-software.de/forum/mix_entry.php?id=3876#p3901](http://www.bttr-software.de/forum/mix_entry.php?id=3876#p3901)

[http://rayer.g6.cz/hardware/asup5ld2.htm#SB](http://rayer.g6.cz/hardware/asup5ld2.htm#SB)

One thing that might be fun to try one day is MPXPlay, which has a native DOS SB Live driver baked into it:

[http://mpxplay.sourceforge.net/](http://mpxplay.sourceforge.net/)

(write a blog post on this experience?)

Apparently the only two cards that will work in DOS are YM724/744 based cards or Aureal Vortex 2 chips. You can learn a bit more about this here:

[http://rayer.g6.cz/hardware/sbemu.htm](http://rayer.g6.cz/hardware/sbemu.htm)

[http://www.bttr-software.de/forum/mix_entry.php?id=15563#p15563](http://www.bttr-software.de/forum/mix_entry.php?id=15563#p15563)

I bought a YM724 card and can try when it arrives. It's certainly an interesting experiment if nothing else

Next up I moved onto Graphics

- First I benchmarked Quake, Duke3D and other apps in the VESA modes. It was fast but not crushingly fast
- Perhaps it is down to the onboard graphics? It will be difficult to tell until I have a dedicated graphics card in here
- In an attempt to make it fast, I tried FastVid. Unfortunately it doesn't seem to do anything and just crashes even in pure DOS
- [https://www.philscomputerlab.com/dos-graphics-boost.html](https://www.philscomputerlab.com/dos-graphics-boost.html)
- Next I installed the Voodoo2. But I was not able to get it working at all. Endless VXD errors even with the FastVoodoo drivers (I should probably write a blog post about this?)

Unfortunately the Voodoo2 crashes, so maybe I’ll need to leave that out. But apparently with Voodoo tweaked tool you can disable direct 3D for voodoo. Maybe that will help it work and we can just use voodoo for just the 3dfx games

Some notes about using DOS on the X58 chipset (which I *think* is the chipset on this Dell PC I bought):

[http://rayer.g6.cz/hardware/gap67ds3.htm](http://rayer.g6.cz/hardware/gap67ds3.htm)

https://www.vogons.org/viewtopic.php?t=24769


- Then I attempted with a PCI-Express graphics card. I tried the Dell OEM F9595 Radeon X600:
- [https://www.parts-people.com/index.php?action=item&id=23426](https://www.parts-people.com/index.php?action=item&id=23426)

It should work OK in the Optiplex 380, but it seemed to end up dead. I couldn't get any display to work. I should try it in another machine

... If it did work, I would install these ATI drivers

[https://www.philscomputerlab.com/ati-9x-driver-archive.html](https://www.philscomputerlab.com/ati-9x-driver-archive.html)

Then get 3D mark to test it out

[https://benchmarks.ul.com/legacy-benchmarks](https://benchmarks.ul.com/legacy-benchmarks)


GPU notes:

My x600 GPUs don’t work on the Dell OptiPlex 380. They just show up as “SDVO card”:
[https://twitter.com/jamesfmackenzie/status/1495872112682278914?s=21](https://twitter.com/jamesfmackenzie/status/1495872112682278914?s=21)

[https://www.vogons.org/viewtopic.php?t=86498](https://www.vogons.org/viewtopic.php?t=86498)

It’s very strange and seems like some kind of hardware incompatibility

Interestingly there is another post where someone sees basically the same thing with the ATI FireMV 2200:

[https://community.spiceworks.com/topic/95756-video-card-not-detected-dell-optiplex-380](https://community.spiceworks.com/topic/95756-video-card-not-detected-dell-optiplex-380)

Both of these share the same RV370 GPU and visually appear to be basically the same card

I suspect a hardware incompatibility, ordered some different GPUs to test:

- Radeon 3450 (Dell branded). This is an official GPU option for this OptiPlex 380
- Radeon X800 XL. A higher powered GPU option. Not sure if it’ll work

After receiving the cards above, it really does seem that this is a hardware incompatibility. I should reply to Twitter / Vogons and make a blog post about this so others can find out in future

Sound card notes:

YMF7x4 (724, 744, 754) are the only common PCI sound cards with genuine OPL3 chip. With SB-Link they have good SB Pro compatibility in DOS. When have good codec they produce not bad sound via LineOut. Also these cards have 3D sound in Win9x games and good GM. This makes YMF7x4 cards interesting for DOS-Win9x retrogaming machines as universal solution. Also with these cards you may get quality SB Pro sounding on machines without ISA slots, like Pentium 4. And real OPL3 FM with DOSBox paththrough in WinXP on later CPUs.

This guide is initially based on "YMF7x4 FAQ" by

Andrey Revvo *, site by N.Shima & Vivas *, Vogons and other sources.

For some links you'll need to use archive.org

Lastly I ran into some issues with USB mouse and keyboard. They became laggy and unsrepsnice in native DOS applications and would often cause a freeze or crash. Luckily this Dell machine has a Serial header on the motherboard and allows us to add a PS/2 mouse and keyboard, fixing the input problem entirely. This was another $X, bringing my total cost to $X


## Inspiration

Taking inspiration from the following Rasteri video

[https://youtu.be/NzAiznHGz-E](https://youtu.be/NzAiznHGz-E)

And also the following comment on Vogons:

Why have a super fast Windows 98 PC?

Windows 9X runs stupidly fast on modern hardware; no joke! For instance, Blood screams at 1600X1200 and looks freakishly smooth with no slowdown on my Piledriver AM3 CPU (see sig). Other games like Duke3D, Mortal Kombat Trilogy, Shadow Warrior, Carmageddon (think you have to slow this one down natively) all have problems running decent with dosbox. There might be other reasons but I don't know right now...

Take inspiration from here:

- [https://youtu.be/NzAiznHGz-E](https://youtu.be/NzAiznHGz-E)
- [https://youtu.be/I1SMEppUZZ4](https://youtu.be/I1SMEppUZZ4)
- [https://youtu.be/3pMaYUdPFKM](https://youtu.be/3pMaYUdPFKM)
- [https://youtube.com/watch?v=uzm5yBYIR6Q&feature=share](https://youtube.com/watch?v=uzm5yBYIR6Q&feature=share)



# YouTube Video

## Thematic Notes

Yes, this is a Dell, but let’s not judge a book by its cover.

Model details will come later, but for now let’s focus on capabilities, and how well this plays old games.

(This PC is right on that knife edge, being new enough to really accelerate newer games, but *just* old enough, and with some unique features that make DOS and Windows 98 work really well)

Even better, these are super cheap, and there are many available on eBay /right now/ for almost the cost of postage 

Another awesome thing with a machine like this: it crushes high end DOS games like Duke Nukem 3D, Blood and Quake. Right here we have Quake running in Software Rendering at 800x600.

I love software rendering, and it’s never looked so good as right here - running at a /locked/ 60 frames per second 

Some of these games perform badly on DOSBox and this PC will blow those away

It runs at a /locked/ 60 frames per second. Have you ever seen software rendering look so good? Some of these perform badly on DOSBox and this PC will blow those away

## Thumbnail Ideas
  
Outline of a PC chassis with a question mark

Amazing DOS, Windows 98, Windows XP performance

Super cheap hardware nobody wants
  
## Structure of Video

**Intro showing b roll of commander keen or another dos game like jazz jackrabbit, maybe a Windows 98 game too, perhaps a high performance one like Unreal, or maybe a slow pan across the hardware I bought**

- _So it’s 2023 and you can still build an amazing retro PC for super cheap_
- _I was able to build a DOS, Windows 98 and Windows XP monster PC for less than $100 - and you can too!_
- _This machine will play everything from DOS classics right the way up to later XP titles - and yes, it even plays Crysis - let’s check it out!_

(intro jingle)

Now, I’m not going to show this PC, I want to save this for a big reveal at the end

The reason, I think folks will pre-judge and write off this machine. Instead, I want to focus on capabilities:

- How well does it play DOS games?
- How does it perform on Windows 98 or XP titles?
- Let’s judge this machine on the retro gaming experience, and how it doesn’t take a lot of money to get a great one.

In terms of specs:

- We’re running a Core 2 Duo, an E7600 at 3.06GHz
- We have 4GB of DDR3 RAM
- A 500GB hard disk
- A DVD writer

And I picked up this whole working machine for $60 shipped

It seems that nobody wants Core 2 - even looking on eBay now I can see many more for almost the cost of postage

But as we’ll see with the build - Core 2 machines can be excellent for retro gaming 

This PC is right on that knife edge, being new enough to really accelerate newer games, but *just* old enough, and with some unique features that make DOS and Windows 98 work really well

(Looking around the back, it has)

- a serial port
- a parallel port 
- and VGA graphics

Looking inside we have an Intel-powered 82 801 GB I/O controller

i.e. we have an Intel ICH7 southbridge and we’re running the Intel G41 chipset

There aren’t any Windows 98 drivers for the G41, but that’s OK because we want to play DOS and Windows 98 games - and for those we’ll need to add our own video and sound cards 

Looking at expansion options, we have 1 PCE-e and 2 PCI slots

There are myths and rumour that PCIe don’t work on Windows 98 - and maybe that’s true with some hardware but it was fine for me

The good news is that PCIe cards are super cheap, and I was able to pick up this untested Radeon X800 XL for $12

The X6,7 and 800 series are the last official supported Radeon cards in Windows 98. So this is really one the fastest cast we can get for 98 - and will cope well with most Windows XP games too - not bad for $12!

So this is almost the fastest GPU you can get for  Windows 98 - there’s only one better. And $12 is an absolute bargain. Hope it works

Next we need a sound card - and here we need to be a bit careful. Most PCI sound cards don’t work well for DOS gaming

After some searching, I was able to find this Yamaha YMF-based card (YMF-724), which is great because:

1. It has a genuine Yamaha OPL3 chip, so our FM music will be super authentic 
2. It’s known for great DOS compatibility, even with newer machines

Even better, I was able to pick this up for $10 - vs the $50 that these normally go for

It’s an off brand variant (S81X), and I had to zoom the photo to confirm this as a Yamaha card. Pretty sure the seller had no idea what it was.

On a side note: This is proof! There are still eBay bargains out there!

Checking on the bill, we’re at $82! Still super cheap

Lastly I picked up this Dell add-in bracket. Native DOS apps and games - including the Windows 98 installer - often misbehave with a USB mouse and keyboard. 

Luckily the optiplex has a serial header on the motherboard, and we can use this bracket to add PS/2 mouse and keyboard support

Time to get this hooked up and test it out!

(grinding noise from fan)

OK, Not good. This fan was totally seized

Perhaps there’s a reason the card was $12 …

BUT After switching out the fan bearing, the noise was much better and the machine posted OK. Time to install Windows 98! 

Right! We're into the BIOS, and this is where we see the first cool feature of this machine. Going to the Post Behaviour section we have this "OS install" feature - and it restricts the available memory to 256MB.

This is perfect for DOS and Windows 98 that don’t play nice with a lot of RAM - especially the 4GB that this machine has

So let’s enable that and we'll get on with the Windows 98 install

To get Windows 98 working, I did have to add Rudy Loew’s SATA patch - without these, Windows would just hang ...

and I also slipstreamed Lone Crusader’s chipset Information files, which helps tidy up some of the Unknown Devices in Device Manger

After those tweaks, we’re in Windows 98!

You’ve probably noticed that the graphics look awful, and that’s because we’re in 640x480, 16 color mode. We need some graphics drivers

After installing the Catalyst 6.2 drivers and rebooting, I did run into some weirdness. The Radeon X800 was detected but not working.

I had to select and remove this extra entry for the Standard Display Adapter. One more reboot, and we're good to go.

A quick Direct3D check, and our spinning cube looks good. I know we’re itching to see performance numbers, but first - sound

---------

A quick install of the Yamaha DS-XG drivers, a reboot, and then (windows startup sound)

One of the awesome things with this card is the General MIDI synth. It supports the XG MIDI standard and it sounds super great. Give this a listen:

It sounds good, right?

Checking the control panel, we can find these DOS settings. We can use these for playing DOS games in Windows. Let's give it a test with Doom:

Works great!

-----------------------------------------------

Another awesome thing with a machine like this: it crushes high end DOS games like Duke Nukem 3D, Blood, Quake, Screamer. Right here we have Quake running in Software Rendering at 800x600.

It runs at a /locked/ 60 frames per second. Have you ever seen software rendering look so good? Some of these perform badly on DOSBox and this PC will blow those away

------------

Next up, let’s try native DOS. 

Now this gets us into cool hardware feature number 3. This sound card has some Yamaha magic in the form of DSDMA - a program that emulates the ISA DMA from legacy sound cards, and allows us to get audio in native DOS

Running the program, we get an IRQ, DMA - it looks promising and … Wolf3D works great!

Because this has a real OPL3, the ad-lib audio is super authentic, this is how your DOS games are supposed to sound … 

On the lower end, games like Keen, Prince of Persia, Monkey Island and even Alley Cat work well

In fact, most of the DOS games I threw at this worked great

A few went too fast. By using cpuspd I was able to throttle down the CPU, turn off caches and even get tricky games like Theme Park to run great

(show keen some other games working well under native DOS)

Now, at last, it’s time for some benchmarks!

Starting with Phil’s DOS benchmark pack

- Doom runs at 216 frames per second
- Quake runs at 653 frames per second 
- And 3dbench is completely broken at 1455 frames per second 

In Windows 98, 3DMark 99 hits 38,612 at 800x600 and 3DMark 2001 hits 33,311

A Quake2 time demo hits 972.4 frames per second and Unreal 497.3. These are lofty numbers!

To get a sense of speed, here’s how quake2 runs if you forget to enable vsync

Fast enough?

Across the board, Windows 98 performance is really great  (show a graph with some popular games)

So where’s the ceiling with this machine? To find that, we need to move up to Windows XP

First up, Return to Castle Wolfenstein - this runs at a flawless 60 frames per second, even at high resolutions

Moving up one notch, Half Life 2 also plays great - and also, by the way, still looks amazing. I'm running at full 1080p here and the frame rate still holds up

A bit tricker to run - Doom 3 - and those stencil shadows - still runs great at High settings, only starting to suffer once we push to Ultra

Finally, and we have to do this ... does it run Crysis?

We have to drop the resolution a bit, but it does hold up!

We're running at 800x600, Medium settings, and the framerate is ... good! In fact, I got distracted a played through the entire first mission - Crysis is still the King!

Now we're playing with POWER! And we're also playing CHEAP because the total cost of this PC is only $92 - Thanks eBay!!

Right, it’s time for the big reveal - what is this miracle machine? Drum roll, please …

There you have it! An ugly dell optiplex, and there are 100s of these available on eBay for almost no money

Jokes aside, I’ve grown to love this machine because of what it can do - play my favourite games from the 1990 thru to 2010.

I even have a Voodoo 3 on order … and will try to get native Glide working on this retro rocket

What are your thoughts? Are you inspired to do your own UGLY retro build? What are your thoughts on old DELL machines? Would love hear your thoughts in the comment below - enjoy!
  



# Research Notes

Must haves when buying a retro PC:

Must have at least PCI expansion slots

Must have a way to restrict memory - [https://www.vogons.org/viewtopic.php?t=48981](https://www.vogons.org/viewtopic.php?t=48981)

Must make SATA devices available to DOS and Win98 via BIOS

(nice to have DDMA etc so sound cards work. But if not I will need to get a Yamaha card)

Why the Optiplex 380? It fits this quite well:

[Last officially supported Windows 98/Me AMD platform : r/windows98 (reddit.com)](https://www.reddit.com/r/windows98/comments/oxxrha/last_officially_supported_windows_98me_amd/?utm_source=share&utm_medium=ios_app&utm_name=iossmf)

It may have trouble with the sound card

This is really hard because after ICH5, DDMA and other essential features were dropped

The best thing you’re likely to get is FM/MIDI audio
[http://dosdays.co.uk/topics/pci_sound_cards_in_dos.php](http://dosdays.co.uk/topics/pci_sound_cards_in_dos.php)

DSDMA support for Yamaha YMF-724

[https://www.vogons.org/viewtopic.php?t=48133&start=100](https://www.vogons.org/viewtopic.php?t=48133&start=100)

[Yamaha YMF744 on G41/ICH7 - is this possible? \ VOGONS](https://www.vogons.org/viewtopic.php?t=66270)

[https://www.vogons.org/viewtopic.php?t=48983](https://www.vogons.org/viewtopic.php?t=48983)

[https://www.vogons.org/viewtopic.php?t=57321](https://www.vogons.org/viewtopic.php?t=57321)

[https://www.vogons.org/viewtopic.php?t=24769](https://www.vogons.org/viewtopic.php?t=24769)

SBLive in DOS:

It probably won’t work in ICH5+ because of the lack of DDMA and other DMA features. But try the below anyway 

Check the settings in Windows Device manager as well (both for emulation and the actual card). I'm not sure if Windows uses the settings in ctsyn.ini.

These should match the hardware resources for the SB Live! in Windows:

PCIPort=1000

PCIIRQ=11

Also make sure the IRQ/DMAs for DOS emulation aren't used by some other hardware in the system.

These are the motherboards I have tried:

Working:

Abit BH6 (440BX)

Aopen AX6C (i820)

Asus TUSL-C (i815)

Fujitsu Siemens D1215 (i815)

Not working:

Abit IS7-E / E2 (i865)

This guy has some useful patches:

[RayeR's homepage/Programming (g6.cz)](http://rayer.g6.cz/programm/programe.htm)

Things still to figure out:

USB keyboard lag: 

[https://www.vcfed.org/forum/forum/vintage-gaming/vintage-gaming-aa/57423-usb-keyboard-lag-in-dos-games](https://www.vcfed.org/forum/forum/vintage-gaming/vintage-gaming-aa/57423-usb-keyboard-lag-in-dos-games)

Awesome links:

Windows 98 support site 
[https://web.archive.org/web/20120512143841/http://windows98.ic.cz/](https://web.archive.org/web/20120512143841/http://windows98.ic.cz/)

PCI sound cards on DOS (not my words):

This is what I can say about PCI soundcards for use in pure DOS, I'll do it from start to finish:

Most DOS programs/games are designed to only access ISA soundcards, by using typical ISA channels for sound data: IRQ, I/O, DMA. A PCI card's DOS driver must setup routings to intercept the ISA-style orders for playing sound and music and pass them through to the PCI hardware. There are two emulation methods to do this in pure DOS:  
1) DDMA (Distributed DMA) (EDIT: combined with an IRQ related method.)  
2) PC/PCI using a Physical SB-LINK connection.  
Such a method must be supported by both soundcard and motherboard for the method to work. DDMA support is more common than PC/PCI support. You should only expect to find such support on PCI soundcards sold new up until about 2001. Roughly the same seems to go for DDMA support on motherboards, not really sure here.

DDMA (Distributed DMA):  
Ensoniq AudioPCI was the first with a pure-dos DDMA emulation. The related software was bought by creative and adjusted for their AudioPCI-clones, SB-Live!'s and Audigy-1's. AFAIK it is all roughly the same program, just that creative replaced the soundscape emulation with SB16 emulation. It requires EMM386 loaded. It supports OPL-3 and General Midi music with a software driver. (I only used SB-PCI 128 and SB-Live!)

Aureal Vortex-2 does SB-Pro DDMA emulation. OPL-3 music in software. It is one of the few to have a functional wavetable daughterboard header in DOS. Otherwise no software General-Midi available. You can use the command "LH AU30DOS.COM" to load the emulator, in this case it only takes 1k of your base memory.

I also tried a more recent Turtle Beach Santa Cruz (Crystal chipset) in DOS once. It worked, doing the usual SB-Pro emulation and software OPL-3 music. General Midi in DOS can possibly be achieved when utilizing an external Midi device, but I could not try this because I don't have one of those. The wavetable daughterboard header is windows only. The driver program (TBCDOS.exe) had very few options and was hardly documented.

PC/PCI using a Physical SB-LINK connection:  
I have seen it supported on the AWE-64 and ESS Solo-1 soundcards. I have only used it with a Yamaha YMF724 based soundcard on a BX440 motherboard. It emulates a SB-Pro too. This setup failed with only one game so far (Quarantine). As a bonus this particular card has an integrated hardware OPL-3 for music. General Midi in DOS can only be achieved when utilizing an external Midi device.

Here is an additional read on this topic, aimed at Ultima 7 players:  
[PCI Soundcards for Ultima 7](http://www.it-he.org/sound.htm)

ISA Cards are probably a fine, if not better, approach. I happended to mess around with PCI cards for no particular reason. 😉


# Modifying BIOS features

Can do this with a SOP8 clip.

https://chatgpt.com/share/69546867-1580-8003-9925-d553cd9af5e1