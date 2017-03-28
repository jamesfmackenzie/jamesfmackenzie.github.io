---
layout: post
title: Dropbox as a Poor Man's GitHub
date: '2017-03-28 00:00:00'
tags: [Programming, How To, Web Development]
---

Want the benefits of private, distributed version control but don't want to pay GitHub's subscription fee? Or simply don't trust GitHub with checked in passwords, tokens and secrets?

You can fashion yourself a quick and dirty solution using Git and Dropbox


### Step 1. Create and Initialise Remote Repository
 
1. Create a directory on Dropbox to act as your remote repository
2. Initialise it via git --bare init


### Step 2. Clone Remote Repository to local

git clone D:\Dropbox\myrepo


### Step 3. Write some code!
 
Get busy, write some code! Save it to your local repo. Or if you're feeling lazy, just copy-paste something in.


### Step 4. Add, Commit and Push
 
1  git add .
2. git commit -a
3. git push origin master


### Step 5. Collaborate

Want to collaborate with someone? Just use Dropbox's built in share functionality. They can clone and commit too. Easy as!
