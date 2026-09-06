---
layout: post
title: Turning a Dell Dimension E520 into a Retro Gaming PC
date: '2026-03-30 08:00:00'
tags: [MS-DOS, PC, Projects, Retrocomputing, Retrogaming, Windows 98, Windows XP]
status: in progress
---

The [Dell Dimension E520]({% link _hardware/dell-dimension-e520.md %}) is the home-market cousin of [the OptiPlex 760]({% link _projects/turning-a-dell-optiplex-760-into-a-retro-gaming-pc.md %}) — same Core 2 / mid-2000s Dell generation, similar retro potential, and its own separate set of quirks to work through.

### Project Notes

Status | In progress
Goal | Turn a Dell Dimension E520 into a working DOS/Windows 98/XP retro gaming PC.

Unlike the 760, the E520's BIOS "OS Install" mode caps RAM at 256MB — genuinely useful for getting a Windows 98 install past its usual memory ceiling. Installing meant slipstreaming rloew's SATA patch, the unofficial Intel INF files, and rloew's PATCHMEM utility onto the setup media ahead of time.

The install itself surfaced a stubborn, still only partly-understood issue: long hangs and freezes on boot that eventually clear on their own, pointing to a timeout rather than a crash. Disabling ACPI at setup (`/p i`) didn't help; disabling 32-bit disk access did fix it, at the cost of disk performance. Graphics brought a separate fight — a Radeon X600 with Catalyst 6.2 (and later 9.0c, and an X700 for comparison) froze Windows outright on driver load, most likely a VRAM-aperture/memory-mapping conflict between this late chipset's AGP emulation and Win98's memory handling. VBE Miniport drivers became the practical fallback — no Direct3D, but higher color depth and DirectDraw for titles like Quake II in software mode. A Voodoo 2 with FastVoodoo 4.6, by contrast, worked great — accelerated Quake II, Unreal, and 3DMark with no issues at all.

DOS performance itself is strong, but the input side isn't solved. There's no PS/2 or serial port — just unpopulated solder pads on the board — so native DOS USB keyboard input stays laggy and buffered. Windows XP, as with the 760, is simply the natural fit for this hardware generation.

Still open: solving native DOS keyboard input (a BIOS unlock, or wiring up the solder pads), finding a smaller disk or SSD to see if the disk hang persists, trying older Catalyst driver versions or softgpu for the graphics issue, and getting sound working (Voodoo 2 succeeded, a sound card hasn't yet).

More details:

- [Dell Dimension E520 hardware page]({% link _hardware/dell-dimension-e520.md %})
- [I Tried to Turn a Dell Dimension E520 into a Windows 98 Retro PC]({% post_url 2026-03-30-i-tried-to-turn-a-dell-dimension-e520-into-a-windows-98-retro-pc %})
