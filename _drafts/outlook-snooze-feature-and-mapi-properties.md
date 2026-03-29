---
layout: post
title: Outlook Snooze Feature and MAPI Properties
summary: A draft on how Outlook stores snooze data internally and how to expose it with VBA.
tags: [Microsoft Outlook, VBA, Windows]
---

Outlook's snooze behaviour is more useful than it first appears, but some of the interesting data is buried in MAPI properties rather than exposed cleanly in the UI.

## The Useful Discovery

The key property in the notes is:

- `0x0F070040`

That appears to hold the snoozed-until value, in UTC.

## Practical Use

The VBA example reads that property from messages in the **Snoozed** folder and copies it into a visible custom Outlook field called **Snooze Until**.

That gives you something Outlook does not make especially easy by default: a visible snooze date you can sort and inspect.

## Example Approach

The current macro:

- opens the mailbox root
- reads the `Snoozed` folder
- iterates over its items
- retrieves the MAPI property
- adjusts the value for local time
- writes it into a user property

## What the Final Version Should Add

- a cleaned-up version of the VBA code
- explanation of the time zone handling
- notes on adding the macro to the ribbon or quick access toolbar
- whether this can be automated on a schedule or integrated into the context menu
