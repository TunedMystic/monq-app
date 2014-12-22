from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views

urlpatterns = patterns("",
  #url(r"^.*$", TemplateView.as_view(template_name = "nil/index.html"), name = "index"),
  url(r"^about/$", TemplateView.as_view(template_name = "nil/about.html"), name = "about"),
  url(r"^404/$", views.error404, name = "error404"),
  url(r"^500/$", views.error500, name = "error500"),
)
