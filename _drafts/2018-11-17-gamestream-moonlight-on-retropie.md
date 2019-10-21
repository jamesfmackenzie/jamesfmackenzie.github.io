---
layout: post
title: Stream PC Games to RetroPie
date: '2018-10-08 11:54:00'
tags: [How To, Videogames, Raspberry Pi, Retrogaming, Streaming]
---

You already have [RetroPie running nicely on your Raspberry Pi]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}). It's the perfect retrogaming experience for your living room TV, but there's one thing missing. The Pi doesn't have the horsepower for more recent games. How can you play the latest PC releases? Or perhaps you fancy some PlayStation 2, Gamecube or Dreamcast emulation on the big screen?

<a href="https://moonlight-stream.com/" target="_blank">Moonlight</a> fits the bill. It streams gameplay from your almighty PC to the RetroPie, allowing you to sit back on the couch and play games that need a bit more grunt

Here's how to get it setup!

### What you need 

* <a href="https://www.raspberrypi.org/" target="_blank">Raspberry Pi</a> with [RetroPie installed]({% post_url 2018-10-08-ultimate-retropie-setup-guide %}). For best performance use a Raspberry Pi 3 Model B+
* Wi-Fi connection or (for best streaming performance) Ethernet cable 
* USB keyboard. To edit config files on your Raspberry Pi. Alternatively you can do this from your networked PC via SSH. Find more details in [this RetroPie guide]({% post_url 2018-10-08-ultimate-retropie-setup-guide %})
* A gaming PC with NVIDIA GeForce GTX/RTX 600+ series GPU (GT-series and AMD GPUs aren't supported by NVIDIA GameStream) and <a href="https://www.nvidia.com/en-us/geforce/geforce-experience/" target="_blank">NVIDIA GeForce Experience (GFE)</a> 2.1.1 or higher installed

### Install Moonlight on your Pi

On your Pi:

1. Quit Emulation Station (hit the Start button and navigate to `Quit > Quit EmulationStation`)

2. Update sources file

From the bash prompt, type `sudo nano /etc/apt/sources.list`. This will launch the nano text editor. Add the following line at the bottom of the file:

{% highlight bash %}
{% raw %}
deb http://archive.itimmer.nl/raspbian/moonlight stretch main
{% endraw %}
{% endhighlight %}

Make sure there is a carriage return below at the bottom of the file. Then hit Ctrl+X then Y to save and exit

3. Install GPG key

Still at the bash prompt, enter the following to fetch and install the GPG key for Moonlight:

{% highlight bash %}
{% raw %}
wget http://archive.itimmer.nl/itimmer.gpg
sudo apt-key add itimmer.gpg
{% endraw %}
{% endhighlight %}

4. Install Moonlight

We'll use apt-get to install Moonlight. Enter the following:

{% highlight bash %}
{% raw %}
sudo apt-get update
sudo apt-get install moonlight-embedded
{% endraw %}
{% endhighlight %}

This should install Moonlight globally. In case anything goes wrong, you can find extra troubleshooting steps <a href="https://github.com/irtimmer/moonlight-embedded/wiki/Packages" target="_blank">here</a>

### Connect Moonlight to your PC 

1. Run the following command to pair Moonlight with your PC

{% highlight bash %}
{% raw %}
moonlight pair <your PC IP address or hostname>
{% endraw %}
{% endhighlight %}

For example:

{% highlight bash %}
{% raw %}
moonlight pair homePC
{% endraw %}
{% endhighlight %}

You'll be asked to enter key on your host PC. Enter that once and the RetroPie is paired forever

2. Optimize controller settings

If you're using an Xbox 360 controller on the Pi, we need to manually change some controller settings. The xpad driver that RetroPie uses leads to weird effects in moonlight

Type the following in bash:

{% highlight bash %}
{% raw %}
sudo rmmod xpad
sudo modprobe xpad triggers_to_buttons=0
{% endraw %}
{% endhighlight %}

This (temporarily) unloads the xpad driver and disables the "triggers to buttons" feature - allowing you to use triggers properly when you stream games via Moonlight. We'll need to revert this setting or reboot before we use Emulation Station again, since this setting will break retro gaming. Later on we'll create a script to help here. Find more info on this issue <a href="https://www.reddit.com/r/RetroPie/comments/7m10x8/disabling_trigger_to_button/" target="_blank">here</a>

3. Run a test stream

Enter the following:

{% highlight bash %}
{% raw %}
moonlight stream -1080 -fps 60 -app "<name of a game to stream from GeForce Experience>" <your PC IP address or hostname>
{% endraw %}
{% endhighlight %}

For example:

{% highlight bash %}
{% raw %}
moonlight stream -1080 -fps 60 -app "Forza Motorsport 6 Apex" homePC
{% endraw %}
{% endhighlight %}

All going well, the game should launch at 1080p, 60fps and be playable on your Pi! Great success!

If you have a slower Pi model, you may experience some lag when streaming at 1080p, 60fps. You can either lower the resolution or overclock your Pi:

{% highlight bash %}
{% raw %}
sudo nano /boot/config.txt
{% endraw %}
{% endhighlight %}

This will open a text editor. Add the following at the bottom of the file:

{% highlight bash %}
{% raw %}
# To enable smooth 1080p60 gameplay in Moonlight
force_turbo=1
h264_freq=333
{% endraw %}
{% endhighlight %}

Press Ctrl+X then Y to save and exit, the enter the following to reboot your Pi and apply the change:

{% highlight bash %}
{% raw %}
sudo reboot
{% endraw %}
{% endhighlight %}

Your streaming experience should now be lag free

### Integrate with EmulationStation

We've proved the Moonlight works well on the Pi, but we'd much prefer to launch and stream games directly through the RetroPie EmulationStation interface. Luckily EmulationStation is very configurable. We can do this without too much hassle.

1. Quit EmulationStation if it is open (hit the Start button and navigate to `Quit > Quit EmulationStation`)

-------------- this is where I got to

1. Create a copy of the ES config (the default one gets overwritten during ES updates and you don't want that)

sudo cp /etc/emulationstation/es_systems.cfg /opt/retropie/configs/all/emulationstation/es_systems.cfg

2. Add a system to the custom config:

sudo nano /opt/retropie/configs/all/emulationstation/es_systems.cfg

Add this at the bottom, but before </systemList>:

  <system>
    <name>Moonlight</name>
    <path>~/RetroPie/roms/moonlight</path>
    <extension>.txt .TXT</extension>
    <command>/opt/retropie/supplementary/runcommand/runcommand.sh 0 _SYS_ moonlight %ROM%</command>
    <theme>Moonlight</theme>
  </system>

More info: https://github.com/RetroPie/RetroPie-Setup/wiki/Add-a-New-System-in-EmulationStation

I can add a new theme too if I like but maybe that's overkill

3. Create a roms directory for your moonlight links:

cd /home/pi/RetroPie/roms
mkdir moonlight
cd moonlight
touch MYGAMENAME.txt (should match the game name from Gamestream on your PC)

4. Create a config directory for moonlight:

cd /opt/retropie/configs
mkdir moonlight
cd moonlight
sudo nano emulators.cfg
put one line in the file:

moonlight = "moonlight stream -1080 -fps 60 -app %BASENAME% desktop"
default = "moonlight"

4. Create startup script for moonlight games:

cd /opt/retropie/configs/all

sudo nano runcommand-onstart.sh

# Set joypad to support triggers when loading Moonlight games
if [ $1 = "moonlight" ]; then
   sudo rmmod xpad
   sudo modprobe xpad triggers_to_buttons=0
fi

sudo nano runcommand-onend.sh

# Revert joypad to regular settings and terminate Moonlight stream
if [ $1 = "moonlight" ]; then
   sudo rmmod xpad
   sudo modprobe xpad triggers_to_buttons=1
   moonlight quit YOURPCNAME
fi

	5. Create a theme for moonlight so it looks nice in the UI

First I’ll need to Quit EmulationStation because it holds onto xml files and whatnot that you’ll need to edit

Second create a copy of the default “carbon” theme - you don’t want to break it. Could call it “carbon-updated” or “carbon-copy” Ho Ho Ho. The location is  /etc/EmulationStation/themes

After that follow this guide to add the new system along with art:

https://github.com/retropie/retropie-setup/wiki/Creating-Your-Own-EmulationStation-Theme




----- HOW DO I ADD CUSTOM GAMES?

How to add UWP games?

	- Some apps are already “onboarded” and will magically appear
	- Others must be added via the GameStream UI. It now has native support for UWP. 
	- This has to be done on the console (i.e. not via RDP. What a pain)
	- Manually added apps will dump you back at the desktop. You should write a batch file wrapper to manage this. See:

https://forums.geforce.com/default/topic/876150/gamestream/on-game-exit-game-stream-back-ground-stays-active-and-connection-does-not-close/




HELP! THE CONTROLLER DOESN’T WORK EVERY NOW AND THEN

There seems to be a funky issue with moonlight embedded where controller input doesn't work in the target game every now and then. You'll need to quit the stream (select + start + L1 + R1) and try again



HELP! I GET A BLACK SCREEN WHEN STREAMING

(Sound but no gameplay)
This happened very occasionally. It seems like connecting to the server with another moonlight client (e.g. PC or phone) will fix the issue. Raise this bug with the moonlight embedded team



MOONLIGHT STUTTERS ON MY IPHONE!?

Moonlight works much smoother on modern Apple devices (iPhone X, new iPad) vs old ones. Suspect that the processor on the old devices can not cope with 60fps decoding requirements

More info:
 
1080p60 is very stuttery on my iPhone 6S and not at all on the Raspberry Pi.

It also (after a very brief test) seems fine on my (more powerful) iPad 

Try at 720p60 instead to see if it fixes the issue. <it does not!>

So I likely have hit a performance ceiling with H264 decoding on my phone 

Another thing I could try is Lil’s iPhone X and retry the iPad to be sure it’s better <confirmed. The iPhone X and new iPad are much better in this respect>


CAN I STREAM THE XBOX APP FROM MY PC TO PLAY XBOX ONE GAMES VIA A “DOUBLE HOP”?

Yes you can and it works surprisingly well

Although it’s better to do this via a single hop (i.e. direct to a Windows 10 machine or a Mac/iOS device via OneCast)





LEGACY NOTES BELOW HERE


RetroPie setup

What you need

(copied from https://retropie.org.uk/docs/First-Installation/)
	- Raspberry Pi (A, A+, B, B+, 2, Zero, or 3) - for best performance use a Raspberry Pi 3 Model B+
	- Raspberry Pi Case (optional but recommended)
	- MicroSD Card (see compatible SD card list here)
	- MicroSD Card Reader (For installing retropie from your computer)
	- HDMI cable or 4 Pole RCA to 3.5mm Cable (HDMI works best)
	- Television or Computer Monitor- really any screen with HDMI or RCA ports
	- Wifi Dongle or Ethernet Cable (Wifi is built into the Pi 3- see wifi dongle compatible list here)
	- 5V 2A Micro USB Power Supply (2.5A for pi 3)
	- USB Keyboard and Mouse (to get things set up or you can use SSH)
	- USB Game Controller of your choice (or you can get the Control Block to use original SNES controllers)

(My own list)
	- Raspberry Pi 2 or 3
	- 8GB MicroSD card
	- USB controller (wired Xbox 360 or Xbox 360 wireless receiver preferred)
	- Gamestream compatible PC (i.e. with Nvidia GeForce GTX 650 or greater)
	- Ethernet connection (wired preferred)
	- USB keyboard

(GFE compatible requirements)
• GFE compatible computer with GTX 600/700/900/1000 series GPU (for the PC you're streaming from)
• High-end wireless router (802.11n dual-band recommended) or wired network
• Geforce Experience 2.1.1 or higher

From <https://github.com/irtimmer/moonlight-embedded> 



Get PC ready

	1. Install GeForce experience, turn on GameStream and leave PC sitting on the desktop, unlocked

Pro-tip: use RDP and then use a special bath file to push the RDP session to the console



Install RetroPie 

	1. Setup RetroPie stretch according to the usual instructions (see https://retropie.org.uk/docs/First-Installation/)



Setup moonlight

	1. On initial boot of RetroPie, press F4 to drop to the console

	1. Install moonlight embedded stretch according to the instructions here (I should copy these for myself into the document)
https://github.com/irtimmer/moonlight-embedded/wiki/Usage

	1. Pair with your PC

moonlight pair YOURPCIPADDRESS (does this work with hostnames? Should right? I don't need static IP? Test this)

	1. Test the moonlight stream

moonlight -1080 -fps 60 -app "Forza Motorsport 6 Apex"

Note: If you have issues with lag streaming at 1080p60, there are two solutions:

	- Overclock the Pi

In /boot/config.txt:

force_turbo=1
h264_freq=333

More info: https://github.com/irtimmer/moonlight-embedded/issues/398

	- Rollback to an old Firmware revision

sudo rpi-update e0db6ba 

More info: https://github.com/irtimmer/moonlight-embedded/issues/645


Enable SSH

See https://github.com/RetroPie/RetroPie-Setup/wiki/SSH

I actually did this instead: https://www.raspberrypi.org/forums/viewtopic.php?t=144839


Configure controller

Most controllers will be auto configured by moonlight. But there are some caveats 

Note: if you are using the Xbox 360 wireless receiver the buttons may be all wrong. You need to change use triggers as buttons in a magic config file (find it)

Note: if your controller jumps all over the place turn off Steam (it confgures he right stick of your controller to act as a mouse and other strange things)


Configure EmulationStation

Now you have streaming all working, you need to integrate it with EmulationStation. Borrow some of the instructions from below:

https://www.instructables.com/id/How-to-Setup-RetroPie-With-Moonlight-Steam-Streami/

Note: by default moonlight will launch steam. You have to specify the “app” parameter to launch a specific game

To make the theme look nice I will need to do some custom setup. See https://github.com/RetroPie/RetroPie-Setup/wiki/Add-a-New-System-in-EmulationStation
	
I can also add cool box art like this:
https://www.reddit.com/r/RetroPie/comments/3n032p/how_can_i_manually_add_cover_art_to_my_games/


PC setup

How to add UWP games?

	- Some apps are already “onboarded” and will magically appear
	- Others must be added via the GameStream UI. It now has native support for UWP. 
	- This has to be done on the console (i.e. not via RDP. What a pain)
	- Manually added apps will dump you back at the desktop. You should write a batch file wrapper to manage this. See:
https://forums.geforce.com/default/topic/876150/gamestream/on-game-exit-game-stream-back-ground-stays-active-and-connection-does-not-close/
	

Issues to watch out for

- "Under voltage" issues. If you're having problems purchase an official raspberry pi power supply
- Sound issues. This seems to stutter. Keep an eye out for it, see how it goes



Other notes

	1. Seems like I just need to follow the standard guide to install retropie. Xbox Wireless receiver works out of the box
 
	1. Once I have that working, follow these guides to install moonlight. Configure it to Stream Forza APEX edition to start (and then I can go from there with Dolphin and other things)



	1. Install some more PC games

Alto's Adventure
Asphalt 8: Airbone
Asphalt 9: Legends
Black Mesa
Dolphin (and some gamecube games)
PCSX 2 (and some PS2 games)
Forza Motorsport 6: Apex
Halo: Spartan Assault
Kentucky Route Zero
Minecraft: Windows 10 Edition
The Stanley Parable

	1. Install some other emulators and things natively on the Pi

Emulators should be already installed. ROMS just need to be added. See https://retropie.org.uk/docs/First-Installation/






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
