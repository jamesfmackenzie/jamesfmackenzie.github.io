---
layout: post
title: "What is a TPM? And Why Do I Need One for Windows 11?"
date: '2021-08-28 11:01:00:00'
summary: A quick post on Trusted Platform Modules (TPMs). I recently rushed to buy and install one after learning that Windows 11 requires a TPM to run ...
tags: [How To, Windows 11]
---

![](/img/posts/tpm-module.png)

A quick post on Trusted Platform Modules (TPMs).
 
I recently rushed to buy and install one after learning that Windows 11 requires a TPM to run. I learned a lot in my (ultimately failed) quest to make my PC Windows 11 compliant. Details below.


### What is a TPM?

A TPM chip communicates with other security systems in your PC, handling security-sensitive operations like key creation/storage and keeping a watch on system integrity. This makes life more difficult for a potential hacker.

Broadly there are two types of TPM:

- Discrete TPMs are dedicated chips that sit on your motherboard, either soldered-on or connected via special "TPM header" pins
- Firmware TPMs ("fTPMs") are part of your CPU

There are also two TPM specifications: TPM 1.2 and the newer TPM 2.0. TPM 2.0 targets many of the same use cases and features but is not backward compatible with TPM 1.2.

More details on Wikipedia <a href="https://en.wikipedia.org/wiki/Trusted_Platform_Module#TPM_1.2_vs_TPM_2.0" target="_blank">here</a>.


### Do I have a TPM already?

To check if you have a TPM:

From Windows, navigate to <code>Start</code> → <code>tpm.msc</code> 

* If you see "The TPM is ready for use", you're good to go – no further action required
* If you see "Compatible TPM cannot be found", you either don't have a TPM, or don't have your TPM *enabled*

If your Intel CPU is Skylake (2015) or newer, you likely have a Firmware TPM and just need to enable it in your BIOS. If your CPU is older (like my i7-4770K), you'll have to buy a Discrete TPM for your motherboard.


### Can I install a Discrete TPM?

To check if you have a compliant motherboard:

1. Go to your BIOS. 
2. Look for *Secure Boot* and *UEFI* options. If you have these, you're good to go

There are many different Discrete TPM pinout standards and you'll need to find the correct one for your motherboard. Check your documentation or look for the TPM header on your motherboard and count the pins. The common standards are:

- TPM/FW3.19 (20-1 pins) - TPM 1.2
- TPM-L R2.0 (20-1 pins) - TPM 2.0
- TPM-M R2.0 (14-1 pins) - TPM 2.0

I have an Asus Z87-PRO motherboard. After some research I bought this one for $7: 

![](/img/posts/supermicro-tpm-module.jpg)


### Preparing your system for a TPM

![](/img/posts/secureboot-legacy-mode.png)

Before you install/enable the TPM, check the <code>System Information</code> app in Windows. If you have "BIOS Mode" = *Legacy* and "Secure Boot State" = *Unsupported*, you need to fix that first

1. In Windows, go to <code>Settings</code> → <code>Recovery Pane</code> → <code>Advanced Startup</code> → <code>Restart Now</code>
2. Choose <code>Troubleshoot</code> → <code>Advanced Options</code> → <code>Command Prompt</code>
3. Type <code>MBR2GPT /validate</code>. If all goes well you should see "Validation completed successfully" 
4. Next type <code>MBR2GPT /convert</code>. This will convert your Windows install from Legacy to UEFI
5. Reboot your PC, enter the BIOS, enable UEFI and Secure Boot
6. Save changes and load Windows. System Information should now show "BIOS mode" = *UEFI* and "Secure Boot State" = *On*

![](/img/posts/uefi-secureboot-bios-mode.png)


### Install and enable the TPM

With UEFI and Secure Boot finally enabled, you're ready to install/enable the TPM:

1. (For Discrete TPM only) Shut down your PC and fit the TPM to your motherboard
2. Power-on your machine and re-enter the BIOS. Find the "TPM" feature and enable it
3. Save BIOS changes and load Windows. 
4. Again navigate to <code>Start</code> → <code>tpm.msc</code>. All going well, you should see "The TPM is ready for use"

Congratulations, you've successfully installed a TPM!


### I've installed a TPM! Can I use Windows 11?

Unfortunately Windows 11 compatibility is more complicated than just TPM. Microsoft has amended the minimum System Requirements a few times already since the initial announcement.

* Currently, TPM Version 2.0 is required. Some older motherboards (like mine) only support TPM 1.2 modules 
* Even if you have TPM 2.0, the Windows 11 CPU requirements have also been confirmed as *minimum* Intel 8th-gen or Ryzen 2000 architecture. My old machine is out of luck!

To check your own machine, download and run the Windows 11 PC Health Check app. It will give you a 

![](/img/posts/windows-11-pc-health-check-app-tool.png)

This was a fun journey and I learned a lot about TPM! Hope you find this post useful too!


