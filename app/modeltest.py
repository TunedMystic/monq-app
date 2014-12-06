from snippet.models import Snippet
from django.contrib.auth import get_user_model as uu

ss = lambda: Snippet.objects.all()

tak = uu().objects.all()[0]
s = Snippet(content = "function hello(){print 'hello';}", language = "javascript", url_code = "abcde")
s.author = tak
s.save()
s.tags.add("js")
s.tags.add("web")
s.tags.add("dev")
s.tags.add("programming")
s.save()