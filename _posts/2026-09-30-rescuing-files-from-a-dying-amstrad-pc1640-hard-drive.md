---
layout: post
title: Rescuing Files From a Dying Amstrad PC1640 Hard Drive
date: '2026-09-30 09:00:00'
summary: "When my Amstrad PC1640's original hard drive started throwing file allocation table errors, I needed its files off fast — over a null-modem cable, with Procomm's Kermit mode on the Amstrad side and TeraTerm on the PC."
tags: [Amstrad, MS-DOS, PC, Retrocomputing]
hero: amstrad-kermit-startech-usb-serial-adapter.jpg
hero_alt: My StarTech ICUSB2321F USB-to-serial adapter, used to rescue files off a dying Amstrad PC1640 hard drive
---

The [Amstrad PC1640]({% link _hardware/amstrad-pc1640.md %})'s original hard drive is 1980s-era MFM storage, and it started throwing file allocation table errors. I needed the files off before it died completely.

## Why serial

The obvious route was a straight drive-to-drive copy onto the CompactFlash card in my [Lo-tech XT-CF adapter]({% link _hardware/lo-tech-xt-cf.md %}). That wasn't possible: the XTIDE BIOS won't load while the original MFM controller card is connected, so only one of the two drives can be active at a time.

That left the PC1640's serial port. I already had a modern PC to receive the files, so it was just a matter of cabling the two together. A null modem cable, with a "Mini Gender Changer" adapter on one end, connected the Amstrad's serial port to a StarTech USB-to-serial adapter on the PC:

![The null modem cable, with the Mini Gender Changer adapter visible on one end](/img/amstrad-kermit-null-modem-cable.jpg)

## Procomm and Kermit

On the Amstrad side I ran **Procomm** (v2.4.2), a shareware terminal program that bundles several transfer protocols. I tried a few of them; only **Kermit** completed a transfer reliably.

![Procomm's startup screen, running on the Amstrad PC1640](/img/amstrad-procomm-splash-screen.jpg)

On the PC, **TeraTerm** handled the other end of the Kermit session — the same terminal program I use for [serial transfers on the Atari ST]({% link _howto/how-to-use-rs232-serial-cable-and-zmodem-to-transfer-files-from-pc-to-st.md %}).

## What came off

These directory listings are from the recovery session itself: old GEM and DOS files, a `KERMIT` folder, the `GEMBOOT`, `GEMAPPS` and `GEMDESK` directories, and, for some reason, `LEMMINGS`.

<div class="image-row">
  <img src="/img/amstrad-kermit-directory-listing-kermit-folder.jpg" alt="A directory listing on the PC1640 showing the KERMIT folder">
  <img src="/img/amstrad-kermit-directory-listing-gem.jpg" alt="A directory listing showing the GEM directories and a LEMMINGS folder">
</div>

With the files safely on the PC, the dying drive could be retired. Its replacement is a CompactFlash card on the XT-CF adapter, running [XTIDE Universal BIOS]({% link _software/xt-ide.md %}), which took its own run of failed attempts to get booting. That story is in [Getting XTIDE Working on the Amstrad PC1640]({% post_url 2026-09-04-getting-xtide-working-on-the-amstrad-pc1640 %}).

### Related on this site

- [Amstrad PC1640]({% link _hardware/amstrad-pc1640.md %})
- [Lo-tech XT-CF]({% link _hardware/lo-tech-xt-cf.md %})
- [XTIDE Universal BIOS]({% link _software/xt-ide.md %})
- [Getting XTIDE Working on the Amstrad PC1640]({% post_url 2026-09-04-getting-xtide-working-on-the-amstrad-pc1640 %})
- [Using Serial Cable and ZMODEM to Transfer Files from PC to ST]({% link _howto/how-to-use-rs232-serial-cable-and-zmodem-to-transfer-files-from-pc-to-st.md %})
