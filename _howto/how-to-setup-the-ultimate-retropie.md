---
layout: post
title: RetroPie Ultimate Setup Guide
date: '2018-10-08 11:54:00'
summary: With RetroPie, your Raspberry Pi can become the ultimate retro-gaming machine. Mega Drive, SNES, even PlayStation all run great and with a little extra work you can stream more taxing games from your home PC ...
image: emulationstation.jpg
tags: [How To, Posts, Raspberry Pi, Retrogaming, Single-Board Computing, Videogames]
---


<a name="Raspberry Pi Retrogaming">
## Raspberry Pi Retrogaming

Status | Completed October 2018
Goal | Build a cheap, small and light device to retrogame on the big screen

I'm a big fan of retro games, with many fond memories of the <a href="https://en.wikipedia.org/wiki/Third_generation_of_video_game_consoles" target="_blank">8-bit</a> and <a href="https://en.wikipedia.org/wiki/Fourth_generation_of_video_game_consoles" target="_blank">16-bit</a> years. Looking for a way to relive those memories on the big screen.

I selected the <a href="https://www.raspberrypi.org/" target="_blank">Raspberry Pi</a> and <a href="https://retropie.org.uk/" target="_blank">RetroPie</a> as the base for my build. After a week of on/off tweaking, I found optimal settings and documented the full setup [here]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}). For Phase 2, I [configured Moonlight Game Streaming]({% post_url 2018-11-17-gamestream-moonlight-on-retropie %}) to allow low latency streaming of more demanding titles from my gaming PC.

Overall very pleased with the result, and pleasantly surprised by how well Moonlight Game Streaming works.

Posts:

- [RetroPie Ultimate Setup Guide]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}) - 08 Oct 2018
- [Stream PC Games to your RetroPie with GameStream and Moonlight]({% post_url 2018-11-17-gamestream-moonlight-on-retropie %}) - 08 Oct 2018

<br />


![](/img/posts/retropie_logo.png)

With <a href="https://retropie.org.uk/" target="_blank">RetroPie</a>, your Raspberry Pi can become the ultimate retro-gaming machine. Mega Drive, SNES, even PlayStation all run great and with a little extra work you can stream more taxing games from your home PC

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

#### Step 1. Download RetroPie image and write to SD card

Some fairly simple first steps. Follow the official instructions <a href="https://retropie.org.uk/docs/First-Installation/" target="_blank">here</a>

#### Step 2. Enable SSH on your Pi
 
Create a file named `ssh` in the root directory of your SD Card. This way you can configure RetroPie from your networked PC, no keyboard required. Learn more [here]({% post_url 2017-01-02-raspberry-pi-headless-rasbian-install %})

![](/img/posts/create_ssh_file_on_sd_card.png)

With this feature enabled, you can use any <a href="https://en.wikipedia.org/wiki/Secure_Shell" target="_blank">SSH</a> client (I like <a href="https://www.putty.org/" target="_blank">PuTTY</a>) to remotely connect to your Pi. The default connection details are:

* Hostname: `retropie`
* Username: `pi`
* Password: `raspberry`

Alternatively, you can use a USB keyboard to configure Retropie directly

#### Step 3. Pair your Wireless Xbox 360 controller

If you have a Wireless Xbox 360 controller, you'll need to pair it with your Wireless Gaming Receiver before continuing. Find the instructions <a href="https://support.xbox.com/en-GB/xbox-on-windows/accessories/xbox-360-wireless-gaming-receiver-windows" target="_blank">here</a>

#### Step 4. Boot up your Pi and configure your controller

Switch on the power to your Raspberry Pi. After a minute or so, EmulationStation will launch and ask you to configure your controller:

![](/img/posts/gamepad_detected.png)

Go ahead and configure your controller as per the diagram below

<strong>An important note!</strong> EmulationStation follows the SNES button layout. So when configuring your Xbox 360 controller, you'll need to switch X with Y, and A with B. Yes, this is confusing - but don't worry there is a fix for this later 

