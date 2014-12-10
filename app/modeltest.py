#!/usr/bin/env python
import os
import sys
import django

def endall():
  # Delete Snippets.
  for obj in Snippet.objects.all():
    obj.delete()
  # Delete Users.
  for obj in get_user_model().objects.all():
    obj.delete()


def main():

  # Make Users.
  Harry = get_user_model().objects.get_or_create(username = "harry", email = "harry@gmail.com", password = "harry")
  Emily = get_user_model().objects.get_or_create(username = "emily", email = "emily@gmail.com", password = "emily")
  Ramin = get_user_model().objects.get_or_create(username = "ramin", email = "ramin@gmail.com", password = "ramin")
  Tyler = get_user_model().objects.get_or_create(username = "tyler", email = "tyler@gmail.com", password = "tyler")
  Bella = get_user_model().objects.get_or_create(username = "bella", email = "bella@gmail.com", password = "bella")
  
  # Make some Snippets!
  s1 = Snippet.objects.create(author = Harry, language = "javascript", content = "function hello() {\nconsole.log('hello');\n}", url_code = "abcde")
  s1.tags.add("js")
  s1.tags.add("web")
  s1.tags.add("dev")
  s1.tags.add("programming")

  s2 = Snippet.objects.create(author = Bella, title = "Python Fibonnaci", language = "python", visibility = "public", url_code = "f4bcp", content = "startNumber = int(raw_input(\"Enter the start number here \"))\nendNumber = int(raw_input(\"Enter the end number here \"))\n\ndef fib(n):\n    if n < 2:\n        return n\n    return fib(n-2) + fib(n-1)\n\nprint map(fib, range(startNumber, endNumber))\n")
  s2.tags.add("python")
  s2.tags.add("dev")
  s2.tags.add("web")

  s3 = Snippet.objects.create(author = Harry, title = "Date program in python", language = "python", visibility = "public", url_code = "pw35g", content = "import datetime\nnow = datetime.datetime.now()\nprint \"-\" * 25\nprint now\nprint now.year\nprint now.month\nprint now.day\nprint now.hour\nprint now.minute\nprint now.second\n\nprint \"-\" * 25\nprint \"1 week ago was it: \", now - datetime.timedelta(weeks=1)\nprint \"100 days ago was: \", now - datetime.timedelta(days=100)\nprint \"1 week from now is it: \",  now + datetime.timedelta(weeks=1)\nprint \"In 1000 days from now is it: \", now + datetime.timedelta(days=1000)\n\nprint \"-\" * 25\nbirthday = datetime.datetime(2012,11,04)\n\nprint \"Birthday in ... \", birthday - now\nprint \"-\" * 25\n")
  s3.tags.add("python")
  s3.tags.add("date")
  s3.tags.add("prompt")

  s4 = Snippet.objects.create(author = Ramin, title = "For-loop in Ruby", language = "ruby", visibility = "public", url_code = "wteu3", content = "# Simple for loop using a range.\r\nfor i in (1..4)\r\n    print i,\" \"\r\nend\r\nprint \"\\n\"\r\n\r\nfor i in (1...4)\r\n    print i,\" \"\r\nend\r\nprint \"\\n\"\r\n\r\n# Running through a list (which is what they do).\r\nitems = [ 'Mark', 12, 'goobers', 18.45 ]\r\nfor it in items\r\n    print it, \" \"\r\nend\r\nprint \"\\n\"\r\n\r\n# Go through the legal subscript values of an array.\r\nfor i in (0...items.length)\r\n    print items[0..i].join(\" \"), \"\\n\"\r\nend")
  s4.tags.add("ruby")
  s4.tags.add("for loop")
  s4.tags.add("program")
  s4.tags.add("programming")


if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
  django.setup()
  from snippet.models import Snippet, SnippetExtras
  from django.contrib.auth import get_user_model
  
  if 'x' in sys.argv[1:]:
    print "Clearing database...\n"
    endall()
  
  main()

