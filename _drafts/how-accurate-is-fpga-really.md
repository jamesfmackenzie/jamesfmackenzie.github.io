---
layout: post
title: How Accurate Is FPGA Really?
summary: A draft about what people mean by FPGA accuracy and why implementation quality matters more than the marketing slogan.
tags: [Emulation, FPGA, Retrocomputing]
---

People often talk about FPGA as if it automatically guarantees perfect hardware accuracy. That is too simple.

## The Short Version

FPGA implementations can be extremely accurate. In some cases they can be cycle accurate or even modeled at a very low level. But none of that is automatic.

The real question is how the core was designed:

- was it based on careful hardware research?
- was it validated properly?
- was it built from good reference material?

If the individual components are modeled well, the final result can be very close to original hardware. If not, an FPGA core can still be wrong.

## Why FPGA Has an Advantage

One big advantage is that hardware blocks interact in parallel, just as they do on real hardware. That gives FPGA an architectural advantage over naive software emulation.

## Why Software Emulation Is Not Automatically Inferior

Software emulators do not get parallel behaviour for free, but modern CPUs are extremely fast and good emulator authors can still build very accurate results. It is just hard work.

## What the Final Version Should Add

- clearer definitions of cycle accuracy, timing accuracy, and gate-level claims
- examples of where FPGA cores get things right
- examples of where they still diverge from original hardware
