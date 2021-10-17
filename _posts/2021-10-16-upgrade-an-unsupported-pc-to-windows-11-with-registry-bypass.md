---
layout: post
title: "How To Install Windows 11 on an Unsupported PC With Registry Bypass"
date: '2021-10-16 10:21:00:00'
summary: Did your PC fail the Windows 11 health check? All is not lost – you may still be able to upgrade ...
tags: [How To, Windows 11]
---

Chasing <a href="https://docs.microsoft.com/en-us/windows/whats-new/windows-11-requirements" target="_blank">Windows 11 compatibility</a>, I recently [added a TPM 1.2 module to my desktop PC]({% post_url 2021-08-28-how-to-install-a-tpm-module %}). Unfortunately even after installing the module, my PC still failed the Windows 11 system requirement check:

![](/img/posts/windows-11-pc-health-check-app-tool.png)

But this isn't the end of the story. Microsoft <a href="https://support.microsoft.com/en-us/windows/ways-to-install-windows-11-e0edbbfb-cfc5-4011-868b-2ce77ac7c70e" target="_blank">recently published upgrade instructions</a> that bypass the check for TPM 2.0 and CPU family/model:

![](/img/posts/windows-11-bypass-check-for-tpm-20-and-cpu-family-model.png)

My unsupported PC is back in play!

There are some <a href="https://support.microsoft.com/en-us/windows/installing-windows-11-on-devices-that-don-t-meet-minimum-system-requirements-0b2dc4a2-5933-4ad4-9c09-ef0a331518f1" target="_blank">risks</a> – notably your PC "won't be entitled to receive updates" (more on that below). If you acknowledge and understand the risks, here's how to upgrade your unsupported PC.


### Installing Windows 11 on an unsupported PC

1. Open <a href="https://support.microsoft.com/en-us/windows/how-to-open-registry-editor-in-windows-10-deab38e6-91d6-e0aa-4b7c-8878d9e07b11" target="_blank">Registry Editor</a> and add the following key:

```
Registry Key: HKEY_LOCAL_MACHINE\SYSTEM\Setup\MoSetup
Name: AllowUpgradesWithUnsupportedTPMOrCPU
Type: REG_DWORD
Value: 1
```

![](/img/posts/windows-11-upgrade-registry-key-allowupgradeswithunsupportedtpmorcpu.png)

{:start="2"}
2. Download the Windows 11 Media Creation Tool. Navigate to the <a href="https://www.microsoft.com/en-us/software-download/windows11" target="_blank">Windows 11 download page</a>, find *Create Windows 11 Installation Media* and click *Download Now* 

3. Launch the tool and follow the instructions to create bootable Windows 11 installation media:

![](/img/posts/windows-11-media-creation-tool-create-media.png)

{:start="4"}
4. With the media ready, run *Setup.exe* to start the Windows 11 install process. Your PC will reboot a few times whilst Windows 11 installs - it's very familiar if you've upgraded Windows before.

5. Once the install completes, you're running Windows 11. Enjoy!

![](/img/posts/welcome-to-windows-11.jpg)


### Windows 11 Updates

As mentioned above, unsupported PCs "won't be entitled to receive updates". However, at least for now, updates seem to be working fine:

![](/img/posts/windows-11-security-updates-cropped.png)

Of course this may stop in future, but it's encouraging that security and other updates for unsupported PCs are working.
