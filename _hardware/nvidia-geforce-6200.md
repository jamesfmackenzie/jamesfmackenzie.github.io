---
layout: post
title: Nvidia GeForce 6200
summary: My notes on the GeForce 6200 PCI — a passively cooled card that looks ideal for a Windows 98 retro build on paper, but disappoints badly in practice because of poor Windows 9x drivers.
date: '2024-08-29 11:33:00'
tags: [Graphics Cards, Nvidia Graphics, PC]
hero: nvidia-geforce-6200-pci-rear.jpg
hero_alt: GeForce 6200 PCI, rear view showing the passive heatsink and DVI/VGA outputs
---

The GeForce 6200 is a budget card from 2004. I bought the **PCI version** — one of the relatively rare non-AGP variants — specifically as a passively cooled GPU for a Windows 98 retro gaming PC. On paper it looks like a big step up from the usual period options. In practice it was a bad buy.

### The Windows 98 problem

Under Windows 98 SE, every game stutters constantly. Direct3D performance is also far lower than the spec sheet suggests — barely ahead of a [3Dfx Voodoo3]({% link _hardware/3dfx-voodoo-3.md %}) 2000, which is a 16 MB, 143 MHz card from 1999. The 6200 is a 256 MB, 300 MHz card from 2004. It should not be close.

My first suspicion was the PCI bus holding back a chip designed for AGP. But running the same card in **Windows XP** roughly doubles the frame rate in some scenes, so the bottleneck is not the bus — it is the driver.

![3DMark2001 Car Chase on the GeForce 6200 under Windows 98, running at about 70 fps](/img/nvidia-geforce-6200-benchmark-windows-98.jpg){: width="480"}

![The same benchmark scene under Windows XP, running at about 150 fps](/img/nvidia-geforce-6200-benchmark-windows-xp.jpg){: width="480"}

Same card, same benchmark scene: roughly 70 fps on Windows 98 versus roughly 150 fps on Windows XP.

### Drivers I tried

- **Windows 98 SE:** [81.98 (December 2005)](https://www.philscomputerlab.com/nvidia-9x-graphics-drivers.html) from Phil's Computer Lab — the source of the stutter and the weak performance.
- **Windows XP:** [93.71 Forceware (October 2006)](https://www.philscomputerlab.com/nvidia-xp-graphics-drivers.html) and the [307.83 GeForce driver (February 2013)](https://www.nvidia.com/en-us/drivers/details/57493/) from Nvidia. Both are dramatically better than the Windows 9x driver.

### The PCI voltage catch

One more quirk from testing the card in a PCI backplane: although the edge connector is keyed for both 3.3 V and 5 V PCI, it will **not** work in a 3.3 V-only slot. The card fails to initialise and the machine will not POST. You need an ATX power supply that provides 5 V on the PCI slot.

### Verdict

Don't buy a GeForce 6200 — or, most likely, any GeForce 6-series card — for a Windows 98 build. For Windows XP it is a fair low-end passive option.

### Related on this site

- [Do Not Buy a GeForce 6200 for Windows 98]({% post_url 2024-09-20-do-not-buy-a-geforce-6200-for-windows-98-retro-gaming %})
- [Recently bought this GeForce 6200 PCI... a thread]({% post_url 2024-09-20-do-not-buy-a-geforce-6200-6-series-for-windows-98 %})
- [3Dfx]({% link _hardware/3dfx.md %})
