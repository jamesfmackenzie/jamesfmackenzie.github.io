
#projects 

(See my similar article [[Turn a Dell Optiplex 380 into a monster retro PC]], this is probably very similar)


# Hardware overview

The hardware is a no-frills Dell home PC using the Intel G965 Express chipset and ICH8 controller / IO hub.

Processor

- Processor type - Intel® Pentium® 4 with Hyper-Threading technology
- Level 1 (L1) cache - 32KB
- Level 2 (L2) cache - 1MB

Memory

- Type - 533-MHz and 667-MHz dual DDR2 unbuffered SDRAM
- Memory connectors - four
- Memory capacities - 256 MB, 512 MB, or 1 GB non-ECC
- Minimum memory - 256 MB
- Maximum memory - 4 GB
- BIOS address F0000h

Computer Information

- Chipset 965
- RAID Support RAID 1 (Mirroring)
- DMA channels eight
- Interrupt levels 24
- BIOS chip (NVRAM) 4 Mb
- NIC Integrated network interface capable of 10/100 communication
- System clock 800- or 1066-MHz data rate

Expansion

- PCI connectors two
- PCI Express connector one x1
- PCI Express connector one x16

Chipset

Chipset wise, it has the ICH8 controller hub with Intel HDA and an Sigmatel STAC9227X5 audio codec chip.

![[Pasted image 20251231094615.jpg]]

My specific model has:

- Intel Core 2 Duo E4300 @ 1.8GHz
- 3GB DDR2 RAM

![[e520-system-info.png]]

![[dell-e520-bios-processor-info.jpg]]

![[dell-e520-bios-memory-info.jpg]]

## OS Install Mode

This is very interesting for retro gaming, as it restricts the maximum available memory to 256MB.

![[dell-e520-bios-os-install-feature.jpg]]


## User Manual

![[dell-e520-user-manual.pdf]]



# Installing Windows 98

This is the process I followed:

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

(Actually this didn’t work, I got an error. I was able to turn off OS install mode later and run PATCHMEM)

Then reboot and continue Windows setup

Product key: PRDDH-83JD9-G6PK4-684GF-6Y73B


## Disk access issues

After following the win 98 install instructions, the installer process rebooted one last time

After restart, there was a black screen for a long time (a few minutes).

I thought windows install failed but eventually it loaded up OK.

Then it went through the last configuration steps, again hanging up on a relatively consistent basis.

Eventually everything loads up, but it became stuck on the “Welcome to Windows 98” screen. Even num lock doesn’t work.

Seems like something is more quite right.

Is it a bad hard disk?
Perhaps it was a mistake to install the SATA patch? 
Perhaps it is some ongoing weirdness with using a USB keyboard?
Or some other incompatibility? 

More investigation is required.

Perhaps a check disk or a scan disk?
Perhaps boot to safe mode?
Perhaps check the event log?

The first thing I tried was disabling multi core CPU in the bios => no go

The second thing I tried was switching the graphics card from the Radeon HD 4870 to a more period appropriate Radeon X600 => no go

The next thing I tried was reinstalling Windows with the setup /p i option

This disables ACPI. The E520’s ACPI implementation is far newer than Win98 expects. 

Unfortunately this also didn’t work — exact same issue.

Because the computer *eventually* unfreezes, it really seems like some kind of timeout issue rather than a freeze/crash.

Suspecting a disk access issue, i booted to safe mode to disable 32-bit disk access:


Disable 32-bit disk access (real, supported)

This is the only supported way to force BIOS disk access in Win98.

Control Panel → System → Performance

- If it says “Compatibility mode paging”, 32-bit disk access is already off

You can also disable it via:  

- File System → Troubleshooting → Disable 32-bit disk access

This does work!! But (allegedly!) performance will be poor.

OK, on with the driver setup!


1. Checked Device Manager, make sure those INF files are good


## Graphics

2. Installed DirectX. I got the latest Windows 98 SE version from here:

http://falconfly.3dfx.pl/directx.htm 

**DONE. I installed directx 7.0a**

3. Radeon 6.2 Drivers -> for X600

**DONE. But something very weird happens. Windows freezes on loading. I had to uninstall the drivers.**

This could be a problem with directx. Being a newer card, the Radeon may require DirectX 9.0b/c to function properly.

Nope. Even with DirectX 9.0c is still has the same issue. I will need to look for other driver versions.

