import sys
from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from definitions import editormodes, privacy


class Snippet(models.Model):
  """
  This model describes the data of a 'Snippet'.
  A Snippet can hold any supported code/text.
  """
  
  title = models.CharField(max_length = 50, default = "Untitled", blank = True)
  content = models.TextField(blank = False)
  language = models.CharField(max_length = 20, choices = editormodes.Modes, default = editormodes._TEXT, blank= False)
  visibility = models.CharField(max_length = 20, choices = privacy.Privacy, default = privacy._PUBLIC, blank = False)
  password = models.CharField(max_length = 40, blank = True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, blank = False)
  url_code = models.CharField(max_length = 80, blank = False)
  tags = TaggableManager(blank = True)
  _date_added = models.DateTimeField(auto_now_add = True)
  
  @property
  def date_added(self):
    return self._date_added.strftime("%A %b %d, %Y - %I:%M:%S %p")
  
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
  snippet = models.OneToOneField(Snippet, unique = True)
  hits = models.PositiveIntegerField(blank = False, default = 0)
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank = True)


# Create a new SnippetExtras model for each Snippet model.
def createSnippetExtras(sender, **kwargs):
  if kwargs.get("created") and kwargs["created"]:
    if kwargs.get("instance") and kwargs["instance"]:
      obj, created = SnippetExtras.objects.get_or_create(snippet = kwargs["instance"])
    
# Connect the signal.
models.signals.post_save.connect(createSnippetExtras, sender = Snippet)
