---
layout: post
title: "iOS Games with Xbox Achievements"
date: '2021-11-27 19:16:00:00'
summary: Want to hunt Xbox Achievements on the go? Here's a list of iOS games with wireless controller support ...
tags: [Consumer Tech, iOS, Videogames, Xbox]
permalink: /ios-games-with-xbox-achievements/
---


<script>
$.getJSON( "https://raw.githubusercontent.com/jamesfmackenzie/ios-games-with-xbox-achievements/master/ios-games-with-xbox-achievements.json", function( data ) {
  var items = [];
  $.each( data, function( index, value ) {
	items.push( "<li id='" + index + "'><a href='" + value.url + "' target='_blank'>" + value.title + " (" + value.gamerscore + ")</a></li>" );
  });
 
  $( "<ul/>", {
    "class": "my-new-list",
    html: items.join( "" )
  }).appendTo( "article .row" );
});
</script>

Want to hunt <a href="https://en.wikipedia.org/wiki/Xbox_network#Gamerscore" target="_blank">Xbox Achievements</a> on the go? Here’s a list of iOS games with achievements support. The list is <a href="https://github.com/jamesfmackenzie/ios-games-with-xbox-achievements" target="_blank">hosted on GitHub</a>. If you'd like to make an update, please <a href="https://guides.github.com/activities/hello-world/#pr" target="_blank">open a pull request</a>.

### iOS Games with Xbox Achievements (including Gamerscore)
