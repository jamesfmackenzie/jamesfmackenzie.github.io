---
layout: post
title: AMD BC-250
summary: A PlayStation 5 APU sold cheap on a crypto-mining blade — Zen 2 cores, an "RDNA 1.5" GPU, and 16GB of unified memory for a fraction of what any of that would normally cost.
date: '2026-09-06 00:00:00'
tags: [Computers, PC]
---

![AMD BC-250 board](/img/hardware/amd-bc-250.png)

The AMD BC-250 looks like an oversized graphics card with a fan bolted to the end. It's actually close to a whole PC on a card — USB ports, Ethernet, an M.2 NVMe slot — and under the heatsink is the exact same silicon as a launch-model PlayStation 5. It's the cheapest way I know of to get a PS5-class APU onto a desk, and I wanted to see what it could actually do.

### Why it exists

AMD makes a huge volume of custom SoCs for console makers, and yields are never perfect — some dies come out with defective CPU cores or broken graphics blocks that fail Sony's PS5 spec. Rather than scrap that silicon, ASRock partnered with AMD to build the **BC-250**: a mining-rack blade built around these binned PS5 dies. One rack holds 12 blades, each with its own PS5 SoC and 16GB of RAM.

The compromises versus a real PS5 are real. Two CPU cores are disabled per blade (6 cores / 12 threads instead of 8), and 16 of the 32 GPU compute units are disabled by default (24 active) — though a community kernel patch can unlock the disabled CUs back up to the die's full 40.

### Specifications

| Component | Details |
|---|---|
| **CPU** | AMD Zen 2, 6 cores / 12 threads (2 of 8 disabled per blade) |
| **GPU** | Custom AMD APU graphics, recognized by Linux as "Cyan Skillfish" (`gfx1013`) — community-labeled **"RDNA 1.5"**: a GFX10.1-era (RDNA1) instruction set with some RDNA2-style ray-tracing extensions added. 24 of 40 compute units active by default; a kernel patch can unlock the rest. |
| **Memory** | 16GB unified GDDR6, shared between CPU and GPU |
| **Storage** | 1× M.2 2280 slot — limited to PCIe Gen 2 x2 (~1GB/s), enough for SATA/entry NVMe but a real bottleneck for fast NVMe drives |
| **I/O** | USB ports, Ethernet, DisplayPort/HDMI |
| **Power** | Standard PCIe 6+2 pin GPU power connectors |
| **Typical price** | $50-150 secondhand (eBay/AliExpress) |

### The catch

Windows has no working driver for this GPU at all — you're stuck with software rendering. On Linux, support only landed in Mesa 25.1+ (merged via [this GitLab merge request](https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/33116)), and **Vulkan is the only working compute path** — AMD's own ROCm stack has no `gfx1013` support in its math libraries, so anything that touches ROCm just aborts.

Once it's running, though, it's a genuinely capable little machine: modern-console emulation (PCSX2, RPCS3), native Linux gaming through Proton, and even local LLM inference all turn out to be viable with the right driver and configuration work.
