// Build the ui.
$(document).ready(function() {
  
  // Set up the editor's language choices.
  function editorModes() {
    var modes = ace.require("ace/ext/modelist");
    
    // Build 'Editor Mode' options.
    _.each(modes.modes, function(element, index) {
      $("#snippet-language").append($("<option/>").attr({"value": element.name}).text(element.caption));
    });
  }
  
  // Set up the editor's theme choices.
  function editorThemes() {
    var themes = ace.require("ace/ext/themelist");
    
    _.each(themes.themes, function(element, index) {
      $("#snippet-theme").append($("<option/>").attr({"value": element.name}).text(element.caption));
    });
  }
  
  // **
  // Build the editor
  // **
  var editor = ace.edit("snippet-content");
  window.editor = editor;
  editor.setTheme("ace/theme/ambiance");
  editor.getSession().setMode("ace/mode/javascript");
  
  editorModes();
  editorThemes();
  
  // Add listener to 'snippet-language'.
  $("#snippet-language").change(function() {
    var changed = $(this).find("option:selected");
    if(changed.text() != "Language") {
      console.log("Mode has changed to " + changed.text());
       
      editor.getSession().setMode("ace/mode/" + changed.val());
    }
  });
  
  // Add listener to 'snippet-theme'.
  $("#snippet-theme").change(function() {
    var changed = $(this).find("option:selected");
    console.log("Theme has changed to " + changed.text());
    
    editor.setTheme("ace/theme/" + changed.val());
  });
  
  // Add listener to 'snippet-font-size'.
  $("#snippet-font-size").change(function() {
    var changed = $(this).find("option:selected");
    console.log("Font size has changed to " + changed.text());
    
    $("#snippet-content").css({"font-size": changed.text()});
  });
  
});


// Snippet privacy options.
$(document).ready(function() {
  
  $("#snippet-visibility-check").change(function() {
    if($(this).is(":checked"))
      $("#snippet-visibility").attr("disabled", false);
    else {
      $("#snippet-visibility").attr("disabled", "disabled")
      $("#snippet-visibility").val("");
    }
  });
});


// Initialize 'chosen' selectboxes and 'bootstrap-tokenfield' inputs.
$(document).ready(function() {
  var noResultsTxt = "Nothing to show.";
  $("#snippet-language").chosen({no_results_text: noResultsTxt});
  $("#snippet-theme").chosen({no_results_text: noResultsTxt});
  $("#snippet-font-size").chosen({no_results_text: noResultsTxt});
  
  // Snippet-tags Tokenfield.
  $("#snippet-tags").tokenfield({
    limit: 10,
    //tokens: ["monq!"]
  });
});

