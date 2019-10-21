---
layout: post
title: Understanding the Twitter API
date: '2015-02-25 17:06:57'
summary: Want to schedule a Twitter post for later? Or re-post a message at the same time every day? To get the most out of Twitter, you’ll want to extend it via the Developer API ...
tags: [Programming, API, How To, Twitter]
---

Want to schedule a Twitter post for later? Or re-post a message at the same time every day? To get the most out of Twitter, you'll want to extend it via the <a href="https://dev.twitter.com/rest/public" target="_blank">Developer API</a>.

In the real world, I'd always recommend that you <a href="http://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants" target="_blank">stand on the shoulders of giants</a> and find a <a href="https://dev.twitter.com/overview/api/twitter-libraries" target="_blank">Twitter Library</a> for your programming language of choice. But since this a learning exercise, we're going to build everything from scratch in <a href="http://en.wikipedia.org/wiki/Shell_script" target="_blank">UNIX shell script</a>.

### Step 1. Create an App in the Twitter Application Management Portal

Head over to <a href="https://apps.twitter.com/" target="_blank">https://apps.twitter.com/</a>, login and click "Create New App".

Choose a Name, Description, Website and Callback URL. Choose anything you like - even the Callback URL doesn't matter at this point. Accept the Developer Agreement and click "Create your Twitter application".

![](/img/posts/Create_an_application___Twitter_Application_Management_1.png)

### Step 2. Get your Consumer Keys and Access Tokens

On your application management page, navigate to the "Keys and Access Tokens" tab. Make a note of the "Consumer Key" and "Consumer Secret". You're going to need these.

Also note that the "Access Level" is Read-only by default. If you want you application to post Tweets, now is the time to change it to "Read and write".

![](/img/posts/jamesfmackenzie_com_Test_App___Twitter_Application_Management.png)

Next, scroll to the bottom of the page and click "Create my access token". This will generate an Access Token and Access Token Secret that let your new App make Twitter API calls on your account's behalf. Make a note of these too.

![](/img/posts/jamesfmackenzie_com_Test_App___Twitter_Application_Management_2.png)

If you want your App to make API calls on behalf of *other users*, there's a more complicated <a href="https://dev.twitter.com/web/sign-in/implementing" target="_blank">Authorization Process</a> your apps needs to follow. But we won't go into it today.

Before we move on, let's add these keys, tokens and secrets to our shell script as constants:

{% highlight bash %}
consumer_key="[YOUR CONSUMER TOKEN]"
consumer_secret="[YOUR CONSUMER TOKEN SECRET]"
access_token="[YOUR ACCESS TOKEN]"
access_token_secret="[YOUR ACCESS TOKEN SECRET]"
{% endhighlight %}

### Step 3. Establish request options

We've got all the tokens we need, but before making a request we need to choose a request method and the corresponding parameters.

You can see the full API listings <a href="https://dev.twitter.com/rest/public" target="_blank">here</a>, but for this example we'll use <a href="https://dev.twitter.com/rest/reference/get/statuses/user_timeline" target="_blank">GET statuses/user\_timeline</a>, which "returns a collection of the most recent Tweets posted by the user".

**Mandatory Parameters**

* **user\_id** OR **screen\_name** - The ID or screen name of the user for whom to return results for

**Optional Parameters**

* **count** - Specifies the number of tweets to try and retrieve, up to a maximum of 200 per distinct request

**Method URL**
<pre>
https://api.twitter.com/1.1/statuses/user_timeline.json
</pre>

**Method Verb**
<pre>
GET
</pre>

### Step 4. Add request options to shell script

Now we've established the request options, let's set these up as constants in our shell script too:

{% highlight bash %}
{% raw %}
method_verb="GET"
method_url="https://api.twitter.com/1.1/statuses/user_timeline.json"
screen_name="[YOUR SCREEN NAME]"
count=5
{% endraw %}
{% endhighlight %}

### Step 5. Make a request

OK, so we've got all the options, let's make a request!

**Example Request**
<pre>
GET
https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=jamesfmackenzie&count=5
</pre>

