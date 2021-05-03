<ul>
  {% for post in site.posts reversed %}
  {% if post.tags contains "VR Photography" %}
  <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
  </li>
  {% endif %}
  {% endfor %}
</ul>