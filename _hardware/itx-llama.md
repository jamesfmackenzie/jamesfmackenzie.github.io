---
layout: post
title: ITX Llama
summary: A modern retro PC motherboard built specifically for authentic DOS and early Windows gaming.
date: '2024-08-29 11:33:00'
tags: [Computers, PC]
---

![](/img/hardware/som-128-ex.png)

The **ITX Llama** is a *modern, open‑source motherboard* designed from the ground up to deliver maximum compatibility with **real MS‑DOS and early Windows (95/98)** software — without relying on emulation. Unlike typical retro builds that repurpose old hardware, the ITX Llama is brand new hardware engineered specifically to solve the problems of running classic software on *authentic x86 hardware* in a modern, compact form factor.

---

### What the ITX Llama is

At its core, the ITX Llama is a **retro‑focused ITX motherboard** built around a **Vortex86EX system‑on‑module (SOM)** — an x86 compatible processor that behaves much like a classic Pentium / Pentium MMX‑era CPU. The goal is not to emulate classic PC hardware, but to *run legacy software on real x86 silicon with hardware features that match* what DOS and Windows 9x games expect.

This project is fully **open source**, with schematics, board files, and BIOS available for anyone to build or modify. Although boards have been offered via community group buys, the designs are not restricted to a single supplier — hobbyists can have their own boards manufactured from the design files.
---

### Technical specifications

| Component | Details |
|-----------|---------|
| **CPU / Core** | Vortex86EX system‑on‑module (x86 compatible) |
| **CPU performance** | Selectable clock ~60–500 MHz, roughly Pentium MMX class |
| **RAM** | 128 MB DDR3 on the SOM |
| **Audio** | Crystal CS4237B with Sound Blaster Pro 2, AdLib, Windows Sound System support |
| **Optional audio features** | Header for genuine Yamaha OPL3 module, wavetable MIDI header, MT32‑pi integration |
| **Storage** | SD card slot, SATA port, USB mass storage support |
| **Expansion slot** | AGP 1× (3.3V keyed) with PCI Express to PCI/AGP conversion |
| **I/O** | PS/2 keyboard/mouse, USB 2.0, RS‑232 serial, gameport/MIDI support |
| **Network** | 10/100 Ethernet + ESP8266 serial‑to‑WiFi modem |
| **BIOS** | Coreboot/SeaBIOS based firmware |
| **Legacy support** | MS‑DOS, FreeDOS, Windows 3.1/95/98 |
| **Form factor** | ITX form factor designed for retro builds |

---

### What makes the ITX Llama special

#### 1. Designed for authentic legacy software

Unlike repurposed modern motherboards, the ITX Llama’s CPU, chipset, and I/O subsystems are *intentionally chosen and configured* to behave more like classic PC architectures. This helps avoid the common pitfalls of retro gaming on modern hardware — such as missing Sound Blaster support, timing issues, and driver incompatibilities.

#### 2. Sound and music support

The integrated Crystal CS4237B audio chipset delivers:

- **AdLib FM synthesis**
- **Sound Blaster Pro 2 compatibility**
- **Windows Sound System support**

For purists, there are headers to add a **real Yamaha OPL3 module** for 100% authentic FM synthesis — or connect a Raspberry Pi using **mt32‑pi firmware** for Roland MT‑32 MIDI playback.

#### 3. AGP and legacy graphics

Unlike many retro boards that only support PCI, the ITX Llama includes a **3.3V‑keyed AGP 1× slot** via an onboard converter bridge. This allows a wide range of classic AGP cards — including **Radeon 9200/9250 and Voodoo3** — to function in an authentic AGP environment.

#### 4. Flexible storage options

The board supports multiple storage media:

- **microSD card slot** (can emulate an IDE hard drive)
- **SATA port** for SSD or optical drives
- **USB mass storage** support via BIOS

This range makes it easy to install DOS and Windows without special drivers or adapters.

#### 5. PC‑style legacy I/O

The ITX Llama provides:

- PS/2 keyboard and mouse (with USB‑to‑HID to PS/2 translation)
- Serial RS‑232 port
- Gameport with MIDI interfaces
- Audio I/O including SPDIF digital out
- Ethernet networking with optional Wi‑Fi modem emulation

This combination lets you use classic peripherals and connect to vintage hardware with minimal adapters.

---

### Operating system support

The ITX Llama is designed to boot and run a variety of legacy operating systems natively:

- **MS‑DOS and FreeDOS**
- **Windows 3.1**
- **Windows 95**
- **Windows 98**

This makes it one of the rare modern boards where classic OSes run without extensive patching or hardware trickery.

---

### Practical retro use cases

- **DOS gaming:** Native Sound Blaster, FM, and MIDI support make classic games feel “just right”
- **Windows 98 gaming:** AGP graphics and legacy sound make early 3D titles playable
- **Hardware MIDI setups:** Connect real or emulated MT‑32, SC‑55, or other sound modules
- **BBS and serial hobbyist projects:** ESP8266 modem emulation adds a fun retro networking twist

---

### Community, availability, and group buys

The ITX Llama hardware is **open source**, and though boards are not mass‑produced commercially, they have been offered via **community group buys** and Discord coordination. Enthusiasts can also order PCB fabrication from any PCB house using the open design files.

Online forums such as Vogons have active discussions on compatibility, construction, and retro builds, while community hardware group buys have helped get assembled boards into hands around the world.

---

### Known limitations and quirks

No project is perfect, and the ITX Llama has a few edge cases to be aware of:

- **Audio limitations on early batches:** Some boards downmix analog audio; later revisions are being improved.
- AGP support depends on 3.3V‑keyed cards; some PCI‑only GPUs may not fit.
- Classic game compatibility may still require tweaking settings or drivers, just like real vintage hardware.

---

### Summary

The ITX Llama is a **modern retro computing dream** — a clean‑sheet motherboard designed for legacy DOS and Windows gaming without emulation. By combining authentic sound, legacy I/O, AGP graphics support, and open‑source hardware design, it offers an experience closer to the classic PCs of the 1990s than almost any other modern project.

Whether you’re interested in building a *true hardware retro platform* or exploring MS‑DOS and early Windows titles with real hardware behaviour, the ITX Llama delivers an unmatched blend of **authenticity, flexibility, and modern reliability**.
