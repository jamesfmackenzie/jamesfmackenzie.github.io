---
layout: post
title: Getting Started With the Pocket Developer API
date: '2014-12-21 00:48:10'
summary: I want to automatically extract the video from my Pocketed content and sync it to my phone. To do this, I’ll need to extend Pocket via the Developer API. Here’s how to get started ...
image: 2014-12-20-19_05_12-Pocket_-Developer-API.png
tags: [API, How To, Programming, Web Development]
permalink: /getting-started-with-the-pocket-developer-api/
---

### Updated 2016-03-31 to use the Pocket HTTPS API

I want to [automatically extract the video from my Pocketed content and sync it to my phone]({% post_url 2014-12-17-i-cant-stream-video-on-the-commute-how-can-i-fix-it %}). To do this, I'll need to extend Pocket via the <a href="http://getpocket.com/developer/" target="_blank">Developer API</a>. Here's how to get started.

### Step 1. Create an App in the Pocket Developer Portal, Get Your Consumer Key

Head over to the <a href="http://getpocket.com/developer/" target="_blank">Pocket Developer Portal</a> and create a new App. It doesn't really matter how you fill out the fields as long as you remember to:

* Give your App the right permissions:
	* Add - to add new items to Pocket
    * Modify - to modify existing items in Pocket
    * Retrieve - to retrieve items from Pocket
* Make a note of the **Consumer Key** (see screenshot below)

![](/img/posts/2014-12-20-19_05_12-Pocket_-Developer-API.png)

![](/img/posts/2014-12-20-23_39_03-Pocket_-Developer-API.png)

### Step 2. Obtain a Request Token

Using your new **Consumer Key**, issue a POST request (I prefer <a href="http://curl.haxx.se/" target="_blank">cURL</a>) to get a temporary **Request Token**. This'll be used to authorize your new App.

Two mandatory parameters which *must* be included in the POST body:

* **consumer_key** - Consumer Key retrieved above
* **redirect_uri** - URL to be called when the authorization process has been completed. Since we're doing this manually, we can set this to anything we like (e.g. http://www.google.com)

**Method URL**
<pre>
https://getpocket.com/v3/oauth/request
</pre>

**Example Request**
{% highlight http %}
{% raw %}
POST /v3/oauth/request HTTP/1.1
Host: getpocket.com
Content-Type: application/json
X-Accept: application/json

{"consumer_key":"1234-abcd1234abcd1234abcd1234",
"redirect_uri":"http://www.google.com"}
{% endraw %}
{% endhighlight %}

**Example Request (cURL)**
{% highlight bash %}
{% raw %}
curl https://getpocket.com/v3/oauth/request --insecure -X POST -H "Content-Type: application/json" -H "X-Accept: application/json" -d "{\"consumer_key\":\"1234-abcd1234abcd1234abcd1234\",\"redirect_uri\":\"http://www.google.com\"}"
{% endraw %}
{% endhighlight %}

**Example Response**
{% highlight http %}
{% raw %}
HTTP/1.1 200 OK
Content-Type: application/json
Status: 200 OK

{"code":"dcba4321-dcba-4321-dcba-4321dc"}
{% endraw %}
{% endhighlight %}

Make a note of this Request Token. You'll need it for the next step.

### Step 3. Visit the Pocket Website to Authorize Your App

Manufacture the following URL and open it in your Browser:

<pre>
https://getpocket.com/auth/authorize?request_token=YOUR_REQUEST_TOKEN&redirect_uri=YOUR_REDIRECT_URI
</pre>

e.g.

<pre>
https://getpocket.com/auth/authorize?request_token=dcba4321-dcba-4321-dcba-4321dc&redirect_uri=http://www.google.com
</pre>

You'll be prompted to login to Pocket (if you aren't already) and authorize your new App

![](/img/posts/2014-12-21-00_23_49-Pocket_-Authorize-App.png)

Upon clicking Authorize, you'll be sent back to the redirect URL (in this case http://www.google.com) - authorization done.

### Step 4. Convert your Request Token Into a Pocket Access Token

Issue the following POST request to obtain a **Pocket Access Token**:

**Mandatory Parameters**

* **consumer_key** - Consumer Key retrieved in Step 1
* **code** - Request Token retrieved in Step 2

**Method URL**
<pre>
https://getpocket.com/v3/oauth/authorize
</pre>

