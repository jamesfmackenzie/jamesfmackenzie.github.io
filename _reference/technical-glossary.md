---
layout: post
title: Technical Glossary
summary: Short definitions of the technical terms that come up across this site, from subtractive decode to the BLASTER variable, with links to where each one comes up.
date: '2026-11-01 09:00:00'
tags: [Lists, MS-DOS, PC, Sound Cards]
---

Short definitions of the technical terms that come up on this site, mostly from [getting PCI sound cards working on a modern PC]({% link _projects/get-pci-sound-cards-working-on-a-modern-pc.md %}). Posts link straight to the entry they need. I'll add to it as new terms come up.


### 8237 DMA controller {#dma-controller-8237}

The chip the original IBM PC used for DMA (direct memory access): moving data between memory and a card without the CPU copying every byte. The PC AT added a second one, for eight channels in all: 0 to 3 for 8-bit transfers and 5 to 7 for 16-bit. A Sound Blaster usually uses channel 1, and a 16-bit card such as the Sound Blaster 16 adds a 16-bit channel, usually 5. To play a digitised sound, a DOS game programs this controller to feed samples to the card.

See also: [Distributed DMA](#ddma), [PC/PCI](#pc-pci), [BLASTER variable](#blaster-variable)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %})


### BLASTER variable {#blaster-variable}

A DOS environment variable that tells games and setup programs where to find a Sound Blaster, for example `SET BLASTER=A220 I5 D1 T4`. `A` is the I/O address, `I` the IRQ, `D` the 8-bit DMA channel, `H` the 16-bit DMA channel if the card has one, and `T` the card type. Some games read it; others ask during setup instead.

See also: [I/O port](#io-port), [IRQ](#irq), [8237 DMA controller](#dma-controller-8237)


### Distributed DMA (DDMA) {#ddma}

A chipset feature for PCI sound cards. When a game programmed the old 8237 DMA controller, the chipset passed those writes on to the PCI card, which then did the transfer itself. Among Intel chipsets, it only ever existed in the PIIX3 and PIIX4 southbridges of the mid-to-late 1990s.

See also: [PC/PCI](#pc-pci), [8237 DMA controller](#dma-controller-8237)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %}), [Dell OptiPlex 380]({% link _hardware/dell-optiplex-380.md %})


### DEBUG {#debug}

A small debugger that came with MS-DOS from its first version (FreeDOS has its own). Rather than stepping through source code, it works on the machine directly: it can show and change memory and the CPU's registers, read and write I/O ports, and assemble and run a few lines of assembly language. That makes it a handy way to poke at hardware without writing a program. It reads commands one line at a time, so `DEBUG < SCRIPT.TXT` replays a saved set of commands.

See also: [PCI configuration space](#pci-configuration-space), [Register](#register)


### DPMI host {#dpmi-host}

DOS Protected Mode Interface: a standard way for a DOS program to run in protected mode, with access to all of the PC's memory rather than just DOS's first megabyte, while still calling DOS. The DPMI host is the program that provides it. Many protected-mode games come with a DOS extender, such as DOS/4GW, which uses a DPMI host if one is loaded and otherwise brings its own. Sound Blaster emulators like SBEMU work through a particular host, so a game that brings its own can slip past them.

See also: [TSR](#tsr)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %})


### FM synthesis {#fm-synthesis}

How most DOS games play music on a sound card: a Yamaha chip builds each instrument by combining simple waveforms. The AdLib card used the OPL2 (YM3812), and later Sound Blasters used the OPL3 (YMF262). Games find the chip at I/O port 388h. Some PCI sound cards, like the Yamaha YMF724, have real Yamaha FM hardware of their own.

See also: [I/O port](#io-port), [Legacy mode (PCI sound cards)](#legacy-mode)

Comes up in: [Resound 2 OPL3]({% link _hardware/resound-2-opl3.md %}), [Yamaha YMF724]({% link _hardware/yamaha-ymf724.md %}), [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %})


### I/O port {#io-port}

An address the CPU uses to talk to hardware directly, separate from memory. ISA sound cards sat at fixed ports: 220h is the usual Sound Blaster address (the h means hexadecimal), and 388h is the FM chip.

See also: [Legacy mode (PCI sound cards)](#legacy-mode), [Positive decode](#positive-decode), [Subtractive decode](#subtractive-decode)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %}), [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})


### IRQ {#irq}

Interrupt request: a signal a card uses to get the CPU's attention, for example when it has finished playing a block of sound. A Sound Blaster usually uses IRQ 5 or 7, and the game has to know which. On ISA, each card had its own line. PCI cards share interrupts that the BIOS assigns, so getting a PCI card's interrupt to the IRQ a DOS game expects is a problem of its own.

See also: [BLASTER variable](#blaster-variable)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %}), [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})


### ISA {#isa}

Industry Standard Architecture: the expansion bus of the IBM PC, 8-bit from 1981 and 16-bit from the PC AT in 1984. An ISA card sat at fixed I/O addresses, usually set with jumpers, with its own IRQ and DMA wires running to the motherboard. DOS sound was designed around that arrangement. PCs phased ISA slots out at the end of the 1990s.

See also: [I/O port](#io-port), [IRQ](#irq), [8237 DMA controller](#dma-controller-8237)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %})


### Legacy mode (PCI sound cards) {#legacy-mode}

A setting on late-1990s PCI sound cards that makes the card also answer at the old Sound Blaster and FM addresses (220h and 388h), as an ISA card would. It exists purely for backwards compatibility. DOS games were still a big reason to buy a sound card at the time, and they only knew how to find a Sound Blaster at those fixed addresses. It's usually switched on by a small DOS utility at boot. Not to be confused with Intel's PCI Legacy Mode, which is a chipset feature.

See also: [PCI Legacy Mode](#pci-legacy-mode), [I/O port](#io-port)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %}), [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})


### PC/PCI {#pc-pci}

The other chipset route to DMA for PCI sound cards: an extra pair of request and grant signals wiring the card to the chipset, so it could take part in the old 8237 DMA scheme. Intel's chipsets dropped it after the ICH5, in 2003.

See also: [Distributed DMA](#ddma), [8237 DMA controller](#dma-controller-8237)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %}), [Dell OptiPlex 380]({% link _hardware/dell-optiplex-380.md %})


### PCH {#pch}

Platform Controller Hub: Intel's name for its chipset since the 5-series in 2009. It handles most of the PC's I/O, including USB, SATA and the PCI Express root ports.

See also: [Root port](#root-port), [PCI Legacy Mode](#pci-legacy-mode)

Comes up in: [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})


### PCI configuration space {#pci-configuration-space}

A block of registers every PCI device has, 256 bytes in the original PCI design, used to identify and set up the device. The first part is standard: the maker and model, and the addresses and interrupt the BIOS assigned. The rest is specific to the chip, and its datasheet says what each register does. Software can read and write it while the PC runs, in DOS usually through the PCI BIOS (interrupt 1Ah). Nothing written there survives a power-off.

See also: [Register](#register), [DEBUG](#debug), [Subtractive decode](#subtractive-decode)


### PCI Legacy Mode {#pci-legacy-mode}

Intel's name for a PCH feature that lets old PCI cards work behind a PCIe-to-PCI bridge. Both the chipset's root port and the bridge act as subtractive PCI-to-PCI bridges, so legacy accesses fall through to the cards behind them. On the chipset side it's a single bit, "Subtractive Decode Enable", in each root port. Intel documents it in the [8-series datasheet](https://www.intel.com/content/dam/www/public/us/en/documents/datasheets/8-series-chipset-pch-datasheet.pdf) (section 5.2.2), and the [100-series datasheet](https://www.intel.com/content/www/us/en/content-details/332690/intel-100-series-chipset-family-platform-controller-hub-pch-datasheet-volume-1.html) says it's no longer supported.

See also: [Subtractive decode](#subtractive-decode), [Root port](#root-port), [PCIe-to-PCI bridge](#pcie-to-pci-bridge), [PCH](#pch), [Legacy mode (PCI sound cards)](#legacy-mode)

Comes up in: [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %}), [Supermicro X10SAE]({% link _hardware/supermicro-x10sae.md %})


### PCIe-to-PCI bridge {#pcie-to-pci-bridge}

A chip that turns a PCI Express link into a PCI bus, so old PCI cards can run in a modern PC. Some motherboards have one built in to feed their PCI slots (the Supermicro X10SAE uses an IDT 89HPEB383). Otherwise, an adapter card with one, such as the ASMedia ASM1083, plugs into a PCIe slot. For DOS sound, the bridge has to support subtractive decode, and not all of them do.

See also: [Subtractive decode](#subtractive-decode), [Root port](#root-port), [PCI Legacy Mode](#pci-legacy-mode)

Comes up in: [I made 3Dfx Voodoo2 work on a modern PC!]({% post_url 2026-08-30-voodoo-2-on-a-modern-pc %}), [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %}), [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %}), [Supermicro X10SAE]({% link _hardware/supermicro-x10sae.md %})


### Positive decode {#positive-decode}

The normal way a device or bridge decides which accesses are its own: it claims only the address ranges it's been given, usually by the BIOS at boot. Anything outside those ranges passes it by. That's why a DOS game's write to 220h never reaches a PCI card the BIOS put somewhere else.

See also: [Subtractive decode](#subtractive-decode), [I/O port](#io-port)

Comes up in: [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})


### Register {#register}

A small storage slot inside a chip, usually 8, 16 or 32 bits wide. Software reads a register to find out what the chip is doing, and writes one to tell it what to do; often each bit is a separate on/off setting. A CPU has its own registers too, which is what `DEBUG` shows after running code.

See also: [PCI configuration space](#pci-configuration-space), [DEBUG](#debug)


### Root port {#root-port}

Where a PCI Express link starts: a port on the chipset (or the CPU) that a slot or an onboard device hangs off. On Intel's 8-series chipsets, each root port has its own Subtractive Decode Enable bit.

See also: [PCI Legacy Mode](#pci-legacy-mode), [PCH](#pch), [PCIe-to-PCI bridge](#pcie-to-pci-bridge)

Comes up in: [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})


### Sound Blaster {#sound-blaster}

Creative Labs' line of sound cards, first released in 1989, whose design became the standard DOS games were written for. A game talks to a Sound Blaster directly: through I/O ports (usually 220h), an IRQ (usually 5 or 7) and a DMA channel (usually 1), with music from a Yamaha FM chip at 388h. Most later sound cards, ISA and PCI, copied that interface so games would work with them.

See also: [BLASTER variable](#blaster-variable), [FM synthesis](#fm-synthesis), [Legacy mode (PCI sound cards)](#legacy-mode)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %}), [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})


### Subtractive decode {#subtractive-decode}

The opposite of positive decode: a bridge that decodes subtractively claims any access that nothing else claimed, and forwards it on. Older PCs used it to reach the ISA bus, where cards sat at fixed addresses the PCI side knew nothing about. For a PCI sound card in a modern PC, it's what lets a game's write to 220h fall through the chipset and the PCIe-to-PCI bridge to the card. Both of those hops need it switched on.

See also: [Positive decode](#positive-decode), [PCI Legacy Mode](#pci-legacy-mode), [PCIe-to-PCI bridge](#pcie-to-pci-bridge)

Comes up in: [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})


### TSR {#tsr}

Terminate and stay resident: a DOS program that loads, leaves part of itself in memory and returns to the prompt, so it keeps working in the background while other programs run. Sound card drivers and set-up utilities often work this way, and so do Sound Blaster emulators such as [SBEMU]({% link _software/sbemu.md %}).

See also: [DPMI host](#dpmi-host)

Comes up in: [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %}), [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})


### Related on this site

- [Get PCI Sound Cards Working on a Modern PC]({% link _projects/get-pci-sound-cards-working-on-a-modern-pc.md %})
- [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %})
- [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})
- [Disassembly vs Decomp vs Recomp vs Port: What's the Difference?]({% post_url 2026-10-03-disassembly-vs-decomp-vs-recomp-vs-port %})
