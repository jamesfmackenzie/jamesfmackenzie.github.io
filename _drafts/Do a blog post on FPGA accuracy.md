

  

#blog/ideas 

  

Thanks for your kind message!

   

My take: whist it’s possible for FPGA implementations to be cycle accurate (or even accurate at the gate level etc), this is not always the case. Core developers are often working in a “black box” fashion or using existing software emulators as a reference to create their cores.

  

So it can be *very* accurate, but not always 1:1.

  

One advantage that FPGAs have: once you define components in FPGA, they will interact in parallel with each other, just like with real hardware. If each component if implemented accurately, the FPGA implementation will be very accurate to original hardware.

  

Naively, software emulators operate on a single CPU thread, with the code that emulates each components being executed sequentially - which means you need a *very* fast CPU (compared to the original hardware) to approximate original behaviour. Of course today we have multi GHz CPUs, and also the ability to distribute threads across multiple CPU cores - so with the right programming, it is possible to write very accurate software emulators too - but it’s not easy! 😂

  

There are some great articles that explain this a lot better than I can - but I hope this helps!