The same also happens with an X700 card.

After some research, it seems like this might be a problem memory timings, chipset and AGP emulation (although this could be LLM nonsense)

*Why the Radeon X600 is a “danger zone” card for Win98*

*The [ATI](chatgpt://generic-entity?number=0) Radeon X600 sits right on the ragged edge of Windows 98 support:*

- *First-gen PCIe-native Radeon*
- *Very late Win9x driver stack*
- *Requires perfect chipset + memory + AGP emulation behaviour*

*Extremely sensitive to:*  

- *RAM size*
- *VCache behaviour*
- *PCIe bridge quirks*

*On mid-2000s Intel chipsets (like the E520), this often fails exactly as you’re seeing.*

*The #1 cause in* your case (very likely)

*Given everything we’ve already learned:*

*The Catalyst driver is crashing when allocating video memory due to Win98 memory / VCache interaction.*

*This is not obvious, but it’s one of the most common X-series failure modes.*

*Why Standard VGA works*

- *No acceleration*
- *No DMA*
- *No VRAM aperture programming*

*Why Catalyst crashes*

- *Driver asks Windows for memory mappings*
- *VCache / RAM limits are still wrong*
- *Driver receives invalid addresses*
- *💥 hard crash at splash*


I tried incrementally turning down hardware acceleration in safe mode display settings.

Unfortunately even at “None” settings it still don’t work.

Next up, I tried to install PATCHMEM. Previously it wasn’t needed (since we’re using OS Install feature to restrict the memory to 256MB). But it’s worth a try? => nope, still doesn’t work.

For the future, I should probably try a different Radeon driver (i.e. not 6.2). But as a short term workaround, i decided to move ahead with VBE Miniport drivers — which at least give access to higher color depth and direct draw — if not direct 3d.

With these installed, Windows loaded OK and i was able to boost the resolution.

I tried some basic games — quake 2 in software rendering mode works especially well.

![[Pasted image 20260101010632.jpg]]

## Voodoo 2

Next up, i installed a Voodoo 2 with FastVoodoo 4.6 drivers. This worked very well and i was even able to get Quake 2, Unreal and 3D Mark running with accelerated graphics.

![[Pasted image 20260101013959.jpg]]

![[Pasted image 20260101014043.jpg]]

![[Pasted image 20260101014057.jpg]]

![[Pasted image 20260101014114.jpg]]

## Still to do on Win 98

For the disk issues:

- Use a smaller disk or SSD. Do I still get the random disk hang ups etc and do i still need to disable 32-bit disk access.
- If I'm unable to resolve the disk issue, consider getting a SATA controller card (ask ChatGPT which versions are good and research it)

For the GPU issues:

- Try lower versions of Radeon graphics drivers. Allegedly catalyst 5.9 may work better?
- Try out softgpu

For sound:

- Try a sound card. I was able to get Voodoo 2 working, but not a sound card (yet).
- Try WDMHDA


# Installing Windows XP

This is a much more suitable Operating System for this machine.

Although designed for Vista, XP drivers exist for the chipset and integrated peripherals.



# DOS

I was able to boot the e520 into DOS mode relatively easily and play some DOS games.

![[Pasted image 20260101014357.jpg]]

## Keyboard Issues

One issue I ran into: when running in native DOS, USB keyboard input can become very buffered and laggy. This is a known issue with Dell Dimension/Optiplex PCs and DOS.

The fix is to use a serial or PS/2 keyboard. 

Unfortunately this PC has no PS/2 or serial ports. Is it possible to buy a PCI or PCIe port expansion card with PS/2 ports, but unfortunately these use USB-to-PS/2 adapter chips, and won’t work in DOS.

So seems like the only solution is either to:

1. ==Flash or unlock the BIOS to enable USB legacy keyboard support==
2. ==Solder a serial header into the PC (it has the port on the motherboard, just with solder pads and no header)==

## Voodoo 2

On top of that, I was also able to get the shortcut voodoo 2 demo working on DOS 

![[Pasted image 20260101010730.jpg]]


# Other Photos

![[dell-e520-bios-pci-info.jpg]]

![[dell-e520-bios-system-info.jpg]]

# Modifying BIOS features

Can do this with a SOP8 clip.

https://chatgpt.com/share/69546867-1580-8003-9925-d553cd9af5e1