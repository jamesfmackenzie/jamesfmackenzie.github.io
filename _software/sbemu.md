---
layout: post
title: SBEMU
summary: Notes on SBEMU, the DOS utility that emulates Sound Blaster and AdLib audio on hardware with no real legacy sound path at all.
date: '2024-08-29 11:33:00'
tags: [MS-DOS, PC, Sound, Utilities]
---

Most PCI-era and later motherboards dropped proper legacy DOS audio entirely — no ISA bus, no real Sound Blaster compatibility, just silence in old games. SBEMU (by GitHub user [crazii](https://github.com/crazii/SBEMU)) fixes that in software.

### What it is

SBEMU is a DOS TSR that emulates a Sound Blaster card and AdLib FM synth, using whatever real audio hardware is actually present as the output path. It supports a specific set of chipsets: Intel ICH southbridge audio, VIA VT82C686/VT8233, nForce, Intel HD Audio, and PCI cards like the Sound Blaster Live! and Audigy. Point it at one of those, and DOS games get genuine Sound Blaster-compatible digital audio and AdLib-compatible FM music, with no real ISA Sound Blaster in the machine at all.

### Why it matters

I got it running on a Core i7 PC — hardware with no legacy DOS audio path whatsoever — and had Doom running with FM audio, and Duke Nukem 3D with full digital sound, natively in DOS. Not an emulator, not DOSBox: real DOS, real games, sound working on a machine that should have been completely silent.

It also gives later PCI sound cards a second life. A [Sound Blaster Live!]({% link _hardware/creative-labs-sound-blaster-live.md %}) has a shaky story under native DOS on its own, but as an SBEMU output target it becomes genuinely useful there.

### Setting it up

Getting it onto a bootable USB stick and configured is straightforward but has a couple of specific steps — see [How To Install SBEMU on a Bootable USB Stick]({% link _howto/how-to-install-sbemu-on-a-bootable-usb-stick.md %}) for the full walkthrough.

### Related on this site

- [How To Install SBEMU on a Bootable USB Stick]({% post_url 2023-03-22-how-to-install-sbemu-on-bootable-usb-stick %})
- [SBEMU Just Killed Your DOS Gaming PC]({% post_url 2023-03-12-sbemu-just-killed-your-dos-gaming-pc %})
- [Can you run Doom: On a Core i7 PC? With Sound Blaster and AdLib audio? Natively in DOS? With SBEMU you can! It's a game changer!]({% post_url 2023-03-07-you-can-run-doom-on-a-core-i7-pc-in-native-dos-with-sbemu %})
- [Creative Labs Sound Blaster Live!]({% link _hardware/creative-labs-sound-blaster-live.md %})
