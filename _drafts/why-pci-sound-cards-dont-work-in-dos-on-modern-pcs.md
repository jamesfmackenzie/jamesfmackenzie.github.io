---
layout: post
title: "Why Don't PCI Sound Cards Work in DOS on a Modern PC?"
date: '2026-10-25 09:00:00'
summary: "What's the fastest PC that can still run a real 1990s sound card in DOS? Graphics turned out to be the easy part. Here's why sound is so hard, and what it takes to get a late-90s PCI card working in a modern machine."
tags: [MS-DOS, PC, Posts, Retrocomputing, Sound Cards]
---

<!-- DRAFT: post 1 of the "Get PCI Sound Cards Working on a Modern PC" series. No results here by design; the comparison results arrive with the YMF724 and Solo-1 posts. -->
<!-- TODO: hero photo (X10SAE with a PCI card in the slot) and the four-layers diagram -->

What's the fastest PC that can still run a real 1990s sound card in DOS?

I want to play original DOS games stupidly fast, at resolutions nobody had in 1996. I've written about [why I love software rendering]({% post_url 2026-10-13-i-love-software-rendering %}), and why it needs a fast PC running native DOS. Graphics turned out to be the easy part. Sound is the real challenge. As Rasteri put it in [his video on the Portwell RUBY-9719](https://www.youtube.com/watch?v=6eew0uRZ84E), "the main reason that DOS games won't run on modern PCs is because of audio output."

What I want is a real late-1990s PCI sound card, with its own FM chip and its own Sound Blaster processor, in the fastest machine that can host it. On paper that should be easy. The PCI sound cards of that time, like the Yamaha YMF724, the ESS Solo-1 and the Sound Blaster Live!, were sold with DOS compatibility, so they should be able to pretend to be a Sound Blaster. In practice, plug one into a modern machine and you get silence, or worse.

Getting from that silence to games with sound turns out to be complicated. Here's why.

### What a DOS game expects

A DOS game doesn't ask an operating system for sound. It talks to the hardware directly. For a Sound Blaster, that means writing to I/O ports at fixed addresses (220h for the card, 388h for the FM chip) and picking an IRQ and a DMA channel from the `BLASTER` environment variable. When it plays a digitised sound, the game programs the PC's DMA controller to move the samples from memory to the card.

Everything in that list assumed an ISA slot. The card sat at a fixed address, had its own IRQ line, and had a DMA request wire running to the motherboard's 8237 DMA controller.

### What the PCI cards did about it