**Example Request (cURL)**
{% highlight bash %}
{% raw %}
curl --get 'https://api.twitter.com/1.1/statuses/user_timeline.json' --data 'count=5&screen_name=jamesfmackenzie'
{% endraw %}
{% endhighlight %}

Easy right? Well, not quite so easy. Issuing the request above yields the following response:

{% highlight bash %}
{% raw %}
$ curl --get 'https://api.twitter.com/1.1/statuses/user_timeline.json' --data 'count=5&screen_name=jamesfmackenzie'
{"errors":[{"code":215,"message":"Bad Authentication data."}]}
{% endraw %}
{% endhighlight %}

What went wrong? Well, it turns out that Twitter considers the above request invalid, because there's no way of knowing:

* Which application is making the request
* Which user the request is posting on behalf of
* Whether the user has granted the application authorization to post on the user's behalf
* Whether the request has been tampered by a third party while in transit

For our request to work, we need to provide these details to Twitter in the form of an *Authorization Header*.

### Step 6. Collect parameters for Authorization Header

In their <a href="https://dev.twitter.com/oauth/overview/authorizing-requests" target="_blank">documentation</a>, Twitter provide the following Authorization Header as an example:

{% highlight bash %}
{% raw %}
Authorization: OAuth
oauth_consumer_key="xvz1evFS4wEEPTGEFPHBog",
oauth_nonce="kYjzVBB8Y0ZFabxSWbWovY3uYSQ2pTgmZeNu2VS4cg",
oauth_signature="tnnArxj06cWHq44gCs1OSKk%2FjLY%3D",
oauth_signature_method="HMAC-SHA1",
oauth_timestamp="1318622958",
oauth_token="370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb",
oauth_version="1.0"
{% endraw %}
{% endhighlight %}

(Note: line breaks have been added for readability)

Let's run through the parameters one-by-one, checking them off:

**oauth\_consumer\_key**

Easy. This is the consumer\_key we created in Step 2.
 
**oauth\_nonce**

According to the documentation, this is "a unique token your application should generate for each unique request" and "any approach which produces a relatively random alphanumeric string should be OK".

For a one-off, you could just hammer away at the keyboard randomly. But a better approach is to generate the nonce. My approach:

* Use <a href="https://www.openssl.org/" target="_blank">OpenSSL</a>'s rand function to generate a random base64 encoded string
* Use <a href="http://en.wikipedia.org/wiki/Sed" target="_blank">sed</a> to strip out the non-alphanumeric characters

{% highlight bash %}
{% raw %}
nonce=`openssl rand -base64 32 | sed -e s'/[+=/]//g'`
{% endraw %}
{% endhighlight %}

**oauth_signature**

Ugh! This is a nasty one. The signature is created by running all the other request parameters through an annoyingly specific signing algorithm. The parameters include:

* **Method Verb**
* **Method URL**
* **Method Parameters**
* **All other Authorization Header parameters** - i.e. oauth\_consumer\_key, oauth\_nonce, oauth\_signature\_method, oauth\_timestamp, oauth\_token, oauth\_version

These parameters are then:

* <a href="http://en.wikipedia.org/wiki/Percent-encoding" target="_blank">Percent encoded</a>
* Sorted alphabetically
* Concatenated
* Signed using the consumer_secret and access_token_secret defined in Step 2. 

If you want more detail you can find it <a href="https://dev.twitter.com/oauth/overview/creating-signatures" target="_blank">here</a>. My implementation is as follows:

{% highlight bash %}
{% raw %}
# Use perl to percent encode the method url
percent_encoded_method_url=`echo ${method_url} | perl -MURI::Escape -ne 'chomp;print uri_escape($_),"\n"'`

# create signature base string (alphabetical sorting and some percent encoded is hardcoded)
signature_base_string="${method_verb}&${percent_encoded_method_url}&count%3D${count}%26oauth_consumer_key%3D${consumer_key}%26oauth_nonce%3D${nonce}%26oauth_signature_method%3D${oauth_signature_method}%26oauth_timestamp%3D${timestamp}%26oauth_token%3D${access_token}%26oauth_version%3D${oauth_version}%26screen_name%3D${screen_name}"

