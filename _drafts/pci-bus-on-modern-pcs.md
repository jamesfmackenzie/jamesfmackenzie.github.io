---
layout: post
title: PCI Bus on Modern PCs
summary: A technical draft on how PCI survives on newer systems through PCIe bridge chips, and why some legacy cards work better than others.
tags: [PC Hardware, PCI, Retrocomputing]
---

Modern consumer PCs no longer provide a native PCI bus in the way older chipsets did. If a current-era motherboard or adapter still exposes PCI slots, there is usually a bridge chip involved.

That matters a lot if you are trying to use old hardware like:

- 3dfx Voodoo cards
- PCI sound cards
- unusual industrial or test equipment

## Native PCI Versus Bridged PCI

One of the key questions for the finished post is:

- what was the last mainstream chipset with true native PCI support?

After that point, PCI support generally has to be recreated through a PCIe-to-PCI bridge.

## Why Some Cards Work and Others Do Not

Graphics cards such as a **Voodoo 2** can work surprisingly well behind a bridge.

Sound cards are harder.

The major problem in the notes is legacy DMA behaviour:

- many PCI sound cards expect features associated with older southbridges
- DDMA support matters
- subtractive decode support matters
- some cards have their own workaround technology, such as Yamaha's DSDMA

That means "does it fit in the slot?" is only the beginning of the compatibility question.

## Bridge Chips Worth Covering

The draft notes mention several families worth investigating:

- ASMedia PCIe-to-PCI bridges
- Pericom `PI7C9X111SL`
- Texas Instruments `XIO2001`
- IDT-based bridge solutions

The final version should explain which chips are used in real motherboards and adapter cards, and what kinds of behaviour they permit.

## Important Sound Card Angle

One of the strongest practical points in the notes is that some Yamaha cards can partially function, but settings may not persist because of missing subtractive decode support.

That gives the article a useful real-world troubleshooting angle rather than making it just a chipset taxonomy.

## What the Final Version Should Add

- identify the last native PCI chipsets clearly
- explain DDMA, PC-PCI, and subtractive decode in plain language
- map common bridge chips to known working and failing card types
- include your own tested combinations where possible
