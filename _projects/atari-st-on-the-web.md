---
layout: post
title: Atari ST on the Web
date: '2018-06-01 12:00:00'
tags: [Atari ST, Projects, Retrocomputing]
status: completed
---

The Atari ST was released in 1985. But is it usable on the modern Web today? How far can I push the experience?

These are important questions to answer! So I pushed ahead.


### Project Notes

Status | Completed
Goal | Connect my venerable [Atari ST]({% post_url 2015-08-15-atari-in-the-attic %}) to the World Wide Web. Browse some sites!

Starting with a <a href="https://lotharek.pl/productdetail.php?id=46" target="_blank">NetUSBee</a> Ethernet adapter, <a href="http://hardware.atari.org/manuals/netsting.htm" target="_blank">I installed TOS drivers and the STinG TCP/IP stack</a>. I also used an <a href="http://www.atari-wiki.com/index.php/Graphics_cards" target="_blank">ET4000 graphics card</a> to push the resolution to a (somewhat) modern 1024x768 in 256 colours.

With those (and a successful TCP/IP ping) in place, <a href="https://breakintochat.com/blog/2017/09/05/web-browsing-on-the-atari-st-with-a-cosmosex/" target="_blank">I downloaded and configured Crystal Atari Browser (CAB)</a>.

The Web experience is slow and doesn't support SSL or CSS – which rules out a lot of content. However I was able to make <a href="https://twitter.com/jamesfmackenzie/status/1004495104885886978" target="_blank">older sites work</a>.

I'll call this a success!

![Pray before the head of Bob!](/img/projects/atari-st-on-the-web.jpg)


### Project Updates

- [How to Browse the Web on Atari ST]({% link _howto/how-to-browse-the-web-on-atari-st.md %}) 


### One Day Maybe

Is it possible to push this further?

In search of a better experience, it might be possible to use a <a href="https://en.wikipedia.org/wiki/Proxy_server" target="_blank">proxy server</a> to strip CSS and shrink images. Or use a text-based browser like <a href="http://lynx.browser.org/" target="_blank">Lynx</a>. <a href="https://www.brow.sh/" target="_blank">Browsh</a> also looks interesting.

Lots of avenues for future investigation!

<br />