from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'webapp.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),
  
  #url(r"^", include("nil.urls", namespace = "nil")),
  url(r"^", include("userextension.urls", namespace = "userext")),
  url(r'^admin/', include(admin.site.urls)),
)
