---
layout: post
title: TPM Modules
summary: What I learned buying and fitting a discrete TPM module to try to get Windows 11 onto an older PC — how the headers work, which module I needed, and why it still wasn't enough.
date: '2024-08-29 11:33:00'
tags: [PC, Peripherals]
---

![A Supermicro discrete TPM module](/img/supermicro-tpm-module.jpg){: width="480"}

A **Trusted Platform Module** is a small security chip that handles key storage and system-integrity checks. Windows 11 requires one, which sent a lot of people — me included — rushing to buy a discrete module for an older motherboard.

### Discrete vs firmware

- **Firmware TPM (fTPM)** — built into the CPU. Intel Skylake (2015) / AMD Zen+ (Ryzen 2000) and newer usually have one; you just enable it in the BIOS (Intel PTT / AMD fTPM).
- **Discrete TPM** — a physical chip, either soldered to the board or plugged into a **TPM header**. This is what older boards need.

There are also two specs — **TPM 1.2** and the newer, incompatible **TPM 2.0**. Windows 11 wants 2.0.

### Fitting one

The catch with discrete modules is that there is no single header standard. You have to match your motherboard's header exactly. The common ones:

- `TPM/FW3.19` — 20-1 pin, TPM 1.2
- `TPM-L R2.0` — 20-1 pin, TPM 2.0
- `TPM-M R2.0` — 14-1 pin, TPM 2.0

For my Asus Z87-PRO I found a matching module for about $7. Before fitting it, the system also needs to be on **UEFI with Secure Boot**, which meant an `MBR2GPT` conversion from the old Legacy/MBR install first. After that, fitting the module and enabling TPM in the BIOS got me "The TPM is ready for use."

### Why it wasn't enough

Two problems remained. My board's module was only **TPM 1.2**, not 2.0 — and even with 2.0, Windows 11 also enforces a **minimum CPU generation** (Intel 8th-gen / Ryzen 2000). My i7-4770K was never going to qualify. The module was, in the end, unnecessary: a registry bypass turned out to be the real answer.

### Related on this site

- [What is a TPM? And Why Do I Need One for Windows 11?]({% post_url 2021-08-28-how-to-install-a-tpm-module %})
- [How To Install Windows 11 on an Unsupported PC With Registry Bypass]({% post_url 2021-10-16-upgrade-an-unsupported-pc-to-windows-11-with-registry-bypass %})
