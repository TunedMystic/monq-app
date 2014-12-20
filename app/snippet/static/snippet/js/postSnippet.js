

$(document).ready(function() {
  
  // Post Snippet data to create it.
  function postNewSnippet() {
    $.ajax({
      url: "/newSnippet/",
      headers: {
        "X-CSRFToken": $.cookie("csrftoken")
      },
      type: "POST",
      dataType: "json",
      data: {
        "title": $("#snippet-title").val(),
        "content": $("#snippet-content").val(),
        "language": $("#snippet-language").val(),
        "visibility": $("#snippet-visibility").val(),
        "password": $("#snippet-password").val(),
        "tags": $("#snippet-tags").val()
      },
      success: function(data, status, jqXHR) {
        console.log("Success!\n\n");
        
        window.sdata = data;
        console.log(window.sdata);
      },
      error: function(data, status, jqXHR) {
        console.log("Error!\n\n");
        
        window.sdata = data;
        console.log(window.sdata);
      }
    });
  }
  
  // Post new Snippet using Ajax.
  $("#snippetForm").submit(function(e) {
    e.preventDefault();
    postNewSnippet();
  });
  
  // If the hidden language element exists, use it in the form.
  if($("#hidden-snippet-language").length) {
    $("#snippet-language").val($("#hidden-snippet-language").data("language"));
    // Update the 'Chosen' plugin.
    $("#snippet-language").trigger("chosen:updated");
    // Trigger 'change' event to for the Snippet Editor's listeners to hook into.
    $("#snippet-language").trigger("change");
  }
  
});