---
layout: post
title: USB ISA Storage Card
summary: A CH376-based 8-bit ISA storage card that lets a USB stick stand in for a hard drive on my Homebrew 8088 — bought directly from its maker.
date: '2024-08-29 11:33:00'
tags: [PC, Peripherals]
---

Getting storage onto an [8-bit ISA PC]({% link _hardware/8088-pc-xt-isa-card-sbc.md %}) usually means XT-IDE or an XT-CF adapter. This card does the same job a different way — a CH376-based USB-to-ISA design, bought directly from Elijah Miller (EMM Computers, homebrew8088.com) at the same time as my [Homebrew 8088]({% link _hardware/8088-pc-xt-isa-card-sbc.md %}) board.

### What it is

An 8-bit ISA card built around the CH376 USB controller chip — Elijah's own design, rather than a PicoMEM, XT-IDE, or XT-CF board. It presents a USB stick to DOS as a fixed disk. Elijah's own reasoning for recommending it over the alternatives: he'd built and sold this card before, hadn't tested the PicoMEM himself and had heard of at least one buyer having trouble with it, and wasn't sure about CF adapters either.

### Setting it up

It shipped with a USB stick pre-loaded with DOS 6.22. The one real requirement: the USB drive has to be formatted **FAT16** — a DOS limitation — which caps how large a usable partition can be, and larger partitions run slower.

### Related on this site

- [Homebrew 8088]({% link _hardware/8088-pc-xt-isa-card-sbc.md %})
- [Lo-tech XT-CF]({% link _hardware/lo-tech-xt-cf.md %})
