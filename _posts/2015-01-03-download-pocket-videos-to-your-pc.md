---
layout: post
title: Download Pocket Videos to Your PC
date: '2015-01-03 00:47:50'
tags: [Automation, Productivity, Lifehacks, Programming, Web Development]
---

As [mentioned before](), I want to automatically extract the video from my Pocketed content and sync it to my phone. To achieve this, I'm going to:

1. Scan my Pocketed items for video, download the videos to my PC
2. Sync the videos from my PC to the phone

Here's how to do the former.

### Step 1. Download required tooling

Download and install the following tools on your machine. You'll need to make sure they're in your <a href="http://en.wikipedia.org/wiki/PATH_%28variable%29" target="_blank">PATH</a> too (<a href="http://www.computerhope.com/issues/ch000549.htm" target="_blank">this</a> might help).

* <a href="http://curl.haxx.se/" target="_blank">cURL</a> - "a command line tool and library for transferring data with URL syntax"
* <a href="http://stedolan.github.io/jq/" target="_blank">jq</a> - "a lightweight and flexible command-line JSON processor"
* <a href="http://rg3.github.io/youtube-dl/" target="_blank">youtube-dl</a> - "a small command-line program to download videos from YouTube.com and a few more sites"

### Step 2. Get a Pocket Access token

You'll need a Pocket Access token before you can make authenticated requests against the Pocket API. Follow my guide <a href="/getting-started-with-the-pocket-developer-api/">here</a> to get one.

### Step 3. Ask the Pocket API which of your items have embedded videos

Using cURL, make an authenticated request against the Pocket API and download all the items which have a contentType of "video". You'll need to swap out the consumer key and access token below for your own.

**Method URL**
<pre>
https://getpocket.com/v3/get
</pre>

**Example HTTP Request**
{% highlight http %}
{% raw %}
POST /v3/get HTTP/1.1
Host: getpocket.com
Content-Type: application/json

{"consumer_key":"1234-abcd1234abcd1234abcd1234",
"access_token":"5678defg-5678-defg-5678-defg56",
"detailType":"complete",
"contentType":"video"}
{% endraw %}
{% endhighlight %}

**Example HTTP Request (cURL)**
{% highlight bash %}
{% raw %}
curl http://getpocket.com/v3/get -X POST -H "Content-Type: application/json" -H "X-Accept: application/json" -d "{\"consumer_key\":\"1234-abcd1234abcd1234abcd1234\", \"access_token\":\"5678defg-5678-defg-5678-defg56\", \"detailType\":\"complete\", \"contentType\":\"video\"}"
{% endraw %}
{% endhighlight %}

