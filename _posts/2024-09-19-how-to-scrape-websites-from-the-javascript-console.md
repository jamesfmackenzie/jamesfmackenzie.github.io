---
layout: post
title: "How To Scrape Website Data With the JavaScript Console"
date: '2024-09-19 10:59:00:00'
summary: Want to grab some structured data from the Web? It's easy via the JavaScript console.
image: browser-dom-query.png
tags: [How To, Posts, Programming, Web Development]
---

Want to grab some data from the Web? It's easy via the JavaScript console.

### Step 1. Navigate to your target page

Open your browser and navigate to the page you want to extract data from. In this case its <a href="https://www.metacritic.com" target="_blank">Metacritic</a>.

### Step 2. Open the JavaScript console

Open the JavaScript console. On most browsers you can do this with a keyboard shortcut: <code>F12</code>. If the  shortcut doesn't work, Open it from the Developer or Tools menu.

![How to open the JavaScript Console](/img/posts/browser-open-javascript-console.png)

### Step 3. Issue a DOM query

![JavaScript DOM query](/img/posts/browser-dom-query.png)

A Document Object Model (DOM) query can be used to interrogate the page and extract data.

In this case I made two queries to extract game titles and scores from Metacritic, saving the result into two string variables: <code>titles</code> and <code>scores</code>

{% highlight javascript %}
{% raw %}
$$('.c-finderProductCard_titleHeading').forEach(function(element) { titles += element.children[1].innerHTML + "\n"; })
{% endraw %}
{% endhighlight %}

{% highlight javascript %}
{% raw %}
$$('.c-siteReviewScore').forEach(function(element) { scores += element.children[0].innerHTML + "\n"; })
{% endraw %}
{% endhighlight %}

### Step 4. Copy paste to save structured data

With the query done, just print and copy your structured data to the clipboard. Enjoy!

![JavaScript DOM query result](/img/posts/browser-dom-query-result.png)

