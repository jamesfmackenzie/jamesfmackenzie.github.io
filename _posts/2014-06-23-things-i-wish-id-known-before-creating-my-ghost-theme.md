---
layout: post
title: Things I Wish I'd Known Before Creating My Own Ghost Theme
date: '2014-06-23 20:40:48'
summary: Ghost themes make extensive use of Handlebars.js ... 
tags: [Ghost Blogging Platform, Posts, Programming, Web Design, Web Development]
---

### Ghost themes make extensive use of Handlebars.js

[Handlebars](http://handlebarsjs.com/) is a templating language, designed to allow separation between HTML and a data source:

{% highlight html %}
{% raw %}
<div class="entry">
  <h1>{{title}}</h1>
  <div class="body">
    {{body}}
  </div>
</div>
{% endraw %}
{% endhighlight %}	

Above shows a simple Handlebars template. <code>{% raw %}{{title}}{% endraw %}</code> and <code>{% raw %}{{body}}{% endraw %}</code> are Handlebars expressions which will be swapped out at runtime with actual data. The rest of the snippet is standard HTML which (along with CSS) provides the structure, layout and design.

For more detail head over to the [Handlebars website](http://handlebarsjs.com/) and do some reading!

### A Ghost theme is just a directory

As [mentioned previously]({% post_url 2014-06-10-create-your-own-ghost-theme-in-5-minutes %}), a Ghost theme is simply:

* A directory on the file system
* This directory contains multiple Handlebars templates, each with the .hbs file extension.
* The templates work collaboratively to render your blog content.

### There's a recommended file structure for a Ghost theme

Stick to this for great benefit:

<pre>
.
├── /assets [contains all your static content, e.g. css, fonts, images, javascript]
├── default.hbs [contains common content for every page e.g. header, footer etc]
├── index.hbs [**required** the template for your blog home page]
├── post.hbs [**required** the template for each post]
└── package.json [contains template details e.g. name, version, description]
</pre>

### There are only two mandatory files in a Ghost theme.

A Ghost theme <em>must</em> contain the following two files:

* <code>post.hbs</code>
	* This is the template for an individual post.
* <code>index.hbs</code>
	* This is the template for the blog homepage.

Everything else is optional.

### Ghost makes data available to your Handlebars templates by magic

* <code>post.hbs</code> is always passed a <code>post</code> object
	* The <code>post</code> object consists of:
		* <code>id</code> – the post id
		* <code>title</code> – the post title
		* <code>url</code> – the relative URL for a post
		* <code>content</code> – the post content
		* <code>published_at</code> – date the post was published
		* <code>author</code> – an object representing the post author
		    * <code>author.name</code> – the name of the author
			* <code>author.email</code> – the author's email address
			* <code>author.bio</code> – the author's bio
			* <code>author.website</code> – the author's website
			* <code>author.image</code> – the author's profile image
			* <code>author.cover</code> – the author's cover image
		* <code>tags</code> – an object representing the post's tags
            * <code>tag.name</code> – the name of the tag
            * You can use the <code>{% raw %}{{foreach}}{% endraw %}</code> helper to iterate over the tags
		* Each of these properties can be output using a standard Handlebars expression, e.g. <code>{% raw %}{{title}}{% endraw %}</code>. In addition, you can use just <code>{% raw %}{{author}}{% endraw %}</code> to output the author's name:

		
{% highlight html %}
{% raw %}
{{#post}}
<h1 class="post-title">{{title}}</h1>
<p>Published by {{author}} on {{published_at}}</p>
<p>Tags:
    {{#foreach tags}}
        <li>{{name}}</li>
    {{/foreach}}
</p>
<p>{{content}}</p>
{{/post}}
{% endraw %}
{% endhighlight %}
        
* <code>index.hbs</code> is always passed the <code>posts</code> object.
	* This is a collection of all the <code>post</code> objects in your blog.
    * Again you can loop over these using the <code>{% raw %}{{foreach}}{% endraw %}</code> helper:
    
{% highlight html %}
{% raw %}
{{#foreach posts}}
  <h1 class="post-title"><a href="{{url}}">{{title}}</a></h1>
  <p>{{content}}</p>
{{/foreach}}
{% endraw %}
{% endhighlight %}

* All Handlebars templates are passed global blog properties via the <code>@blog</code> object
	* <code>{% raw %}{{@blog.url}}{% endraw %}</code> – the blog url specified in config.js
	* <code>{% raw %}{{@blog.title}}{% endraw %}</code> – the blog title from the settings page
	* <code>{% raw %}{{@blog.description}}{% endraw %}</code> – the blog description from the settings page
	* <code>{% raw %}{{@blog.logo}}{% endraw %}</code> – the blog logo from the settings page
 
    
### There are many Handlebars helpers available

* You've already seen <code>{% raw %}{{foreach}}{% endraw %}</code>, but Ghost has many other built in helpers to help you build or customize your theme.
* They're accessed via a Handlebars expression e.g. <code>{% raw %}{{foreach}}{% endraw %}</code> or <code>{% raw %}{{content}}{% endraw %}</code>.
* You can find the complete list [here](http://docs.ghost.org/themes/#helpers).

### You should use Handlebars inheritance to minimize waste

Handlebars templates can inherit from each other. This really helps to cut down on code duplication/waste:

* <code>{% raw %}{{!< templatename}}{% endraw %}</code> indicates extension.
	* The entire output of the current template will be rendered into the <code>{% raw %}{{{body}}{% endraw %}}</code> of <code>templatename.hbs</code>.
* <code>{% raw %}{{!> templatename}}{% endraw %}</code> indicates injection.
	* The entire output of <code>templatename.hbs</code> will be rendered in situe.

### You should read the official Ghost Themes documentation

It's really good. Go and check it our [here](http://docs.ghost.org/themes/).