**Example HTTP Response**
{% highlight json %}
{
  "status": 1,
  "complete": 1,
  "list": {
    "796410494": {
      "item_id": "796410494",
      "resolved_id": "796410494",
      "given_url": "https://m.youtube.com/watch?feature=youtu.be%26v=vXr-2hwTk58",
      "given_title": "The Internets Own Boy: The Story of Aaron Swartz",
      "favorite": "0",
      "status": "0",
      "time_added": "1419176466",
      "time_updated": "1419176466",
      "time_read": "0",
      "time_favorited": "0",
      "sort_id": 0,
      "resolved_title": "The Internet's Own Boy: The Story of Aaron Swartz (CC available: en,es,ru,fr,it,tr,cn,ja,vi)",
      "resolved_url": "https://m.youtube.com/watch?feature=youtu.be%26v=vXr-2hwTk58",
      "excerpt": "The film follows the story of programming prodigy and information activist Aaron Swartz. From Swartz's help in the development of the basic internet protocol RSS to his co-founding of Reddit, his fingerprints are all over the internet. But it was Swartz's groundbreaking work in social justice and po",
      "is_article": "0",
      "is_index": "0",
      "has_video": "2",
      "has_image": "1",
      "word_count": "0",
      "tags": {
        "onlineonly": {
          "item_id": "796410494",
          "tag": "onlineonly"
        }
      },
      "image": {
        "item_id": "796410494",
        "src": "http://img.youtube.com/vi/vXr-2hwTk58/0.jpg",
        "width": "480",
        "height": "360"
      },
      "images": {
        "1": {
          "item_id": "796410494",
          "image_id": "1",
          "src": "http://img.youtube.com/vi/vXr-2hwTk58/0.jpg",
          "width": "480",
          "height": "360",
          "credit": "",
          "caption": ""
        }
      },
      "videos": {
        "1": {
          "item_id": "796410494",
          "video_id": "1",
          "src": "http://www.youtube.com/v/vXr-2hwTk58"
          "width": "0",
          "height": "0",
          "type": "1",
          "vid": "vXr-2hwTk58"
        }
      }
    },
    "766276760": {
      "item_id": "766276760",
      "resolved_id": "766276760",
      "given_url": "http://vimeo.com/m/49367318",
      "given_title": "Design For Replaceability - Architecture For An Agile Lifestyle",
      "favorite": "0",
      "status": "0",
      "time_added": "1419176466",
      "time_updated": "1419176466",
      "time_read": "0",
      "time_favorited": "0",
      "sort_id": 1,
      "resolved_title": "Design For Replaceability - Architecture For An Agile Lifestyle",
      "resolved_url": "http://vimeo.com/m/49367318",
      "excerpt": "The most important question to be asked when developing a new software system is \"How will we replace it?\" It is however a question seldom asked. Instead organization focus on reusability, which unfortunately helps create rigid and inflexible architectures. The talk shows how to design systems made",
      "is_article": "0",
      "is_index": "0",
      "has_video": "2",
      "has_image": "1",
      "word_count": "0",
      "tags": {
        "onlineonly": {
          "item_id": "766276760",
          "tag": "onlineonly"
        }
      },
      "authors": {
        "1288911": {
          "item_id": "766276760",
          "author_id": "1288911",
          "name": "JavaZone",
          "url": "http://vimeo.com/javazone"
        }
      },
      "image": {
        "item_id": "766276760",
        "src": "http://i.vimeocdn.com/video/340591828_640.jpg",
        "width": "640",
        "height": "360"
      },
      "images": {
        "1": {
          "item_id": "766276760",
          "image_id": "1",
          "src": "http://i.vimeocdn.com/video/340591828_640.jpg",
          "width": "640",
          "height": "360",
          "credit": "",
          "caption": ""
        }
      },
      "videos": {
        "1": {
          "item_id": "766276760",
          "video_id": "1",
          "src": "http://vimeo.com/play_redirect?clip_id=49367318&quality=hd"
          "width": "0",
          "height": "0",
          "type": "2",
          "vid": "49367318"
        }
      }
    },
   
... Lots more JSON
{% endhighlight %}

See the video URLs above? We want to download from each one of those. But first we need to parse them out somehow.

### Step 4. Parse out video URLs using jq

jq is a command line JSON processor. We can use it to separate out our previous video URLs from all that other JSON data - and dump the results into a file. Here's how:

**This command line call ...**
{% highlight bash %}
{% raw %}
curl http://getpocket.com/v3/get -X POST -H "Content-Type: application/json" -H "X-Accept: application/json" -d "{\"consumer_key\":\"35939-55223ffc2c3e123d25dc67e4\", \"access_token\":\"b59ef60e-a7fe-76a8-750b-87edfc\", \"detailType\":\"complete\", \"contentType\":\"video\"}" | jq -r .list[].videos[]?.src > output.txt
{% endraw %}
{% endhighlight %}

**... dumps all the video URLs in the response body to output.txt**
<pre>
output.txt
----
http://www.youtube.com/v/vXr-2hwTk58
http://vimeo.com/play_redirect?clip_id=49367318&quality=hd
http://www.youtube.com/embed/BTUMKkAXe7M?showsearch=0&modestbranding=1
http://www.youtube.com/v/QdVFvsCWXrA
//www.youtube.com/embed/UXjTEw9Qm0k
http://no-mans-sky.com/elk/wp-content/themes/nomanssky/images/loop.mp4
http://no-mans-sky.com/elk/wp-content/themes/nomanssky/images/loop.webm
http://www.youtube.com/v/1sFhOWPD-uA?fs=1&hl=en_US
http://player.vimeo.com/video/70417843
http://www.youtube.com/embed/TCswu85rJYY?wmode=transparent&rel=0&autohide=1&showinfo=0&enablejsapi=1
http://www.youtube.com/embed/Snyo6kSnGt4?wmode=transparent&rel=0&autohide=1&showinfo=0&enablejsapi=1
http://www.youtube.com/v/PGRRXKek8G0
chezbruce.swf
rc_img/rc_logo_2.swf
http://www.youtube.com/embed/AcqWohF1YFo
http://www.youtube.com/v/u0tSlCt33ac&hl=ru_RU&fs=1&autoplay=1
//www.youtube.com/embed/YxgsxaFWWHQ
</pre>

If you're interested in jq, you can find out more <a href="http://stedolan.github.io/jq/" target="_blank">here</a>. But back to the task at hand. We have a bunch of video URLs. How do we download them?

### Step 5. Download videos using youtube-dl

Youtube-dl is an open source video downloader. It was initially built for YouTube only, but it's expanded over time to support many online video sites and formats.

**This command line call ...**
{% highlight bat %}
{% raw %}
youtube-dl.exe --ignore-errors --batch-file ./video-downloader/urls.txt --continue --no-part --no-overwrites -f 135+140/0 1>> ./video-downloader/log.txt 2>&1
{% endraw %}
{% endhighlight %}

**... downloads all the videos referenced in output.txt to the current directory**

![](/img/posts/2015-01-03-00_36_48-Downloaded-Videos.png)

To find out more about the youtube-dl configuration options, head over <a href="http://rg3.github.io/youtube-dl/documentation.html" target="_blank">here</a>. You should also read up on <a href="http://en.wikipedia.org/wiki/YouTube#Quality_and_formats" target="_blank">YouTube's Media and Encoding Options</a>.

### Step 6. Putting it all together

That's it! Pretty easy right? To make things even easier, copy and paste the lines below into a new cmd script (I called mine <code>video-downloader.cmd</code>) and leave it minimized and running on your PC. Any videos you add to Pocket will be automatically downloaded to your PC - ace!

{% highlight bat %}
{% raw %}
:beginloop

:: download, parse video URLs from Pocket and flush into a text file
curl http://getpocket.com/v3/get -X POST -H "Content-Type: application/json" -H "X-Accept: application/json" -d "{\"consumer_key\":\"1234-abcd1234abcd1234abcd1234\", \"access_token\":\"5678defg-5678-defg-5678-defg56\", \"detailType\":\"complete\", \"contentType\":\"video\"}" | jq -r .list[].videos[]?.src > urls.txt

:: download videos to the file system, skipping those already downloaded
youtube-dl.exe --restrict-filenames --ignore-errors --batch-file urls.txt --continue --no-part --no-overwrites -f 135+140/18/h264-sd/mp4/webm/swf/0 1>> log.txt 2>&1

:: sleep for 20 minutes
timeout /t 1200 /nobreak

:: start again
goto beginloop
{% endraw %}
{% endhighlight %}

