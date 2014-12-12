from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',  
  #url(r"^", include("nil.urls", namespace = "nil")),
  #url(r"^", include("userextension.urls", namespace = "userext")),
  url(r"", include("snippet.urls", namespace = "snippet")),
  url(r'^admin/', include(admin.site.urls)),
)
