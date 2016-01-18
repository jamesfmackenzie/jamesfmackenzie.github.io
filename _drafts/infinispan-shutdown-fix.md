---
layout: post
title: Tomcat
date: '2015-03-15 12:33:15'
---

Tomcat, Infinispan shutdown hooks, etc

I recently came across some shutdown issues with a Tomcat-hosted Java service. After (most of) a day running round in circles, I tracked the issue down to embedded Infinispan - and specifically JGroups.

I'm writing the solution up here in the hopes someone might find it useful.

###Background

In a managed environment like Tomcat, it's best to disable the shutdown hooks.

When you do this, the regular shutdown doesn't run, which can cause issues with Tomcat shutdown (it gets stuck - where?)

To fix this, you need to manually shutdown the infinispan threads

You can do this using a context listener and cachemanager stop

Code snippet 