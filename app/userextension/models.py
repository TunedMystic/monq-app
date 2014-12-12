from django.db import models
from django.conf import settings
from jsonfield import JSONField
from snippet.definitions import editormodes
from definitions import accounttypes
from django.contrib.auth.signals import user_logged_in
import usertools


class UserProfile(models.Model):
  """
  Additional User information that will link to a User account.
  Each User account will have it's own unique User profile.
  """
  # Foreign key back to the User.
  user = models.OneToOneField(settings.AUTH_USER_MODEL, unique = True)
  # User's website.
  websiteUrl = models.URLField(max_length = 80, blank = True)
  # Which social account id the User associated with? (Twitter, Facebook, Googleplus)
  accountType = models.CharField(max_length = 20, default = accounttypes._LOCAL, blank = False)
  # The (programming) language that the editor will be configured with on startup.
  defaultSnippetLanguage = models.CharField(max_length = 20, default = editormodes._TEXT, blank = False)
  MAX_DATA_AMT = 25
  DEFAULT_LOGIN_DETAIL_DATA = {"data":[]}
  # Collection of login data for a User. (NOTE: Will collect 'date' and 'ip' of login).
  loginDetails = JSONField(default = DEFAULT_LOGIN_DETAIL_DATA)
  """
  Schema for loginDetails:
  {
    "data": [
      [{
        "date": "2014-12-10T22:33:15.853089-05:00",
        "ip"  : "172.16.254.1"
      }],
      [{
        "date": "....",
        "ip"  : "...."
      }],
    ]
  }
  """
  
  def addLoginDetails(self, date, ipAddress):
    """
    Add login details to the user profile.
    NOTE: This will save WHERE and WHEN the user logs in.
    """
    if len(self.loginDetails["data"]) == UserProfile.MAX_DATA_AMT:
      self.loginDetails["data"].pop(0)
    self.loginDetails["data"].append([{"date": date, "ip": ipAddress}])
    
  # Print login details
  def getLoginDetails(self):
    details = ""
    for chunk in self.loginDetails["data"]:
      details += "Date - " + usertools.formatDate(usertools.isoToDate(chunk[0]["date"]))
      details += "   :   "  + "IP - " + chunk[0]["ip"] + "\n"
    return details
  getLoginDetails.short_description = "Login Details"
  
  def __unicode__(self):
    return "%s's profile" %(self.user.username)


def createUserProfile(sender, **kwargs):
  """
  Each time a new User is created, a corresponding UserProfile object is created.
  """
  if kwargs.get("created") and kwargs["created"]:
    if kwargs.get("instance") and kwargs["instance"]:
      print "creating user profile for", kwargs["instance"].username
      obj, created = UserProfile.objects.get_or_create(user = kwargs["instance"])

# Connect the signal.
models.signals.post_save.connect(createUserProfile, sender = settings.AUTH_USER_MODEL)


def collectLoginInfo(sender, **kwargs):
  """
  Each time a User logs in, collect data about the login.
  Collect time of login, and ip address.
  """
  if kwargs.get("user") and kwargs.get("request"):
    print "\nUser", kwargs["user"].username ," has just logged in :)"
    usr = kwargs["user"]
    isoDate = usertools.getIsoDate()
    ipAddress = usertools.getIp(kwargs["request"])
    usr.userprofile.addLoginDetails(isoDate, ipAddress)
    usr.userprofile.save()

# Connect the signal.
user_logged_in.connect(collectLoginInfo)
