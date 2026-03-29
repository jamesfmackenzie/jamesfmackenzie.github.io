
(See my similar article [[Turn a Dell Optiplex 380 into a monster retro PC]], this is probably very similar)

# Hardware Overview

(Insert general details about the Optiplex here)

Unfortunately it doesn’t have the useful “OS Install” mode to limit system RAM, so I will likely need to use some kind of Windows 98 memory patch to make it work.

However I did turn off multi core support, speedstep, C States control.

Chip wise, it has the ICH10 controller hub with Intel HDA and an Analog Devices AD1984A audio codec chip.

![[Pasted image 20251230235437.jpg]]

My Optiplex 760 has the following spec:

![[Pasted image 20251229205114.jpg]]

# Windows 98
## Installing Windows 98

Similar to the e520, i tried to get Windows 98 installed and working.

Unfortunately it doesn’t have the useful “OS Install” mode to limit system RAM, so I will likely need to use some kind of Windows 98 memory patch to make it work.

However I did turn off multi core support, speedstep, C States control

Because i am lazy, i decided to just plug in the same windows 98 hard disk from the e520 and boot it. Of course the caused a cascade of add new hardware steps and was non ideal and messy — but perhaps not so bad if it gives me a quick feel for windows 98 viability on the system

Pretty quickly Windows 98 came up.

## Graphics

I was able to install and get the Radeon X600 with catalyst 6.2 drivers installed and working very quickly, including hardware Direct 3D acceleration.

3D Mark works great, with a very high score.

It seems like Voodoo 2 is not possible to work. Constant crashes and FXMEMMAP blue screen errors.

To work around the memory conflict/clash. I tried removing all hardware (even the discrete GPU) and disabling all onboard devices. Still no go.

Running one of the demos in dos I got a dos/4gw general protection fault. Perhaps this is memory address related (a clash?), or perhaps this is just an incompatibility with ICH10.

This will be very complicated to fix, perhaps impossible without flashing and unlocking bios features.

# Sound

The built in Intel audio is not officially supported on Windows 98.

However there is budding community support via the WDMHDA project.

https://github.com/andrew-hoffman/WDMHDA

I was able to install this driver but unfortunately no audio is output from either the headphone or line out ports.

This is a known issue with WDMHDA. It does not work with my Audio Devices codec chip (yet!)

I posted this on Vogons:

https://www.vogons.org/viewtopic.php?t=109373

## Still to do

==I should try out the 32 bit disk access (what was it called? Does it work or not. Since this was an issue on the Dell e520.==

==I should also try to unlock features on the bios. Perhaps some of those will help me address the memory issues that are preventing voodoo 2 from working.==

==I should also keep an eye on the Vogons thread above on WDMHDA. It would sure be cool to get built in audio working with Win98.==

==I should also try to get Win XP dual boot working with 98==

# Windows XP

This is a great fit for this system. All chipset drivers install OK and it’s blazing fast. We can also install a faster GPU like the Radeon 4670.

# Windows 7

Of course installs OK but really struggles performance wise. Perhaps would benefit from an SSD and more RAM (the max on this device is 4GB?)

# DOS

Good news, there is a serial header on the motherboard, so i added a header and added a PS/2 keyboard — to sidestep and alleviate some of the USB keyboard issues I saw with the e520.

That fixes up a lot of the issues that were preventing me from playing DOS games.

The other issue to tackle is sound. I installed SBEMU and it works great. No dramas. This is very competent DOS gaming PC.


# Modifying BIOS features

Can do this with a SOP8 clip.

https://chatgpt.com/share/69546867-1580-8003-9925-d553cd9af5e1
