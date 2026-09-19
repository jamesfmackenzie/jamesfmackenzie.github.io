---
layout: post
title: "How to Install Half-Life 2 on Raspberry Pi"
date: '2024-10-27 08:35:00:00'
summary: How to build and install Half-Life 2 on a Raspberry Pi — an ARM64-native build with zero emulation overhead.
hero: pi5-half-life-2-stock-cooler.jpg
hero_alt: My Raspberry Pi 5 running Half-Life 2
tags: [How To, Raspberry Pi, Retrogaming, Videogames]
---

Here's how to build and run Half-Life 2 natively on a Raspberry Pi. This is an ARM64-native version of the game, giving the best possible performance with zero emulation overhead.


### What You Need

To get started you need:

* A Raspberry Pi (Pi 5 is best) with Ubuntu installed
* A copy of Half-Life 2 (e.g. from Steam)


### Step 1. Install Build Tools

Open up the Ubuntu terminal and type the following to install the necessary build tools:

{% highlight bash %}
{% raw %}
sudo apt-get install build-essential gcc-multilib g++-multilib pkg-config ccache
{% endraw %}
{% endhighlight %}


### Step 2. Install Dev Libraries

Next, add the dev libraries:

{% highlight bash %}
{% raw %}
sudo apt-get install libsdl2-dev libfontconfig1-dev libopenal-dev libjpeg-dev libpng-dev libcurl4-gnutls-dev libbz2-dev libedit-dev
{% endraw %}
{% endhighlight %}


### Step 3. Download Source Engine Code

Run the following command to download the Source Engine source code:

{% highlight bash %}
{% raw %}
cd ~/Downloads
git clone https://github.com/nillerusr/source-engine.git --recursive
{% endraw %}
{% endhighlight %}

Then navigate to the downloaded files with <code>cd source-engine</code>.


### Step 4. Configure the Build

Type the following to configure your Source Engine build for Half-Life 2:

{% highlight bash %}
{% raw %}
python3 ./waf configure -T release --prefix=hl2 --build-games=hl2 --disable-warns
{% endraw %}
{% endhighlight %}

You can also configure with different parameters to build other Source Engine games (see "Other Source Engine Games" below).


### Step 5. Build Half-Life 2

With that done, build Half-Life 2 with:

{% highlight bash %}
{% raw %}
python3 ./waf build -p -v 
{% endraw %}
{% endhighlight %}

This will take some time on the Pi’s power-sipping CPU. Be prepared to wait!


### Step 6. Install Binaries

Once the build is done, run the following to install Half-Life 2 to the <code>hl2</code> directory:

{% highlight bash %}
{% raw %}
python3 ./waf install
{% endraw %}
{% endhighlight %}

You should now have an <code>hl2</code> folder with the <code>hl2-launcher</code> executable inside. Navigate and check this with:

{% highlight bash %}
{% raw %}
cd hl2
ls
{% endraw %}
{% endhighlight %}


### Step 7. Download Game Assets

Last but not least, download the Half-Life 2 game assets to the Pi.

This uses <a href="https://github.com/SteamRE/DepotDownloader" target="_blank">DepotDownloader</a>. First, download and extract it:

{% highlight bash %}
{% raw %}
cd ~/Downloads
wget https://github.com/SteamRE/DepotDownloader/releases/download/DepotDownloader_2.7.4/DepotDownloader-linux-arm64.zip
unzip DepotDownloader-linux-arm64.zip
{% endraw %}
{% endhighlight %}

Next, use the following command to download Half-Life 2. You'll need a Steam account with a purchased copy of the game:

{% highlight bash %}
{% raw %}
./DepotDownloader -app 220 -depot 221 -manifest 3666218991449795038 -username <steam_username>
{% endraw %}
{% endhighlight %}

This will download the Half-Life 2 games files to the <code>depots</code> directory.


### Step 8. Copy Game Assets

With the game files downloaded, copy them to your <code>source-engine</code> folder:

* Copy the <code>depots/221/16557524/hl2</code> folder to <code>source-engine/hl2</code>
* Copy the <code>depots/221/16557524/platform</code> folder to <code>source-engine/hl2</code>

You might be prompted to merge files. Press <em>Yes</em> if prompted.

If you want to do this in the terminal:

{% highlight bash %}
{% raw %}
rsync -ah --progress ./depots/221/16557524/hl2/* ~/Downloads/source-engine/hl2/hl2
cp -r ./depots/221/16557524/platform ~/Downloads/source-engine/hl2/
{% endraw %}
{% endhighlight %}


### Run Half-Life 2

Time to play. Back in the Raspberry Pi terminal, launch Half-Life 2 with:

{% highlight bash %}
{% raw %}
cd ~/Downloads/source-engine/hl2
./hl2-launcher
{% endraw %}
{% endhighlight %}


### Optimized Graphics Settings

For ~60fps gameplay:
* Change all settings to low
* Change the resolution to 1280x720

For ~30fps gameplay:
* Change settings to medium
* Change texture and shader settings to high
* Change the resolution to 1920x1080

Anti-aliasing and filtering should always be turned off.

To check the framerate, use <code>cl_showfps 1</code> from the Half-Life 2 console.


### Other Source Engine Games

These instructions are for building Half-Life 2, but you can also build other Source Engine games with the following parameters:

* hl1 = Half-Life 1: Source
* hl2 = Half-Life 2 
* episodic = Half-Life 2 Episode 1 and 2
* hl2mp = Half-Life 2: Deathmatch
* dod = Day of Defeat
* cstrike = Counter-Strike: Source
* portal = Portal


### On YouTube

I covered the original Half-Life 2 build on YouTube first, to a great response — over 60,000 views:

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/-S_J-3CJsPU?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

I later followed that up with a dedicated step-by-step how-to video — the one that actually walks through the commands on this page, and also covers building **Portal** the same way:

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/ipQ1trbWeX0?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

### Related on this site

- [Half-Life 2 and Portal on Raspberry Pi]({% link _projects/half-life-2-and-portal-on-raspberry-pi.md %}) — the project notes
- [I Made Half-Life 2 Run Natively on a Raspberry Pi 5]({% post_url 2026-09-14-i-made-half-life-2-run-natively-on-a-raspberry-pi-5 %})
- [Raspberry Pi 5]({% link _hardware/raspberry-pi-5.md %})