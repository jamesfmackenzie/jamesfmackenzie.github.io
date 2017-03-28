---
layout: post
title: Dropbox as a GitHub Alternative
date: '2017-03-28 22:40:21'
tags: [Programming, How To, Web Development]
---

Want the benefits of private, <a href="https://en.wikipedia.org/wiki/Distributed_version_control" target="_blank">distributed version control</a> but don't want to pay <a href="https://github.com/pricing" target="_blank">GitHub's subscription fee</a>? Or simply don't trust GitHub with checked in passwords, tokens and secrets?

You can fashion yourself a quick and dirty solution using Git and Dropbox.


### What you need

* <a href="https://git-scm.com/downloads" target="_blank">Git</a>
* <a href="https://www.dropbox.com" target="_blank">Dropbox</a> (or some alternative file hosting service)

### Step 1. Create and initialise Remote repository
 
* Create a directory on Dropbox to act as your Remote repository
* Initialise it via <code>git --bare init</code>

![](/img/posts/2017-03-28 22_23_19-git-dropbox-1.png)

### Step 2. Clone Remote repository to local

* Clone the Remote to your local via <code>git clone &lt;path to Dropbox folder&gt;</code>

![](/img/posts/2017-03-28 22_24_39-git-dropbox-2.png)

### Step 3. Write some code!
 
* Get busy, write some code! Save it to your local repo.
* Or if you're feeling lazy, just copy-paste the code from somewhere else.

![](/img/posts/2017-03-28 22_28_53-git-dropbox-3.png)

### Step 4. Add, commit and push
 
* Stage the source code via <code>git add</code>
* Commit to your local repository via <code>git commit</code>
* Push to the Remote via <code>git push</code>

![](/img/posts/2017-03-28 22_31_01-git-dropbox-4.png)

### Step 5. Share and Collaborate!

* Want to collaborate with someone? Just use Dropbox's built in Share feature.
* Anyone you add can <code>clone</code>, <code>add</code>, <code>commit</code> and <code>push</code> too. Easy as!

![](/img/posts/2017-03-28 22_33_04-git-dropbox-5.png)
