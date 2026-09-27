<div class="row latestposts">
    <h2>Other Posts</h2>
    <ul>
    {% for page in site.posts limit:10 %}
        <li>
        {% if page.layout == "tweet" %}
            <img class="post-type-icon" src="/img/twitter-icon.png" alt="" />
            <a href="{{ page.url }}">{{ page.title }}</a> - {{ page.date | date_to_string }}
        {% elsif page.layout == "youtube" %}
            <img class="post-type-icon" src="/img/youtube-icon.png" alt="" />
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