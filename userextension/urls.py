from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views

urlpatterns = patterns("",
  url(r"^logintest$", views.LoginTest.as_view(), name = "logintest"),
  url(r"^login/$", views.LoginView.as_view(), name ="login"),
  url(r"^u/(?P<usrname>.+)/$", views.UserProfileView.as_view(), name = "profile"),
  url(r"^me/$", views.UserDashboardView.as_view(), name = "dashboard"),
  url(r"^me/snippets(?:/(?P<pg>[\d]+))?/$", views.UserSnippetsView.as_view(), name = "usersnippets"),
  url(r"^me/likes(?:/(?P<pg>[\d]+))?/$", views.UserSnippetLikesView.as_view(), name = "usersnippetlikes"),
)
