

#blog/ideas

  

There are four generations of Mac:

  

1. Motorola 680x0-based Macs (aka "68k" Macs)
2. PowerPC-based Macs
3. Intel-based Macs
4. ARM64-based Macs (aka Apple Silicon)

  

Normally software compiled for one CPU type would *not run* at all on other Macs. Luckily for us, Apple has been very good with emulation/translation technology to allow newer Macs to run older software. These are:

  

1. [Mac 68k emulator - Wikipedia](https://en.wikipedia.org/wiki/Mac_68k_emulator) - this is a software emulator built into all versions of Classic Mac OS for PowerPC. This enabled running applications and system code that were originally written for the 680x0-based Macintosh models. With a few exceptions, the emulator ran all software with no noticeable impact other than lower performance relative to the same program when compiled for PowerPC

  

2. [Rosetta (software) - Wikipedia](https://en.wikipedia.org/wiki/Rosetta_\(software\)#Rosetta) - another software emulator, designed to facilitate the Mac transition to Intel processors. Rosetta was embedded in [Mac OS X v10.4.4](https://en.wikipedia.org/wiki/Mac_OS_X_Tiger) "Tiger", allowing many [PowerPC](https://en.wikipedia.org/wiki/PowerPC) applications to run on Intel-based Mac computers without modification. Unfortunately Rosetta does not support the [Classic environment](https://en.wikipedia.org/wiki/Classic_\(Mac_OS_X\)), and thus any [non-Carbon application](https://en.wikipedia.org/wiki/Carbon_\(API\)) built for [Mac OS 9](https://en.wikipedia.org/wiki/Mac_OS_9) or earlier will not work.

  

3. [Rosetta (software) - Wikipedia](https://en.wikipedia.org/wiki/Rosetta_\(software\)#Rosetta_2) aka "Rosetta 2" - In 2020, Apple announced Rosetta 2 would be bundled with [macOS Big Sur](https://en.wikipedia.org/wiki/MacOS_Big_Sur), to aid in the [Mac transition to Apple silicon](https://en.wikipedia.org/wiki/Mac_transition_to_Apple_silicon). The software permits many applications compiled exclusively for execution on [x86-64](https://en.wikipedia.org/wiki/X86-64)-based processors to be translated for execution on Apple silicon

  

So which Mac should I buy to run classic software?

  

68k Macs:

- The run from the original Macintosh, running a Motorola 68000 processor, to the Macintosh Quadra line, running a 68040 processor
- Most models can run up to Mac OS 7.x. The very last version is 8.1 (double confirm this)
- The Quadra line is by far the most expandable, with swapable system RAM, VRAM, storage, and even a slot for a dedicated PowerPC processor upgrade
- All models can (pretty much) run all 680x0 software

  

From Quora: "What is the fastest 68k Mac?"

- "The question stated 68K based, not the 68000 parts per se. So we’re looking for a 68040 based Quadra or Performa, all of which could run the gamut of System 7.x through MacOS 8.6* and maybe 9. Edit: Per MacObserver the very last 68K Mac was the Quadra 630 model and supported up to 8.1 (8.0 was basically a renamed 7.7, a bit of subterfuge to kill of the clone agreements)

  

Full list of 68k Macintosh models:

https://vintagemacmuseum.com/collection/68k-macintosh/

  

PowerPC Macs:

- As mentioned above, some models can run 68k software through emulation
- An even smaller subset of models, up until the G4 processor, can also natively boot and run MacOS Classic. This provides the best backwards compatibility solution, as these Macs can run both PowerPC software *and* most 68k software through OS-integrated Mac 68k emulator
- Super good news, the forum members over at Mac OS 9 Lives were able to get MacOS 9 booting natively on a G4 Mac Mini. This makes a super nice machine for both 68k and PowerPC software

  

More reading on how to install and run MacOS 9 on a Mac Mini G4:

[Mac OS 9.2.2 (Mac mini PPC G4 Only) Install Image](https://forums.system7today.com/smforum/index.php?topic=4365.msg30502#msg30502) [(system7today.com)](http://system7today.com)

[Tutorial : Dual Booting Mac OS X And Mac OS 9 On The Mac Mini G4 (Same HDD)](https://forums.system7today.com/smforum/index.php?topic=5345.0) [(system7today.com)](http://system7today.com)

  

One side note:

- There are a few different revisions of the Mac Mini G4. The earler models ran at 1.25GHz and 1.42GHz. The later models ran at 1.33GHz and 1.5GHz. The earlier ones seem to work slightly better with this mod/hack:

  

"TL;DR Go for the 1.25 or 1.42 GHz models if you can, they are better unless if the Mac heroes that brought Mac OS 9 to the mini come back to address a bunch of issues (don't bet on that happening, they did enough for us, and I don't imagine they will be inspired to fix these). But if all you can get are the other 2 models (1.5 or 1.33 GHz), then that is fine as well, but expect further caveats."

  

Lastly, find this nice thread on Vogons that talks about OS9 games on the Mac Mini G4:

[http://www.vogons.org/viewtopic.php?t=31386](http://www.vogons.org/viewtopic.php?t=31386)