---
layout: post
title: Dell Dimension E520
summary: Hardware notes on the Dell Dimension E520 — a Core 2-era Dell tower, and what to know about it before using one for a retro build.
date: '2025-12-29 10:30:00'
tags: [Computers, PC]
---

![Dell Dimension E520 tower](/img/posts/dell-dimension-e520.jpg){: width="500"}

The Dell Dimension E520 is a no-frills mid-2000s home tower built around Intel's G965 platform — cheap, common, and visually unremarkable, the sort of ordinary Windows XP-era family PC that still turns up for very little. For retro use it sits right on a boundary: fast enough to brute-force a lot of late DOS and Win9x software, but new enough that those older operating systems have some quirks.

So if you're looking for a DOS or Windows 98 retro machine, there are better options. But for Windows XP, it's a great fit.


### Specifications

Configurations vary, but most E520 systems share:

- **Chipset:** Intel G965 Express with an `ICH8` southbridge
- **Memory:** DDR2-533 or DDR2-667
- **Storage:** SATA
- **Graphics:** Intel GMA 3000 onboard
- **Expansion:** PCI Express x16, PCI Express x1, 2 PCI
- **Networking:** integrated Ethernet

My own machine is a modest one: a Core 2 Duo `E4300 @ 1.80GHz` on an 800MHz bus, 2MB of L2 cache, 3GB of DDR2-667 running in dual interleaved mode, and Intel HD Audio with a Sigmatel codec.

<div class="image-row">
  <img src="/img/posts/dell-dimension-e520-bios-processor-info.jpg" alt="E520 BIOS screen showing the Core 2 Duo E4300">
  <img src="/img/posts/dell-dimension-e520-bios-memory-info.jpg" alt="E520 BIOS screen showing 3GB of DDR2-667 in dual interleaved mode">
</div>

### Things worth knowing before you use one

- **BIOS "OS Install" mode** temporarily caps available RAM at 256MB. It's genuinely useful — it removes one of the first hurdles to a Windows 98 install before setup even starts.
- **No rear PS/2 or serial ports.** USB keyboards can be laggy or buffered in native DOS, and there's no easy legacy fallback. The motherboard appears to have solder pads for a serial or PS/2 header, but that's an untested path.
- The **`ICH8` southbridge** is late enough that it was never designed with Windows 98 or DOS in mind. That's the main reason the machine feels far more natural under Windows XP than under either of them.

![The E520 BIOS "OS Install" option, which caps RAM at 256MB](/img/posts/dell-dimension-e520-bios-memory-limiting-option.jpg){: width="720"}

### Where it fits

Windows XP is the natural home for this hardware generation. Windows 98 is possible but you'll be managing storage quirks and patches, and DOS is viable given the CPU headroom but wants input and sound workarounds.

For the full experiment — the SATA patching, the PCIe Radeon trouble, the surprisingly good Voodoo 2 results, and where it all landed — see [I Tried to Turn a Dell Dimension E520 into a Windows 98 Retro PC]({% post_url 2026-03-30-i-tried-to-turn-a-dell-dimension-e520-into-a-windows-98-retro-pc %}).
