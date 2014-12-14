from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import views

urlpatterns = patterns("",
  url(r"^logintest$", views.LoginTest.as_view(), name = "logintest"),
  url(r"^login/$", TemplateView.as_view(template_name = "userextension/login.html"), name ="login"),
  url(r"^u/(?P<usrname>.+)/$", views.UserProfileView.as_view(), name = "profile"),
  url(r"^me/$", views.UserDashboardView.as_view(), name = "dashboard"),
)
