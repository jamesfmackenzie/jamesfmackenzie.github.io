---
layout: post
title: This Fully Functional PC Fits on a Single Card
summary: An industrial Pentium III single-board computer, built for factory floors rather than gaming, turned into a genuinely capable DOS and Windows 98 machine.
tags: [MS-DOS, PC, Retrocomputing, Retrogaming, Windows 98]
---

Industrial PCs work backwards from a normal desktop. Instead of a motherboard with a chipset, a northbridge and southbridge, and a CPU socket, all of that is squeezed onto a single card — a genuine, complete PC on a card. That card then plugs into a backplane, and the backplane does almost nothing on its own: it just supplies ATX or AT power through to the card, and breaks the ISA and PCI buses out into physical slots for add-on hardware.

It's a strange, backwards way to build a PC — but it makes a lot of sense in an industrial setting. The backplane is dead simple (just sockets and power), so it's very unlikely to fail. And if the actual computer part does die, you don't troubleshoot whether it's the RAM, the CPU, or the motherboard — you just pull the card, drop in an identical one, and you're back running.

None of that has anything to do with gaming. So naturally, I wanted to see if I could turn one into a DOS and Windows 98 machine anyway.

### The board

The card in question is a [MiTAC MSC-373]({% link _hardware/mitac-msc-373.md %}) — a 440BX-chipset, Socket 370 single-board computer, populated here with a Pentium III. Full specs, the PICMG backplane arrangement, and the power/LED gotchas are on the hardware page; the short version is 4 DIMM slots for PC100 SDRAM, 2 IDE ports, onboard Chips & Technologies B69000 graphics, and a rear panel with 10/100 Ethernet, VGA, and PS/2 ports.

There's no documentation at all for the specific backplane model I ended up with (an MBP-PCI6R-ATX), so getting it powered up the first time took some intuition: reading the jumper guide printed right on the board silkscreen to pick ATX power mode, then discovering there's no actual power button on the backplane — the power switch is just a jumper (J3) waiting to be shorted. Once it came alive, a row of unlabeled LEDs turned out to be per-rail power indicators; the only one that reads "off" is −5V, which is completely expected on a modern ATX supply, and harmless unless you're running one of the small number of old ISA cards that specifically need that rail.

### Putting it together

For input, PS/2 keyboard and mouse plug directly into the SBC. For storage, an IDE-to-CompactFlash adapter, preloaded with DOS and the Windows 98 setup files, does the job of a hard disk. For sound, an ISA card by Aztech — part sound card, part modem, a real Frankenstein of a combo card — buried somewhere in its feature list is genuine Sound Blaster Pro compatibility, which turned out to be all that mattered.

### DOS

Straight to a DOS prompt on first boot — always a good sign. `MEM` confirmed 64MB of RAM, and Unisound reported a clean initialization for the Aztech card. Testing followed the usual pattern: Commander Keen 4 for FM synth audio, then Tyrian for PCM — both sounded great and ran smoothly.

For performance, Phil's DOSBench put this thing at roughly 120fps in both the Doom and Quake benchmarks at max detail — leagues ahead of a 486 or an early Pentium. SysInfo actually misidentified the CPU as a Pentium at 850MHz; it's really a Pentium III at 750MHz, but either way, there was plenty of headroom to spare. With that kind of speed on tap, Duke Nukem 3D's SVGA mode — normally the kind of setting that grinds a period-correct DOS machine to a crawl — ran completely smoothly.

### Windows 98

The Windows 98 setup program predicted 60 minutes. It took about 6. Device Manager confirmed the onboard Chips & Technologies B69000 graphics, and dxdiag confirmed the expected: no Direct3D acceleration at all on that chip. So it needed a graphics boost — a Voodoo 3 PCI card went in next.

With the Voodoo 3 installed, 3DMark confirmed Direct3D was working well, Quake II covered OpenGL, and Unreal covered Glide — all fine. One more test for good measure: a handful of DOS games support Glide natively, and a properly patched copy of Tomb Raider is one of them. That worked too, straight from DOS.

### Verdict

Mission successful — there was no "industrial PC" penalty anywhere in this. It behaved exactly like a normal period PC would, across DOS, Windows 98, software rendering, and accelerated 3D. The part I like most about the format is what happens next: since the backplane and all the peripherals are separate from the actual computer, the whole setup is modular. If I want a 386 or a 486 machine, I can swap in a different SBC. If I want something faster than this Pentium III, there's PICMG-format cards up to Pentium 4-class hardware. Same backplane, same peripherals, completely different era of PC, just by swapping one card.

Now I just need a proper chunky AT case to put it all in.
