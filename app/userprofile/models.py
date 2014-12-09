from django.db import models
from django.conf import settings
from snippet.definitions import editormodes

class UserProfile(models.Model):
  """
  Additional User information that will link to a User account.
  Each User account will have it's own unique User profile.
  """
  user = models.OneToOneField(settings.AUTH_USER_MODEL, unique = True)
  websiteUrl = models.URLField(max_length = 80, blank = True)
  accountType = models.CharField(max_length = 20, blank = False)
  defaultSnippetLanguage = models.CharField(max_length = 20, choices = editormodes.Modes, default = editormodes._TEXT, blank = False)
  #loginDetails = JSONField
  
  def __unicode__(self):
    return "%s's profile" %(self.user.username)


