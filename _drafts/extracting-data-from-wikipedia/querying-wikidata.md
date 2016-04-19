Run at https://query.wikidata.org/

<code>
SELECT DISTINCT ?game ?article WHERE
{
  ?game wdt:P31/wdt:P279* wd:Q7889 .  # find instances of subclasses of video game
  ?game p:P400 ?s1 . # with a platform (P400) statement
  ?s1 ps:P400 wd:Q627302 . # ... that has the value Q627302 (Atari ST)
  ?article schema:about ?game .  # with a wikipedia article
  ?article schema:inLanguage "en" . # ... in english
  FILTER (SUBSTR(str(?article), 1, 25) = "https://en.wikipedia.org/") # ... that has the prefix "https://en.wikipedia.org"
}
</code>