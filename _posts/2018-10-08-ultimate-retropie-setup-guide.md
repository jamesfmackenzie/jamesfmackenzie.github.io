---
layout: post
title: RetroPie Ultimate Setup Guide
date: '2018-10-08 11:54:00'
tags: [How To, Videogames, Raspberry Pi, Retrogaming, Streaming]
---

With <a href="https://retropie.org.uk/" target="_blank">RetroPie</a>, your Raspberry Pi can become the ultimate retro-gaming machine. Mega Drive, SNES and even PlayStation all run great - and (with a little extra work) you can even stream more taxing games from your home PC

Interested and want to get started? Read on

### What you need 

* <a href="https://www.raspberrypi.org/" target="_blank">Raspberry Pi</a> and a <a href="https://www.raspberrypi.org/documentation/hardware/raspberrypi/power/README.md" target="_blank">compatible power supply</a>. For best performance use a Raspberry Pi 3 Model B+
* Raspberry Pi case. Optional but recommended. I use <a href="http://amzn.eu/d/7mWFf5S" target="_blank">this one</a>
* MicroSD card. At least 8GB recommended. Find compatible cards listed <a href="https://www.raspberrypi.org/documentation/installation/sd-cards.md" target="_blank">here</a>
* MicroSD card reader. To write the downloaded RetroPie image to your SD card
* Television/monitor and HDMI cable
* Wi-Fi dongle or (for best streaming performance) Ethernet cable 
* <a href="http://amzn.eu/d/dagIzPm" target="_blank">Wired Xbox 360 controller</a>, or a <a href="http://amzn.eu/d/j070KCH" target="_blank">Wireless Xbox 360 controller</a> paired with a <a href="http://amzn.eu/d/dnOt76e" target="_blank">Wireless Gaming Receiver</a>. Many other controllers are supported, but the Xbox 360 controllers work best
* USB keyboard. To edit config files on your Raspberry Pi. Alternatively you can do this from your networked PC via SSH. More details below

### Install RetroPie

#### 1. Download RetroPie image and write to SD card

You can find official instructions <a href="https://retropie.org.uk/docs/First-Installation/" target="_blank">here</a>

### 2. Enable SSH on your Pi
 
Create a file named `ssh` in the root directory of your SD Card. This way you can configure RetroPie from your networked PC - no USB keyboard required. Find more information [here]({% post_url 2017-01-02-raspberry-pi-headless-rasbian-install %})

#### 3. Pair your controller

(if you have a wireless one). Find some existing instructions for this online and link here

#### 4. Turn on your RetroPie and configure your controller

On first boot, you'll be asked to configure your controller. RetroPie will automatically recognize wireless and wired Xbox 360 controllers and a few other varieties.

When setting up the controller, SNES layout is used. For the 360 controller, this means you should reverse around X and Y, A and B!

(insert screenshots from RetroPie wiki here)

#### 5. Make a note of the RetroPie hotkeys

These will enable you quickly access emulator features from your joypad:

Hotkeys | Action
--- | ---
Select+Start | Exit
Select+Right Shoulder | Save
Select+Left Shoulder | Load
Select+Right | Input State Slot Increase
Select+Left |Input State Slot Decrease
Select+X | RGUI Menu
Select+B | Reset

### Optimize controller settings

#### 1. Fix the "A and B" controller issue 

Since the 360 controller has A and B reversed vs a SNES controller, the Emulation Station will be extra confusing! Prompting you to press A when it means B and vice versa.

You can fix this via the following config:

Configuration -> RetroPie Setup -> Manage packages > Manage core packages > emulationstation > Configurations/Options > Swap A/B Buttons in ES

#### 2. Enable analog sticks

Wouldn't it be great to use the 360 controller's analog sticks instead of that mushy d-pad? Well you can!

In the EmulationStation menu:

