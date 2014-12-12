from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views

urlpatterns = patterns("",
  # Template for new Snippet.
  url(r"^new/$", TemplateView.as_view(template_name = "snippet/new.html"), name = "new"),
  # Create a new Snippet (AJAX)
  url(r"^newSnippet/$", views.SnippetCreateView.as_view(), name = "newSnippet"),
  # View (and search) all Snippets.
  #url(r"^snippets/$", views.SnippetListView.as_view(), name = "listSnippet"),
  #url(r"^snippets(/y/(?P<year>\d{4}))?(/m/(?P<month>0?[1-9]|1[012]))?/$", views.SnippetListView.as_view(), name = "listSnippet"),
  url(r"^snippets(/y/(?P<year>[\d]{4}))?(/m/(?P<month>0?[1-9]|1[012]))?(/pg/(?P<page>[\d]+))?/$", views.SnippetListView.as_view(), name = "listSnippet"),
  # View a single Snippet.
  url(r"^(?P<urlcode>[\w-]+)/$", views.SnippetDetailView.as_view(), name = "detailSnippet"),
)

"""
/new/           template for a new snippet
/newSnippet/    post a new snippet (AJAX)
/snippets/...   view and search snippets
/<urlcode>/     view a single snippet
/<urlode>/raw/  view the raw text of a snippet
/<urlcode/copy/ copy an existing (public) snippet
/u/<usrname>/   view a user's profile
/me/            view your dashboard
----------------------------------------------------

/snippets/y/2013/m/3/

/snippets/(?P<month>/m/[])
^m/(0?[1-9]|1[012])$   # Month.

^(?P<month>m/(0?[1-9]|1[012]))$   # Month.
^(?P<year>y/(\d{4}))$        # year

^snippets(?P<year>/y/(\d{4}))?/(?P<month>m/(0?[1-9]|1[012]))?/$

^snippets(/y/(?P<year>\d{4}))?(/m/(?P<month>0?[1-9]|1[012]))?/$


"""

