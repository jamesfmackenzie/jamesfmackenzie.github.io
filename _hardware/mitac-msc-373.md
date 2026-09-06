---
layout: post
title: MiTAC MSC-373
summary: A Pentium III single-board computer built for the PICMG 1.0 industrial-PC standard — a full 440BX-chipset PC squeezed onto one card, running in a passive PCI/ISA backplane instead of a normal motherboard.
date: '2026-09-06 00:00:00'
tags: [Computers, PC]
---

The MiTAC MSC-373 is an industrial single-board computer (SBC) — instead of a motherboard with a chipset and a CPU socket, the whole PC (chipset, CPU, RAM, graphics) is squeezed onto one long card that plugs into a passive backplane. I picked one up out of curiosity to see if an industrial board with no gaming pedigree could still make a fun DOS/Windows 98 machine — see [This Fully Functional PC Fits on a Single Card!]({% post_url 2024-10-05-this-fully-function-pc-fits-on-a-single-card-pentium-iii-sbc %}).

### How PICMG passive-backplane PCs work

Unlike a normal PC, the backplane itself does almost nothing — it exists purely to (1) supply ATX/AT power to the SBC through the PICMG connector, and (2) break out the ISA and PCI buses into physical slots for add-on cards. The SBC plugs into a long PICMG 1.0 slot that's really just a PCI connector and an ISA connector lined up next to each other. This gives a genuinely different repair model than a normal PC: if the machine dies, you don't troubleshoot RAM vs. CPU vs. motherboard — you just swap the whole card for an identical one and you're back running, with the peripherals in the backplane's slots untouched.

Mine came paired with an **MBP-PCI6R-ATX** backplane: 4 ISA slots and 3 PCI slots, two of the PCI slots wired into the PICMG arrangement for the SBC itself.

### Specifications

- **Chipset**: Intel 440BX
- **CPU**: Socket 370 (mine is a Pentium III)
- **Memory**: 4× DIMM sockets, PC100 SDRAM
- **Graphics**: onboard Chips & Technologies B69000
- **Storage**: 2× IDE, plus a floppy connector
- **I/O headers**: serial, parallel, USB
- **Rear panel**: 10/100 Ethernet, VGA, PS/2 keyboard and mouse
- **Other onboard**: PC speaker, real-time clock + CMOS battery, an unlabeled connector believed to be for an LCD panel
- **Backplane interface**: PICMG 1.0 (a combined ISA + PCI edge connector)

### Setup notes

- **Power jumper**: the board supports both AT and ATX power — for an ATX single-board computer with an ATX supply, the on-board silkscreen guide calls for setting jumper 1 to position 2–3.
- **No power button on the backplane** — the power switch header is jumper J3; shorting it powers the system on.
- **Unlabeled status LEDs**: most likely per-rail power indicators — one general "power good" LED, then +5V, −5V, +12V, −12V, and +3.3V. The −5V rail reads as missing on a modern ATX supply, since ATX dropped −5V from the spec — harmless unless you're running one of the small number of old ISA cards that specifically need it. (If you do, the [Voltage Blaster](https://github.com/necroware/voltage-blaster) project is a small ISA card that derives −5V from +5V for exactly this case.)
- **No official documentation exists for this specific backplane model** — the above was worked out by intuition and the printed jumper guide on the board silkscreen itself.

### Where it fits

Genuinely capable as a DOS and Windows 98 machine — see the full writeup for performance numbers, sound testing, and a Voodoo 3 upgrade. The real appeal of the format is modularity: the same backplane and peripherals work with any PICMG 1.0 SBC, so swapping in a 386, 486, or a faster Pentium 4-class card is just a matter of pulling one board and pushing in another.

### Related on this site

- [This Fully Functional PC Fits on a Single Card!]({% post_url 2024-10-05-this-fully-function-pc-fits-on-a-single-card-pentium-iii-sbc %}) — my video on this board
- [TheRetroWeb: MiTAC Trigon MSC-373](https://theretroweb.com/motherboards/s/mitac-trigon-msc-373)
