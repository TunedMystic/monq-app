from django.db import models
from django.conf import settings
from jsonfield import JSONField
from snippet.definitions import editormodes, editorthemes
from definitions.accounttypes import _LOCAL as BACKEND_LOCAL, SOCIAL_BACKENDS
from django.contrib.auth.signals import user_logged_in
import usertools
import arrow


class UserProfile(models.Model):
  """
  Additional User information that will link to a User account.
  Each User account will have it's own unique User profile.
  """
  # Foreign key back to the User.
  user = models.OneToOneField(settings.AUTH_USER_MODEL, unique = True)
  # User's website.
  websiteUrl = models.URLField(max_length = 80, blank = True)
  # The (programming) language that the editor will be configured with on startup.
  defaultSnippetLanguage = models.CharField(max_length = 20, default = editormodes._TEXT, blank = False)
  # The default theme for the ace editor.
  defaultEditorTheme = models.CharField(max_length = 20, default = editorthemes._AMBIANCE, blank = False)
  MAX_DATA_AMT = 10
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
  @property
  def shortUrl(self):
    if len(self.websiteUrl) > 24:
      return self.websiteUrl[:22] + "..."
    return self.websiteUrl
  
  def addLoginDetails(self, date, ipAddress):
    """
    Add login details to the user profile.
    NOTE: This will save WHERE and WHEN the user logs in.
    """
    if len(self.loginDetails["data"]) == UserProfile.MAX_DATA_AMT:
      self.loginDetails["data"].pop(0)
    self.loginDetails["data"].append([{"date": date, "ip": ipAddress}])
  
  def getLoginDetailsList(self):
    """
    Turn self.loginDetails into a list of tuples.
    """
    d = []
    # Limit the amount of login details returned.
    for chunk in self.loginDetails["data"][:self.MAX_DATA_AMT]:                                                                               
      d.append((chunk[0]["ip"], arrow.get(chunk[0]["date"]).datetime))
    d.reverse()
    return d
  
  def getLoginDetails(self):
    """
    Print login details for admin site.
    """
    details = ""
    for chunk in self.loginDetails["data"]:
      details += "Date - " + usertools.formatDate(usertools.isoToDate(chunk[0]["date"]))
      details += "   :   "  + "IP - " + chunk[0]["ip"] + "\n"
    return details
  getLoginDetails.short_description = "Login Details"
  
  def getProvider(self):
    """
    Returns the name of the Social Backend that the User is
    currently authenticated with. If None, defaults to 'Local'.
    """
    # Social Auth backend exists.
    if self.user.social_auth.all():
      try:
        return SOCIAL_BACKENDS[self.user.social_auth.all()[0].provider]
      except KeyError:
        return BACKEND_LOCAL
    else:
      return BACKEND_LOCAL
  
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
