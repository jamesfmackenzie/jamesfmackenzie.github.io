---
layout: post
title: "How to Browse the Web on Atari ST"
date: '2019-12-08 00:00:02:00'
summary: 
tags: [Atari ST, How To, Retrocomputing]
---

I was recently able to <a href="https://twitter.com/jamesfmackenzie/status/1004495104885886978" target="_blank">make an Atari ST browse the Web!</a>. Here's how I did it.


### Network setup

Starting with a <a href="https://lotharek.pl/productdetail.php?id=46" target="_blank">NetUSBee</a> Ethernet adapter, <a href="http://hardware.atari.org/manuals/netsting.htm" target="_blank">I installed TOS drivers and the STinG TCP/IP stack</a>.


### Graphics

An optional step, but really helps with the modern web. I used an <a href="http://www.atari-wiki.com/index.php/Graphics_cards" target="_blank">ET4000 graphics card</a> to push the resolution to a (somewhat) modern 1024x768 in 256 colours.


### Browser

With a successful TCP/IP ping in place, <a href="https://breakintochat.com/blog/2017/09/05/web-browsing-on-the-atari-st-with-a-cosmosex/" target="_blank">I downloaded and configured Crystal Atari Browser (CAB)</a>.

The Web experience is slow and doesn't support CSS - which rules out a lot of content. However I was able to make <a href="https://twitter.com/jamesfmackenzie/status/1004495104885886978" target="_blank">older sites work</a>.

![Pray before the head of Bob!](/img/projects/atari-st-on-the-web.jpg)


### Future investigation

In search of a better experience: it might be possible to use a <a href="https://en.wikipedia.org/wiki/Proxy_server" target="_blank">proxy server</a> to strip CSS and shrink images. Or use a text-based browser like <a href="http://lynx.browser.org/" target="_blank">Lynx</a>. <a href="https://www.brow.sh/" target="_blank">Browsh</a> also looks interesting. Lots of avenues for future investigation!

<br />