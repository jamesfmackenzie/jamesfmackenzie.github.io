---
layout: post
title: "Two Switches and a Frozen Keyboard"
summary: "I've found the fastest PCs that should be able to route a DOS game's sound to a PCI card. Each needs two switches flipping: one in the bridge chip, one in the chipset. Can I actually flip them, and will a real PCI sound card make a sound?"
tags: [MS-DOS, PC, Posts, Retrocomputing, Sound Cards]
---
<!-- DRAFT -->
<!-- TODO: hero. Candidates: the X10SAE FM video still, or a DEBUG screen photo (vault: PCI Sound Cards 20 or 46). -->

In [the last post]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %}), I found the newest chipsets that can still route a DOS game's sound to a PCI card, and it turned out I already owned two boards that fit: an ASUS Z87-PRO and a Supermicro X10SAE.

Finding them was the paperwork. Now I need to make it work on real hardware. If I can get address routing working, a DOS game should be able to find a PCI sound card for the first time.


### Two switches

As a reminder, a game's write to 220h has two hops to make before it reaches the card: the chipset's PCIe [root port]({% link _reference/technical-glossary.md %}#root-port), then the [PCIe-to-PCI bridge]({% link _reference/technical-glossary.md %}#pcie-to-pci-bridge). Each one needs [subtractive decode]({% link _reference/technical-glossary.md %}#subtractive-decode) switched on, so that addresses nobody else claims fall through to the card.

![Two rows. By default, a DOS game's write to 220h reaches the chipset's PCIe root port and is not forwarded to the PCIe-to-PCI bridge or the PCI sound card. With subtractive decode on at both hops, the unclaimed write is forwarded through the chipset and the bridge, and the card answers at 220h.](/img/chipset-and-bridge-hops-diagram.svg)
*The two hops again. Both need switching on.*

So that's two switches: one in the bridge chip and one in the chipset. Neither is on by default, and nothing in a normal boot turns them on. That might explain why Phil's Computer Lab got a PCIe CMI8738 card working in Windows 98, but not in DOS.

For the sound card, I picked a Yamaha YMF724. Yamaha's DOS driver package is easy to find, and it comes with a setup tool, `SETUPDS`, that switches on the card's legacy mode, plus a test program that plays FM music.

I started with the Z87-PRO.


### The Z87-PRO and the ASM1083

The Z87-PRO has no PCI slots, so the card goes in a PCIe-to-PCI adapter: the same one from [my Voodoo 2 experiments]({% post_url 2023-04-15-3dfx-voodoo2-voodoo-2-on-a-modern-pc-core-i7 %}). Its bridge chip is an ASMedia ASM1083.

The ASM1083 datasheet had what I was looking for. At offset 40h of the bridge's configuration registers, bit 6 is labelled "Patch subtractive decode enable (Legacy enable)". It defaults to off, but it's an ordinary read-write bit, not something burned in at the factory. A second bit, at offset 41h, lets the card's interrupts pass back up through the bridge once legacy mode is on.

To flip them, I used `DEBUG`, the little debugger that has shipped with DOS since the beginning. It can assemble a few instructions and run them, which is enough to ask the PCI BIOS to find a device, read one of its registers, and write it back with a bit set.

<!-- TODO: image pair. Vault: PCI Sound Cards 02 (find ASM1083) and 05 (write offset 40h). -->

The first time, I typed it all in by hand, and made a couple of mistakes along the way. Once it worked, I saved the commands to a script file, so `DEBUG < BRIDGEFX.TXT` sets both bits in one go on every boot.

Next, the card. `SETUPDS` found the YMF724 straight away, and its native sound test played fine. But neither of those touches the old I/O ports. `SETUPDS` finds the card through PCI configuration space, and the native test uses the card's modern addresses. Neither needs subtractive decode.

The real test was whether anything could find a [Sound Blaster]({% link _reference/technical-glossary.md %}#sound-blaster) at 220h. With the bridge fixed and the [`BLASTER` variable]({% link _reference/technical-glossary.md %}#blaster-variable) set, `SETUPDS` couldn't. Neither could Creative's own `SBTEST`, which shares no code with Yamaha's tools.

<!-- TODO: image. Vault: PCI Sound Cards 23 (SETUPDS still fails). -->

That was expected. One switch on, one to go.


### The chipset's switch

The chipset's switch is a bit called SDE (Subtractive Decode Enable), and the 8-series chipset has one for each of its PCIe root ports. A rule in the datasheet says only one can be on at a time, so I needed to find the port that leads to the adapter.

Each root port records the number of the bus behind it. The bridge sat on bus 09h, so I walked the ports one by one, reading that register on each:

| Root port function | Bus behind it |
|---|---|
| 0 | 07h |
| 1 | 08h |
| 2 | none |
| **3** | **09h** |

Function 3. Its SDE bit read 0. I wrote a 1, and `DEBUG` reported success.

<!-- TODO: image. Vault: PCI Sound Cards 20 (the SDE write). -->

Then the keyboard stopped working.

Nothing I typed reached the screen, and the Num Lock light was stuck on. I power-cycled and tried again with a PS/2 keyboard instead of USB, in case the BIOS's USB keyboard support was the problem. It froze in exactly the same way.

The third time, I took away everything I could. Real MS-DOS instead of FreeDOS, booted from a floppy disk instead of a USB stick, with the BIOS's Fast Boot off and its USB 3 controller disabled. Same freeze, the moment SDE went on.

Luckily, it did no lasting harm. These settings are lost at power-off, so a power-cycle brought everything back each time.

Looking for anyone who'd seen this before, I found the dISAppointment project, which adds a real ISA slot to modern PCs. Its builders hit something very similar: switching on subtractive decode broke the keyboard controller and sometimes hung the whole machine. Their best guess was a clash with the board's Super I/O chip, which handles the keyboard on modern boards. They never found a fix.

Three identical freezes, and no fix from anyone else. I set the Z87-PRO aside and moved on to the X10SAE.


### The X10SAE and the IDT bridge

The X10SAE has real PCI slots, fed by an IDT 89HPEB383 bridge chip on the board. That chip has its own legacy bit, at offset 48h, bit 7.

<!-- TODO: image. Vault: PCI Sound Cards 39 (Port 60/64 Emulation help text). -->

Before going near DOS, I went through the BIOS. There was no setting for subtractive decode, but in the USB settings I found something I hadn't seen on the ASUS: "Port 60/64 Emulation", enabled. Ports 60h and 64h belong to the keyboard controller, and the help text explains that this setting fakes them so a USB keyboard works in "non-USB aware OSes". In other words, DOS. Something sitting between the keyboard and the chipset seemed worth getting out of the way, so I made a note to switch it off before trying SDE.

In DOS, I found the IDT bridge with `DEBUG` and read offset 48h.

<!-- TODO: image. Vault: PCI Sound Cards 42 (offset 48h = 80h). -->

It came back 80h. Bit 7 was already set! Supermicro's BIOS switches on the bridge's legacy mode by itself, so there was nothing to do.

Even so, Yamaha's test program still failed, and `SETUPDS` still couldn't find a Sound Blaster. One switch left.

Walking the root ports again, function 5 led to the bridge's bus. This time, I prepared first: a PS/2 keyboard, and Port 60/64 Emulation switched off. Then I set SDE.

<!-- TODO: image. Vault: PCI Sound Cards 46 (SDE write, no freeze). -->

The keyboard kept working.


### First sound

I ran Yamaha's FM test program again. This time, it played music.

<!-- TODO: video. Vault: PCI Sound Cards 47 (X10SAE FM audio working, .MOV), needs uploading to YouTube. -->

That's FM music from a PCI sound card, in DOS, on a Haswell Xeon. The writes to 388h now make it through both hops to the card.

I don't know exactly why the X10SAE worked where the Z87-PRO didn't. It could be switching off Port 60/64 Emulation, the different Super I/O chip (a Nuvoton NCT6776D, against the ASUS's NCT6791D), or something about that particular root port. I haven't been back to find out yet. For now, the [X10SAE]({% link _hardware/supermicro-x10sae.md %}) is the board.


### What's next

That's address routing working: the card answers at the right addresses, and the game's accesses reach it.

FM music only needs those writes. Digitised sound, the explosions and speech in most games, also needs the other two requirements: interrupts and DMA. That's the next post.


### Related on this site

- [Get PCI Sound Cards Working on a Modern PC]({% link _projects/get-pci-sound-cards-working-on-a-modern-pc.md %}) — the project this post is part of
- [Finding the Fastest Possible DOS PC]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %})
- [Why Don't PCI Sound Cards Work on a Modern PC?]({% post_url 2026-10-26-why-pci-sound-cards-dont-work-in-dos-on-modern-pcs %})
- [Supermicro X10SAE]({% link _hardware/supermicro-x10sae.md %})
- [Yamaha YMF724]({% link _hardware/yamaha-ymf724.md %})
- [Technical Glossary]({% link _reference/technical-glossary.md %})
