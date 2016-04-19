Run at http://dbpedia.org/snorql/

<pre>
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
</pre>
