
{% highlight html %}
<div class="youtube-container">
    <!-- YouTube embed code -->
    <iframe width="560" height="349" src="http://www.youtube.com/embed/n_dZNLr2cME?rel=0&hd=1" frameborder="0" allowfullscreen></iframe>
</div>
{% endhighlight %}

{% highlight css %}
.youtube-container {
	position: relative;
	padding-bottom: 56.25%; /* 16:9 */
	padding-top: 25px;
	height: 0;
}
.youtube-container iframe {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}
{% endhighlight %}

More info:
https://css-tricks.com/NetMag/FluidWidthVideo/Article-FluidWidthVideo.php


