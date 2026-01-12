---
layout: post
title: Dell Dimension e520
summary: 
date: '2025-12-29 10:30:00'
tags: [Computers, PC]
---

The Dell Dimension E520 is a no-frills mid-2000s home PC built around Intel’s **G965 Express chipset** and **ICH8** southbridge.

This page documents what makes the E520 interesting for retro experimentation, where it works well, and where it becomes challenging — particularly for **Windows 98** and **native DOS** use.

---


### Why the Dimension E520 is interesting (and sometimes challenging)

The E520 sits right on the transition point where PC hardware starts to drift away from classic DOS and Windows 9x expectations:

- Core 2–class performance for late DOS and Win9x games
- PCI *and* PCIe expansion
- A BIOS feature that can **limit RAM to 256MB**
- SATA storage exposed via BIOS

…but also:

- A newer chipset and southbridge (**ICH8**) than Win98 expects
- No native PS/2 or serial ports
- Increasing sensitivity to memory timing, disk access, and PCIe quirks

As a result, the E520 can be made to work — but it requires more compromise and experimentation.


### Core specifications

Specifications vary by configuration, but most Dimension E520 systems share the following baseline:

- **Chipset:** Intel G965 Express + ICH8
- **Memory:** DDR2-533 / DDR2-667
  - 4 DIMM slots
  - Up to 4GB total
- **Storage:** SATA
- **Graphics:** Intel GMA 3000 (onboard)
- **Networking:** Integrated 10/100 Ethernet

My personal machine has:

- **CPU:** Intel Core 2 Duo E4300 @ 1.8GHz
- **Memory:** 3GB DDR2


### Expansion slots

The Dimension E520 offers reasonable expansion for its era:

- **2× PCI**
- **1× PCI Express x1**
- **1× PCI Express x16**

This allows for:

- A discrete PCIe graphics card
- PCI sound cards or I/O expansion cards

However, not all PCIe GPUs behave well under Windows 98 on this platform.


### BIOS features that matter

#### OS Install mode (RAM limiting)

Like some Dell systems of this era, the E520 BIOS includes an **“OS Install”** option.

When enabled, this limits available system memory to **256MB**, which is extremely useful for:

- Installing **Windows 98**
- Avoiding early setup crashes on high-RAM systems

This feature is one of the E520’s biggest advantages for retro experimentation.


### Windows 98 compatibility overview

Windows 98 compatibility is there, but needs a bit of work:

**Out of the box:** ❌  
**With patches and workarounds:** ⚠️ mixed

#### Required patches and files

To get Windows 98 installed at all, the following is recommended:

- **rloew SATA patch**
- **Unofficial Intel chipset INF files**
  - LoneCrusader’s Intel INF set
- **Optional:** rloew PATCHMEM (for >256MB RAM)

The hard disk was prepared as a **32GB FAT32** partition before installation.


## Windows 98 behaviour (important)

Windows 98 *does* install on the E520, but once installed it behaves oddly:

- Long black screens after reboot (minutes, not seconds)
- Apparent freezes during boot that eventually recover
- Hanging on the “Welcome to Windows 98” screen
- Keyboard input sometimes unresponsive

Because the system eventually unfreezes, this appears to be a **timeout or disk-access issue**, not a hard crash.


### Disk access problems and the key workaround

The most reliable way to stabilize Windows 98 on this machine was to **disable 32-bit disk access**:

```
Control Panel → System → Performance
```

or  

```
File System → Troubleshooting → Disable 32-bit disk access
```

This forces BIOS-level disk access and dramatically improves stability — at the cost of (some) disk performance.

This is a *real, supported* Windows 98 setting, but it highlights how close to the edge the E520 is for Win98 use.


### Graphics under Windows 98: the Radeon problem

This system exposed a major Windows 98 pitfall.

Multiple Radeon cards were tested, including:

- Radeon X600
- Radeon X700

Results:

- **Standard VGA driver:** works
- **Catalyst drivers:** system freezes during Windows load

Even with:

- Hardware acceleration disabled
- DirectX 9.0c installed
- PATCHMEM applied
- RAM restricted to 256MB

