---
layout: post
title: Querying DBpedia
summary: A draft showing how DBpedia can be queried for structured information, using Atari ST games as an example.
tags: [DBpedia, Data, Wikipedia]
---

DBpedia is an interesting middle ground between raw Wikipedia pages and manually curated datasets. It exposes structured data that can be queried with SPARQL, but the data is not always as clean or complete as you might hope.

## Example Goal

Find video games associated with the Atari ST and extract Wikipedia page identifiers for them.

## Example Query

```sparql
SELECT DISTINCT * WHERE
{
  {
    SELECT ?game ?wikiPageId WHERE
    {
      ?game a dbo:VideoGame .
      ?game dbo:computingPlatform :Atari_ST .
      ?game dbo:wikiPageID ?wikiPageId .
    }
  }
  UNION
  {
    SELECT ?game ?wikiPageId WHERE
    {
      ?game a dbo:VideoGame .
      ?game dbp:platforms :Atari_ST .
      ?game dbo:wikiPageID ?wikiPageId .
    }
  }
  UNION
  {
    SELECT ?game ?wikiPageId WHERE
    {
      ?game a dbo:VideoGame .
      ?game dct:subject dbc:Atari_ST_games .
      ?game dbo:wikiPageID ?wikiPageId .
    }
  }
}
```

## What This Post Should Explore

- why multiple query patterns are needed
- how DBpedia data differs from Wikidata
- where DBpedia is useful despite its inconsistencies