![](/img/posts/xbox_360_controller_layout.png)

#### Step 5. Make a note of the RetroPie hotkeys

During controller configuration, you'll be asked to specify a "Hotkey". I recommend "Select" or the Xbox Guide button. Pressing this Hotkey in combination with other buttons  enables fast access to emulator features directly from your joypad. Make a note of these below:

Button Combo | Action
--- | ---
Hotkey+Start | Exit
Hotkey+Right Shoulder | Save
Hotkey+Left Shoulder | Load
Hotkey+Right | Input State Slot Increase
Hotkey+Left |Input State Slot Decrease
Hotkey+X | RGUI Menu
Hotkey+B | Reset

### Optimize controller settings

Now you're done with the initial RetroPie install, it's time to optimize the controller settings 

#### Step 1. Switch A and B buttons in EmulationStation

As mentioned above, the Xbox 360 controller differs from the SNES controller layout preferred by EmulationStation: notably the A and B buttons are reversed. The good news: EmulationStation has a setting to fix this:

1. In EmulationStation, head to `RetroPie > Configuration > RetroPie Setup`. This will launch a separate settings program
2. Navigate to `Manage packages > Manage core packages > emulationstation > Configurations/Options`, then enable `Swap A/B Buttons in ES`
3. Save changes and exit the settings program

#### Step 2. Enable analog sticks

Wouldn't it be great to use the 360 controller's analog sticks instead of that mushy d-pad? Here's how:

1. From the EmulationStation menu, navigate to `RetroPie > Configuration > Configuration Editor`. This will launch a separate settings program
2. Navigate to `Advanced Configuration > Configure Libretro options`
3. Select `all/retroarch.cfg`
4. Change the setting for `input_player1_analog_dpad_mode` to `1`. This will enable the left analog stick on your Xbox 360 controller
5. Navigate back to the main screen with `Cancel`. Save changes and exit the settings program

#### Step 3. (Re)configure input to enable your changes

You'll need to reconfigure input before EmulationStation and your emulators will pick up the changes above. In EmulationStation, press `Start` and choose `Configure Input`. This will take you through the same controller configuration wizard from earlier. As before, don't forget to switch X with Y, and A with B.

### Copy ROMs

#### Step 1. Copy some ROMs via SFTP

You've probably noticed the EmulationStation home screen is a little blank. Where are the NES, SNES and Mega Drive emulators? EmulationStation is smart: it won't show you any emulators or platforms unless you have ROMs to play on them. You need to transfer them first

I recommend <a href="https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol" target="_blank">SFTP</a> to transfer files. On Windows, I use FileZilla, but any SFTP client is good. Go to `File > Site Manager > New Site` and add the below:

* Host: `retropie`
* Protocol: `SFTP - SSH File Transfer Protocol`
* Logon Type: `Normal`
* User: `pi`
* Password: `raspberry`

The Site Manager should look like this:

![](/img/posts/filezilla-site-settings.png)

Hit `Connect` and navigate to the following directory: `/home/pi/RetroPie/roms`

You'll see lots of folders for each platform. Copy the ROMs into the corresponding folder for their platform. I recommend you copy zips (the file size adds up!) and to use the <a href="https://datomatic.no-intro.org/stuff/The%20Official%20No-Intro%20Convention%20(20071030).pdf" target="_blank">No Intro ROM naming convention</a> (if you use a naming convention, EmulationStation and any metadata scrapers can easily find and surface game metadata like descriptions, release dates, screenshots etc for your games)

![](/img/posts/filezilla-retropie-roms-folder.png)


#### Step 2. Restart EmulationStation to make ROMs appear

How do you make the ROMs and emulators show up? Hit the Start Button on your controller and navigate to `Quit > Restart EmulationStation`. After a brief moment you should see the following:

![](/img/posts/emulationstation.jpg)

Time to get playing!


### Add metadata