# create signature key
signature_key="${consumer_secret}&${access_token_secret}"

# sign signature base string with signature key to generate signature
oauth_signature=`echo -n ${signature_base_string} | openssl dgst -sha1 -hmac ${signature_key} -binary | openssl base64 | sed -e s'/+/%2B/' -e s'/\//%2F/' -e s'/=/%3D/'`
{% endraw %}
{% endhighlight %}

**oauth\_signature\_method**

Easy peasy. This is always hardcoded to "HMAC-SHA1".

{% highlight bash %}
{% raw %}
oauth_signature_method="HMAC-SHA1"
{% endraw %}
{% endhighlight %}

Note: make sure this is declared above the oauth_signature declaration

**oauth\_timestamp**

The number of seconds since UNIX epoch. You can use timestamp to generate this:

{% highlight bash %}
{% raw %}
timestamp=`date +%s` 
{% endraw %}
{% endhighlight %}

Note: make sure this is declared above the oauth_signature declaration

**oauth\_token**

This is the access\_token we created in Step 2.

**oauth\_version**

Last one (and an easy one). This is always hardcoded to "1.0".

{% highlight bash %}
{% raw %}
oauth_version="1.0" 
{% endraw %}
{% endhighlight %}

Note: make sure this is declared above the oauth_signature declaration

### Step 7. Create Authorization Header

Finally! Now we've got all the parameters together, we can switch them together to create the Authorization Header:

{% highlight bash %}
{% raw %}
Authorization: OAuth
oauth_consumer_key="[YOUR CONSUMER KEY]",
oauth_nonce="[YOUR GENERATED NONCE]",
oauth_signature="[YOUR GENERATED SIGNATURE]",
oauth_signature_method="HMAC-SHA1",
oauth_timestamp="[YOUR GENERATED TIMESTAMP]",
oauth_token="[YOUR ACCESS TOKEN]",
oauth_version="1.0"
{% endraw %}
{% endhighlight %}

My implementation:

{% highlight bash %}
{% raw %}
header="Authorization: OAuth oauth_consumer_key=\"${consumer_key}\", oauth_nonce=\"${nonce}\", oauth_signature=\"${oauth_signature}\", oauth_signature_method=\"${oauth_signature_method}\", oauth_timestamp=\"${timestamp}\", oauth_token=\"${access_token}\", oauth_version=\"${oauth_version}\""
{% endraw %}
{% endhighlight %}

### Step 8. Make Authenticated Requests Against the Twitter API

All done! Now you're ready to make authorized requests against the Twitter API.

To retrieve your 5 most recent Tweets using cURL:

{% highlight bash %}
{% raw %}
result=`curl --get "${method_url}" --data "screen_name=${screen_name}&count=${count}" --header "${header}"`
echo "${result}"
{% endraw %}
{% endhighlight %}

