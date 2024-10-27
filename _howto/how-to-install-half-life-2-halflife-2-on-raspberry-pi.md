---
layout: post
title: "How to Install Half-Life 2 on Raspberry Pi"
date: '2024-10-27 08:35:00:00'
summary: In this guide, we’ll explore how to install Half-Life 2 on the Raspberry Pi, with step-by-step instructions to build your own mini Half-Life machine!
image:
tags: [Raspberry Pi]
---

I recently installed Half Life 2 on the Raspberry Pi and the response was super great!

More than 25,000 of you tuned in and you can find that video here:

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/-S_J-3CJsPU?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div> 

In this how to guide, we’ll explore how to install Half-Life 2 on your own Pi, with step-by-step instructions and a deep-dive on the graphics settings you need to boost performance.


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

Next, we need to add our dev libraries:

{% highlight bash %}
{% raw %}
sudo apt-get install libsdl2-dev libfontconfig1-dev libopenal-dev libjpeg-dev libpng-dev libcurl4-gnutls-dev libbz2-dev libedit-dev
{% endraw %}
{% endhighlight %}


### Step 3. Download Source Engine Code

Run the following command to download the Source Engine source code to the <code>source-engine</code> directory:

{% highlight bash %}
{% raw %}
git clone https://github.com/nillerusr/source-engine.git —-recursive
{% endraw %}
{% endhighlight %}

Then navigate to the downloaded files with <code>cd source-engine</code>.


### Step 4. Configure the Build

Type the following to configure your Source Engine build for Half-Life 2:

{% highlight bash %}
{% raw %}
python3 ./waf configure -T release -prefix=hl2 —build-games=hl2 —disable-warns
{% endraw %}
{% endhighlight %}

As a side note, we can also configure with different parameters to build other Source Engine games (see “Other Source Engine Games” below).


### Step 5. Build Half-Life 2

With that done, we’re ready to build Half-Life 2 with:

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


### Copy Game Assets

Last but not least, we need to copy the Half-Life 2 assets to the Pi.

From your Steam PC, download Half-Life 2. In your Steam library, right click on the Half-Life 2 entry and select <em>Manage</em>, <em>Browse local files</em>.

This will show us the location of the Half-Life 2 assets. They’re normally located in <code>/Users/USERNAME/Library/Application Support/Steam/steamapps/common/Half-Life 2</code>).

Use a USB stick or network file transfer to copy the <code>hl2</code> and <code>platform</code> folders to the newly created <code>hl2</code> directory on your Pi.

You might be prompted to merge files. Press <em>Yes</em> and once you’re done, the <code>hl2</code> directory should look like this:


### Run Half-Life 2

You’re ready to play! Back in the Raspberry Pi terminal, type the following to launch Half-Life 2:

{% highlight bash %}
{% raw %}
./hl2-launcher
{% endraw %}
{% endhighlight %}

Enjoy!


### Other Source Engine Games

These instructions are for building Half-Life 2, but you can also build other Source Engine games with the following parameters:

* hl1 = Half-Life 1: Source
* hl2 = Half-Life 2 
* episodic = Half-Life 2 Episode 1 and 2
* hl2mp = Half-Life 2: Deathmatch
* dod = Day of Defeat
* cstrike = Counter-Strike: Source
* portal = Portal

