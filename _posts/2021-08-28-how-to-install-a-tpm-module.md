---
layout: post
title: "How to install a TPM module"
date: '2021-08-28 11:01:00:00'
summary: How to install a TPM module
tags: [How To]
---

A quick post on Trusted Platform Modules (TPMs).
 
I recently rushed to buy and install one after learning that Windows 11 requires a TPM to run. I learned a lot in my (ultimately failed) quest to make my PC Windows 11 compliant. Details below.


### What is a TPM?

A TPM chip communicates with other security systems in your PC, handling security-sensitive operations like key creation/storage and keeping a watch on system integrity. This makes life more difficult for a potential hacker.

Broadly there are two types of TPM:

- Discrete TPMs are dedicated chips that sit on your motherboard, either soldered-on or connected via special "TPM header" pins
- Firmware TPMs ("fTPMs") are part of your CPU

There are also two TPM specifications: TPM 1.2 and the newer TPM 2.0

While TPM 2.0 addresses many of the same use cases and has similar features vs TPM 1.2, the details are different. TPM 2.0 is not backward compatible with TPM 1.2.

You can learn more details on Wikipedia here


### Do I have a TPM already?

To check if you have a TPM:

From Windows, navigate to Start -> tpm.msc. 

- If you see "The TPM is ready for use", you're good to go - no further action required
- If you see "Compatible TPM cannot be found", you either don't have a TPM, or don't have your TPM *enabled*

If your Intel CPU is Skylake (2015) or newer, you likely have a Firmware TPM and just need to enable it in your BIOS

If your CPU is older (like my i7-4770K), you'll have to buy a Discrete TPM for your motherboard


### Can I install a Discrete TPM?

To check if you have a compliant motherboard:

1. Go to your BIOS
2. Go to Secure Boot and check if the UEFI option is there. If you have this, you are good to go

There are many different Discrete TPM pinout standards and you'll need to find the correct one for your motherboard. Check your documentation or look for the TPM header on your motherboard and count the pins. The common standards are:

- TPM/FW3.19 (20 pins) - TPM 1.2
- TPM-L R2.0 (20 pins) - TPM 2.0
- TPM-M R2.0 (14 pone) - TPM 2.0

After some research I bought this one for $7: 

![](/img/posts/tpm-module.png)


### Preparing your system for a TPM

Before you install/enable the TPM, check the System Information app in Windows. If you have "BIOS Mode" = Legacy and "Secure Boot State" = Unsupported, you need to fix that first

1. In Windows, go to Settings -> Recovery Pane -> Advanced Startup -> Restart Now
2. Choose Troubleshoot -> Advanced Options -> Command Prompt
3. Type MBR2GPT /validate. If all goes well you should see "Validation completed successfully" 
4. Next type MBR2GPT /convert. This will convert your Windows install from Legacy to UEFI
5. Reboot your PC, enter the BIOS, enable UEFI and Secure Boot
6. Save changes and load Windows. System Information should now show "BIOS mode" = UEFI and "Secure Boot State" = On


### Install and enable the TPM

With UEFI and Secure Boot finally enabled, you're ready to install/enable the TPM:

1. (For Discrete TPM only) Shut down your PC and fit the TPM to your motherboard
2. Power-on your machine and re-enter the BIOS. Find the "TPM" feature
and turn it on (PUT SOME COMMON OPTIONS HERE)
3. Save BIOS changes and load Windows. 
4. Again navigate to Start -> tpm.msc. All going well, you should see "The TPM is ready for use"

Congratulations, you've successfully installed a TPM!


### I've installed a TPM! Can I use Windows 11?

Unfortunately it's a little more complicated. 

Microsoft has amended their Windows 11 System Requirements a few times since the initial announcement.

Currently, TPM Version 2.0 (a newer revision of the TPM standard) is required. Some older motherboards (like mine) only support TPM 1.2 modules 

Even if you have TPM 2.0, 
the Windows 11 CPU requirements have also been confirmed as *minimum* Intel 8th-gen or Ryzen 2000 architecture. My old machine is out of luck!

To check your own machine, download the Windows 11 checker tool

This was a fun journey and I learned a lot about TPM! Hope you find this post useful too!

