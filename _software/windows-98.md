---
layout: post
title: Windows 98
summary: The genuinely awkward middle-child OS on most of my retro PC builds — a real target, but one that gets harder to hit the newer the chipset gets.
date: '2025-11-26 23:35:00'
tags: [Operating Systems, PC]
---

Windows 98 is usually the hardest of the three targets I test for on a retro PC build — DOS, Windows 98, Windows XP. It's old enough that later chipsets and onboard audio were never designed with it in mind, but new enough that people expect a "beige box" build to run it without a fight.

### Where it actually lands

Across the machines I've tried it on, Windows 98 support tends to track how late the chipset is:

- The [Dell OptiPlex 380]({% link _hardware/dell-optiplex-380.md %}) has a BIOS RAM-limiting mode built in for exactly this, and is the cleaner, lower-drama Win98 build of the two OptiPlex machines.
- The [OptiPlex 760]({% link _hardware/dell-optiplex-760.md %}) doesn't have that RAM-limiting option, and its `ICH10` southbridge and `AD1984A` HD Audio codec are late enough that onboard sound under Win98 is still an open problem.
- The [Dell Dimension E520]({% link _hardware/dell-dimension-e520.md %}) landed somewhere in between — some genuinely useful Win98 roles, but more of a hybrid machine than a clean answer.

On all three, DOS was consistently the easy part and Windows XP the natural fit — it's specifically the Windows 98 window that narrows as the hardware gets newer.

### Related on this site

- [I Tried to Turn a Dell OptiPlex 760 into a Windows 98 Retro PC]({% post_url 2026-03-29-i-tried-to-turn-a-dell-optiplex-760-into-a-windows-98-retro-pc %})
- [I Tried to Turn a Dell Dimension E520 into a Windows 98 Retro PC]({% post_url 2026-03-30-i-tried-to-turn-a-dell-dimension-e520-into-a-windows-98-retro-pc %})
- [Dell OptiPlex 380]({% link _hardware/dell-optiplex-380.md %})
- [MS-DOS]({% link _software/ms-dos.md %})
