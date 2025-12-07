<ul>
  {% assign sorted_posts = site.posts | reverse %}
  {% for post in sorted_posts | sort: "date", "desc" %}
  {% if post.tags contains "MiSTer FPGA" %}
  {% if post.layout == "post" %}
  <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
  </li>
  {% endif %}
  {% endif %}
  {% endfor %}
</ul>



