---
layout: post
title: MiSTer FPGA PlayStation SNAC Adapter
summary: My take on the PlayStation SNAC adapter for MiSTer FPGA, which wires an original PlayStation controller port straight into the FPGA for zero-lag, fully authentic input.
date: '2024-08-29 11:33:00'
tags: [Emulation, MiSTer FPGA, Sony PlayStation]
---

SNAC stands for **Serial Native Accessory Converter**. Instead of routing controllers through MiSTer's USB stack, a SNAC adapter connects an original console controller port directly to the FPGA's IO pins, so the core speaks the console's native controller protocol with nothing in between. The PlayStation SNAC adapter does this for the original PlayStation's controller connector.

### What it is

The adapter plugs into the MiSTer **user port** (provided by the [IO board]({% link _hardware/mister-fpga-io-board.md %})) and presents a real PlayStation controller socket. You then plug in genuine Sony controllers and peripherals exactly as you would on a real console.

### What it enables

- **Zero added latency.** The FPGA polls the controller itself, on the original timing, with no USB polling interval or driver layer.
- **Peripherals that USB adapters handle badly or not at all.** In testing it worked cleanly with the [Namco NeGcon]({% link _hardware/namco-negcon.md %}) twist controller and the [PlayStation Mouse]({% link _hardware/playstation-mouse.md %}), both of which are awkward to get working authentically over USB.
- **DualShock rumble and analog** behaving as the game and hardware originally intended.

### Why I rate it

MiSTer is at its best when the whole chain is authentic, and input is the part you feel most directly. The USB route is fine for a pad, but SNAC is what lets original oddball peripherals work the way they did on the real machine — and it removes latency questions entirely. If you care about the PlayStation core or about accessory accuracy, it is one of the more worthwhile add-ons.

### Trade-offs

- needs the user port, so realistically an IO board as well
- only relevant if you own genuine PlayStation controllers and accessories worth connecting

### Related on this site

- [Native PlayStation Accessories on MiSTer (video)]({% post_url 2022-11-19-native-playstation-accessories-on-mister-controller-memory-card-snac %})
- [How to Connect PlayStation Accessories to MiSTer (video)]({% post_url 2022-11-26-how-to-connect-playstation-controllers-accessories-to-mister-fpga %})
- [MiSTer FPGA]({% link _hardware/mister-fpga.md %})
- [MiSTer FPGA IO Board]({% link _hardware/mister-fpga-io-board.md %})
- [PlayStation Mouse]({% link _hardware/playstation-mouse.md %})
