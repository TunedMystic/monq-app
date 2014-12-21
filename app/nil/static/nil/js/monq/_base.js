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


var utils = {} || utils;

// For each error in the errors list, wrap error in 'p' element
// and append it to #alertBox.
utils.appendErrors = function(errors, f) {
  $("#alertBoxInner").html("");
  
  _.each(errors, function(el, i) {
    $("<p>").text((i + 1) + ". " + el).appendTo("#alertBoxInner");
  });
  
  if(f && typeof(f) == "function")
    f();
  
};

// Takes an Error object, gets all values from it, and flattens if to a single array.
/*
   Error object will look like this:
   var errors = {
     "title" :["Title cannot be empty."],
     "url"   :["Please enter a valid Url."],
     "tags"  :["You cannot have more than 10 tags."]
   };
*/
utils.buildErrors = function(errorObj) {
  return _.flatten(_.values(errorObj));
};

utils.clearAll = function() {
  $("#alertBox").hide();
  $("#successBox").hide();
}

utils.showAlert = function() {
  $("#alertBox").fadeIn();
};

utils.showSuccess = function() {
  $("#successBox").fadeIn();
}

// Takes an error object, appends the errors, and shows the alert.
utils.comboAlert = function(x) {
  utils.clearAll();
  x = x.responseJSON || x;
  utils.appendErrors(utils.buildErrors(x), function() {
    utils.showAlert();
  });
};

// Takes a message, appends it to success box, and shows the success box.
utils.comboSuccess = function(x) {
  utils.clearAll();
  $("#successBoxInner").html("");
  $("<p>").text(x).appendTo("#successBoxInner");
  utils.showSuccess();
};

// Make #alertBox fadeOut (not destroy) on 'x' click.
$(document).ready(function() {
  $("#alertBox button.close").click(function(e) {
    e.preventDefault();
    $("#alertBox").fadeOut();
  });
  
  $("#successBox button.close").click(function(e) {
    e.preventDefault();
    $("#successBox").fadeOut();
  });
});

