---
layout: post
title: Framerate Analysis Tool
summary: 
date: '2024-08-29 11:33:00'
tags: [Tools]
---

<a name="Framerate Analysis Tooling">
## Framerate Analysis Tooling

Status | In-Progress
Goal | Build my own "Digital Foundry" style tooling to analyze videogame performance

Inspired by <a href="https://www.youtube.com/user/DigitalFoundry" target="_blank">Digital Foundry</a>, <a href="https://www.youtube.com/c/VGTech" target="_blank">VG Tech</a> and <a href="https://www.youtube.com/c/NXGamer" target="_blank">NX Gamer</a>, I wanted to deep-dive on videogame technical analysis. I set myself the following goals:

1. **Write my own performance analysis tooling**. Look at captured videogame footage and analyze framerate, torn frames, resolution etc
2. **Run some real performance comparisons** (e.g. Xbox Series X vs PS5 performance)
3. **Technical learning!** Build some proficiency in videogame technical analysis and machine vision

After some background research, I selected <a href="https://opencv.org/" target="_blank">OpenCV</a> as the foundational project library. As a specialised framework for computer vision and image analysis, it's a great project fit.

First, I worked on <a href="https://twitter.com/jamesfmackenzie/status/1516036998947028992" target="_blank">difference detection between video frames</a>. If two frames show zero difference, that means we have a duplicate frame (i.e. a frame drop vs the target frame rate).

With diff detection in place, I was able to <a href="https://twitter.com/jamesfmackenzie/status/1515344348313002000" target="_blank">do some rudimentary framerate analysis on The Legend of Zelda: Breath of the Wild</a> and (after some more iteration) <a href="https://twitter.com/jamesfmackenzie/status/1519647506254254080" target="_blank">add performance monitoring and graphing</a>.

Next, I investigated detection of torn frames. This is when the renderer doesn't have enough time to complete an entire frame, so a partial frame is rendered to the screen instead (with the remaining row gaps filled in with data from the last frame). I <a href="https://twitter.com/jamesfmackenzie/status/1520448444074188800" target="_blank">enhanced diff detection</a> and was able to <a href="https://twitter.com/jamesfmackenzie/status/1520807871549779970" target="_blank">reliably detect torn frames in Gran Turismo 5</a> (a game known for significant image tearing).

My next focus was resolution counting. Videogames often dynamically reduce rendering solution to keep frames "within budget" (i.e. rendered fast enough to hit the desired 30fps or 60fps target). This is known as Dynamic Resolution Scaling (DRS). The frame is then upscaled back to the target resolution (e.g. 1080p or 4K). It's an effective approach, but reduces image quality vs "native resolution" rendering. Artifacts (such as jagged edges) appear in the image, and it's possible to exploit these to identify the original render resolution of the frame.  

As a first pass, I was able to <a href="https://twitter.com/jamesfmackenzie/status/1531623625702400000" target="_blank">find all edges in each frame</a>. I was then able <a href="https://twitter.com/jamesfmackenzie/status/1532721445222158336" target="_blank">find "countable edges"</a> - straight line edges that can be <a href="https://www.youtube.com/watch?v=3ra-P3gH7Dg" target="_blank">pixel counted</a> to identify the original render resolution of the frame.

Unfortunately the automation didn't work. Despite hours or tuning, the edge detection algorithm wasn't able to distinguish between polygon edges (which are suitable for counting) and straight line edges found within filtered textures (which aren't). The counts are unreliable, **so I've parked this for now**.

Next, I looked at framerate counting for *compressed* video. Video compression is typically lossy <a href="https://en.wikipedia.org/wiki/Compression_artifact" target="_blank">and introduces image artifacts e.g. pixelation, macroblocking etc</a>. These artifacts make it very challenging to detect duplicate frames. 100% identical frames rendered by the game engine will appear different in compressed video.

In short, compressed video broke my diff detection. Every single frame is perceived as unique - no frame drops detected. To address this, I needed to adopt a more statistical approach. Instead of looking for *zero* difference between frames, I looked at *difference trend*:

* Hypothesis: because video frames from a 3D engine are temporally connected, we would *usually* expect frame difference trend to be relatively consistent between frames. Significant trend divergence is aberration - and might indicates a frame drop

To test the hypothesis, I created a time series of frame-to-frame difference (Euclidean difference) for compressed video with known frame drops:

<img src="https://pbs.twimg.com/media/FVdxbEFXsAEgcJn?format=png" />

See those downspikes in the graph above? Those are the frame drops. And they're easy to identify. This is great news!

A few updates later, I was able to <a href="https://youtu.be/aQsxzAXpaHk" target="_blank">complete framerate analysis for the Starfield Official Gameplay Reveal</a>.

Finally, I looked at high quality video export from OpenCV. Unfortunately the built-in OpenCV VideoWriter is not super configurable - and video output is relatively low bitrate and blocky. Instead I chose to output results as PNG and then re-assemble into video using <a href="https://ffmpeg.org/" target="_blank">ffmpeg</a>.

Challenges overcome:

- Sampling framerate from captured gameplay video
- Identifying duplicate frames and torn frames
- Graphics and performance graphing in OpenCV
- How to accommodate compression noise in captured video
- High quality video export from OpenCV

Upcoming goals:

- Side-by-side comparison of 2 (or 3) videos
- Resolution counting revisited

You can also find the journey chronicled on Twitter <a href="https://twitter.com/jamesfmackenzie/status/1515054433889144834" target="_blank">here</a>.
