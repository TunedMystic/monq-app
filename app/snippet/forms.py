from django import forms
from .models import Snippet

# 300kb
LOGGED_IN_SIZE = (300000, "300kb")
# 50kb
ANONYMOUS_SIZE = (50000, "50kb")
# Max number of tags allowed.
MAX_TAGS = 10

class SnippetForm(forms.ModelForm):
  class Meta:
    model = Snippet
    #fields = ["title", "content", "language", "visibility", "password", "tags" ]
    exclude = ["author", "_date_added", "url_code"]
  
  def clean_content(self, *args, **kwargs):
    """
    Checks the size(in bytes) of the content being posted.
    Logged-in Users can post larger snippets then anonymous Users.
    """
    data = self.cleaned_data.get("content", None)
    # If we have access to the request, we can clean content based on size.
    if hasattr(self, "request"):
      # Is the user anonymous?
      if request.user.is_anonymous():
        # Does size exceed the limit for an anonymous user?
        if Snippet.rawSize(data) > ANONYMOUS_SIZE[0]:
          raise forms.ValidationError("Anonymous users cannot post content exceeding " + ANONYMOUS_SIZE[1])
      # Is the user logged in?
      else:
        # Does size exceed the limit for a logged-in user?
        if Snippet.rawSize(data) > LOGGED_IN_SIZE[0]:
          raise forms.ValidationError("Users cannot post content exceeding " + LOGGED_IN_SIZE[1])
    return data
  
  def clean_tags(self, *args, **kwargs):
    """
    Checks if the number of tags is within the allowed limit.
    """
    data = self.cleaned_data.get("tags", None)
    
    if len(data) > MAX_TAGS:
      raise forms.ValidationError("Maximum of %s tags allowed per Snippet." %(MAX_TAGS))
    
    return data
  
  def clean(self, *args, **kwargs):
    """
    If visibility is private, Snippet must gave a password.
    If visibility is public, Snipper doesn't need a password.
    """
    cleaned_data = super(SnippetForm, self).clean(*args, **kwargs)
    
    # Private snippets must contain a password.
    if (cleaned_data.get("visibility", None) == "private") and (cleaned_data.get("password", None) == ""):
      raise forms.ValidationError("You must provide a password for private Snippets.")
    
    # Private snippets have no password.
    if (cleaned_data.get("visibility", None) == "public") and (cleaned_data.get("password", None) != ""):
      cleaned_data["password"] = ""
    
    return cleaned_data
