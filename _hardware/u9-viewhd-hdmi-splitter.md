---
layout: post
title: U9 ViewHD HDMI Splitter
summary: Notes on the cheap 1x2 HDMI splitter (sold as U9, ViewHD and other brands) that strips HDCP as a side effect — handy for capturing from HDCP-locked sources like the PlayStation 3.
date: '2024-08-29 11:33:00'
tags: [Video Capture]
---

This is a cheap 1-in, 2-out HDMI splitter sold under a rotating cast of brand names — U9, ViewHD and others — usually a small metal box with a micro-USB power lead.

### The useful side effect

Its intended job is to send one HDMI source to two displays. But to do that it has to re-clock the signal, and in the process it **drops HDCP**. The output is a clean, unprotected copy of the input.

That matters because some devices force HDCP on *all* output, even menus and non-video content, which blocks most capture cards. The **PlayStation 3** and **PlayStation TV** are the usual culprits. Put one of these splitters between the console and the capture card and the picture comes through fine.

### Notes

- it does not change resolution, frame rate or anything else — it just passes the signal
- both outputs are active at once, so you can feed a display and a capture card together
- these are commodity boxes; the exact PCB and branding vary, and not every unit behaves identically, but the U9 / ViewHD ones have a good track record for HDCP stripping

### Related on this site

- [The U9/ViewHD splitter will strip HDCP and allow capture from devices like PlayStation 3]({% post_url 2022-05-03-the-u9-viewhd-splitter-will-strip-hdcp-and-allow-capture-from-devices-like-playstation-3 %})
- [Sony PlayStation 3]({% link _hardware/sony-playstation-3.md %})
