---
layout: post
title: "Apple Arcade Games with Wireless Controller Support"
date: '2021-07-09 18:03:00:00'
summary: I love Apple Arcade. But touchscreen game controls? Nothing beats a real gamepad. Here's a list of Apple Arcade games with wireless controller support ...
tags: [Consumer Tech, Posts, Videogames]
permalink: /apple-arcade-games-with-controller-support/
---


<script>
$.getJSON( "https://raw.githubusercontent.com/jamesfmackenzie/apple-arcade-games-with-controller-support/main/apple-arcade-games-with-controller-support.json", function( data ) {
  var items = [];
  $.each( data, function( index, value ) {
	items.push( "<li id='" + index + "'><a href='" + value.url + "' target='_blank'>" + value.title + "</a></li>" );
  });
 
  $( "<ul/>", {
    "class": "my-new-list",
    html: items.join( "" )
  }).appendTo( "article .row" );
});
</script>

I love <a href="https://www.apple.com/apple-arcade/" target="_blank">Apple Arcade</a>. So many great games, only $5 per month. But touchscreen game controls? Not so much. For action games, platformers, racers – nothing beats a real gamepad.

Here's a list of Apple Arcade games with <a href="https://support.apple.com/en-us/HT210414" target="_blank">wireless controller support</a>. The list is <a href="https://github.com/jamesfmackenzie/apple-arcade-games-with-controller-support" target="_blank">hosted on GitHub</a>. If you'd like to make an update, please <a href="https://guides.github.com/activities/hello-world/#pr" target="_blank">open a pull request</a>.

### Apple Arcade Games with Wireless Controller Support