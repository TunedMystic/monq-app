$(document).ready(function() {
  
  function likeSnippet() {
    $.ajax({
      url: "/likeSnippet/",
      headers: {
        "X-CSRFToken": $.cookie("csrftoken")
      },
      type: "POST",
      dataType: "json",
      data: {
        "snippetUrl": $("#snUrl").data("snippeturl")
      },
      success: function(data, status, jqXHR) {
        console.log("Success!\n\n");
        
        window.sdata = data;
        console.log(window.sdata);
        
        // If you successfully UNfavorited a Snippet.
        if(data.deleted == true) {
          $("#likeButton").text("Like");
          // Decrement the "Likes" element.
          var likes = parseInt($("#snippet-likes span").text(), 10);
          likes -= 1;
          $("#snippet-likes span").text(likes);
        }
        // If you successfully favorited a Snippet.
        else {
          $("#likeButton").text("You Liked");
          // Increment the "Likes" element.
          var likes = parseInt($("#snippet-likes span").text(), 10);
          likes += 1;
          $("#snippet-likes span").text(likes);
        }
      },
      error: function(data, status, jqXHR) {
        console.log("Error!\n\n");
        
        window.sdata = data;
        console.log(window.sdata);
      }
    });
  }
  
  // Like a snippet through an Ajax post.
  $("#likeButton").click(function(e) {
    e.preventDefault();
    e.stopPropagation();
    likeSnippet();
  });
  
});

