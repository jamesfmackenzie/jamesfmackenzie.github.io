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
        replies: "<svg class=\"tweet-stat-icon\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M12 3C6.5 3 2 6.6 2 11c0 2.6 1.6 4.9 4 6.3V22l4.1-2.3c.6.1 1.2.1 1.9.1 5.5 0 10-3.6 10-8S17.5 3 12 3z\"/></svg>",
        reposts: "<svg class=\"tweet-stat-icon\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M6 5h9a3 3 0 0 1 3 3v3M9 2 6 5l3 3M18 19H9a3 3 0 0 1-3-3v-3m9 6 3-3-3-3\"/></svg>",
        likes: "<svg class=\"tweet-stat-icon\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M12 20.5s-7-4.4-9.3-8.6C1 8.6 2.4 5 6 5c2 0 3.3 1 4 2 .7-1 2-2 4-2 3.6 0 5 3.6 3.3 6.9C19 16.1 12 20.5 12 20.5z\"/></svg>",
        views: "<svg class=\"tweet-stat-icon\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M3 20V10M9 20V4M15 20v-7M21 20V7\"/></svg>"
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