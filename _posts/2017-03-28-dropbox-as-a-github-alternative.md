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
* <a href="https://www.dropbox.com" target="_blank">Dropbox</a>
* <a href="https://github.com/anishathalye/git-remote-dropbox" target="_blank">git-remote-dropbox</a>

### Step 1. Clone an Empty Repository

* Decide on a folder name for your new repo
* Clone it via <code>git clone dropbox://<reponame></code>
* This will create a new, empty directory in your local with all the necessary .git gubbins

![](/img/posts/git-dropbox-step-1.png)

### Step 2. Write Some Code!

* Get busy, write some code! Save it to your new local repo.
* Or if you’re feeling lazy, just copy-paste the code from somewhere else.

![](/img/posts/git-dropbox-step-2.png)

### Step 3. Add, Commit and Push

* Stage the source code via <code>git add</code>
* Commit to your local repository via <code>git commit</code>
* Push to the Remote via <code>git push</code>

![](/img/posts/git-dropbox-step-3.png)

### Step 4. Share and Collaborate

* Want to collaborate with someone? Just use Dropbox’s built in Share feature.
* Anyone you add can clone, add, commit and push too. Easy as!

![](/img/posts/git-dropbox-step-4.png)