**Example Response**
{% highlight json %}
{% raw %}
[
   {
      "created_at":"Tue Feb 24 03:35:14 +0000 2015",
      "id":570064382656253952,
      "id_str":"570064382656253952",
      "text":"Oh, and current TVs don't support all the #4KBD features like HDR and expanded color gamut. If you want the best quality you should hold off",
      "source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e",
      "truncated":false,
      "in_reply_to_status_id":null,
      "in_reply_to_status_id_str":null,
      "in_reply_to_user_id":null,
      "in_reply_to_user_id_str":null,
      "in_reply_to_screen_name":null,
      "user":{
         "id":165913533,
         "id_str":"165913533",
         "name":"James Mackenzie",
         "screen_name":"jamesfmackenzie",
         "location":"London",
         "profile_location":null,
         "description":"Science, Computers, Programming. All good.",
         "url":"http:\/\/t.co\/GUwCHWp6xx",
         "entities":{
            "url":{
               "urls":[
                  {
                     "url":"http:\/\/t.co\/GUwCHWp6xx",
                     "expanded_url":"http:\/\/www.jamesfmackenzie.com",
                     "display_url":"jamesfmackenzie.com",
                     "indices":[
                        0,
                        22
                     ]
                  }
               ]
            },
            "description":{
               "urls":[

               ]
            }
         },
         "protected":false,
         "followers_count":733,
         "friends_count":1375,
         "listed_count":31,
         "created_at":"Mon Jul 12 21:36:16 +0000 2010",
         "favourites_count":148,
         "utc_offset":0,
         "time_zone":"London",
         "geo_enabled":true,
         "verified":false,
         "statuses_count":1649,
         "lang":"en",
         "contributors_enabled":false,
         "is_translator":false,
         "is_translation_enabled":false,
         "profile_background_color":"666666",
         "profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_tile":true,
         "profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_link_color":"444444",
         "profile_sidebar_border_color":"FFFFFF",
         "profile_sidebar_fill_color":"DDEEF6",
         "profile_text_color":"333333",
         "profile_use_background_image":false,
         "default_profile":false,
         "default_profile_image":false,
         "following":false,
         "follow_request_sent":false,
         "notifications":false
      },
      "geo":null,
      "coordinates":null,
      "place":null,
      "contributors":null,
      "retweet_count":0,
      "favorite_count":0,
      "entities":{
         "hashtags":[
            {
               "text":"4KBD",
               "indices":[
                  42,
                  47
               ]
            }
         ],
         "symbols":[

         ],
         "user_mentions":[

         ],
         "urls":[

         ]
      },
      "favorited":false,
      "retweeted":false,
      "lang":"en"
   },
   {
      "created_at":"Tue Feb 24 03:29:59 +0000 2015",
      "id":570063061479874560,
      "id_str":"570063061479874560",
      "text":"100GB disk, 2 hour movie = 111Mbit\/s. So until your broadband\/wifi combo exceeds that, it's reasonable to expect better quality from #4KBD",
      "source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e",
      "truncated":false,
      "in_reply_to_status_id":null,
      "in_reply_to_status_id_str":null,
      "in_reply_to_user_id":null,
      "in_reply_to_user_id_str":null,
      "in_reply_to_screen_name":null,
      "user":{
         "id":165913533,
         "id_str":"165913533",
         "name":"James Mackenzie",
         "screen_name":"jamesfmackenzie",
         "location":"London",
         "profile_location":null,
         "description":"Science, Computers, Programming. All good.",
         "url":"http:\/\/t.co\/GUwCHWp6xx",
         "entities":{
            "url":{
               "urls":[
                  {
                     "url":"http:\/\/t.co\/GUwCHWp6xx",
                     "expanded_url":"http:\/\/www.jamesfmackenzie.com",
                     "display_url":"jamesfmackenzie.com",
                     "indices":[
                        0,
                        22
                     ]
                  }
               ]
            },
            "description":{
               "urls":[

               ]
            }
         },
         "protected":false,
         "followers_count":733,
         "friends_count":1375,
         "listed_count":31,
         "created_at":"Mon Jul 12 21:36:16 +0000 2010",
         "favourites_count":148,
         "utc_offset":0,
         "time_zone":"London",
         "geo_enabled":true,
         "verified":false,
         "statuses_count":1649,
         "lang":"en",
         "contributors_enabled":false,
         "is_translator":false,
         "is_translation_enabled":false,
         "profile_background_color":"666666",
         "profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_tile":true,
         "profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_link_color":"444444",
         "profile_sidebar_border_color":"FFFFFF",
         "profile_sidebar_fill_color":"DDEEF6",
         "profile_text_color":"333333",
         "profile_use_background_image":false,
         "default_profile":false,
         "default_profile_image":false,
         "following":false,
         "follow_request_sent":false,
         "notifications":false
      },
      "geo":null,
      "coordinates":null,
      "place":null,
      "contributors":null,
      "retweet_count":0,
      "favorite_count":0,
      "entities":{
         "hashtags":[
            {
               "text":"4KBD",
               "indices":[
                  133,
                  138
               ]
            }
         ],
         "symbols":[

         ],
         "user_mentions":[

         ],
         "urls":[

         ]
      },
      "favorited":false,
      "retweeted":false,
      "lang":"en"
   },
   {
      "created_at":"Tue Feb 24 03:27:51 +0000 2015",
      "id":570062525519302656,
      "id_str":"570062525519302656",
      "text":"Nice primer on #4KBD. \"Ultra HD '4K' Blu-ray: Here's what we know\" http:\/\/t.co\/hiQYV94nxg",
      "source":"\u003ca href=\"http:\/\/bufferapp.com\" rel=\"nofollow\"\u003eBuffer\u003c\/a\u003e",
      "truncated":false,
      "in_reply_to_status_id":null,
      "in_reply_to_status_id_str":null,
      "in_reply_to_user_id":null,
      "in_reply_to_user_id_str":null,
      "in_reply_to_screen_name":null,
      "user":{
         "id":165913533,
         "id_str":"165913533",
         "name":"James Mackenzie",
         "screen_name":"jamesfmackenzie",
         "location":"London",
         "profile_location":null,
         "description":"Science, Computers, Programming. All good.",
         "url":"http:\/\/t.co\/GUwCHWp6xx",
         "entities":{
            "url":{
               "urls":[
                  {
                     "url":"http:\/\/t.co\/GUwCHWp6xx",
                     "expanded_url":"http:\/\/www.jamesfmackenzie.com",
                     "display_url":"jamesfmackenzie.com",
                     "indices":[
                        0,
                        22
                     ]
                  }
               ]
            },
            "description":{
               "urls":[

               ]
            }
         },
         "protected":false,
         "followers_count":733,
         "friends_count":1375,
         "listed_count":31,
         "created_at":"Mon Jul 12 21:36:16 +0000 2010",
         "favourites_count":148,
         "utc_offset":0,
         "time_zone":"London",
         "geo_enabled":true,
         "verified":false,
         "statuses_count":1649,
         "lang":"en",
         "contributors_enabled":false,
         "is_translator":false,
         "is_translation_enabled":false,
         "profile_background_color":"666666",
         "profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_tile":true,
         "profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_link_color":"444444",
         "profile_sidebar_border_color":"FFFFFF",
         "profile_sidebar_fill_color":"DDEEF6",
         "profile_text_color":"333333",
         "profile_use_background_image":false,
         "default_profile":false,
         "default_profile_image":false,
         "following":false,
         "follow_request_sent":false,
         "notifications":false
      },
      "geo":null,
      "coordinates":null,
      "place":null,
      "contributors":null,
      "retweet_count":0,
      "favorite_count":0,
      "entities":{
         "hashtags":[
            {
               "text":"4KBD",
               "indices":[
                  15,
                  20
               ]
            }
         ],
         "symbols":[

         ],
         "user_mentions":[

         ],
         "urls":[
            {
               "url":"http:\/\/t.co\/hiQYV94nxg",
               "expanded_url":"http:\/\/cnet.co\/1MNZmOo",
               "display_url":"cnet.co\/1MNZmOo",
               "indices":[
                  67,
                  89
               ]
            }
         ]
      },
      "favorited":false,
      "retweeted":false,
      "possibly_sensitive":false,
      "lang":"en"
   },
   {
      "created_at":"Mon Feb 23 18:12:01 +0000 2015",
      "id":569922641697640448,
      "id_str":"569922641697640448",
      "text":"Made me LOL because it's true. \"vi has two modes \u2013 'beep repeatedly' and 'break everything'\" http:\/\/t.co\/NauklKGvpi",
      "source":"\u003ca href=\"http:\/\/bufferapp.com\" rel=\"nofollow\"\u003eBuffer\u003c\/a\u003e",
      "truncated":false,
      "in_reply_to_status_id":null,
      "in_reply_to_status_id_str":null,
      "in_reply_to_user_id":null,
      "in_reply_to_user_id_str":null,
      "in_reply_to_screen_name":null,
      "user":{
         "id":165913533,
         "id_str":"165913533",
         "name":"James Mackenzie",
         "screen_name":"jamesfmackenzie",
         "location":"London",
         "profile_location":null,
         "description":"Science, Computers, Programming. All good.",
         "url":"http:\/\/t.co\/GUwCHWp6xx",
         "entities":{
            "url":{
               "urls":[
                  {
                     "url":"http:\/\/t.co\/GUwCHWp6xx",
                     "expanded_url":"http:\/\/www.jamesfmackenzie.com",
                     "display_url":"jamesfmackenzie.com",
                     "indices":[
                        0,
                        22
                     ]
                  }
               ]
            },
            "description":{
               "urls":[

               ]
            }
         },
         "protected":false,
         "followers_count":733,
         "friends_count":1375,
         "listed_count":31,
         "created_at":"Mon Jul 12 21:36:16 +0000 2010",
         "favourites_count":148,
         "utc_offset":0,
         "time_zone":"London",
         "geo_enabled":true,
         "verified":false,
         "statuses_count":1649,
         "lang":"en",
         "contributors_enabled":false,
         "is_translator":false,
         "is_translation_enabled":false,
         "profile_background_color":"666666",
         "profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_tile":true,
         "profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_link_color":"444444",
         "profile_sidebar_border_color":"FFFFFF",
         "profile_sidebar_fill_color":"DDEEF6",
         "profile_text_color":"333333",
         "profile_use_background_image":false,
         "default_profile":false,
         "default_profile_image":false,
         "following":false,
         "follow_request_sent":false,
         "notifications":false
      },
      "geo":null,
      "coordinates":null,
      "place":null,
      "contributors":null,
      "retweet_count":0,
      "favorite_count":0,
      "entities":{
         "hashtags":[

         ],
         "symbols":[

         ],
         "user_mentions":[

         ],
         "urls":[
            {
               "url":"http:\/\/t.co\/NauklKGvpi",
               "expanded_url":"http:\/\/bit.ly\/1CzDdh7",
               "display_url":"bit.ly\/1CzDdh7",
               "indices":[
                  93,
                  115
               ]
            }
         ]
      },
      "favorited":false,
      "retweeted":false,
      "possibly_sensitive":false,
      "lang":"en"
   },
   {
      "created_at":"Sun Feb 22 18:12:17 +0000 2015",
      "id":569560320810852353,
      "id_str":"569560320810852353",
      "text":"A really nice, structured collection of #AngularJS training resources. \"A Better Way to Learn AngularJS\" http:\/\/t.co\/utQMj52ZyZ",
      "source":"\u003ca href=\"http:\/\/bufferapp.com\" rel=\"nofollow\"\u003eBuffer\u003c\/a\u003e",
      "truncated":false,
      "in_reply_to_status_id":null,
      "in_reply_to_status_id_str":null,
      "in_reply_to_user_id":null,
      "in_reply_to_user_id_str":null,
      "in_reply_to_screen_name":null,
      "user":{
         "id":165913533,
         "id_str":"165913533",
         "name":"James Mackenzie",
         "screen_name":"jamesfmackenzie",
         "location":"London",
         "profile_location":null,
         "description":"Science, Computers, Programming. All good.",
         "url":"http:\/\/t.co\/GUwCHWp6xx",
         "entities":{
            "url":{
               "urls":[
                  {
                     "url":"http:\/\/t.co\/GUwCHWp6xx",
                     "expanded_url":"http:\/\/www.jamesfmackenzie.com",
                     "display_url":"jamesfmackenzie.com",
                     "indices":[
                        0,
                        22
                     ]
                  }
               ]
            },
            "description":{
               "urls":[

               ]
            }
         },
         "protected":false,
         "followers_count":733,
         "friends_count":1375,
         "listed_count":31,
         "created_at":"Mon Jul 12 21:36:16 +0000 2010",
         "favourites_count":148,
         "utc_offset":0,
         "time_zone":"London",
         "geo_enabled":true,
         "verified":false,
         "statuses_count":1649,
         "lang":"en",
         "contributors_enabled":false,
         "is_translator":false,
         "is_translation_enabled":false,
         "profile_background_color":"666666",
         "profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/668567178\/9627556962007cb48e3344e03dd8a374.png",
         "profile_background_tile":true,
         "profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/531419563422801921\/sdtKDzv4_normal.png",
         "profile_link_color":"444444",
         "profile_sidebar_border_color":"FFFFFF",
         "profile_sidebar_fill_color":"DDEEF6",
         "profile_text_color":"333333",
         "profile_use_background_image":false,
         "default_profile":false,
         "default_profile_image":false,
         "following":false,
         "follow_request_sent":false,
         "notifications":false
      },
      "geo":null,
      "coordinates":null,
      "place":null,
      "contributors":null,
      "retweet_count":1,
      "favorite_count":2,
      "entities":{
         "hashtags":[
            {
               "text":"AngularJS",
               "indices":[
                  40,
                  50
               ]
            }
         ],
         "symbols":[

         ],
         "user_mentions":[

         ],
         "urls":[
            {
               "url":"http:\/\/t.co\/utQMj52ZyZ",
               "expanded_url":"http:\/\/bit.ly\/1v47RiB",
               "display_url":"bit.ly\/1v47RiB",
               "indices":[
                  105,
                  127
               ]
            }
         ]
      },
      "favorited":false,
      "retweeted":false,
      "possibly_sensitive":false,
      "lang":"en"
   }
]
{% endraw %}
{% endhighlight %}

