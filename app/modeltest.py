from snippet.models import Snippet, SnippetExtras
from django.contrib.auth import get_user_model as uu

ss = lambda: Snippet.objects.all()
se = lambda: SnippetExtras.objects.all()
def endall():
  for obj in ss():
    obj.delete()

tak = uu().objects.get(pk = 1)

s1 = Snippet.objects.create(author = tak, content = "function hello(){print 'hello';}", language = "javascript", url_code = "abcde")
#s1.author = tak
s1.tags.add("js")
s1.tags.add("web")
s1.tags.add("dev")
s1.tags.add("programming")

s2 = Snippet.objects.create(author = tak, title = "Python Fibonnaci", visibility = "public", url_code = "f4bcp", content = "startNumber = int(raw_input(\"Enter the start number here \"))\nendNumber = int(raw_input(\"Enter the end number here \"))\n\ndef fib(n):\n    if n < 2:\n        return n\n    return fib(n-2) + fib(n-1)\n\nprint map(fib, range(startNumber, endNumber))\n")
#s2.author = tak
s2.tags.add("python")
s2.tags.add("dev")
s2.tags.add("web")

s3 = Snippet.objects.create(author = tak, title = "Python Fibonnaci", visibility = "public", url_code = "f4bcp", content = "import datetime\nnow = datetime.datetime.now()\nprint \"-\" * 25\nprint now\nprint now.year\nprint now.month\nprint now.day\nprint now.hour\nprint now.minute\nprint now.second\n\nprint \"-\" * 25\nprint \"1 week ago was it: \", now - datetime.timedelta(weeks=1)\nprint \"100 days ago was: \", now - datetime.timedelta(days=100)\nprint \"1 week from now is it: \",  now + datetime.timedelta(weeks=1)\nprint \"In 1000 days from now is it: \", now + datetime.timedelta(days=1000)\n\nprint \"-\" * 25\nbirthday = datetime.datetime(2012,11,04)\n\nprint \"Birthday in ... \", birthday - now\nprint \"-\" * 25\n")
#s3.author = tak
s3.tags.add("python")
s3.tags.add("date")
s3.tags.add("prompt")

