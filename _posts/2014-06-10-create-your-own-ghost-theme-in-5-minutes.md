---
layout: post
title: Create Your Own Ghost Theme in 5 Minutes
date: '2014-06-10 14:18:00'
tags: [Blogging, Ghost, Web Design, Branding, Themes, Web Development, Programming]
---

I spent some time reading about [Ghost themes](http://marketplace.ghost.org/) today, with a view to [creating my own]({% post_url 2014-04-24-getting-to-grips-with-ghost-themes %}).

The folks over at Ghost are smart cookies, and they've made the theming process remarkably simple. So simple, in fact, that you can create your own theme (from scratch) in 5 minutes. Here's how to do it.

### Wait! What are Ghost themes?

Ghost themes take your blog content (the data) and format it for the web (the presentation). By separating these two, you're always free to change the look and feel of your blog without adjusting the content. At a high level, they work like this:

![](/img/posts/g.png)

### Handlebars expressions? What are they?

Handlebars is a templating language, designed to allow separation between HTML and a data source:

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

### OK. What does a Ghost theme look like? And how does it use these Handlebars templates?

A Ghost theme is:

* A directory on the file system
* This directory contains multiple Handlebars templates, each with the <code>.hbs</code> file extension.
* The templates work collaboratively to render your blog content.

A Ghost theme *must* contain the following two files. Everything else if optional.

* <code>post.hbs</code>
	* This is the template for an individual post.
    * Ghost always passes it a <code>post</code> object which is used to render post data to the page.
    * An example <code>post.hbs</code> file:
    
{% highlight html %}
{% raw %}
{{#post}}
<h1 class="post-title">{{title}}</h1>
<p>{{content}}<p>
{{/post}}
{% endraw %}
{% endhighlight %}	 
    
* <code>index.hbs</code>
	* This is the template for the blog homepage.
    * Ghost always passes it the <code>posts</code> object. This is a collection of all the posts that should be displayed.
    * You can loop through the collection to output all your posts to the page.
    * An example <code>index.hbs</code> file:
   
{% highlight html %}
{% raw %}
{{#foreach posts}}
  <h1 class="post-title"><a href="{{url}}">{{title}}</a></h1>
  <p>{{content}}<p>
{{/foreach}}
{% endraw %}
{% endhighlight %}	

**That really is it**. To prove it, try this:

### Create your own theme in 5 minutes

1. Create and configure a [Ghost development instance]({% post_url 2014-05-17-setting-up-a-ghost-dev-environment %}) (if you haven't already).
2. Navigate to the <code>themes</code> directory (mine's at <code>/ghost-0.4.2/content/themes</code>).
3. Create a new folder for your theme. Call it whatever you like (I chose the rather boring "mytheme").
4. Use the code snippets above to create the two new files: <code>post.hbs</code> and <code>index.hbs</code>.
5. Start/restart your Ghost development instance by issuing <code>npm start</code> from the command line.
6. Navigate to your Ghost blog's settings page (mine's at http://localhost:2368/ghost/settings/general/#)
7. Scroll to the bottom of the page. You should see your new theme listed in the Themes drop-down. Select it and hit Save.
8. Navigate to your blog (mine's at http://localhost:2368/) to see your new theme in action!

Pretty easy huh?