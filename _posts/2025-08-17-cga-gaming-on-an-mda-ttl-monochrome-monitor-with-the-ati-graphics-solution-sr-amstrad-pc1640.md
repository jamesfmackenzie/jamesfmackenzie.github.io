--- 
layout: post
title: "CGA Gaming on an MDA Monochrome Monitor"
date: '2025-08-17 06:28:00:00'
summary: |-
  The 1987 **ATI Graphics Solution SR** is a retro graphics card with a unique trick. It can **emulate CGA output on an MDA monochrome monitor**.
  
  Let’s try it out!  
tags: [ATi Graphics, How To, MS-DOS, PC]
---

![Amstrad PC1640](/img/posts/amstrad-pc1640-2.jpg)

One of the quirks of retro hardware is that what you see on paper doesn’t always line up with what you get in practice.

Take the **[Amstrad PC1640]({% link _hardware/amstrad-pc1640.md %})** for example: although the built-in Paradise graphics chip is fully capable of both **CGA** and **EGA** colour modes, the bundled **PC-MD monochrome monitor** limits you to text and Hercules-style monochrome graphics.  

That’s fine for productivity, but what about games? The vast majority of them need to run in CGA or EGA graphics mode.

I wanted to enjoy some classic games on my Amstrad without swapping the whole monitor setup, and the solution came in the form of an **[ATI Graphics Solution SR]({% link _hardware/ati-graphics-solution-sr.md %})** graphics card — a clever piece of hardware with a unique trick: it can **emulate CGA output on an MDA monitor**. Perfect!


### Step 1. Disabling the Built-In Graphics  

Before installing the ATI card, the PC1640 needs to be told to expect an add-on CGA card instead of its built-in graphics chip. That’s done via DIP switches on the motherboard:  

- **SW10 = On** (disable on-board graphics)  
- **SW6, SW7 = Off, On** (select add-on CGA, 80-column mode)  

Reference: [Amstrad PC1640 DIP switch settings](https://www.seasip.info/AmstradXT/pc1640dip.html)  


### Step 2. Configuring the Graphics Solution SR  

With the machine ready, it’s time to configure the **Graphics Solution SR** for CGA emulation:  

- **SW1, SW2 = Off, Off** (CGA emulation mode)  
- **SW3, SW4, SW5 = On, Off, Off** (mono monitor selected)  

Reference: [ATI Graphics Solution SR documentation (The Retro Web)](https://theretroweb.com/expansioncard/documentation/52891.pdf)


### Results!  

After powering up — success! The system booted with the ATI card handling video, and I was able to play a selection of **classic CGA games** on the monochrome Amstrad monitor.  

Even better, the card displayed **grayscale tones**, which look much richer than standard black or white Hercules graphics. The downside is a noticeable **flicker**, caused by the interlaced screen mode the card uses to display CGA emulation on an MDA display. Still, for the novelty of playing colour games on a mono display, it’s a pretty neat trick.


### Switching Back to Hercules  

Want to return to Hercules mode? No problem — we just need to reverse the changes above with a quick switch configuration:  

**On the PC1640 motherboard:**  
- **SW10 = On** (disable on-board graphics)  
- **SW6, SW7 = On, On** (select add-on MDA)  

**On the Graphics Solution SR:**  
- **SW1, SW2 = On, Off** (monochrome mode)  
- **SW3, SW4, SW5 = On, Off, Off** (mono monitor)

And just like that, you’re back in Hercules mode.  


### Final Thoughts  

The **[ATI Graphics Solution SR]({% link _hardware/ati-graphics-solution-sr.md %})** is a very interesting card that bridges the gap between productivity-oriented mono PCs and the world of CGA gaming — and it really expands what’s possible on Amstrad PC1640’s PC-MD monochrome monitor.

So far as I can tell, this is (almost!) a unique feature — the only other card that does this is ATI’s **EGA Wonder** graphics card. 

As a next step, I’m trying to buy an EGA Wonder. This should achieve the same graphics emulation support as the Graphics Solution SR — but this time with **EGA** colour mode. Wish me luck!

![ATI Graphics Solution SR](/img/posts/ati-graphics-solution-sr.png)


### Further Reading

- <a href="https://www.vogons.org/viewtopic.php?t=87689" target="_blank">Displaying CGA/EGA graphics on an MDA monitor</a>
- <a href="https://www.tumblr.com/swarmik/178909439269/full-cga-graphics-on-mda-monitors-a-few-weeks-ago" target="_blank">Full CGA graphics on MDA monitors</a>