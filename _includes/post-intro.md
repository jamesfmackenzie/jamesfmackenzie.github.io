{% assign kicker = nil %}
{% case page.collection %}
  {% when 'hardware' %}{% assign kicker = 'Hardware' %}
  {% when 'howto' %}{% assign kicker = 'Guide' %}
  {% when 'software' %}{% assign kicker = 'Software' %}
  {% when 'projects' %}{% assign kicker = 'Project' %}
  {% when 'reference' %}{% assign kicker = 'Reference' %}
{% endcase %}
{% if kicker == nil and page.layout == 'youtube' %}{% assign kicker = 'Video' %}{% endif %}
{% if kicker == nil and page.layout == 'tweet' %}{% assign kicker = 'Tweet' %}{% endif %}
<header class="intro">
	<div class="row">
		{% if kicker %}<p class="kicker">{{ kicker }}</p>{% endif %}
		<h1>{{ page.title }}</h1>
		{% if page.date or page.tags.size > 0 %}
		<p class="meta">
			{% if page.date %}<time datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date: "%b %-d, %Y" }}</time>{% endif %}
			{% if page.date and page.tags.size > 0 %}&nbsp;&middot;&nbsp;{% endif %}
			{% for tag in page.tags %}<a href="/sitemap/#{{ tag | slugify }}">{{ tag }}</a>{% unless forloop.last %}, {% endunless %}{% endfor %}
		</p>
		{% endif %}
	</div>
</header>
{% if page.hero %}
<figure class="hero">
	<div class="row">
		<img src="/img/{{ page.hero }}" alt="{{ page.hero_alt | default: page.title }}"{% if page.hero_class %} class="{{ page.hero_class }}"{% endif %} />
		{% if page.hero_caption %}<figcaption>{{ page.hero_caption | markdownify | remove: '<p>' | remove: '</p>' }}</figcaption>{% endif %}
	</div>
</figure>
{% endif %}
