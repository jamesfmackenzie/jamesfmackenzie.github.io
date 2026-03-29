---
layout: post
title: Querying Wikidata
summary: A draft showing how to use Wikidata queries to pull structured datasets, using Atari ST games as an example.
tags: [Data, Wikidata, Wikipedia]
---

Wikidata is often the cleanest starting point when you want structured data related to Wikipedia articles.

## Example Goal

Find video games that have an Atari ST platform statement and an English Wikipedia article.

## Example Query

```sparql
SELECT DISTINCT ?game ?article WHERE
{
  ?game wdt:P31/wdt:P279* wd:Q7889 .
  ?game p:P400 ?s1 .
  ?s1 ps:P400 wd:Q627302 .
  ?article schema:about ?game .
  ?article schema:inLanguage "en" .
  FILTER (SUBSTR(str(?article), 1, 25) = "https://en.wikipedia.org/")
}
```

## Why This Is Useful

- cleaner than scraping HTML
- more structured than plain Wikipedia pages
- easy to refine with extra conditions

## What the Final Post Should Add

- a breakdown of what the query is doing
- guidance on identifying the right property and entity IDs
- a comparison with DBpedia and direct Wikipedia API access