…the Catalyst driver still crashes during initialization.


#### Why this happens

The Radeon X600 and X700 sit in a known **Windows 98 danger zone**:

- First-generation PCIe-native Radeon
- Late Win9x driver stack
- Operates with a PCIe bridge and AGP emulation

On mid-2000s Intel chipsets like G965, this might cause issues with when the driver attempts VRAM and memory mapping.

Perhaps older cards might work better. But for now I found a workaround.


### The workaround: Universal VBE video display driver

As a practical workaround, we can use the <a href="https://bearwindows.zcm.com.au/vbe9x.htm" target="_blank">Universal VBE video display driver</a>.

This driver is designed as a "fall back" for when manufacturer drivers are missing or not working.

It provides:

- Higher resolutions
- Better colour depth
- DirectDraw support

However it *doesn't* provide OpenGL or Direct3D accleration.

This setup works well for:

- Software-rendered games (e.g. Quake II in software mode)
- DOS titles


### Adding a Voodoo 2

To restore 3D acceleration:

- A **Voodoo 2** was installed
- **FastVoodoo 4.6** drivers used

Results:

- Quake II, Unreal, and 3DMark run with Glide acceleration
- Glide games are also supported in DOS

This hybrid approach (VBE + Voodoo) proved very effective.


### Sound support

Windows 98 sound works normally with supported cards and drivers.

If you *don't* have a dedicated sound card, the <a href="https://github.com/andrew-hoffman/WDMHDA" target="_blank">WDMHDA</a> project looks interesting. It's an effort to create a Windows 98 driver for Intel High Definition Audio — the perfect match for the e520.

Unfortunately WDMHDA hasn't reached maturity yet, but is something to watch with enthusiasm!


#### Native DOS audio

Native DOS sound is more limited due to the **ICH8 southbridge**, which lacks legacy DMA features expected by many PCI sound cards. A dedicated DOS-friendly PCI sound card is recommended, but compatibility varies.

Those without a dedicated sound card are also in luck, as <a href="https://github.com/crazii/SBEMU" target="_blank">SBEMU</a> Sound Blaster emulation works well.


### Keyboard issues in DOS

A significant DOS-specific issue:

- USB keyboard input becomes **laggy and buffered**
- Keystrokes may arrive late or in bursts
- Can cause hangs or crashes in DOS programs

This is a known issue on Dell Dimension / OptiPlex systems in DOS.


#### A potential fix

On other machines of this era, the fix is to use a **PS/2 or serial keyboard**. But unfortunately, the E520 has **no native PS/2 or serial ports**.

However, it *does* have solder pads for a serial / PS/2 header on the motherboard. Can this be used to restore PS/2 functionality? Perhaps!


### Windows XP compatibility

Windows XP is a far better match for the Dimension E520:

- Full chipset driver support
- Stable disk access
- Proper PCIe graphics support
- No RAM or ACPI issues

For Windows XP gaming, the E520 behaves exactly as intended.


### Summary: known quirks and limitations

- Windows 98 disk access instability unless 32-bit disk access is disabled
- PCIe Radeon X-series cards can be unstable or unusable in Win98
- USB keyboard input is unreliable in DOS
- Native DOS sound support is limited by chipset design
- Requires more workarounds than other Core 2 systems


## Who is the Dimension E520 *for*?

The E520 makes sense if you:

- Enjoy **experimentation and troubleshooting**
- Want a **Windows XP–first** retro system
- Plan to use **Voodoo hardware** for Win9x 3D
- Don’t mind mixing solutions (VBE + Glide)

It is *not* ideal if you want:

- A simple Windows 98 setup
- Reliable PCIe Direct3D under Win98
- Plug-and-play DOS compatibility


### Summary

The Dell Dimension E520 *almost* works for classic PC gaming — but lives just far enough past the comfort zone that Windows 98 and DOS require compromise.

With patience, it can still deliver a decent hybrid retro experience, especially when paired with 3dfx hardware. Just be prepared to experiment — and to accept that not everything will work as expected.

Sometimes the most interesting retro machines are the difficult ones. 🙂
