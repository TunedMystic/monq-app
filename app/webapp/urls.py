from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url('', include('social.apps.django_app.urls', namespace='social')),
  url(r"", include("nil.urls", namespace = "nil")),
  url(r"", include("userextension.urls", namespace = "userext")),
  url(r"", include("snippet.urls", namespace = "snippet")),
)

handler404 = "nil.views.error404"
handler500 = "nil.views.error500"
