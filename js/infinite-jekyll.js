$(function () {

  var postURLs,
    isFetchingPosts = false,
    shouldFetchPosts = true,
    postsToLoad = $(".post-list").children().length,
    loadNewPostsThreshold = 3000,
    postToAppend;

  // Load the JSON file containing all URLs
  $.getJSON('/all-posts.json', function (data) {
    postURLs = data["posts"];

    // If there aren't any more posts available to load than already visible, disable fetching
    if (postURLs.length <= postsToLoad)
      disableFetching();
  });

  // If there's no spinner, it's not a page where posts should be fetched
  if ($(".infinite-spinner").length < 1)
    shouldFetchPosts = false;

  // Are we close to the end of the page? If we are, load more posts
  $(window).scroll(function (e) {
    if (!shouldFetchPosts || isFetchingPosts) return;

    var windowHeight = $(window).height(),
      windowScrollPosition = $(window).scrollTop(),
      bottomScrollPosition = windowHeight + windowScrollPosition,
      documentHeight = $(document).height();

    // If we've scrolled past the loadNewPostsThreshold, fetch posts
    if ((documentHeight - loadNewPostsThreshold) < bottomScrollPosition) {
      fetchPosts();
    }
  });

  // Fetch a chunk of posts
  function fetchPosts() {
    // Exit if postURLs haven't been loaded
    if (!postURLs) return;

    isFetchingPosts = true;

    // Load as many posts as there were present on the page when it loaded
    // After successfully loading a post, load the next one
    var loadedPosts = 0,
      postCount = $(".post-list").children().length,
      callback = function () {
        loadedPosts++;
        var postIndex = postCount + loadedPosts;

        if (postIndex > postURLs.length - 1) {
          disableFetching();
          return;
        }

        if (loadedPosts < postsToLoad) {
          fetchPostWithIndex(postIndex, callback);
        } else {
          isFetchingPosts = false;
        }
      };

    fetchPostWithIndex(postCount + loadedPosts, callback);
  }

  function fetchPostWithIndex(index, callback) {
    var postToAppend = postURLs[index];
    if (postToAppend.tags) {
      var tagsHtml = "<p class=\"tags\">";
      postToAppend.tags.forEach(function (item, index) {
        tagsHtml += "<a href=\"/sitemap/#" + item.urlSafeName + "\">" + item.name + "</a>, "
      });
      tagsHtml = tagsHtml.slice(0, -2);
      tagsHtml += "</p>";
    }


    var hyperlink = "<a href=\"" + postToAppend.url + "\">" + postToAppend.title + "</a>";
    
	if (postToAppend.overrideUrl && postToAppend.overrideUrl != "") {
		hyperlink = "<a target=\"_blank\" href=\"" + postToAppend.overrideUrl + "\">";
    }
	else if (postToAppend.layout == "tweet") {
		hyperlink = "<a target=\"_blank\" href=\"https://twitter.com/jamesfmackenzie/status/" + postToAppend.tweetId + "\">“" + postToAppend.title + "”</a>";
	}
	else if (postToAppend.layout == "youtube") {
		hyperlink = "<a target=\"_blank\" href=\"https://youtu.be/" + postToAppend.videoId + "\">" + postToAppend.title + "</a>";
	}
	
	
	var mediaFragment = "";
	
	if (postToAppend.image && postToAppend.image != "") {
		mediaFragment = "<p><img src=\"/img/posts/" + postToAppend.image + "\" /></p>";
	}
	else if (postToAppend.layout == "youtube") {
		mediaFragment = "<div class=\"youtube-container\"><iframe src=\"https://www.youtube.com/embed/" + postToAppend.videoId + "?rel=0\" frameborder=\"0\" allowfullscreen class=\"youtube-video\"></iframe></div>"
	}


    var htmlFragment = "";

    if (postToAppend.layout == "tweet") {			
		
      htmlFragment = "<div class=\"row\">" + tagsHtml + "<h2 class=\"quote\">" + hyperlink + "</h2><blockquote class=\"twitter-tweet twitter-tweet-blockquote\"><p lang=\"en\" dir=\"ltr\">" + postToAppend.title + "</p>&mdash; James Mackenzie (@jamesfmackenzie) <a target=\"_blank\" href=\"https://twitter.com/jamesfmackenzie/status/" + postToAppend.tweetId + "\">" + postToAppend.date + "</a></blockquote><script async src=\"https://platform.twitter.com/widgets.js\" charset=\"utf-8\"></script>";
    } 
	else {
      
	  htmlFragment = "<div class=\"row\">" + tagsHtml + "<h2>" + hyperlink + "</h2><p class=\"post-summary\">" + postToAppend.summary + "</p><p><date>" + postToAppend.date + "</date></p>" + mediaFragment + "</div>";
    }

    $("<article class=\"post\">" + htmlFragment + "</article>").appendTo(".post-list");

    callback();
  }

  function disableFetching() {
    shouldFetchPosts = false;
    isFetchingPosts = false;
    $(".infinite-spinner").fadeOut();
  }

});