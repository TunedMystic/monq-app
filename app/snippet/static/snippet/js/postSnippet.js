

$(document).ready(function() {
  
  var DefaultLanguage = "javascript";
  
  function collectTags(s) {
    var tagslist = [];
    _.each($(s).tokenfield("getTokens"), function(el, i) {
        tagslist.push(el["value"]);
    });
    return tagslist.join(",");
  }
  
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
        "content": ed.editor.getSession().getValue(),
        "language": $("#snippet-language").val() || DefaultLanguage,
        "visibility": $("#snippet-visibility-check").prop("checked") === false ? "public" : "private",
        "password": $("#snippet-visibility").val(),
        "tags": collectTags("#snippet-tags")
      },
      success: function(data, status, jqXHR) {
        ////console.log("Success!\n\n");
        
        ////window.sdata = data;
        ////console.log(window.sdata);
        // Redirect to new snippet.
        window.location = sdata.next;
      },
      error: function(data, status, jqXHR) {
        ////console.log("Error!\n\n");
        
        ////window.sdata = data;
        ////console.log(window.sdata);
        utils.comboAlert(data);
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