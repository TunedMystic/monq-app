from django.test import TestCase
from django.core.urlresolvers import reverse
from snippet.models import Snippet
import arrow

class UrlTests(TestCase):
  def get(self, url, status = 200):
    res = self.client.get(reverse(url))
    self.assertEqual(res.status_code, status)
    return res
  
  def test_all_snippet_urls(self):
    self.get("snippet:index")
    self.get("snippet:new")
    self.get("snippet:allSnippet")
    self.get("snippet:searchFormSnippet")
  
  def test_create_snippet(self):
    self.assertEqual(Snippet.objects.count(), 0)
    data = {
      "content": "Hello, World! A simple snippet.",
      "date_added_raw": arrow.now().datetime
    }
    s = Snippet.objects.create(**data)
    self.assertEqual(Snippet.objects.count(), 1)
    self.assertEqual(s.content, data["content"])
  
  def test_post_snippet(self):
    r = self.client.post(
      reverse("snippet:newSnippet"), 
      {
        "content": "hello", 
        "date_added_raw": arrow.now().datetime,
        "visibility": "public",
        "language": "text"}
    )
    self.assertEqual(r.status_code, 200)
    
    