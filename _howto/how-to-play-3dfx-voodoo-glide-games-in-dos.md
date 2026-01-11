---
layout: post
title: How To Play 3Dfx Glide Games in DOS
date: '2024-09-18 22:47:00'
summary: How to play 3Dfx Glide games in the DOS environment
tags: [How To, 3Dfx Voodoo, MS-DOS, PC, Retrocomputing]
---

We all know that many Windows 98 games take advantage of the 3Dfx Glide API — in fact the widespread support for Glide was a big reason to buy a Voodoo card back in the 90s.

But do you know that Glide games are supported in DOS too?

Here's what you need to know.


### There are two types of games

1. **Statically linked** games have their Voodoo support baked into the application binary. In short, the game is hardcoded to talk directly to the Voodoo hardware.

2. **Dynamically linked** games take advantage of the <code>glide2x.ovl</code> library. When a Glide game starts up, it first looks for this file in the game directory, then starts to look through the directories specified in the <code>%PATH</code>.


### Statically linked games

Because the Voodoo support is baked in, these games only support earlier Voodoo hardware — i.e. the Voodoo1 and Voodoo2 3D accelerator cards. Without these cards present, the game or PC will usually freeze.


### Dynamically linked games

For these games, it's good news: we can take advantage of the OVL abstraction to play these games on a Voodoo 3, 4 or even Voodoo 5 card!

All official Voodoo driver packages include a copy of <code>glide2x.ovl</code>. Just grab the appropriate version for your card, and place it in the game directory.


### Environment variables

The Voodoo behaviour can be modified by setting DOS <a href="https://en.wikipedia.org/wiki/Environment_variable#DOS,_OS/2_and_Windows" target="_blank">environment variables</a>.

These can be set via a <a href="https://en.wikipedia.org/wiki/Batch_file#DOS" target="_blank">batch file</a>, which you could run prior to launching your game:

```
REM ===== GLIDE ENVIRONMENT VARIABLES (ALL CARDS) =====
SET FX_GLIDE_LOD_DITHER=1
SET FX_GLIDE_SWAPINTERVAL=0
SET FX_GLIDE_NO_SPLASH=1
SET FX_GLIDE_ALLOC_COLOR=3

REM ===== VOODOO 1 ENVIRONMENT VARIABLES =====
SET SST_GRXCLK=50
SET SST_FT_CLK_DEL=0x4
SET SST_TF0_CLK_DEL=0x6
SET SST_TF1_CLK_DEL=0x6
SET SST_VIN_CLKDEL=0x1
SET SST_VOUT_CLKDEL=0x0
SET SST_FASTMEM=0
SET SST_TMUMEM_SIZE=2
SET SST_SCREENREFRESH=60

REM ===== VOODOO 2 ENVIRONMENT VARIABLES =====
SET SSTV2_GRXCLK=50
SET SSTV2_SWAP_EN_WAIT_ON_VSYNC=0
SET SSTV2_SCREENREFRESH=60
SET SSTV2_VIDEO_24BPP=1
SET SSTV2_FASTPCIRD=0
SET SSTV2_FASTMEM=0
SET SSTV2_SWAPINTERVAL=1
SET SSTV2_ANTIALIAS=1
SET SSTV2_SCREENREFRESH=60
SET SSTV2_REFRESH_512x384=60
SET SSTV2_REFRESH_640x400=60
SET SSTV2_REFRESH_640x480=60
SET SSTV2_REFRESH_800x600=60
SET SSTV2_GAMMA=1.7
SET SSTV2_RGAMMA=1.20
SET SSTV2_GGAMMA=1.20
SET SSTV2_BGAMMA=1.20
SET SSTV2_OVERLAYMODE=1

REM ==== VOODOO 3-5 ENVIRONMENT VARIABLES ====
SET SSTh3_GRXCLK=50
SET SSTh3_SWAP_EN_WAIT_ON_VSYNC=0
SET SSTh3_SCREENREFRESH=60
SET SSTh3_VIDEO_24BPP=1
SET SSTh3_FASTPCIRD=0
SET SSTh3_FASTMEM=0
SET SSTh3_SWAPINTERVAL=1
SET SSTh3_ANTIALIAS=1
SET SSTh3_SCREENREFRESH=60
SET SSTh3_REFRESH_512x384=60
SET SSTh3_REFRESH_640x400=60
SET SSTh3_REFRESH_640x480=60
SET SSTh3_REFRESH_800x600=60
SET SSTh3_GAMMA=1.7
SET SSTh3_RGAMMA=1.20
SET SSTh3_GGAMMA=1.20
SET SSTh3_BGAMMA=1.20
SET SSTH3_SLIDETECT=0
SET SSTh3_OVERLAYMODE=0
```

Find the full list (with explanations!) right <a href="https://www.mdgx.com/3dfx.htm" target="_blank">here</a>.


### Running a Voodoo 1/2 and 3/4/5 in the same machine

This is possible, and perhaps desirable to play both newer and older Glide games. Find more details <a href="https://www.vogons.org/viewtopic.php?t=62534" target="_blank">here<a/>. 


### Supported games

Statically linked games:

* Actua Soccer '96
* Battle Arena Toshinden
* EF2000: Tactcom
* Fatal Racing/Whiplash
* Starfighter 3000

Dynamically linked games:

* Descent II
* Tomb Raider
* Screamer 2
* XCar: Experimental Racing

Note: there are some compatibility problems even for these dynamically linked games. One example is Archimedean Dynasty.

Find more details <a href="https://www.vogons.org/viewtopic.php?t=886" target="_blank">here</a>.


### Troubleshooting individual games

#### Tomb Raider

For Tomb Raider, there are <a href="https://www.philscomputerlab.com/tomb-raider.html" target="_blank">two patches available</a>.

- The first is statically linked and works with Voodoo 1 cards only.
- The second (sometimes referred to as the Voodoo Rush patch), is dynamically linked and works with all Voodoo cards.

By default, the second patch is a little dark. Gamma can be adjusted using the environment variables above. This works well for Voodoo 1/2, but doesnt seem to work for Voodoo 3+

Find more details <a href="https://www.vogons.org/viewtopic.php?t=46532" target="_blank">here</a> and <a href="https://nerdlypleasures.blogspot.com/2014/07/tomb-raider-pc-oldskool-style.html" target="_blank">here</a>.


### More reading on Voodoo environment variables

- <a href="https://www.descentbb.net/viewtopic.php?t=1650" target="_blank">Descent Bulletin Board</a>
- <a href="https://www.3dfxzone.it/enboard/index.php?topic=16480" target="_blank">3dfxzone.it (1)</a>
- <a href="https://www.3dfxzone.it/enboard/index.php?action=profile;area=showposts;sa=messages;u=2687" target="_blank">3dfxzone.it (2)</a>
- <a href="https://www.mdgx.com/3dfx.htm" target="_blank">MDGx Voodoo Environment Variables</a>
- <a href="http://www.vogonswiki.com/index.php/3dfx" target="_blank">Vogons Wiki 3dfx</a>
- <a href="https://www.vogons.org/viewtopic.php?t=35721" target="_blank">Voodoo 2 DOS Glide compaibility matrix</a>

