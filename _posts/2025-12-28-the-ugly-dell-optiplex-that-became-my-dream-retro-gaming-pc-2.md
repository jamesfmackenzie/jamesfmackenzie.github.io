--- 
layout: post
title: "Reviving an ASUS EeeTop as a Linux Kitchen PC"
date: '2026-01-05 10:04:00:00'
summary: |-
  A practical step-by-step guide to turning an old ASUS EeeTop Atom touchscreen PC into a modern Linux kitchen calendar and email kiosk, covering legacy BIOS installs, GRUB fixes, touchscreen drivers, and networking quirks.
tags: [Computers, PC, Posts, Retrocomputing]
---

*A practical guide to legacy hardware, touchscreens, and patience*

> **TL;DR**  
> I turned an old ASUS EeeTop Atom touchscreen PC into a fast, reliable kitchen calendar and email display using Linux Mint XFCE.  
> The key challenges were legacy BIOS booting, GRUB installation, touchscreen drivers, and Wi-Fi quirks — all of which are solvable with the right (boring) configuration.

—

### Hardware overview

![ASUS EeeTop on the workbench](images/eetop-workbench.jpg)

*The ASUS EeeTop all-in-one PC before refurbishment.*

My EeeTop has:

- Intel Atom D510 (dual-core, 64-bit capable)
- Legacy BIOS (no UEFI support)
- Integrated NVIDIA ION graphics
- Built-in NextWindow touchscreen
- Internal Atheros Wi-Fi
- 2.5” SATA hard drive (replaced)

#### Essential upgrades

![SSD and RAM upgrade](images/ssd-ram-upgrade.jpg)
*Replacing the original hard drive with an SSD and upgrading the RAM.*

Before touching software, I strongly recommend:

- **Replace the HDD with an SSD**
- **Max out the RAM** (cheap and very effective)

This alone makes the system feel *dramatically* more responsive.

—

### OS choice

I chose **Linux Mint XFCE** because it is:

- Lightweight
- Stable
- Conservative
- Well documented
- Familiar to anyone who has used Windows

XFCE also performs well on Atom CPUs and doesn’t insist on GPU acceleration.

—

### Step 1: BIOS configuration (important)

Enter the BIOS (usually `F2`) and ensure:

- Boot mode: **Legacy / CSM**
- UEFI: **Disabled**
- Secure Boot: **Disabled**
- SATA mode: **AHCI**
- Legacy USB support: **Enabled**

Save and exit.

—

### Step 2: Booting the installer (graphics quirks)

![Linux Mint boot screen](images/mint-boot-screen.jpg)
*Linux Mint installer booting in compatibility mode.*

On this hardware, the installer may hang on a black screen with white squares.

If that happens:
- Boot the Linux Mint DVD
- Choose **Compatibility Mode**, *or*
- Edit the boot entry and add the following kernel parameter:

```
nomodeset
```

If the system still hangs, **unplug the Ethernet cable** during boot.  
Surprisingly, this can avoid early boot deadlocks on older Atom systems.

—

### Step 3: Correct disk partitioning (legacy BIOS!)

This is where most people go wrong.

#### Open GParted *before* installing

```
Menu → Administration → GParted
```

![GParted with msdos partition table](images/gparted-msdos.jpg)
*Using an msdos (MBR) partition table instead of GPT.*

#### Create a new partition table
- Device → Create Partition Table
- Choose: **msdos**

⚠️ Do **not** use GPT  
⚠️ Do **not** create an EFI partition  

#### Create a single partition
- Primary
- ext4
- Use the full disk

You should end up with:

```
/dev/sda1  ext4
```

—

### Step 4: Install Linux Mint

Start the installer and when asked about installation type:

- Choose **“Something else”**

Assign:
- `/dev/sda1` → mount point `/` → format enabled

#### Bootloader location (critical)

```
Install bootloader to: /dev/sda
```

Not `/dev/sda1`.

You may see a warning about **no EFI partition** — this is **normal and safe to ignore** on legacy BIOS systems.

—

### Step 5: Fixing GRUB if the installer fails

![GRUB error during install](images/grub-error.jpg)
*A GRUB installation failure — common on legacy systems.*

If the installer reports a GRUB error:

```
sudo mount /dev/sda1 /mnt
sudo mount —bind /dev /mnt/dev
sudo mount —bind /proc /mnt/proc
sudo mount —bind /sys /mnt/sys
sudo chroot /mnt
```

Then install legacy GRUB explicitly:

```
grub-install —target=i386-pc /dev/sda
update-grub
```

Exit, unmount, and reboot.  
After this, the system should boot cleanly from disk.

—

### Step 6: Networking quirks

#### Ethernet
I found Ethernet worked best if:
- The cable was unplugged during boot
- Plugged in **after login**

Once the system is running, it’s stable.

#### Wi-Fi (USB adapter)

![USB Wi-Fi adapter](images/usb-wifi.jpg)
*Using a USB Wi-Fi adapter instead of the internal card.*

The internal Atheros Wi-Fi reports a **phantom hardware kill switch**, which disables all Wi-Fi globally.

The clean solution:

```
echo “blacklist ath9k” | sudo tee /etc/modprobe.d/blacklist-ath9k.conf
sudo update-initramfs -u
```

After reboot, the USB Wi-Fi adapter works normally.

—

### Step 7: Touchscreen support (NextWindow)

![Touchscreen calibration](images/touch-calibration.jpg)
*Calibrating the built-in touchscreen.*

The built-in touchscreen uses a **NextWindow controller**, which modern kernels don’t handle particularly well out of the box.

I used the community-maintained **nwfermi** driver, which improves touch behaviour — but it is an **out-of-tree kernel module** and can be fragile.

**Lessons learned:**
- A bad boot can temporarily kill all input devices
- Rebooting may fix it
- Always keep a GRUB menu timeout so you can recover

—

### Step 8: Software choices

#### Browser
- **Chromium**
- Launched in kiosk mode
- Keyring disabled using:

```
—password-store=basic
```

#### Email & calendar

![Thunderbird calendar view](images/thunderbird-calendar.jpg)
*Thunderbird used as a full-screen calendar display.*

- **Thunderbird**
- Built-in calendar view
- Works well with Microsoft 365 via IMAP + CalDAV
- Can start directly in calendar mode:

```
thunderbird -calendar
```

—

### Step 9: Kiosk behaviour

To make the system feel like an appliance:

- Enable auto-login
- Disable screen blanking and sleep
- Autostart Chromium or Thunderbird
- Increase font sizes for touch readability
- Disable unnecessary desktop UI elements

—

### The end result

![Finished kitchen PC](images/kitchen-pc-finished.jpg)
*The finished kitchen PC in daily use.*

The finished system:

- Boots reliably from SSD
- Supports touch input
- Has wired and wireless networking
- Displays a large, readable family calendar
- Allows light email interaction
- Feels purpose-built rather than “an old PC”

Most importantly, it’s **pleasant to use**, which is the real success metric for a kitchen device.

—

### Final thoughts

This project was a reminder that:

- Legacy hardware is still very usable
- Modern Linux defaults don’t always suit old machines
- Explicit, boring configurations are often best
- Touchscreens on Linux still require patience
- Reusing old hardware can be genuinely rewarding

What started as a slow, obsolete Windows machine is now a **useful, always-on household appliance** — and that feels like a good outcome.