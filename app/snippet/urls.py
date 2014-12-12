from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views

urlpatterns = patterns("",
  url(r"^new/$", TemplateView.as_view(template_name = "snippet/new.html"), name = "new"),
  url(r"^newSnippet/$", views.SnippetCreateView.as_view(), name = "newSnippet")
)