**Example Request**
{% highlight http %}
{% raw %}
POST /v3/oauth/authorize HTTP/1.1
Host: getpocket.com
Content-Type: application/json
X-Accept: application/json

{"consumer_key":"1234-abcd1234abcd1234abcd1234",
"code":"dcba4321-dcba-4321-dcba-4321dc"}
{% endraw %}
{% endhighlight %}

**Example Request (cURL)**
{% highlight bash %}
{% raw %}
curl https://getpocket.com/v3/oauth/authorize --insecure -X POST -H "Content-Type: application/json" -H "X-Accept: application/json" -d "{\"consumer_key\":\"1234-abcd1234abcd1234abcd1234\",\"code\":\"dcba4321-dcba-4321-dcba-4321dc\"}"
{% endraw %}
{% endhighlight %}

**Example Response**
{% highlight http %}
{% raw %}
HTTP/1.1 200 OK
Content-Type: application/json
Status: 200 OK

{"access_token":"5678defg-5678-defg-5678-defg56",
"username":"pocketuser"}
{% endraw %}
{% endhighlight %}

**Make a note of this Access Token. This is the token you can use to make authenticated requests against the Pocket API on a permanent basis**.

### Step 5. Make Authenticated Requests Against the Pocket API

All done! Now you have an Access Token you can make authenticated requests against the Pocket API.

E.g. to retrieve your Pocketed items:

**Mandatory Parameters**

* **consumer_key** - Consumer Key (retrieved in Step 1)
* **access_token** - Access Token (retrieved in Step 4)

**Method URL**
<pre>
https://getpocket.com/v3/get
</pre>

**Example Request**
{% highlight http %}
{% raw %}
POST /v3/get HTTP/1.1
Host: getpocket.com
Content-Type: application/json

{"consumer_key":"1234-abcd1234abcd1234abcd1234",
"access_token":"5678defg-5678-defg-5678-defg56"}
{% endraw %}
{% endhighlight %}

**Example Request (cURL)**
{% highlight bash %}
{% raw %}
curl https://getpocket.com/v3/get --insecure -X POST -H "Content-Type: application/json" -H "X-Accept: application/json" -d "{\"consumer_key\":\"1234-abcd1234abcd1234abcd1234\", \"access_token\":\"5678defg-5678-defg-5678-defg56\"}"
{% endraw %}
{% endhighlight %}

**Example Response**
{% highlight json %}
{% raw %}
{
  "status": 1,
  "complete": 1,
  "list": {
    "786228232": {
      "item_id": "786228232",
      "resolved_id": "786228232",
      "given_url": "http://m.bbc.co.uk/news/entertainment-arts-30392163",
      "given_title": "Mark Ronson single rush-released after Fleur East's X Factor performance - ",
      "favorite": "0",
      "status": "0",
      "time_added": "1418118328",
      "time_updated": "1418118329",
      "time_read": "0",
      "time_favorited": "0",
      "sort_id": 0,
      "resolved_title": "Mark Ronson single rush-released after Fleur East's X Factor performance",
      "resolved_url": "http://m.bbc.co.uk/news/entertainment-arts-30392163",
      "excerpt": "The release date of Mark Ronson's single Uptown Funk has been brought forward by five weeks after an X Factor cover topped the iTunes chart.  Fleur East's version of the track was called \"one of the top three performances\" in X Factor history by Simon Cowell.",
      "is_article": "1",
      "is_index": "0",
      "has_video": "0",
      "has_image": "1",
      "word_count": "284"
    },
    "65587491": {
      "item_id": "65587491",
      "resolved_id": "65587491",
      "given_url": "https://pinboard.in/faq/",
      "given_title": "",
      "favorite": "0",
      "status": "0",
      "time_added": "1418107173",
      "time_updated": "1418107541",
      "time_read": "0",
      "time_favorited": "0",
      "sort_id": 1,
      "resolved_title": "Frequently Asked Questions",
      "resolved_url": "https://pinboard.in/faq/",
      "excerpt": "What is Pinboard?  Pinboard is a personal archive for links you find online. You save bookmarks to the site and can find and search them later from any computer. The site can automatically import your links and tweets from a number of outside services.",
      "is_article": "1",
      "is_index": "1",
      "has_video": "0",
      "has_image": "0",
      "word_count": "4340"
    },
    
... much more JSON
{% endraw %}
{% endhighlight %}

That's it!