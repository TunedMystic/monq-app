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
        ////console.log("Success!\n\n");
        
        ////window.sdata = data;
        ////console.log(window.sdata);
        
        var message = "";
        
        // If you successfully UNfavorited a Snippet.
        if(data.deleted == true) {
          $("#likeButton span").text("Like!");
          $("#likeButton span").removeClass("label-primary");
          $("#likeButton span").addClass("label-warning");
          // Decrement the "Likes" element.
          var likes = parseInt($("#snippet-likes span").text(), 10);
          likes -= 1;
          $("#snippet-likes span").text(likes);
          
          message = "You unfavorited this snippet!";
        }
        // If you successfully favorited a Snippet.
        else {
          $("#likeButton span").text("You Liked");
          $("#likeButton span").removeClass("label-warning");
          $("#likeButton span").addClass("label-primary");
          // Increment the "Likes" element.
          var likes = parseInt($("#snippet-likes span").text(), 10);
          likes += 1;
          $("#snippet-likes span").text(likes);
          
          message = "You favorited this snippet!";
        }
        
        utils.comboSuccess(message);
      },
      error: function(data, status, jqXHR) {
        ////console.log("Error!\n\n");
        
        ////window.sdata = data;
        ////console.log(window.sdata);
        
        utils.comboAlert(data);
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

