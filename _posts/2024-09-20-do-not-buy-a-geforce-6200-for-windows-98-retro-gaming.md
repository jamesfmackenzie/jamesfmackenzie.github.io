---
layout: post
title: "Do Not Buy a GeForce 6200 for Windows 98"
date: '2024-09-20 17:54:00:00'
summary: |-
  A warning post!
  
  I recently bought this GeForce 6200 PCI as a passively cooled GPU for Windows 98. It was a bad idea!
  
  Read on for full details.
image: nvidia-geforce-6200-pci.jpg
tags: [Nvidia Graphics, Posts]
---

![nvidia GeForce 6200 PCI](/img/posts/nvidia-geforce-6200-pci.jpg)

I recently bought this GeForce 6200 PCI as a passively cooled GPU for Windows 98.

It was a bad idea!

In Windows 98, all games exhibit constant stuttering.

Direct3D performance is also much lower than expected - barely better than a (much older) Voodoo 3 2000.

For comparison:

* The Voodoo 3 is a 16MB, 143MHz GPU from 1999.
* The GeForce 6200 is a 256MB, 300MHz GPU from 2004.

The performance should be *way* better.

Initially I suspected a PCI bottleneck. The 6200 is normally an AGP card and may be held back by the (comparatively slow) PCI bus.

However!

When I try the same card in Windows XP, the performance is *way* better - almost double in some scenarios.


### Conclusion

The Windows 98 drivers are not good for this card.

Don’t buy the GeForce 6200 (or probably any GeForce 6 series card) for Windows 98 gaming!

