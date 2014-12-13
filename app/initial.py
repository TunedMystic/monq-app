#!/usr/bin/env python
import os
import sys
import datetime
import arrow
import django

def endall():
  # Delete Snippets.
  for obj in Snippet.objects.all():
    obj.delete()
  # Delete Users.
  for obj in get_user_model().objects.all():
    obj.delete()

def makeUser(n, e, p):
  try:
    usr = get_user_model().objects.get(username = n)
    return usr
  except get_user_model().DoesNotExist:
    return get_user_model().objects.create_user(username = n, email = e, password = p)

def makeSnippet(author = None, title = None, language = None, visibility = None, url_code = None, content = None, date = None, tags = None):
    s = Snippet.objects.create(author = author, title = title, language = language, visibility = visibility, \
                url_code = url_code, content = content, date_added_raw = date)
    for t in tags:
      s.tags.add(t)
    s.save()

def main():

  # Make Users.
  Harry = makeUser("harry", "harry@gmail.com", "harry")
  Emily = makeUser("emily", "emily@gmail.com", "emily")
  Ramin = makeUser("ramin", "ramin@gmail.com", "ramin")
  Tyler = makeUser("tyler", "tyler@gmail.com", "tyler")
  Bella = makeUser("bella", "bella@gmail.com", "bella")
  Drogo = get_user_model().objects.create_superuser(username = "drogo", email = "drogo@gmail.com", password = "drogo")
  
  # Make some Snippets!
  '''
  s1 = Snippet.objects.create(author = Harry, language = "javascript", content = "function hello() {\nconsole.log('hello');\n}", url_code = "abcde")
  s1.tags.add("js")
  s1.tags.add("web")
  s1.tags.add("dev")
  s1.tags.add("programming")
  s1.save()

  s2 = Snippet.objects.create(author = Bella, title = "Python Fibonnaci", language = "python", visibility = "public", url_code = "f4bcp", content = "startNumber = int(raw_input(\"Enter the start number here \"))\nendNumber = int(raw_input(\"Enter the end number here \"))\n\ndef fib(n):\n    if n < 2:\n        return n\n    return fib(n-2) + fib(n-1)\n\nprint map(fib, range(startNumber, endNumber))\n")
  s2.tags.add("python")
  s2.tags.add("dev")
  s2.tags.add("web")
  s2.save()

  s3 = Snippet.objects.create(author = Harry, title = "Date program in python", language = "python", visibility = "public", url_code = "pw35g", content = "import datetime\nnow = datetime.datetime.now()\nprint \"-\" * 25\nprint now\nprint now.year\nprint now.month\nprint now.day\nprint now.hour\nprint now.minute\nprint now.second\n\nprint \"-\" * 25\nprint \"1 week ago was it: \", now - datetime.timedelta(weeks=1)\nprint \"100 days ago was: \", now - datetime.timedelta(days=100)\nprint \"1 week from now is it: \",  now + datetime.timedelta(weeks=1)\nprint \"In 1000 days from now is it: \", now + datetime.timedelta(days=1000)\n\nprint \"-\" * 25\nbirthday = datetime.datetime(2012,11,04)\n\nprint \"Birthday in ... \", birthday - now\nprint \"-\" * 25\n")
  s3.tags.add("python")
  s3.tags.add("date")
  s3.tags.add("prompt")
  s3.save()

  s4 = Snippet.objects.create(author = Ramin, title = "For-loop in Ruby", language = "ruby", visibility = "public", url_code = "wteu3", content = "# Simple for loop using a range.\r\nfor i in (1..4)\r\n    print i,\" \"\r\nend\r\nprint \"\\n\"\r\n\r\nfor i in (1...4)\r\n    print i,\" \"\r\nend\r\nprint \"\\n\"\r\n\r\n# Running through a list (which is what they do).\r\nitems = [ 'Mark', 12, 'goobers', 18.45 ]\r\nfor it in items\r\n    print it, \" \"\r\nend\r\nprint \"\\n\"\r\n\r\n# Go through the legal subscript values of an array.\r\nfor i in (0...items.length)\r\n    print items[0..i].join(\" \"), \"\\n\"\r\nend")
  s4.tags.add("ruby")
  s4.tags.add("for loop")
  s4.tags.add("program")
  s4.tags.add("programming")
  s4.save()
  '''
  
  makeSnippet(author = Harry, title = "Untitiled something...", language = "javascript", content = "function hello() {\nconsole.log('hello');\n}", visibility = "public", url_code = "abcde", tags = ["js", "web", "dev", "programming"], date = arrow.get(datetime.datetime(2013, 7, 7, 23, 15, 45)).datetime)
  
  makeSnippet(author = Bella, title = "Python Fibonnaci", language = "python", visibility = "public", url_code = "f4bcp", content = "startNumber = int(raw_input(\"Enter the start number here \"))\nendNumber = int(raw_input(\"Enter the end number here \"))\n\ndef fib(n):\n    if n < 2:\n        return n\n    return fib(n-2) + fib(n-1)\n\nprint map(fib, range(startNumber, endNumber))\n", tags = ["python", "dev", "web"], date = arrow.get(datetime.datetime(2010, 9, 3, 4, 5, 12)).datetime)
  
  makeSnippet(author = Harry, title = "Date program in python", language = "python", visibility = "public", url_code = "pw35g", content = "import datetime\nnow = datetime.datetime.now()\nprint \"-\" * 25\nprint now\nprint now.year\nprint now.month\nprint now.day\nprint now.hour\nprint now.minute\nprint now.second\n\nprint \"-\" * 25\nprint \"1 week ago was it: \", now - datetime.timedelta(weeks=1)\nprint \"100 days ago was: \", now - datetime.timedelta(days=100)\nprint \"1 week from now is it: \",  now + datetime.timedelta(weeks=1)\nprint \"In 1000 days from now is it: \", now + datetime.timedelta(days=1000)\n\nprint \"-\" * 25\nbirthday = datetime.datetime(2012,11,04)\n\nprint \"Birthday in ... \", birthday - now\nprint \"-\" * 25\n", tags = ["python", "date", "prompt"], date = arrow.get(datetime.datetime(2011, 8, 13, 16, 45, 56)).datetime)
  
  makeSnippet(author = Ramin, title = "For-loop in Ruby", language = "ruby", visibility = "public", url_code = "wteu3", content = "# Simple for loop using a range.\r\nfor i in (1..4)\r\n    print i,\" \"\r\nend\r\nprint \"\\n\"\r\n\r\nfor i in (1...4)\r\n    print i,\" \"\r\nend\r\nprint \"\\n\"\r\n\r\n# Running through a list (which is what they do).\r\nitems = [ 'Mark', 12, 'goobers', 18.45 ]\r\nfor it in items\r\n    print it, \" \"\r\nend\r\nprint \"\\n\"\r\n\r\n# Go through the legal subscript values of an array.\r\nfor i in (0...items.length)\r\n    print items[0..i].join(\" \"), \"\\n\"\r\nend", tags = ["ruby", "for loop", "program", "programming"], date = arrow.get(datetime.datetime(2008, 5, 16, 14, 26, 54)).datetime)
  
  makeSnippet(language = "text", title = "what", content = "this is a cool website", visibility = "public", url_code = "hfslj", tags = ["nice", "college", "web"], date = arrow.get(datetime.datetime(2014, 3, 7, 13, 15, 45)).datetime)
  
  makeSnippet(language = "text", title = "nice programin", content = "let the interview begin", visibility = "public", url_code = "hfplj", tags = ["name", "bird"], date = arrow.get(datetime.datetime(2007, 10, 17, 10, 19, 15)).datetime)
  
  makeSnippet(author = Ramin, language = "text", title = "oh yea", content = "what?", visibility = "public", url_code = "gfslj", tags = ["what?", "ok", "well", "book"], date = arrow.get(datetime.datetime(2002, 3, 8, 13, 15, 54)).datetime)
  
  makeSnippet(author = Bella, language = "text", title = "draco", content = "dracovallis", visibility = "public", url_code = "hfskj", tags = ["nice", "college", "web"], date = arrow.get(datetime.datetime(2014, 3, 7, 13, 15, 45)).datetime)
  
  makeSnippet(language = "text", title = "bulgaria", content = "what?", visibility = "public", url_code = "gfslp", tags = ["barbie", "ok", "python"], date = arrow.get(datetime.datetime(2003, 2, 4, 16, 15, 54)).datetime)
  
  makeSnippet(language = "text", title = "epic music is cool", content = "brian tyler", visibility = "public", url_code = "eziol", tags = ["creed", "python"], date = arrow.get(datetime.datetime(2009, 5, 14, 3, 15, 12)).datetime)
  
  makeSnippet(author = Tyler, language = "text", title = "Assassin's Creed", content = "This is an Assasin's Creed Post!!", visibility = "public", url_code = "plaew", tags = ["creed", "assassin's creed", "cool"], date = arrow.get(datetime.datetime(2009, 5, 14, 15, 15, 12)).datetime)
  

if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
  django.setup()
  from snippet.models import Snippet, SnippetExtras
  from django.contrib.auth import get_user_model
  
  if 'x' in sys.argv[1:]:
    print "Clearing database...\n"
    endall()
  
  main()

