---
layout: post
title: "MiSTer FPGA Part 1 – Intro and Hardware Overview"
date: '2020-08-22 15:02:00:00'
summary: MiSTer is an open project that aims to recreate various classic computers, game consoles and arcade machines using modern FPGA hardware. I plan to deep-dive on some of the retro computing cores – but first a project introduction and hardware overview ...
tags: [FPGA, MiSTer, Posts, Retrocomputing, Retrogaming, Single-Board Computing]
---


<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/qBDSzpBh_oY?rel=0" 
frameborder="0" allowfullscreen class="youtube-video"></iframe>
</div> 

MiSTer is an open project that aims to recreate various classic computers, game consoles and arcade machines using modern FPGA hardware. I plan to deep-dive on some of the retro computing cores – but first a project introduction and hardware overview.


### Introduction

The base hardware is the <a href="https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046" target="_blank">Terasic DE10-Nano</a>, which is built as a learning and development platform for FPGA. FPGA stands for <a href="https://en.wikipedia.org/wiki/Field-programmable_gate_array" target="_blank">Field-Programmable Gate Array</a> – the key concept here is that FPGA circuits are designed to be configured by the developer *after* manufacturing (hence "Field-Programmable").


#### How does FPGA work?

An FPGA chip contains an array of programmable logic blocks, memory and interconnects that can be "wired together" by the developer. Developers write "Hardware Description Language" (HDL) – instructing the FPGA to create electronic circuits and compose logic gates into fully functional, working hardware.

Most importantly for retro-enthusiats, it's possible to author HDL to replicate the hardware from old computers and consoles – perhaps even down to the circuit level. It's possible to recreate an Amiga or Atari ST *inside* the FPGA – and then run it for a very authentic retro computing experience. *How* authentic depends on the accuracy of the HDL implementation vs the original hardware. Today (August 2020) the experience is already very good


### What is MiSTer?

Realising the potential of the DE10-Nano for retro computing, a developer known as Sorgelig started the <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki" target="_blank">MiSTer project</a> with the specific intent of recreating retro computers, consoles and arcade machines on modern FPGA hardware. "MiSTer" is:

* The base hardware: the DE10-Nano board
* *Plus* retro computer hardware definitions in the form of HDL (aka "cores")
* *Plus* a Linux-based operating system to load and run the cores
* *Plus* <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki/Addons_Overview" target="_blank">hardware add-ons</a> – so you can expand your MiSTer with additional memory, IO options, a USB hub or even a case

The whole project is <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki" target="_blank">on GitHub</a> and open-sourced so anyone can contribute.


### Hardware Overview

![](/img/posts/mister-fpga-layout.jpg)

Taking a look at the hardware itself:

* On the base board we have the Cyclone V SoC. This contains the FPGA and also a dual-core ARM Cortex-A9 to run the host OS

Around the outside we have:

* The power jack, which uses a 5V DC barrel connector
* HDMI-out for video
* Two Mini-USB sockets, which are used for FPGA programming
* An RJ45 socket for Ethernet 
* A Micro-USB socket to connect your peripherals: mouse, keyboard and gamepad

Underneath the device we have a microSD card slot. The microSD card contains the OS and also any cores/software you want to load. The DE10-Nano kit ships with an 8GB card which is plenty for MiSTer use.


#### Add-Ons

In terms of <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki/Addons_Overview" target="_blank">add-ons</a>, I have a <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki/SDRAM-Board" target="_blank">32MB SDRAM board</a>. This is strongly recommended – the majority of computer and console cores require it. <a href="https://github.com/MiSTer-devel/Main_MiSTer/wiki/Addons_Overview" target="_blank">Other add-ons</a> are optional. 

<hr />

That's it for the hardware overview. Next up: [Install and Setup]({% post_url 2020-09-20-mister-fpga-install-and-setup %}).


### Other Posts in this Series

{% include mister-fpga-series.md %}
