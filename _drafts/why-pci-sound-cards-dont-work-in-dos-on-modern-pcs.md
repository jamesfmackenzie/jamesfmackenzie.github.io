---
layout: post
title: "Why Don't PCI Sound Cards Work in DOS on a Modern PC?"
date: '2026-10-25 09:00:00'
summary: "What's the fastest PC that can still run a real 1990s sound card in DOS? Here's why sound is so hard, and what it takes to get a late-90s PCI card working in a modern machine."
tags: [MS-DOS, PC, Posts, Retrocomputing, Sound Cards]
---

<!-- DRAFT: post 1 of the "Get PCI Sound Cards Working on a Modern PC" series. No results here by design; the comparison results arrive with the YMF724 and Solo-1 posts. -->
<!-- TODO: hero photo (X10SAE with a PCI card in the slot) and the four-layers diagram -->

What's the fastest PC that can still run a real 1990s sound card in DOS?

I want to play original DOS games stupidly fast, at resolutions nobody had in 1996. I've written about [why I love software rendering]({% post_url 2026-10-13-i-love-software-rendering %}), and why it needs a fast PC running native DOS. Graphics turned out to be the easy part. Sound is the real challenge. As Rasteri put it in [his video on the Portwell RUBY-9719](https://www.youtube.com/watch?v=6eew0uRZ84E), "the main reason that DOS games won't run on modern PCs is because of audio output."

What I want is a real late-1990s sound card, with its own FM chip and its own Sound Blaster processor, in the fastest machine that can host it.

Firstly, ISA cards are a non starter. The ISA bus was removed from PCs back in (… fill out the missing details here)

Next up, we have PCI sound cards. On paper these should work. PCIe-to-PCI adapters, exist, and modern PCIe was designed to be software compatible with legacy PCI. In addition, PCI sound cards of the era actively advertised DOS and Sound Blaster compatibility.

In practice, plug one into a modern machine and you get silence — no sound.

Getting from that silence to games with sound turns out to be complicated. Here's why.


### What a DOS game expects

A DOS game doesn't ask an operating system for sound. It talks to the hardware directly. For a Sound Blaster, that means writing to I/O ports at fixed addresses (220h for the card, 388h for the FM chip) and claiming an IRQ and a DMA channel for sample transfers. When it plays a digitised sound, the game programs the PC's DMA controller to move the samples from memory to the card.

Everything in the process above assumes an ISA slot. The card sat at a fixed address, had its own IRQ line, and had a DMA request wire running to the motherboard's 8237 DMA controller.


### What the PCI cards did about it

ISA sound cards used fixed, hardcoded hardware channels. PCI cards, by contrast, are dynamic; the BIOS maps them to whatever memory address or resource pool is free during bootup. Because a DOS game bypasses the OS and expects to find a sound card sitting explicitly at I/O ports 220h and 388h, it would completely miss a native PCI card.

To fix this, the PCI sound cards added a legacy mode: a register that makes the card also answer at 220h and 388h, along with a once-per-boot DOS utility to configure the sound card and instruct the chipset to route traffic to the right place.

In addition, chipset mechanisms existed to pass DMA writes the card (DDMA), or even a pair of extra request and grant wires to physically connect the card to the chipset (PC/PCI).

Together, these mechanisms are a great facsimile of the old ISA setup. DOS games don’t know they’re talking to a PCI card — it just works(TM).

Unfortunately, on a modern PC, these mechanisms are gone. So we need to find alternatives.


### Four things that have to work

The way I've come to think about it, we have four separate layers, and a card needs to get through all of them:

1. **Address mapping.** Can the card be made to answer at 220h and 388h? This is the card's job, and the vendor setup tool usually handles it.
2. **Bus-cycle delivery.** When the CPU writes to port 220h, does that cycle actually reach the card? Behind a PCIe-to-PCI bridge, it only does if the bridge and the chipset's root port are both set to forward cycles nobody else has claimed (subtractive decode).
3. **Interrupts.** Does the card's IRQ reach the CPU, on the line the game expects?
4. **DMA.** Can the samples get from memory to the card, when the game is writing to a DMA controller the card has no connection to?

(Let’s shape the above to cover only “what do we need to solve”. The above digs too much into the solutions, and starts setting out responsibilities and how we will do it. It’s too early for that)


### How SBEMU and VSBHDA get around it

(Briefly explain that getting a PCI card working isn’t the only game in town. We can use emulation too. And then expand on what SBEMU and VSBHDA are and how they solve the above. We could even have a comparison table of the four layers, and how pci card solve them vs emulation. We already have a table in our vault note, so we could use that for inspiration)

(I’ve left the original section wording below, but of course it needs to be rejigged to cover the above + explain how SBEMU and VSBHDA cover the four layers above). 

[SBEMU]({% link _software/sbemu.md %}) and VSBHDA take a different approach. They don't use the sound card's DOS mode at all. They load a protected-mode driver that traps the game's port writes, pretends to be a Sound Blaster, and plays the result through audio hardware that does work on a modern machine, usually the onboard HD Audio. The game thinks it's talking to a Sound Blaster. It's actually talking to software.

I got [Doom running with SBEMU on a Core i7 in native DOS]({% post_url 2023-03-07-you-can-run-doom-on-a-core-i7-pc-in-native-dos-with-sbemu %}) a few years ago and it was a real step forward. But it has limits. The trapping relies on a DPMI host that the game's DOS extender is willing to use, so a game that insists on its own extender can slip past it. And an emulated card can't be any better than the emulation.


### Why bother with the real hardware?

(Let’s rejig the below to really nail our core principle: we want to do this all in hardware, not emulation. From experience, we know that the software solutions have some issues especially with protected mode (or real mode? Or some other cohort of games — use our research to article what the weak points are). Wild success here looks like an end-to-end hardware native solution to run PCI sound cards on a modern PC — and the hope/expectation that this will best emulation solutions in both reliability and authenticity)

The case for the real card is that once it's set up, a game is just writing to real ports on real silicon. There's no DPMI host involved and no emulation layer to get wrong, so in principle it should work with anything that worked on the original card. The FM synthesis and the mixer are the card's own.

I say "in principle" because I don't know yet. The real-card approach has its own fragile pieces. For the cards that need it, the DMA settings get to the card through one of the four routes above, all of them small pieces of software I'm in no position to call bulletproof. It could easily turn out that the emulators are the better bet. Finding out is the point.


### How I'll judge it

(I don’t think we’re ready for any of this — we need to research and find a compatible board first. Let’s remove this section)

For every card I get working, I'll run the same games on the same machine with the real card and with the emulators, and compare:

- the same PC, the same stick, the same game installs
- `BLASTER=A220 I5 D1 T4` for every setup, so each game's sound settings are identical
- emulators launched with no special switches
- three runs per game for each setup, because some problems only show up now and then
- a listening test, by ear, with notes on effects, music, hangs and glitches

I'll report counts, like "one hang in three runs", instead of impressions.


### The plan

(Why are we talking about the future and what’s going to happen? We are getting way ahead of ourselves. The only thing we need to cover here is: we need do our research, figure out how we (think) we can solve the challenges above, and find the FASTEST COMPATIBLE BOARD TO USE AS A FOUNDATION FOR THIS PROJECT)

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
