

#blog/ideas 

  

Lower priority, but I can use it as a soft way to market my Mac Pro video on the blog

  

  

**OS versions**

  

- The highest OS version that can be *directly* installed on the Mac Pro 5.1 is High Sierra (10.13). This can be installed via regular USB install media
- Mojave (10.14) is the highest OS officially supported by the Mac Pro 5.1, and can be installed as an upgrade from High Sierra without any hacks (i.e. it doesn’t need OpenCore etc)
- Newer MacOS versions (up to Sonoma 14.4) can be installed with OpenCore Legacy Patcher (OCLP)
- OCLP is built for a large variety of Hackintosh hardware and relies on root patches to add hardware compatibility. There is another version of OpenCore (Martin Lo’s OpenCore) that is built specifically for Mac Pro 5,1 hardware and tries to keep things as vanilla as possible. This supports up to Mac OS Monterey 12.7

  

32-bit and 64-bit applications 

  

- MacOS version up to and including Mojave (10.14) can support 32-bit applications. This is useful for some older games like Half-life 2, Warcraft 3 etc
- OS versions from Catalina 10.15 and up support 64-bit apps only

  

Here’s a list of 32-bit vs 64-bit games:

  

[Catalina 64-bit Compatibility - Google Drive](https://docs.google.com/spreadsheets/d/17DkOsI9AwAT4dzPkLmunYJJmUpf1FuWR62Q1vAEfJzM/htmlview#)

  

Graphics cards

  

- Older versions of MacOS (up to High Sierra) typically require dedicated Mac graphics cards. Driver support has to be built into the OS
- MacOS Mojave 10.14 and up require a “Metal compatible” GPU. These are slightly more modern cards that support the Metal 3D API
- Unfortunately MacOS Mojave does not support *very* modern graphics cards. The best you can support is something like Radeon RX 580, or GeForce GTX 770. In fact these cards are great as a “one size fits all” card since they support both older and newer MacOS versions
- Newer versions of MacOS can support much newer graphics hardware. For example my RX 6600 XT works well on MacOS Monterey

  

More details here:

  

[https://blog.greggant.com/posts/2018/05/07/definitive-mac-pro-upgrade-guide.html](https://blog.greggant.com/posts/2018/05/07/definitive-mac-pro-upgrade-guide.html)

  

The “best compromise” Mac Pro 5,1

  

- Dual boot with MacOS Mojave for 32-bit apps and MacOS Monterey (OpenCore) for modern apps
- Either a GeForce GTX 770 or (slightly better with more VRAM) a RX 580. These are new enough to run modern Metal games on Monterey but old enough to still support Monterey and 32-bit apps

  

The “ultimate” Mac Pro 5,1

  

- OpenCore install of MacOS Monterey
- Fast modern GPU like the RX 6600 XT to play modern games 

  

Installing MacOS Mojave

  

- First install High Sierra using a dedicated Mac graphics card (old EFI card is needed for the boot picker, menus etc)
- Switch the GPU for a Metal compatible (but still Mojave compatible) GPU - like the GeForce GTX 770 - and upgrade to Mojave via the built in system upgrade feature

  

The steps are also outlined in this video:

  

[https://youtu.be/eUbo1a1LtKI?si=xAcR26e3gij4EVyo](https://youtu.be/eUbo1a1LtKI?si=xAcR26e3gij4EVyo)

  

Installing MacOS Monterey (or newer)

  

- Start with MacOS Mojave installed first
- Follow the steps on this video:

  

[https://youtu.be/-S0eN_hzMto?si=1SVpl3e4w4WOWSUS](https://youtu.be/-S0eN_hzMto?si=1SVpl3e4w4WOWSUS)