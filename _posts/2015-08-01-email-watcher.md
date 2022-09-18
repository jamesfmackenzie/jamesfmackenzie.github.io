---
layout: post
title: EmailWatcher - a .NET Library for Email Automation
date: '2015-08-01 23:13:05'
summary: Jobs to download videos for me. Jobs to Tweet messages. I love automation. And outside of the enterprise, most of it hinges on email. So I created a .NET library to do some of the email heavy lifting more me ...
tags: [Automation, Posts, Programming]
---

Jobs to [download videos for me]({% post_url 2015-01-03-download-pocket-videos-to-your-pc %}). Jobs to [Tweet messages]({% post_url 2015-02-25-understanding-the-twitter-api %}). I love automation. And outside of the enterprise, most of it hinges on email. So I created a .NET library to do some of the email heavy lifting more me. Please <a href="https://github.com/jamesfmackenzie/EmailWatcher" target="_blank">check it out</a>!

### Usage

{% highlight csharp %}
{% raw %}
// setup some options
var options = new EmailWatcherOptions {
  Host = "[POP host]",
  Username = "[POP username]",
  Password = "[POP password]",
  TimeBetweenRefreshes = 30 // seconds
  };

// create an Email Watcher and register a listener
var watcher = EmailWatcher.Public.EmailWatcher.WithOptions(options);
watcher.EmailReceivedEvent += (sender, args)
  => Console.WriteLine("Email Received! Id {0} Subject: {1}, Body: {2}", args.Message.Id, args.Message.Subject, args.Message.Body);

// start watching
watcher.StartWatching();
{% endraw %}
{% endhighlight %}

* <a href="https://github.com/jamesfmackenzie/EmailWatcher" target="_blank">EmailWatcher on GitHub</a>