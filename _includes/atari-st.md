<ul>
  {% for post in site.posts %}
  {% if post.tags contains "Atari ST" %}
  {% if post.layout == "post" %}
  <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
  </li>
  {% endif %}
  {% endif %}
  {% endfor %}
</ul>