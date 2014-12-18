import sys
from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from definitions import editorthemes, editormodes, privacy


class Snippet(models.Model):
  """
  This model describes the data of a 'Snippet'.
  A Snippet can hold any supported code/text.
  """
  # Title of the Snippet.
  title = models.CharField(max_length = 50, default = "Untitled", blank = True)
  # The content of the Snippet.
  content = models.TextField(blank = False)
  # The (programming) language the Snippet is written in.
  language = models.CharField(max_length = 20, default = editormodes._TEXT, blank= False)
  # Will the Snippet be public or private?
  visibility = models.CharField(max_length = 20, choices = privacy.Privacy, default = privacy._PUBLIC, blank = False)
  # The password for the (private) Snippet.
  password = models.CharField(max_length = 40, blank = True)
  # The User that wrote the snippet. (Can be an Anonyous user).
  author = models.ForeignKey(settings.AUTH_USER_MODEL, blank = True, null = True)
  # Uniquely generated hash for the Snippet.
  url_code = models.CharField(max_length = 80, unique = True, blank = False)
  # The tags associated with the Snippet.
  tags = TaggableManager(blank = True)
  # The date the Snippet was posted.
  #_date_added = models.DateTimeField(auto_now_add = True, verbose_name = "Date Added")
  date_added_raw = models.DateTimeField(verbose_name = "Date Added")
  
  @property
  def date_added(self):
    return self.date_added_raw.strftime("%A %b %d, %Y - %I:%M:%S %p")
  
  @property
  def preview(self):
    return "%s" %(self.content[:150])
  
  @staticmethod
  def rawSize(x):
    return sys.getsizeof(x)

  @property
  def size(self):
    def formatSize(amt):
      """
      This function takes a file size (in bytes) and converts
      the output into readable format. Supports file sizes in:
      'bytes', 'kb',  and 'mb'.
      """
      fmt = lambda x: "{:,}".format(x)
      fstr = lambda x, y: float("%.1f" % (x / float(y)))
      kb = 1024
      mb = (1024 * 1024)
      if amt >= mb:
        amt = fmt(fstr(amt, mb)) + " mb"
        return amt 
      if amt >= kb:
        amt = fmt(fstr(amt, kb)) + " kb"
        return amt
      return fmt(amt) + " bytes"
    
    return formatSize(Snippet.rawSize(self.content))
  
  def __unicode__(self):
    return "%s" %(self.title[:24] + ": [" + self.language + "]")


class SnippetExtras(models.Model):
  """
  This model defines extra (but not primary) information for a Snippet.
  Each Snippet model will have an associated SnippetExtras model.
  """
  # The Foriegn Key back to the Snippet.
  snippet = models.OneToOneField(Snippet, unique = True)
  # The number of times the Snippet has been viewed.
  hits = models.PositiveIntegerField(blank = False, default = 0)
  # The number of likes the Snippet has.
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, through = "SnippetLike", blank = True)
  # The editor's theme for this Snippet.
  editorTheme = models.CharField(max_length = 20, default = editorthemes._AMBIANCE, blank = False)
  
  def __unicode__(self):
    return "%s" %("Extras to : '" + self.snippet.title[:24] + "..' [" + self.snippet.language + "]")
  
  # Display number of likes.
  def getLikes(self):
    return "%d" %(self.likes.count())
  getLikes.short_description = "Likes"


def createSnippetExtras(sender, **kwargs):
  """
  Create a new SnippetExtras model each time a new Snippet is created and saved.
  """
  if kwargs.get("created") and kwargs["created"]:
    if kwargs.get("instance") and kwargs["instance"]:
      obj, created = SnippetExtras.objects.get_or_create(snippet = kwargs["instance"])

# Connect the signal.
models.signals.post_save.connect(createSnippetExtras, sender = Snippet)


class SnippetLike(models.Model):
  """
  A model to represent a 'Favorite' between a Snippet and a User.
  Also stores the date of favoriting.
  """
  # The Snippet being favorited.
  snippetextras = models.ForeignKey(SnippetExtras, blank = False)
  # The User that favorites the Snippet.
  author = models.ForeignKey(settings.AUTH_USER_MODEL, blank = False)
  # The time and date that the User favorited the Snippet.
  date_liked = models.DateTimeField(auto_now_add = True)
  
  def __unicode__(self):
    return "Like [%s > %s]" %(self.author.username, self.snippetextras.snippet)
  
  @property
  def snippet(self):
    return self.snippetextras.snippet
  
  def __unicode__(self):
    return "Fav [%s] - [%s]" %(self.author, self.snippet)

