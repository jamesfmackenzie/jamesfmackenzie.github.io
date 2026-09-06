---
layout: post
title: The Secret 3Dfx Graphics Card (You Never Knew Existed)
date: '2024-11-30 09:00:00'
tags: [3Dfx Voodoo, Projects, Retrocomputing, Retrogaming]
status: completed
---

Real Voodoo 3 cards have gotten expensive — a quick scroll through eBay listings routinely turns up prices well over $100, with some cards going for $300–400+. I wanted the same Glide-accelerated era of gaming without paying collector prices, and that led me to a card that stayed almost completely off the radar: the [3Dfx Velocity 100]({% link _hardware/3dfx-voodoo-velocity-100.md %}).

### Project Notes

Status | Completed
Goal | Confirm whether the budget, OEM-only Velocity 100 can really perform like a full Voodoo 3 — and unlock the trick that makes it do so.

Built for the OEM market rather than sold under the 3Dfx brand, the Velocity 100 is priced like a bargain-bin card — I picked mine up for $99, with others turning up on eBay for less. Side by side with a real Voodoo 3, it's hard to tell apart: same heatsink and memory layout, same BIOS chip placement. The full spec story — the shared Avenger chip, the 143MHz clock it shares with a Voodoo3 2000, the 8MB (vs. 16MB) framebuffer — lives on the [hardware page]({% link _hardware/3dfx-voodoo-velocity-100.md %}).

With the card installed in a Windows 98 machine, a Glide donut demo and a DirectX cube in dxdiag both confirmed the GPU was working, and PowerStrip identified it plainly as a Voodoo 3 — just with half the RAM.

**Benchmarking, before the fix:**

| Resolution | 3DMark99 (D3D) | Unreal (Glide) | Quake II (OpenGL) |
|---|---|---|---|
| 640×480 | 6,240 | 56.8 fps | 59.2 fps |
| 800×600 | 5,540 | 40.2 fps | 42.7 fps |
| 1024×768 | 2,830 | 28.5 fps | 30.5 fps |

Against a real Voodoo3 2000 on the same driver vintage — 5,300 / 5,190 / 4,380 in 3DMark, and roughly 92 / 73 / 54 fps in Unreal, 110 / 96 / 69 fps in Quake II — the picture split right down API lines: in Direct3D, the Velocity matched or slightly outperformed the real Voodoo 3 at 640×480 and 800×600, only falling behind at 1024×768. But in Glide and OpenGL, the Voodoo 3 was comfortably ahead — almost double the framerate.

The reason turned out to be the card's whole gimmick: the Velocity 100 physically has two texture mapping units (TMUs), same as a Voodoo 3, but the second one is disabled by the drivers in Glide and OpenGL — while Direct3D always gets both. That's a documented, reversible registry change: adding a string value `FX_GLIDE_NUM_TMU` set to `2` under `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Class\Display\0000\Glide` flips the second TMU back on for Glide and OpenGL too.

**After the registry fix:**

| Resolution | 3DMark99 (D3D) | Unreal (Glide) | Quake II (OpenGL) |
|---|---|---|---|
| 640×480 | 6,240 *(unchanged — D3D already used both TMUs)* | 96.9 fps | 128.8 fps |
| 800×600 | 5,540 *(unchanged)* | 71.2 fps | 98.1 fps |
| 1024×768 | 2,830 *(unchanged)* | 49.2 fps | 68.5 fps |

That's roughly a 70% jump in Unreal and more than double the Quake II framerate — enough to put the Velocity 100 level with or slightly ahead of a real Voodoo3 2000 at 640×480 and 800×600, before falling behind again at 1024×768, where the smaller 8MB framebuffer likely starts to run short. As a sanity check on how much of that is really the hardware talking: Quake II's pure software renderer manages only 37.6fps at 640×480 — well under even the *crippled*, pre-fix 59.2fps the Velocity got in hardware.

One more test for good measure — DOS. Running the 3Dfx-patched version of Tomb Raider natively from DOS, the card accelerated it exactly like a real Voodoo 3 would. No surprises, no compromises.

More details:

- [3Dfx Velocity 100 hardware page]({% link _hardware/3dfx-voodoo-velocity-100.md %}) — full spec breakdown and the registry fix
- [The Secret 3Dfx Graphics Card (You Never Knew Existed)]({% post_url 2024-11-30-the-secret-3dfx-graphics-card-velocity-100 %})

And also in video form below. Enjoy!

<div class="youtube-container">
<iframe src="https://www.youtube.com/embed/7Pf-amyWM20?rel=0" 
allowfullscreen class="youtube-video"></iframe>
</div>

<br />
