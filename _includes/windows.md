<ul>
  {% for post in site.posts %}
  {% if post.tags contains "Windows 98" or post.tags contains "Windows XP" %}
  {% if post.layout != "quote" %}
  <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
  </li>
  {% endif %}
  {% endif %}
  {% endfor %}
</ul>