So everything works, but EmulationStation looks a bit plain. You want metadata and screenshots, right? Here's how

#### Step 1. Exit EmulationStation

We need to close EmulationStation down before we update the metadata as EmulationStation holds onto the metadata files. The scraper we're going to use won't even open if EmulationStation is running. So hit the Start button and navigate to `Quit > Quit EmulationStation`

#### Step 2. Install and Run Steven Selph's scraper

Either via SSH or with a USB keyboard attached to your pi, enter the following

{% highlight bash %}
{% raw %}
sudo ~/RetroPie-Setup/retropie_setup.sh
{% endraw %}
{% endhighlight %}

This will launch the RetroPie Setup script. Once it launches, navigate to `Manage Packages > Manage Optional Packages` and select `scraper` (right at the bottom for me)

Select `Install from source` to install the scraper. This will install Steven Selph's metadata scraper - one of the better ones out there. The install may take some time as it has to install various software libraries. 

Once the install completes, select `Scrape all systems`. Again, this will take some time as the scraper downloads game metadata and images from the web

Once the scrape completes, select `Cancel`, `Back` multiple times and eventually `Perform Reboot`. When EmulationStation reloads, you should now see pretty metadata for your ROMs!

![](/img/posts/emulationstation-scraped-data.png)

#### Step 3. Fix broken metadata

The scraper won't pick up everything. Especially for obscure Japanese titles and ROM hacks, you'll need to add your own metadata and artwork

You can do this by editing the `gamelist.xml` file located in `~/​.emulationstation/​gamelists/​[SYSTEM_NAME]/​gamelist.xml`. In the XML file, each game has an entry like so:

{% highlight xml %}
{% raw %}
<game>
  <path>./10-Yard Fight (USA, Europe).nes</path>
    <name>10-Yard Fight</name>
    <desc>You're the quarterback in this amazingly real football game! Enjoy realistic gridiron action as you move your team up and down the field to victory! Run, pass, kick, punt... you call the plays in this true-to-life football game. Play against the computer or against a friend for hours of real football action. The sights, the sounds and the plays are so real you'll think you're right on the fifty yard line!</desc>
    <image>~/.emulationstation/downloaded_images/nes/10-Yard Fight (USA, Europe)-image.jpg</image>
    <releasedate>19851001T000000</releasedate>
    <publisher>Nintendo</publisher>
    <genre>Sports</genre>
    <developer>Irem</developer>
    <players>2</players>
</game>
{% endraw %}
{% endhighlight %}

Just edit the XML file as needed. Use SFTP to upload images to your Pi which you can then reference in the XML. The default (and best) location is `~/​.emulationstation/​downloaded_images/​[SYSTEM_NAME]/`

### Adjust screen border

Perhaps you're using a monitor or TV in "Just Scan" or "Pixel Perfect" mode and see black borders around the EmulationStation menu and all your games? You can fix this with some Pi settings

#### Step 1. Update boot config to disable overscan

Exit EmulationStation and enter the following from the command line:

{% highlight bash %}
{% raw %}
sudo nano /boot/config.txt
{% endraw %}
{% endhighlight %}

This will load the nano text editor. Uncomment the line `#disable_overscan=1` so that it becomes `disable_overscan=1`

Press Ctrl+X to Exit and Y to save (this is a common pattern for RetroPie)

#### Step 2. Reboot Pi to see the new settings

Reboot the pi with the following command:

{% highlight bash %}
{% raw %}
sudo reboot
{% endraw %}
{% endhighlight %}

Once the Pi restarts, the border should be gone! There are a bunch of controls to optimize overscan and borders in a more granular way. For more info see the <a href="https://www.raspberrypi.org/documentation/configuration/config-txt/video.md" target="_blank">official Raspberry Pi Video Options documentation</a>

That's it! If you want to play some more demanding games you can [setup Game Streaming]({% post_url 2018-11-17-gamestream-moonlight-on-retropie %}). Otherwise enjoy your RetroPie!