RetroPie -> Configuration -> Configuration Editor
Advanced Configuration
Configure Libretro options
all/retroarch.cfg
input_player1_analog_dpad_mode = 1
Cancel -> Cancel -> Cancel -> Cancel

#### 3. (Re)configure input to enable your changes

You'll need to reconfigure input before EmulationStation and your emulators will pick up the changes above. Go to:

Start -> Configure Input

As before, don't forget to reverse around A and B, X and Y

### Copy ROMs

#### 1. Copy some ROMs via SFTP

You've probably noticed nothing shows up, right? EmulationStation is smart. It won't show you any emulators or platforms unless you have ROMs to play on them.

I recommend SFTP to transfer files. 

On Windows, I use FileZilla, but any SFTP client is good. Go to "Site", "Add new Site" and add the following:

[screenshot of SFTP config in FileZilla)

Then connect and navigate to the following directory: `/home/pi/RetroPie/roms`

You'll see lots of folders for each platform. Copy the ROMs into the corresponding folder for their platform. I recommend you copy zips (the file size adds up!) and to use the No Intro naming convention (which EmulationStation and any metadata scrapers understand and will present to you appropriately)

#### 2. Restart Emulation Station to make ROMs appear

How do you make the ROMs and emulators show up? Start -> Quit -> Restart Emulation Station

Now you should see the following:

[insert screenshot of EmulationStation with emulators)

Time to get playing!


### Add metadata

So everything works, but EmulationStation looks a bit plain. You want metadata and screenshots, right? Here's how

#### 1. Exit EmulationStation

We need to close Emulation Station down before we update the metadata as EmulationStation holds on to the metadata files. The scraper we're going to use won't even open if EmulationStation is running. So:

Start -> Quit -> Quit Emulation Station

#### 2. Install Steven Selph's scraper

Either via SSH or a USB keyboard attached to your pi, enter the following

```bash
sudo ~/RetroPie-Setup/retropie_setup.sh
```

Once this launches, navigate to:
Manage Packages -> Manage Optional Packages -> scraper (right at the bottom for me)
Install from source
Back -> Back -> Back -> Exit

This will install Steven Selph's metadta scraper - one of the better ones out there

Once that's installed, select "Scrape all systems" (under 
Manage Packages -> Manage Optional Packages -> scraper
Configuration / Options)

Once this completes successfully, select 
Cancel -> Back -> Back -> Back -> Perform Reboot

Once EmulationStation reloads, you should now see pretty metadata for your ROMs!

### Fix broken metadata

TODO - this needs to be improved

The scraper won't pick up everything. For the items that are't picked up, you can upload box art and correct the metadata manually. See https://www.reddit.com/r/RetroPie/comments/3n032p/how_can_i_manually_add_cover_art_to_my_games/?st=JMZ6CWQ2&sh=e4020b34

If you use the built in ES Scraper your gamelist.xml and images folder will be in ~/.emulationstation/gamelists/[SYSTEM_NAME]/gamelist.xml

If you use Sselph's Scraper you can choose whether your scraped data goes in:

* [SYSTEM_PATH]/gamelist.xml (the rom folder) or
* ~/.emulationstation/gamelists/[SYSTEM_NAME]/gamelist.xml

### Adjust screen border

Perhaps you're using a monitor or TV in "Just Scan" or "Pixel Perfect" mode and see black borders around the EmulationStation menu and all your games? You can fix this with some Pi settings

#### 1. Update boot config to disable overscan

Exit EmulationStation and enter the following from the command line:

sudo nano /boot/config.txt

This will load the nano text editor. 

uncomment the line 
#disable_overscan=1

So that it becomes
disable_overscan=1

Press Ctrl+X to Exit and Y to save (this is a common pattern for RetroPie)

#### 2. Reboot Pi to see the new settings

Reboot the pi with the following command:

sudo reboot

Once the Pi restarts, the border should be gone! There are a bunch of controls to optimize overscan and borders in a more granular way. Add a link here
