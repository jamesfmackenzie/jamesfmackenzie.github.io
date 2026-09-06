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
      htmlFragment =
        "<div class=\"row\">" +
        "<p class=\"feed-meta\">Tweet &nbsp;&middot;&nbsp; <time>" + postToAppend.date + "</time></p>" +
        "<blockquote class=\"twitter-title-quote\"><a href=\"" + postToAppend.url + "\"><span lang=\"en\" dir=\"ltr\">" + postToAppend.title + "</span></a></blockquote>" +
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