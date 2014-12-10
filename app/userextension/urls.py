from django.conf.urls import patterns, include, url
from .views import LoginTest

urlpatterns = patterns("",
  url(r"^$", LoginTest.as_view(), name = "logintest"),
)