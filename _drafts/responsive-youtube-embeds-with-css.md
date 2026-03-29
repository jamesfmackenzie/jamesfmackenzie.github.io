---
layout: post
title: Responsive YouTube Embeds with CSS
summary: A short draft showing how to make embedded YouTube videos scale cleanly on responsive layouts.
tags: [CSS, HTML, Web Development]
---

Embedded YouTube videos tend to break layouts if you leave them at a fixed width and height. The simplest fix is to wrap the iframe in a container that preserves the aspect ratio while allowing the video to scale.

## Basic Markup

```html
<div class="youtube-container">
  <iframe
    src="https://www.youtube.com/embed/n_dZNLr2cME?rel=0&hd=1"
    allowfullscreen>
  </iframe>
</div>
```

## Basic CSS

```css
.youtube-container {
  position: relative;
  padding-bottom: 56.25%;
  padding-top: 25px;
  height: 0;
}

.youtube-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```

## Why This Works

The wrapper keeps a 16:9 aspect ratio while the iframe stretches to fill that box. It is a small trick, but it makes old fixed-width embed code behave much better on phones and narrow screens.

## Next Steps

- Update the old example to modern `https` URLs
- Check whether the current site CSS already has a reusable utility for video embeds
