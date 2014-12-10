from django.db import models
from django.conf import settings
from snippet.definitions import editormodes
from django.contrib.auth.signals import user_logged_in

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


def createUserProfile(sender, **kwargs):
  """
  Each time a new User is created, a corresponding UserProfile object is created.
  """
  if kwargs.get("created") and kwargs["created"]:
    if kwargs.get("instance") and kwargs["instance"]:
      print "creating user profile for", kwargs["instance"].username
      acc = "Normal"
      obj, created = UserProfile.objects.get_or_create(user = kwargs["instance"], accountType = acc)

# Connect the signal.
models.signals.post_save.connect(createUserProfile, sender = settings.AUTH_USER_MODEL)


def collectLoginInfo(sender, **kwargs):
  """
  Each time a User logs in, collect data about the login.
  Collect time of login, and ip address.
  """
  if kwargs.get("user"):
    print "User", kwargs["user"].username ," has just logged in :)"

# Connect the signal.
user_logged_in.connect(collectLoginInfo)
