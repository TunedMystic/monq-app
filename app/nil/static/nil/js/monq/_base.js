// Dynamic dates!
$(document).ready(function() {
  var d = new Date();
  $(".credits .year").text(d.getFullYear());
});

// Random Taglines!
$(document).ready(function() {
  var taglines = [
    "Code snippets are the future!",
    "Just click, type and share!",
    "An awesome web app!",
    "Code snippets with Green Tea!",
    "Made with eco-friendly technologies :)",
    "Snippets are made with bagels and butter!",
    "Become a code Jedi!",
  ];
  // Ensure that the same tagline does not get repeated consecutively.
  setInterval(function() {
    var f = "slow"
    $("p.tagline").fadeOut(f, function() {
      var currentTagline = $("p.tagline em").text();
      var newTaglines = _.without(taglines, currentTagline);
      currentTagline = newTaglines[_.random(0, newTaglines.length - 1)];
      $("p.tagline em").text(currentTagline);
      $("p.tagline").fadeIn(f);
    });
  }, 10000);
});

// Set up button click handlers.
$(document).ready(function() {
  
  $("#authenticatedUserButton").click(function(e) {
     e.preventDefault();
     window.location = "/me/";
  });
  
  $("#unauthenticatedUserButton").click(function(e) {
     e.preventDefault();
     window.location = "/login/";
  });
  
  $("#newSnippetButton").click(function(e) {
     e.preventDefault();
     window.location = "/new/";
  });
  
  $("#popularSnippets").click(function(e) {
     e.preventDefault();
     window.location = "/new/";
  });
  
});