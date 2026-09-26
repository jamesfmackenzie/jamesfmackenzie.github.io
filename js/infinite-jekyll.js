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

    var summaryFragment = postToAppend.summary
      ? "<div class=\"post-summary\">" + postToAppend.summary + "</div>"
      : "";

    var tagsSuffix = (postToAppend.tags && postToAppend.tags.length)
      ? " &middot; " + postToAppend.tags.map(function (t) {
          return "<a href=\"/sitemap/#" + t.urlSafeName + "\">" + t.name + "</a>";
        }).join(", ")
      : "";

    var htmlFragment = "";

    if (postToAppend.layout == "tweet") {
      var statsIcons = {
        replies: "<svg class=\"tweet-stat-icon\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z\"/></svg>",
        reposts: "<svg class=\"tweet-stat-icon\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><polyline points=\"17 1 21 5 17 9\"/><path d=\"M3 11V9a4 4 0 0 1 4-4h14\"/><polyline points=\"7 23 3 19 7 15\"/><path d=\"M21 13v2a4 4 0 0 1-4 4H3\"/></svg>",
        likes: "<svg class=\"tweet-stat-icon\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z\"/></svg>",
        views: "<svg class=\"tweet-stat-icon\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><line x1=\"18\" y1=\"20\" x2=\"18\" y2=\"10\"/><line x1=\"12\" y1=\"20\" x2=\"12\" y2=\"4\"/><line x1=\"6\" y1=\"20\" x2=\"6\" y2=\"14\"/></svg>"
      };
      var statsTitles = { replies: "Replies", reposts: "Reposts", likes: "Likes", views: "Views" };
      var statsFragment = "";
      if (postToAppend.stats) {
        var statsItems = ["replies", "reposts", "likes", "views"].filter(function (key) {
          return postToAppend.stats[key];
        }).map(function (key) {
          return "<li title=\"" + statsTitles[key] + "\">" + statsIcons[key] + postToAppend.stats[key] + "</li>";
        });
        if (statsItems.length) {
          statsFragment = "<ul class=\"tweet-stats\">" + statsItems.join("") + "</ul>";
        }
      }
      htmlFragment =
        "<div class=\"row\">" +
        "<p class=\"feed-meta\">Tweet &nbsp;&middot;&nbsp; <time>" + postToAppend.date + "</time></p>" +
        "<blockquote class=\"twitter-title-quote\"><a href=\"" + postToAppend.url + "\"><span lang=\"en\" dir=\"ltr\">" + postToAppend.title + "</span>" + statsFragment + "</a></blockquote>" +
        (postToAppend.summary ? "<div class=\"post-summary\"><a href=\"" + postToAppend.url + "\">" + postToAppend.summary + "</a></div>" : "") +
        "</div>";
    }
    else if (postToAppend.layout == "youtube") {
      htmlFragment =
        "<div class=\"row\">" +
        "<h2><a href=\"" + postToAppend.url + "\">" + postToAppend.title + "</a></h2>" +
        summaryFragment +
        "<p class=\"feed-meta\">Video &nbsp;&middot;&nbsp; <time>" + postToAppend.date + "</time>" + tagsSuffix + "</p>" +
        "<div class=\"youtube-container\"><iframe src=\"https://www.youtube.com/embed/" + postToAppend.videoId + "?rel=0\" frameborder=\"0\" allowfullscreen class=\"youtube-video\"></iframe></div>" +
        "</div>";
    }
    else {
      var url = (postToAppend.overrideUrl && postToAppend.overrideUrl != "") ? postToAppend.overrideUrl : postToAppend.url;
      var thumbFragment = (postToAppend.image && postToAppend.image != "")
        ? "<img class=\"feed-thumb\" src=\"/img/" + postToAppend.image + "\" alt=\"" + postToAppend.title + "\" />"
        : "";
      htmlFragment =
        "<div class=\"row\">" +
        "<h2><a href=\"" + url + "\">" + postToAppend.title + "</a></h2>" +
        summaryFragment +
        "<p class=\"feed-meta\"><time>" + postToAppend.date + "</time>" + tagsSuffix + "</p>" +
        thumbFragment +
        "</div>";
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