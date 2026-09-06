---
layout: post
title: This Fully Functional PC Fits on a Single Card!
date: '2024-10-05 09:30:00'
tags: [MS-DOS, PC, Projects, Retrocomputing, Retrogaming, Windows 98]
status: completed
---

Industrial PCs work backwards from a normal desktop: instead of a motherboard with sockets for a CPU and expansion cards, the entire computer — chipset, CPU, RAM, graphics — is crammed onto one card, which then plugs into a backplane that exists purely to supply power and break out ISA/PCI slots. I wanted to see if one of these industrial boards, never meant for gaming, could be turned into a real DOS and Windows 98 machine.

### Project Notes

Status | Completed
Goal | Turn an industrial PICMG single-board computer into a working DOS/Windows 98 retro gaming PC.

The board is a MiTAC MSC-373 — a 440BX-chipset, Socket 370 Pentium III single-board computer — paired with an MBP-PCI6R-ATX backplane (4 ISA slots, 3 PCI slots, two of them wired for the PICMG connector the SBC plugs into). With no documentation for the backplane to go on, getting it powered up at all took some jumper guesswork (ATX vs AT power selection) and finding the bare power-switch header to short by hand.

Once running, it turned out to be a genuinely capable little PC: DOS booted straight up with 64MB of RAM, Sound Blaster Pro-compatible audio from an ISA sound/modem combo card handled FM and PCM fine across Keen 4, Jazz Jackrabbit, and Tyrian, and DOSBench-measured Doom/Quake performance was strong enough to push into SVGA Duke Nukem 3D territory. Windows 98 installed cleanly too — the onboard Chips & Technologies B69000 graphics chip is predictably weak (no Direct3D acceleration at all), but adding a [3dfx Voodoo 3]({% link _hardware/3dfx-voodoo-3.md %}) fixed that completely, running 3DMark and Quake II under Direct3D/OpenGL, Unreal via Glide, and even a Glide-patched copy of Tomb Raider straight from DOS.

Overall, a clean success — an industrial board with no gaming pedigree turned into a fully functional retro PC, with the added bonus that swapping the single-board "card" out is the whole upgrade path: the same backplane and peripherals could just as easily host a 386, 486, or a much faster Pentium 4-class SBC.

More details:

- [3dfx Voodoo 3 hardware page]({% link _hardware/3dfx-voodoo-3.md %})
- [MiTAC MSC-373 board reference (TheRetroWeb)](https://theretroweb.com/motherboards/s/mitac-trigon-msc-373)
- [This Fully Functional PC Fits on a Single Card!]({% post_url 2024-10-05-this-fully-function-pc-fits-on-a-single-card-pentium-iii-sbc %})

And also in video form below. Enjoy!

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/eGxguvyLegg?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

<br />
