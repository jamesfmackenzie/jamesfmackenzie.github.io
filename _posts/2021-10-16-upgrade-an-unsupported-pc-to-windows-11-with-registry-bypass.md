---
layout: post
title: "How To Install Windows 11 on an Unsupported PC With Registry Bypass"
date: '2021-10-16 10:21:00:00'
summary: Did your PC fail the Windows 11 health check? All is not lost – you may still be able to upgrade ...
tags: [How To, Windows 11]
---

Chasing <a href="https://docs.microsoft.com/en-us/windows/whats-new/windows-11-requirements" target="_blank">Windows 11 compatibility</a>, I recently [added a TPM 1.2 module to my desktop PC]({% post_url 2021-08-28-how-to-install-a-tpm-module %}). Unfortunately even after installing the module, my PC still failed the Windows 11 system requiremnet check:

![](/img/posts/windows-11-pc-health-check-app-tool.png)

But this isn't the end of the story. Microsoft <a href="https://support.microsoft.com/en-us/windows/ways-to-install-windows-11-e0edbbfb-cfc5-4011-868b-2ce77ac7c70e" target="_blank">recently published upgrade instructions</a> that bypass the check for TPM 2.0 and CPU family and model:

![](/img/posts/windows-11-bypass-check-for-tpm-20-and-cpu-family-model.png)

Here's how to upgrade your unsupported PC.

### Installing Windows 11 on an unsupported PC

1. First you need to download the Windows 11 Media Creation Tool. Navigate to the <a href="https://www.microsoft.com/en-us/software-download/windows11" target="_blank">Windows 11 download page</a>, find *Create Windows 11 Installation Media* and click *Download Now* 

2. Launch the tool and follow the instructions. This will create a bootable USB stick to install Windows 11:

![](/img/posts/windows-11-media-creation-tool-create-media.png)

{:start="3"}
3. Once the media is ready, click *Setup.exe* to start the Windows 11 install process. Your PC will reboot a few times whilst Windows 11 installs - it's very familiar if you've upgraded a Windows install before.

4. Once the install completes, you're running Windows 11. Enjoy!

