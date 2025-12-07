<div class="row latestposts">
    <h2>Other Posts</h2>
    <ul>
    {% for page in site.posts limit:10 %}
        <li>
        {% if page.layout == "tweet" %}
            <img src="/img/layout/twitter-icon.png" style="display: inline-block; vertical-align:middle;" />
            <!--<a target="_blank" href="https://twitter.com/jamesfmackenzie/status/{{ page.tweetId }}">{{ page.title }}</a> - {{ page.date | date_to_string }} -->
            <a href="{{ page.url }}">{{ page.title }}</a> - {{ page.date | date_to_string }}
        {% elsif page.layout == "youtube" %}
            <img src="/img/layout/youtube-icon.png" style="display: inline-block; vertical-align:middle;" />
            <!-- <a target="_blank" href="https://youtu.be/{{ page.videoId }}">{{ page.title }}</a> - {{ page.date | date_to_string }} -->
        <a href="{{ page.url }}">{{ page.title }}</a> - {{ page.date | date_to_string }}
        {% elsif page.overrideUrl %} 
            <a href="{{ page.overrideUrl }}">{{ page.title }}</a> - {{ page.date | date_to_string }}
        {% else %}
            <a href="{{ page.url }}">{{ page.title }}</a> - {{ page.date | date_to_string }}
        {% endif %}
        </li>
        {% endfor %}
    </ul>
</div>