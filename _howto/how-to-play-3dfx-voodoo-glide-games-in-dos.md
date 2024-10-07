---
layout: post
title: How To Play 3Dfx Glide Games in DOS
date: '2024-09-18 22:47:00'
summary: How to play 3Dfx Glide games in the DOS environment
tags: [3Dfx, 3Dfx Voodoo, DOS, PC]
---

We all know that many Windows 98 games take advantage of the 3Dfx Glide API - in fact the widespread support for Glide was a big reason to buy a Voodoo card back in the 90s.

But do you know that Glide games are supported in DOS too?

Here's what you need to know.

### There are two types of games

*Statically linked* games have their Voodoo support baked into the application binary. In short, the game is hardcoded to talk directly to the Voodoo hardware.

Because of this, these games only support earlier Voodoo hardware - i.e. the Voodoo1 and Voodoo2 3D accelerator cards. Without these cards present, the game or PC will usually freeze.

*Dynamically linked* games take advantage of the <code>glide2x.ovl</code> library. When a Glide game starts up, it first looks for this file in the game directory, then starts to look through the directories specified in the <code>%PATH</code>.

The good news: we can take advantage of the OVL abstraction to play these games on a Voodoo 3, 4 or even Voodoo 5 card!

All official Voodoo driver packages include a copy of <code>glide2x.ovl</code>. Just grab the appropriate version for your card, and place it in the game directory.
  
### Environment Variables

The Voodoo behaviour can be modified by setting environment variables. Find a comprehensive list below.

<code>
REM ===== VOODOO 1 ENVIRONMENT VARIABLES =====
set SST_GRXCLK=50
SET SST_FT_CLK_DEL=0x4
set SST_TF0_CLK_DEL=0x6
set SST_TF1_CLK_DEL=0x6
set SST_VIN_CLKDEL=0x1
set SST_VOUT_CLKDEL=0x0
SET SST_FASTMEM=0
set SST_TMUMEM_SIZE=2
SET SST_SCREENREFRESH=60

REM ===== GLIDE (?) ENVIRONMENT VARIABLES =====
SET FX_GLIDE_LOD_DITHER=1
SET FX_GLIDE_SWAPINTERVAL=0
REM SET FX_GLIDE_NO_SPLASH=1
rem SET FX_GLIDE_ALLOC_COLOR=3

REM ===== VOODOO 2 ENVIRONMENT VARIABLES =====
SET SSTV2_GRXCLK=50
SET SSTV2_SWAP_EN_WAIT_ON_VSYNC=0
SET SSTV2_SCREENREFRESH=60
SET SSTV2_VIDEO_24BPP=1

rem disable (0) might be more stable
SET SSTV2_FASTPCIRD=0

rem enables FAST DRAM compatibility (1 faster)
SET SSTV2_FASTMEM=0

set SSTV2_SWAPINTERVAL=1
set SSTV2_ANTIALIAS=1
SET SSTV2_SCREENREFRESH=60
set SSTV2_REFRESH_512x384=60
set SSTV2_REFRESH_640x400=60
set SSTV2_REFRESH_640x480=60
set SSTV2_REFRESH_800x600=60
REM SET SSTV2_GAMMA=1.7
REM set SSTV2_RGAMMA=1.20
REM set SSTV2_GGAMMA=1.20
REM set SSTV2_BGAMMA=1.20
set SSTV2_OVERLAYMODE=1

REM ==== VOODOO 3-5 ENVIRONMENT VARIABLES ====
SET SSTh3_GRXCLK=50
SET SSTh3_SWAP_EN_WAIT_ON_VSYNC=0
SET SSTh3_SCREENREFRESH=60
SET SSTh3_VIDEO_24BPP=1

rem disable (0) might be more stable
SET SSTh3_FASTPCIRD=0

rem enables FAST DRAM compatibility (1 faster)
SET SSTh3_FASTMEM=0

set SSTh3_SWAPINTERVAL=1
set SSTh3_ANTIALIAS=1
SET SSTh3_SCREENREFRESH=60
set SSTh3_REFRESH_512x384=60
set SSTh3_REFRESH_640x400=60
set SSTh3_REFRESH_640x480=60
set SSTh3_REFRESH_800x600=60
REM SET SSTh3_GAMMA=1.7
REM set SSTh3_RGAMMA=1.20
REM set SSTh3_GGAMMA=1.20
REM set SSTh3_BGAMMA=1.20
set SSTH3_SLIDETECT=0
set SSTh3_OVERLAYMODE=0
</code>

Full list here: https://www.mdgx.com/3dfx.htm

### Running a Voodoo 1/2 and 3/4/5 in the same machine

This is possible, and perhaps desirable to play both new and old games. See https://www.vogons.org/viewtopic.php?t=62534


### Supported Games

Statically linked game:

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

There are some compatibility problems even for these dynamically linked games. One example is Archimedean Dynasty.

For more details see https://www.vogons.org/viewtopic.php?t=886


### Troubleshooting Individual Games

Tomb Raider:

Some example threads to help us get Tomb Raider working:

https://www.vogons.org/viewtopic.php?t=46532

By default, the game is a little dark. Gamma can be adjusted using the environment variables above. This works well for Voodoo 1/2, but doesnt seem to work for Voodoo 3+


### More Reading

https://www.descentbb.net/viewtopic.php?t=1650

https://www.3dfxzone.it/enboard/index.php?topic=16480

https://www.3dfxzone.it/enboard/index.php?action=profile;area=showposts;sa=messages;u=2687

https://www.mdgx.com/3dfx.htm

http://www.vogonswiki.com/index.php/3dfx

https://www.vogons.org/viewtopic.php?t=35721