---
layout: post
title: "What is a TPM? And Why Do I Need One for Windows 11?"
date: '2021-08-28 11:01:00:00'
summary: A quick post on Trusted Platform Modules (TPMs). I recently rushed to buy and install one after learning that Windows 11 requires a TPM to run ...
image: supermicro-tpm-module.jpg
tags: [How To, Posts, TPM, Windows 11]
---

**Update 2021-10-16: Thanks to <a href="https://support.microsoft.com/en-us/windows/ways-to-install-windows-11-e0edbbfb-cfc5-4011-868b-2ce77ac7c70e" target="_blank">recently published upgrade instructions</a>, it's now possible to upgrade previously unsupported TPM 1.2 PCs to Windows 11. Learn more [here]({% post_url 2021-10-16-upgrade-an-unsupported-pc-to-windows-11-with-registry-bypass %}).**

![](/img/posts/tpm-module.png)

A quick post on Trusted Platform Modules (TPMs).
 
I recently rushed to buy and install one after learning that Windows 11 requires a TPM to run. I learned a lot in my <span class="strikethrough">(ultimately failed)</span> quest to make my PC Windows 11 compliant. Details below.


### What is a TPM?

A TPM chip communicates with other security systems in your PC, handling security-sensitive operations like key creation/storage and keeping a watch on system integrity. This makes life more difficult for a potential hacker.

Broadly there are two types of TPM:

* Discrete TPMs are dedicated chips that sit on your motherboard, either soldered-on or connected via special "TPM header" pins
* Firmware TPMs ("fTPMs") are part of your CPU

There are also two TPM specifications: TPM 1.2 and the newer TPM 2.0. TPM 2.0 targets many of the same use cases and features but is not backward compatible with TPM 1.2.

More details on Wikipedia <a href="https://en.wikipedia.org/wiki/Trusted_Platform_Module#TPM_1.2_vs_TPM_2.0" target="_blank">here</a>.


### Why do I need a TPM for Windows 11?

Microsoft is looking to improve security and reliability in Windows 11, and TPM is part of this push. In their own words:

<blockquote>"Windows 11 raises the bar for security by requiring hardware that can enable protections like Windows Hello, Device Encryption, virtualization-based security (VBS), hypervisor-protected code integrity (HVCI) and Secure Boot. The combination of these features has been shown to reduce malware by 60% on tested devices. To meet the principle, all Windows 11 supported CPUs have an embedded TPM, support secure boot, and support VBS and specific VBS capabilities."</blockquote>


### Do I have a TPM already?

To check if you have a TPM:

From Windows, navigate to <code>Start</code> → <code>tpm.msc</code> 

* If you see "The TPM is ready for use", you're good to go – no further action required
* If you see "Compatible TPM cannot be found", you either don't have a TPM, or don't have your TPM *enabled*

If your CPU is Intel Skylake (2015), Ryzen Zen+ (2000 Series) or newer, you likely have a Firmware TPM and just need to enable it in your BIOS - look for Intel PTT or AMD PSP fTPM.

If your CPU is older (like my i7-4770K), you'll have to buy a Discrete TPM for your motherboard.


### Can I install a Discrete TPM?

To check if you have a compliant motherboard:

1. Check your motherboard documentation. Look for TPM or Trusted Platform Module
2. Locate the TPM header on your motherboard and count the pins

There are many different Discrete TPM pinout standards and you'll need to find the correct one. The common standards are:

- TPM/FW3.19 (20-1 pins) - TPM 1.2
- TPM-L R2.0 (20-1 pins) - TPM 2.0
- TPM-M R2.0 (14-1 pins) - TPM 2.0

I have an Asus Z87-PRO motherboard. After some research I bought this module for $7: 

![](/img/posts/supermicro-tpm-module.jpg)

You also need to verify Secure Boot and UEFI support:

1. Go to your BIOS. 
2. Look for *Secure Boot* and *UEFI* options

If you have all the above, you're good to go


### Preparing your system for a TPM

![](/img/posts/secureboot-legacy-mode.png)

Before you install/enable the TPM, check the System Information app in Windows (<code>Start</code> -> <code>msinfo32</code>). If you have "BIOS Mode" = *Legacy* and "Secure Boot State" = *Unsupported*, you need to fix that first:

1. In Windows, go to <code>Settings</code> → <code>Recovery Pane</code> → <code>Advanced Startup</code> → <code>Restart Now</code>
2. Choose <code>Troubleshoot</code> → <code>Advanced Options</code> → <code>Command Prompt</code>
3. Type <code>MBR2GPT /validate</code>. If all goes well you should see "Validation completed successfully" 
4. Next type <code>MBR2GPT /convert</code>. This will convert your Windows install from Legacy to UEFI
5. Reboot your PC, enter the BIOS, enable UEFI and Secure Boot
6. Save changes and load Windows. System Information should now show "BIOS mode" = *UEFI* and "Secure Boot State" = *On*

![](/img/posts/uefi-secureboot-bios-mode.png)


### Install and enable the TPM

With UEFI and Secure Boot fully enabled, you're ready to install/enable the TPM:

1. (For Discrete TPM only) Shut down your PC and fit the TPM to your motherboard
2. Power-on your machine and re-enter the BIOS. Find the "TPM" feature and enable it
3. Save BIOS changes and load Windows. 
4. Again navigate to <code>Start</code> → <code>tpm.msc</code>. All going well, you should see "The TPM is ready for use"

Congratulations, you've successfully installed a TPM!

![](/img/posts/the-tpm-is-ready-for-use.png)


### I've installed a TPM! Can I use Windows 11?

Unfortunately Windows 11 compatibility is more complicated than just TPM – and Microsoft has already amended the minimum System Requirements a few times since their initial announcement.

* Currently, TPM Version 2.0 is required. Some older motherboards (like mine) only support TPM 1.2 
* Even if you have TPM 2.0, the Windows 11 CPU requirements have also been confirmed as *minimum* Intel 8th-gen or Ryzen 2000 architecture. My old machine is plain out of luck!

To check your own machine, download and run the Windows 11 PC Health Check app. It will run a diagnostic and provide a compatibility summary for you:

![](/img/posts/windows-11-pc-health-check-app-tool.png)

This was a fun journey and I learned a lot about TPM! Hope you find this post useful too!


