---
layout: post
title: Recovering Lost DNS or MX Records
summary: A practical draft on what to do when DNS or mail records are lost and you need to reconstruct them quickly.
tags: [DNS, Email, Sysadmin]
---

If you accidentally delete DNS records, or lose track of the correct MX configuration for a domain, recovery can be awkward. This draft is a starting point for a short practical guide.

## The Problem

You know the domain used to work, but now:

- web traffic may be broken
- mail delivery may be failing
- you may not have a clean record of the old settings

## Possible Recovery Routes

- Check your DNS provider history, if available
- Use historical DNS lookup services
- Look for old mail headers that reference the expected mail path
- Check configuration in old infrastructure notes, screenshots, or deployment tools

## References to Revisit

- Server Fault discussions about historical nameserver and MX lookups
- DNS history services like DNS Trails

## What the Final Post Should Add

- Which tools actually still work
- What data you can and cannot recover
- A suggested order of operations when email is down
