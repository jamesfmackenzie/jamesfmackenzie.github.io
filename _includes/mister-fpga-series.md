<ul>
  {% for post in site.posts reversed %}
  {% if post.tags contains "MiSTer" %}
  {% if post.layout == "post" %}
  <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
  </li>
  {% endif %}
  {% endif %}
  {% endfor %}
</ul>