PCI cards don't get fixed addresses. They get whatever the BIOS gives them. So the PCI sound cards added a legacy mode: a register that makes the card also answer at 220h and 388h, set up once by a DOS utility from the vendor. The interrupts and the DMA were the harder part, and in the late 1990s they relied on the motherboard to help. The chipset would pick up the game's writes to the old DMA controller and pass them on to the card (Intel's PIIX4 did this, as Distributed DMA), or a pair of extra request and grant wires would connect the card to the chipset (PC/PCI, which survived on Intel chipsets until about ICH5).

Both of those are gone. And modern boards have a second problem, because they don't have PCI slots at all.

### Four things that have to work

The way I've come to think about it, there are four separate layers, and a card has to get through all of them:

1. **Address mapping.** Can the card be made to answer at 220h and 388h? This is the card's job, and the vendor setup tool usually handles it.
2. **Bus-cycle delivery.** When the CPU writes to port 220h, does that cycle actually reach the card? Behind a PCIe-to-PCI bridge, it only does if the bridge and the chipset's root port are both set to forward cycles nobody else has claimed (subtractive decode).
3. **Interrupts.** Does the card's IRQ reach the CPU, on the line the game expects?
4. **DMA.** Can the samples get from memory to the card, when the game is writing to a DMA controller the card has no connection to?

Layers 1 and 2 turned out to be a motherboard question, which is the next post. Layer 4 is the one that stops most people.

### Why the DMA writes never arrive

The game programs DMA by writing to the old 8237 controller's ports (00h to 0Fh, 80h to 8Fh, C0h to DFh). On a modern board those ports belong to the chipset's own built-in DMA controller. Intel's datasheet for my chipset says writes to those ranges go to that internal unit, and the "forward anything nobody claimed" trick from layer 2 only applies to cycles nobody claimed. Ports 220h and 388h reach the card because nothing else claims them. The DMA ports never leave the chipset.

The card does have its own DMA hardware. The ESS Solo-1, for instance, has a block of registers laid out like an 8237 (Intel's Distributed DMA shape) and a bus-master engine that moves the data itself. It just never hears the game. Something has to catch the game's writes to the old ports and repeat them into the card's block. The old chipsets did that in hardware. Now it has to be software.

### How SBEMU and VSBHDA get around it

[SBEMU]({% link _software/sbemu.md %}) and VSBHDA take a different approach. They don't use the sound card's DOS mode at all. They load a protected-mode driver that traps the game's port writes, pretends to be a Sound Blaster, and plays the result through audio hardware that does work on a modern machine, usually the onboard HD Audio. The game thinks it's talking to a Sound Blaster. It's actually talking to software.

I got [Doom running with SBEMU on a Core i7 in native DOS]({% post_url 2023-03-07-you-can-run-doom-on-a-core-i7-pc-in-native-dos-with-sbemu %}) a few years ago and it was a real step forward. But it has limits. The trapping relies on a DPMI host that the game's DOS extender is willing to use, so a game that insists on its own extender can slip past it. And an emulated card can't be any better than the emulation.

### Four ways to get the game's DMA settings to the card

Whatever the method, the job is the same: find out what the game asked the DMA controller to do (the buffer's address, its length, the mode) and program the card's DMA block to match. The obvious way is to trap the game's writes to the 8237 ports as they happen. There are three ways to do that trapping, and they cover different kinds of game:

1. **A V86 memory manager with I/O trapping (Jemm386 with QPIEMU, or a small driver for it).** The CPU's virtual-8086 mode can fault on chosen port accesses. This is the lightest option and covers real-mode games, which is a lot of them. It cannot see games that run in protected mode.
2. **A DPMI host with a trap interface (HDPMI).** Protected-mode games ask a DPMI host for services, and HDPMI can trap port I/O on their behalf. This is how VSBHDA works. It covers DOS/4GW-style games, as long as the game uses that host. A game that insists on its own extender slips past it.
3. **One resident program that does both (Yamaha's DSDMA, and my patched copy for the Solo-1).** It edits the I/O permission bitmap of the memory manager's protected-mode monitor, hides VCPI, and presents itself as a DPMI host, so a single mechanism catches real-mode games, protected-mode games and VCPI-based extenders. The price is that it is heavy-handed: a game whose loader wants a standard DPMI host may refuse it.

The fourth way doesn't trap anything:

4. **Read the settings back afterwards.** The chipset's built-in DMA controller is still there. It takes the game's writes as normal, it just never has a device to serve. So the values the game wrote are sitting in it, and a small resident program can read them back a moment later and copy them to the card. There's no memory manager and no DPMI host involved, so it shouldn't matter how the game runs. The catch is that a read-back only ever sees the result, never the moment of the write, and a game can be fussy about what it reads back from the controller.

So the rule of thumb for the trappers is: a real-mode game needs only the first, a DPMI game needs the first and second, and the third tries to cover everything with one blunt tool. The fourth sidesteps the question, if it can be made to work. Whether it can is one of the stories later in the series.

(There's a fifth way on paper: the chipset can raise a System Management Interrupt on a port access. But that means running code in System Management Mode, which on this board means modifying the BIOS. That's a project of its own.)

### Why bother with the real hardware

The case for the real card is that once it's set up, a game is just writing to real ports on real silicon. There's no DPMI host involved and no emulation layer to get wrong, so in principle it should work with anything that worked on the original card. The FM synthesis and the mixer are the card's own.

I say "in principle" because I don't know yet. The real-card approach has its own fragile pieces. For the cards that need it, the DMA settings get to the card through one of the four routes above, all of them small pieces of software I'm in no position to call bulletproof. It could easily turn out that the emulators are the better bet. Finding out is the point.

### How I'll judge it

For every card I get working, I'll run the same games on the same machine with the real card and with the emulators, and compare:

- the same PC, the same stick, the same game installs
- `BLASTER=A220 I5 D1 T4` for every setup, so each game's sound settings are identical
- emulators launched with no special switches
- three runs per game for each setup, because some problems only show up now and then
- a listening test, by ear, with notes on effects, music, hangs and glitches

I'll report counts, like "one hang in three runs", instead of impressions.

### The plan

The rest of the series follows the same path I did:

- **The hardware.** What is the fastest board that can do this at all, and which boards turned out to be dead ends.
- **The Yamaha YMF724.** The easy card, which ships with its own DMA workaround.
- **The ESS Solo-1.** The harder one, where I had to work out the DMA part myself.
- **Reading the DMA settings back.** The fourth route above: whether it works, what broke along the way, and which games it can and can't serve.
- **Where it still breaks, and the scoreboard.** The games that fight back, and every card and setup compared.
- Later: the other cards (a Sound Blaster Live! and a C-Media card), which other PCI cards could work, and a single tool that sets up whichever card is in the machine.

### Related on this site

- [SBEMU]({% link _software/sbemu.md %})
- [Yamaha YMF724]({% link _hardware/yamaha-ymf724.md %})
- [ESS Solo-1]({% link _hardware/ess-solo-1.md %})
- [Creative Labs Sound Blaster Live!]({% link _hardware/creative-labs-sound-blaster-live.md %})
