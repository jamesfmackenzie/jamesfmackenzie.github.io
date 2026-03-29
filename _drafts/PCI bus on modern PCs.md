

#blog/ideas  

  

Modern PCs don’t have a native PCI bus, they have to bridge from PCIe

  

qualify what is the last chipset that has native PCI support

  

If you want to add PCI support back you have to add a bridge chip

  

These are the bridge chips and bridge devices in the market and how well they work

  

**asmedia bridge chip (model number?)**

  

- voodoo 2 = works great!
- PCI sound cards - won’t work on modern PCs because DDMA is missing (find a reference on this)
- BUT - some sound cards like the YMF724 have their own DMA emulation (DSDMA)

  

I was able to make PCM sound play via the setup utility. BUT it didn’t persist in settings. Same issue as here, and it seems to be due to the lack of subtractive decode support in this chip

  

[https://www.vogons.org/viewtopic.php?t=61256&start=40](https://www.vogons.org/viewtopic.php?t=61256&start=40)

  

“DDMA-capable southbridges like VT82C686B can make PCI sound cards work with little efforts.

PC-PCI is a different story as it requires physical connections which I'm yet to find any on modern motherboards using chipsets capable of such. For ISA motherboards using ICH5 or earlier, these wires were used to provide DMA-capable ISA slots. I think PC-PCI might be able to provide better legacy compatibility than DDMA, since most of the operations are being performed directly over physical wires.

On modern chipsets these capabilities are gone so it pretty much depends on whether the sound card's own DMA technology can work with a given chipset. VIA/SiS chipsets might be the most cooperative ones in this aspect.”

  

“Intel ICH only supported PC-PCI up to ICH5. It cannot be used directly, unless the board is generous enough to have the necessary pins accessible (which I've never seen one) so you can connect your sound card to it.”

  

  

  

**PCIe-PCI brigde based on the** [**Pericom Semiconductor PI7C9X111SL**](https://www.diodes.com/products/connectivity-and-timing/pcie-packet-switchbridges/pcie-pci-bridges/part/PI7C9X111SL)

  

  

**PCI\VEN_104C&DEV_8240  
It's a XIO2001 Texas Instruments PCI Express-to-PCI Bridge (model number?)**

  

  

**Idt bridge chip (like used on the x10 sae) (model number?)**

  
![[X10SAE Block Diagram 1.jpeg]]
  

  

  

A note on sound cards

  

Sound cards will normally “need subtractive decode”. Learn a bit more what that means and document it on here - and ultimate on the blog