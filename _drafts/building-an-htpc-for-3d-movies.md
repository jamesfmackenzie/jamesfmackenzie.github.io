---
layout: post
title: Building an HTPC for 3D Movies
summary: A working draft on building a PC setup that can play full-quality 3D Blu-ray rips with proper frame-packed output.
tags: [3D, Home Theater, HTPC, Video]
---

This draft is a follow-up to the projector and 3D cinema experiments. The real goal here is not just "play some 3D video," but to build a no-compromise PC setup that can handle full-quality 3D movie playback properly.

## Why an HTPC at All?

The problem is that many devices can play simple 3D formats, but very few can handle the best one cleanly.

That creates two very different tiers of 3D playback:

- **side-by-side / top-bottom** formats that are easy to play but lose resolution
- **frame packing** that preserves full quality but needs much more specific hardware and software support

## What Frame Packing Is

Frame packing is a special 3D video mode where full-resolution left-eye and right-eye images are packed together into a single larger video frame with the correct signalling metadata.

For a 1080p movie, that effectively means:

- two full 1080p images
- a larger packed transport frame
- metadata that tells the display to engage proper 3D mode

If the display understands the signal, you get the best result without sacrificing horizontal or vertical detail the way side-by-side formats do.

## The High-Level Workflow

The main steps in the notes are already clear:

1. rip the 3D Blu-ray properly
2. choose playback software that understands MVC content
3. get actual frame-packed output working
4. make the audio side practical too

## Acquiring 3D Content

The draft already points to **MakeMKV** as the right starting point.

The key idea is:

- keep the original video quality
- keep the 3D MVC content
- avoid lossy transcoding

That makes this more of an archival and playback workflow than a conversion workflow.

## Playback Software

The notes suggest two workable Windows players:

- **Stereoscopic Player**
- **MPC-BE**

The important distinction is that a player can decode the content without necessarily solving the output problem. Playback and display mode are separate challenges.

## The Real Difficulty: Frame-Packed Output

This is the heart of the article.

The big obstacle is that modern PC graphics drivers mostly abandoned proper 3D display support years ago.

That leads to two broad paths:

### Option 1: Build an Older 3D-Friendly PC

The notes suggest success here with:

- older Intel integrated graphics experiments
- legacy Nvidia driver versions
- eventually using a GTX 1060 with 3D-capable older drivers

This sounds messy, but it is at least a known-good direction.

### Option 2: Revive 3D on a Modern PC

The other interesting route is **3D Fix Manager**, which can restore access to Nvidia 3D Vision functionality on newer setups.

That opens the possibility of:

- keeping a modern machine
- restoring frame-packed support through patched driver flows
- using the same MPC-BE based playback chain

That is probably the most valuable section for readers, because it offers a path that does not require a dedicated legacy HTPC.

## Bonus Topic: 3D Gaming

The notes also point toward **geo-11** and related tools for reviving stereoscopic 3D gaming on PC.

That may be worth treating as a bonus section rather than folding it into the movie workflow, because it is related but not the same problem.

## What the Final Version Should Add

- a much tighter split between movie playback and 3D gaming
- the exact software stack that ended up working reliably
- which GPU and driver combinations were actually successful
- a simple "best modern route" versus "best legacy route" conclusion
