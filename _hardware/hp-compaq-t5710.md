---
layout: post
title: HP Compaq t5710
summary: 
date: '2024-08-29 11:33:00'
tags: [Computers, PC]
---

![](/img/posts/hp-compaq-t5710-back.jpg)

The HP Compaq t5710 is a compact **thin client** released in 2004, designed primarily for enterprise deployments. Despite its intended purpose as a lightweight networked device, it has become a surprisingly capable platform for **DOS and Windows 98 gaming** — particularly for retro enthusiasts with limited space.  

I first purchased one after moving to New York in 2019, seeking a retro PC that didn’t take up much apartment space. Its small footprint hides a surprisingly flexible system that supports classic DOS audio, early Windows 9x gaming, and even PCI graphics expansion.

---

### Why the t5710 is interesting for retro use

Thin clients aren’t usually associated with gaming, but the t5710 has several features that make it attractive:

- Compact, low-noise, and energy-efficient
- Onboard legacy support:
  - **PS/2 keyboard/mouse**
  - Serial header for classic input devices
- A **PCI expansion slot**, uncommon in small thin clients
- Fully DOS-compatible audio:
  - Sound Blaster Pro support
  - AdLib FM synthesis
- Windows 98–friendly hardware once configured

Despite being a 2004 device, it covers nearly every retro use-case in a single, low-cost, ultra-small form factor.

---

### Specifications

| Component           | Details                                                                 |
|---------------------|-------------------------------------------------------------------------|
| **CPU**             | Transmeta Crusoe, 800 MHz                                               |
| **RAM**             | 256–512 MB DDR2 (expandable depending on model)                         |
| **Graphics**        | Integrated ATI Radeon 7000M with 16 MB dedicated graphics memory        |
| **Storage**         | 44-pin IDE for Disk on Module or Compact Flash storage                  |
| **Audio**           | SBPro–compatible audio; supports DOS Sound Blaster / AdLib              |
| **Expansion**       | 1× PCI slot                                                             |
| **I/O**             | PS/2 keyboard/mouse, 4x USB 2.0, serial port, parallel port, VGA output |
| **OS Compatibility**| DOS, Windows 98 SE, Windows XP                                          |
| **Form Factor**     | Thin client (small footprint, fanless design)                           |

---

### DOS and Windows 98 compatibility

The t5710 shines in DOS and early Windows environments:

- Native DOS audio works **out of the box**:
  - Sound Blaster Pro emulation
  - AdLib FM synthesis fully functional
- Windows 98 installation is achievable with minor tweaks
- PS/2 keyboard input works reliably, and USB can be used if necessary
- Storage: a CF-to-IDE adapter provides reliable disk access for Win98

After trial and error, I was able to <a href="https://youtu.be/V4DIPffO-sI" target="_blank">successfully install and game on Windows 98</a>.

---

### PCI expansion: 3dfx Voodoo 2

The single PCI slot opens the door to more ambitious retro builds:

- After testing, I successfully installed a **3dfx Voodoo 2 PCI card**
- This allowed for classic **Glide acceleration** in Windows 98 and DOS games
- Combining onboard SBPro-compatible audio and Voodoo 2 graphics produces a surprisingly authentic retro experience

This is particularly notable because most thin clients of this era do **not** support legacy PCI expansion for 3dfx hardware.

---

### Practical retro notes

- **PS/2 splitter:** I was able to use a [working Monoprice PS/2 splitter]({% post_url 2021-11-13-using-monoprice-ps2-splitter-with-hp-compaq-t5710-review %}) for reliable keyboard and mouse input
- **Sound:** Both native DOS and Win98 sound work well; MIDI playback and FM synthesis are accurate
- **GPU:** While onboard S3 graphics are adequate for early DOS titles, Voodoo 2 PCI support enables higher-end Glide games
- **Form factor:** Ultra-compact; ideal for small desks, apartments, or dedicated retro setups

---

### Known quirks and limitations

- Limited RAM (256–512 MB) may require careful configuration for Windows 98 or XP
- Only one PCI slot: expansion choices are limited
- Onboard graphics performance is weak for later 3D titles
- Storage options may require adapters or compact drives

None of these are deal-breakers, but they require planning for optimal retro performance.

---

### Summary

The HP Compaq t5710 is a remarkable “hidden gem” for retro enthusiasts. It combines:

- Small footprint
- Authentic DOS / Windows 98 sound
- Reliable PS/2 input
- PCI expansion for Voodoo 2 and other legacy cards

For compact retro PC setups where space is at a premium, the t5710 delivers a surprising amount of capability in a single, tiny package.  

I can **thoroughly recommend** it for anyone exploring classic DOS, early Windows
