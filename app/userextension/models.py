from django.db import models
from django.conf import settings
from jsonfield import JSONField
from snippet.definitions import editormodes
from django.contrib.auth.signals import user_logged_in
from usertools import collectUserData


class UserProfile(models.Model):
  """
  Additional User information that will link to a User account.
  Each User account will have it's own unique User profile.
  """
  user = models.OneToOneField(settings.AUTH_USER_MODEL, unique = True)
  websiteUrl = models.URLField(max_length = 80, blank = True)
  accountType = models.CharField(max_length = 20, blank = False)
  defaultSnippetLanguage = models.CharField(max_length = 20, choices = editormodes.Modes, default = editormodes._TEXT, blank = False)
  loginDetails = JSONField()  
  """
  Schema for loginDetails:
  {
    "data": [
      {
        "date": "2014-12-10T22:33:15.853089-05:00",
        "ip"  : "172.16.254.1"
      }
    ]
  }
  """
  
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
  if kwargs.get("user") and kwargs.get("request"):
    print "\nUser", kwargs["user"].username ," has just logged in :)"
    d = collectUserData(kwargs["request"])
    print "Collected data: \n"
    for k in d[0].keys():
      print k, " : ", d[0][k]
    print "\n"
    #usr = kwargs["user"]
    usr = kwargs["user"]
    loginData = collectUserData(kwargs["request"])

# Connect the signal.
user_logged_in.connect(collectLoginInfo)
