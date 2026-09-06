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

The board is a [MiTAC MSC-373]({% link _hardware/mitac-msc-373.md %}) — a 440BX-chipset, Socket 370 Pentium III single-board computer, paired with a PICMG backplane that has no documentation of its own, so getting it powered up at all took some intuition. Full board and backplane details live on the hardware page.

Once running, it turned out to be a genuinely capable little PC — solid DOS performance and sound, a smooth Windows 98 install, and a [3dfx Voodoo 3]({% link _hardware/3dfx-voodoo-3.md %}) upgrade to fix the onboard graphics chip's complete lack of Direct3D acceleration. The full build, testing, and benchmark story is in the writeup below.

Overall, a clean success — an industrial board with no gaming pedigree turned into a fully functional retro PC, with the added bonus that swapping the single-board "card" out is the whole upgrade path: the same backplane and peripherals could just as easily host a 386, 486, or a much faster Pentium 4-class SBC.

More details:

- [MiTAC MSC-373 hardware page]({% link _hardware/mitac-msc-373.md %})
- [3dfx Voodoo 3 hardware page]({% link _hardware/3dfx-voodoo-3.md %})
- "This Fully Functional PC Fits on a Single Card" — full writeup (drafted, not yet published — update this to a real link once it's out)
- [MiTAC MSC-373 board reference (TheRetroWeb)](https://theretroweb.com/motherboards/s/mitac-trigon-msc-373)

And also in video form below. Enjoy!

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/eGxguvyLegg?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

<br />
