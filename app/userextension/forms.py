from django import forms
from .models import UserProfile

class DashboardForm(forms.ModelForm):
  """
  This form updates the User details in the dashboard.
  NOTE: Update only 'websiteUrl' and 'defaultSnippetLanguage'.
  """
  class Meta:
    model = UserProfile
    # fields = ["websiteUrl", "defaultSnippetLanguage"]
    excludes = ["user", "accountType", "loginDetails"]
