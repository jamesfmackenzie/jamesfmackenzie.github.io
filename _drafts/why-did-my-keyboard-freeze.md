---
layout: post
title: "Why Did My Keyboard Freeze?"
summary: "I found the fastest motherboard and CPU that can (in theory!) still play MS-DOS games on an old-school, Sound Blaster compatible card. But on my first attempt, the keyboard froze solid. What gives?"
tags: [MS-DOS, PC, Posts, Retrocomputing, Sound Cards]
---
<!-- DRAFT -->
<!-- TODO: hero. Candidates: the X10SAE FM video still, or one of the DEBUG screen photos below. -->

In [the last post]({% post_url 2026-11-15-finding-the-fastest-possible-dos-pc %}), I went hunting for the fastest motherboard and CPU that can (in theory!) still play DOS games on an old-school, Sound Blaster compatible card. Luckily, I already owned two boards that fit the bill: an ASUS Z87-PRO and a Supermicro X10SAE.

Now for the real test: can I get it all working?


### Why it won't just work

I don't expect to plug a PCI sound card in and have DOS games find it. As I covered last time, a game's write to the standard Sound Blaster address (220h) has two hops to make before it reaches the card:

1. The chipset's PCIe [root port]({% link _reference/technical-glossary.md %}#root-port)
2. The [PCIe-to-PCI bridge]({% link _reference/technical-glossary.md %}#pcie-to-pci-bridge)

By default, neither one will route writes to the sound card.

![Two rows. By default, a DOS game's write to 220h reaches the chipset's PCIe root port and is not forwarded to the PCIe-to-PCI bridge or the PCI sound card. With subtractive decode on at both hops, the unclaimed write is forwarded through the chipset and the bridge, and the card answers at 220h.](/img/chipset-and-bridge-hops-diagram.svg)
*The two hops again. Both need subtractive decode turned on.*

The plan is to turn on [subtractive decode]({% link _reference/technical-glossary.md %}#subtractive-decode) at both hops. This means addresses nobody else claims, like 220h, will fall through to the card. That's the theory, anyway. I'm hoping it routes them correctly, but I won't know until I try.

Subtractive decode starts out disabled, so we'll need to enable it ourselves, by changing the **PCI configuration registers**.


### A quick detour: registers and PCI configuration space

A **[register]({% link _reference/technical-glossary.md %}#register)** is a small storage slot inside a chip, usually 8, 16 or 32 bits wide. Software reads them to find out what the chip is doing, and writes them to tell it what to do.

Every PCI device, including bridges and the chipset's root ports, has a block of these called its **[configuration space]({% link _reference/technical-glossary.md %}#pci-configuration-space)**. The first part tells the PC what the device is, who made it etc. But the rest is up to the chip's maker, and that's where features like subtractive decode live.

The BIOS fills most of the configuration space at boot, but software can read and write it at any time while the PC is running. In DOS, we can poke at the registers directly: first to find our device by maker and model number, and then to read or write any byte of its configuration space. Nothing written there survives a power-off. Every boot resets back to the BIOS's defaults.


### But which bits?

After consulting the chipset and bridge datasheets, I found the registers and bits I need:

| Hop | Chip | Register | Bit |
|---|---|---|---|
| Bridge (the Z87-PRO's adapter) | ASMedia ASM1083 | 40h | Bit 6, "Patch subtractive decode enable (Legacy enable)" |
| Bridge (built into the X10SAE) | IDT 89HPEB383 | 48h | Bit 7, `LEGACY` |
| Chipset | Intel 8-series root port | ECh | Bit 0, "Subtractive Decode Enable" (SDE) |

There's one catch on the chipset side. The 8-series chipset has several root ports, each with its own SDE bit, and its datasheet says only one can be on at a time. So first we need to find out which root port leads to the sound card.

(we should add root port to our glossary and link it)


### A quick detour: what DEBUG is

Today, debugging usually means stepping through your own code in an IDE to find out why it isn't working. **[`DEBUG`]({% link _reference/technical-glossary.md %}#debug)** is a debugger in that sense too, but a much lower-level one. It's a small program that came with MS-DOS from the very first version (FreeDOS has its own), and it works directly on the machine: memory, the CPU's registers, and I/O ports.

That makes it handy for much more than finding bugs. You can type a few lines of assembly language with its `A` (assemble) command, set the CPU's registers with `R`, run the code with `G` (go), and see what the registers hold afterwards. In other words, it's a tiny assembler and a way to poke the hardware directly, built into DOS.

`DEBUG` also reads its commands one line at a time, so you can type them into a text file instead and run `DEBUG < SCRIPT.TXT`. It replays the file as if you'd typed it.


### The Z87-PRO

For the sound card, I picked a [Yamaha YMF724]({% link _hardware/yamaha-ymf724.md %}). It's a late-90s PCI card, built to be [Sound Blaster]({% link _reference/technical-glossary.md %}#sound-blaster) compatible in DOS, with Yamaha's own FM synthesis on board. Its DOS driver package is easy to find, and comes with a setup tool, `SETUPDS`, that turns on the card's [legacy mode]({% link _reference/technical-glossary.md %}#legacy-mode), plus a test program that plays FM music.

The Z87-PRO has no PCI slots, so the card goes in a PCIe-to-PCI adapter: the same one from [my Voodoo 2 experiments]({% post_url 2023-04-15-3dfx-voodoo2-voodoo-2-on-a-modern-pc-core-i7 %}), with an ASM1083 bridge chip.

The bridge came first. The first time, I did it by hand at the `DEBUG` prompt: assemble just two instructions, `INT 1A` to call the PCI BIOS and `INT 3` to stop afterwards, then use `R` to load the registers for each call and `G` to run it. It worked, after a couple of mistakes. But I'd have to redo it on every boot, so I saved the steps as a script, `BRIDGEFX.TXT`. Here's the important part, with comments added (the real file has none):

```nasm
A 100              ; start assembling at address 100h
MOV AX,B102        ; PCI BIOS: find a device...
MOV CX,1080        ;   ...with device ID 1080h (the ASM1083)
MOV DX,1B21        ;   ...from vendor 1B21h (ASMedia)
XOR SI,SI          ;   ...the first one found
INT 1A             ; the BIOS returns where it found it in BX
MOV AX,B108        ; PCI BIOS: read a byte of configuration space...
MOV DI,0040        ;   ...register 40h, into CL
INT 1A
OR CL,40           ; turn on bit 6 (40h), leaving the others alone
MOV AX,B10B        ; PCI BIOS: write CL back to register 40h
INT 1A
```

The rest of the file does the same for one more bit, which lets the card's interrupts back up through the bridge (more on interrupts in a later post), then stops with `INT 3`. At that point, `DEBUG` prints the CPU's registers, so I can check the result: `NC` (no carry) means the last BIOS call worked, and `CL` holds the byte that was written.

Next, the card. `SETUPDS` found the YMF724 straight away, and its native sound test played fine. But neither of those uses the old I/O ports. `SETUPDS` finds the card through its configuration space, which, as we've just seen, needs no help from subtractive decode. And the native test uses the card's modern addresses.

The real test was whether anything could find a Sound Blaster at 220h. With the bridge fixed and the [`BLASTER` variable]({% link _reference/technical-glossary.md %}#blaster-variable) set, `SETUPDS` couldn't. Neither could Creative's own `SBTEST`, which shares no code with Yamaha's tools.

<!-- TODO: image. Vault: PCI Sound Cards 23 (SETUPDS still fails). -->

That was expected. One hop done, one to go.

Unlike the bridge, the chipset's root ports don't need finding: they're always at the same place, bus 0, device 28, functions 0 to 7. The PCI BIOS packs that into `BX`, so they're `00E0` to `00E7`. Each root port records the number of the bus behind it in register 19h, and the BIOS had put the adapter's bridge on bus 09h. So I wrote a small script for each function, `FINDF0.TXT` to `FINDF7.TXT`, to read that register:

```nasm
A 100
MOV AX,B108        ; read a byte of configuration space...
MOV BX,00E3        ;   ...from bus 0, device 28, function 3
MOV DI,0019        ;   ...register 19h: the bus behind this port
INT 1A
INT 3
```

Then I worked through them:

| Root port function | Bus behind it |
|---|---|
| 0 | 07h |
| 1 | 08h |
| 2 | none |
| **3** | **09h** |

Function 3. I read its register ECh, and SDE was 0. I set `CX` to 1 and wrote it back.

![A DEBUG session on the Z87-PRO, photographed from the monitor. Reading register 19h of the root port at BX=00E3 returns CX=0009, reading register ECh returns CX=0000, and writing CX=0001 back succeeds.](/img/z87-pro-debug-root-port-sde-write.jpg)
*Finding and setting SDE on the Z87-PRO by hand. Top: register 19h says bus 09h is behind this port (`CX=0009`). Middle: SDE reads 0. Bottom: the write of 1 succeeds.*

Then the keyboard froze solid.

<!-- TODO (James): a line on your reaction here, at the first freeze or the second. -->

Nothing I typed reached the screen, and the Num Lock light was stuck on. I power-cycled and tried again with a PS/2 keyboard instead of USB, in case the BIOS's USB keyboard support was the problem. It froze in exactly the same way.

The third time, I took away everything I could. Real MS-DOS instead of FreeDOS, booted from a floppy disk instead of a USB stick, with the BIOS's Fast Boot off and its USB 3 controller disabled. By now the write was a script too, `ROOTPORT.TXT`. Same freeze, the moment SDE went on.

Luckily, it did no lasting harm. Configuration space is cleared at power-off, so a power-cycle brought everything back each time.

Looking for anyone who'd seen this before, I found the dISAppointment project, which adds a real ISA slot to modern PCs. Its builders hit something very similar: turning on subtractive decode broke the keyboard controller and sometimes hung the whole machine. Their best guess was a clash with the board's Super I/O chip, which handles the keyboard on modern boards. They never found a fix.

Three identical freezes, and no fix from anyone else. I set the Z87-PRO aside and moved on to the X10SAE.


### The X10SAE

The X10SAE has real PCI slots, fed by the IDT 89HPEB383 bridge on the board.

<!-- TODO: image. Vault: PCI Sound Cards 39 (Port 60/64 Emulation help text). -->

Before going near DOS, I went through the BIOS. There was no setting for subtractive decode, but in the USB settings I found something I hadn't seen on the ASUS: "Port 60/64 Emulation", enabled. Ports 60h and 64h belong to the keyboard controller, and the help text explains that this setting fakes them so a USB keyboard works in "non-USB aware OSes". In other words, DOS. Something sitting between the keyboard and the chipset seemed worth getting out of the way, so I made a note to turn it off before trying SDE.

In DOS, I found the IDT bridge by hand with `DEBUG` (vendor 10E3h, device 8113h), then read its register 48h.

![A DEBUG session on the X10SAE, photographed from the monitor. A find-device call for 10E3:8113 returns BX=0300, then reading register 48h returns CX=8180.](/img/x10sae-debug-idt-bridge-legacy-bit-already-set.jpg)
*Reading the IDT bridge's register 48h on the X10SAE. The byte read lands in `CL`, the right-hand half of `CX=8180`: 80h, so bit 7 was already on.*

Bit 7 was already set! Supermicro's BIOS turns on the bridge's legacy mode by itself, so there was nothing to do.

Even so, Yamaha's test program still failed, and `SETUPDS` still couldn't find a Sound Blaster. One hop left.

The `FINDFn` scripts found the bridge's bus, 03h, behind root port function 5. `SDE.TXT` is the same script as `ROOTPORT.TXT`, with `MOV BX,00E5` for function 5. This time, I prepared first: a PS/2 keyboard, and Port 60/64 Emulation turned off. Then I ran it.

![Running DEBUG < SDE.TXT on the X10SAE, photographed from the monitor. The script reads register ECh of BX=00E5, sets bit 0 and writes it back; the register dump afterwards shows CX=0001 and NC.](/img/x10sae-debug-sde-script-no-freeze.jpg)
*`SDE.TXT` on the X10SAE: the script, then the result. `CX=0001` means SDE is on, and `NC` means the BIOS call worked.*

The keyboard kept working.


### First sound

I ran Yamaha's FM test program again. This time, it played music.

<!-- TODO: video. Vault: PCI Sound Cards 47 (X10SAE FM audio working, .MOV), needs uploading to YouTube. -->

That's FM music from a PCI sound card, in DOS, on a Haswell Xeon. The writes to 388h now make it through both hops to the card.

So why did my keyboard freeze on the Z87-PRO? I still don't know. It could be the Port 60/64 Emulation setting, the different Super I/O chip (a Nuvoton NCT6776D, against the ASUS's NCT6791D), or something about that particular root port. I haven't been back to find out yet. For now, the [X10SAE]({% link _hardware/supermicro-x10sae.md %}) is the board.


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