That's it! I hope to make use of the Twitter API over the next few weeks and post something interesting/useful.

### Full code listing
{% highlight bash %}
{% raw %}
#!/bin/bash

consumer_key="Bg6pHWiVYhmi3y79ZuBMQ"
consumer_secret="eSZxN15yTlqoxpbhOdM6SWHERi8VqiU8TVs4VZtPc"
access_token="165913533-p7glGCmvZyapIGW7sk2kIGzTygNrqfWOG9FfJBJr"
access_token_secret="bwYnLDcv4SsVw9lEubsFfmvph2ZunpdJdyOBQqBJGODbd"

method_verb="GET"
method_url="https://api.twitter.com/1.1/statuses/user_timeline.json"
screen_name="jamesfmackenzie"
count=5

nonce=`openssl rand -base64 32 | sed -e s'/[+=/]//g'`

oauth_version="1.0"

oauth_signature_method="HMAC-SHA1"

timestamp=`date +%s` 

# Use perl to percent encode the method url
percent_encoded_method_url=`echo ${method_url} | perl -MURI::Escape -ne 'chomp;print uri_escape($_),"\n"'`

# create signature base string (alphabetical sorting and some percent encoded is hardcoded)
signature_base_string="${method_verb}&${percent_encoded_method_url}&count%3D${count}%26oauth_consumer_key%3D${consumer_key}%26oauth_nonce%3D${nonce}%26oauth_signature_method%3D${oauth_signature_method}%26oauth_timestamp%3D${timestamp}%26oauth_token%3D${access_token}%26oauth_version%3D${oauth_version}%26screen_name%3D${screen_name}"
echo "${signature_base_string}"

# create signature key
signature_key="${consumer_secret}&${access_token_secret}"
echo "${signature_key}"

# sign signature base string with signature key to generate signature
oauth_signature=`echo -n ${signature_base_string} | openssl dgst -sha1 -hmac ${signature_key} -binary | openssl base64 | sed -e s'/+/%2B/' -e s'/\//%2F/' -e s'/=/%3D/'`
echo "${oauth_signature}"

header="Authorization: OAuth oauth_consumer_key=\"${consumer_key}\", oauth_nonce=\"${nonce}\", oauth_signature=\"${oauth_signature}\", oauth_signature_method=\"${oauth_signature_method}\", oauth_timestamp=\"${timestamp}\", oauth_token=\"${access_token}\", oauth_version=\"${oauth_version}\""
echo "${header}"

result=`curl --get "${method_url}" --data "screen_name=${screen_name}&count=${count}" --header "${header}"`
echo "${result}"
{% endraw %}
{% endhighlight %}
