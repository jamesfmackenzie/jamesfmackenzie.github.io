---
layout: post
title: Turning a Dell OptiPlex 760 into a Retro Gaming PC
date: '2026-03-29 09:00:00'
tags: [MS-DOS, PC, Projects, Retrocomputing, Retrogaming, Windows 98, Windows XP]
status: in progress
---

![Dell OptiPlex 760 tower](/img/posts/dell-optiplex-760.jpg)

After the [OptiPlex 380]({% link _hardware/dell-optiplex-380.md %}) turned into such a strong multi-era retro PC, I wanted to see if the same trick would work on its newer sibling — the [OptiPlex 760]({% link _hardware/dell-optiplex-760.md %}). It didn't repeat quite as cleanly.

### Project Notes

Status | In progress
Goal | See whether a newer, ICH10-generation OptiPlex can match the 380's DOS/Win98/XP retro range.

Unlike the 380, the 760 has no BIOS "OS Install" RAM-limiting mode, so a proper Windows 98 install needs a memory patch rather than a BIOS shortcut — I initially sidestepped this by cloning over an existing Win98 drive from [my Dimension E520 build]({% link _projects/turning-a-dell-dimension-e520-into-a-retro-gaming-pc.md %}) to get a quick read on viability. A Radeon X600 dropped in easily with Catalyst 6.2 and full hardware Direct3D, but a Voodoo 2 refuses to work at all — constant crashes and `FXMEMMAP` blue screens that survive even stripping the system down to bare hardware, most likely a memory-map conflict tied to the `ICH10` southbridge.

Onboard audio (an Analog Devices `AD1984A` HD codec) has no official Windows 98 support, and the community [WDMHDA](https://github.com/andrew-hoffman/WDMHDA) driver installs but currently doesn't support this specific codec chip — [reported on Vogons](https://www.vogons.org/viewtopic.php?t=109373) for anyone tracking that project's progress.

DOS fares much better: the motherboard exposes a serial header, so adding a PS/2 keyboard sidesteps the USB input lag that's a running theme on these Dell boards, and SBEMU handles sound cleanly with no drama. Windows XP is the machine's natural home — every chipset driver installs without a fight and it's fast — while Windows 7 boots but clearly wants an SSD and more RAM than this box has.

Still open: fixing Voodoo 2 (possibly needs a BIOS unlock via SOP8 clip to free up memory-mapping options), confirming whether 32-bit disk access needs disabling as it did on the E520, and keeping an eye on WDMHDA for AD1984A support.

More details:

- [Dell OptiPlex 760 hardware page]({% link _hardware/dell-optiplex-760.md %})
- [I Tried to Turn a Dell OptiPlex 760 into a Windows 98 Retro PC]({% post_url 2026-03-29-i-tried-to-turn-a-dell-optiplex-760-into-a-windows-98-retro-pc %})
