from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
  
  url(r'^admin/', include(admin.site.urls)),
  url(r"", include("userextension.urls", namespace = "userext")),
  url(r"^logout/$", "django.contrib.auth.views.logout", kwargs = {"next_page": "/"}, name = "auth_logout"),
  url('', include('social.apps.django_app.urls', namespace='social')),
  url(r"", include("nil.urls", namespace = "nil")),
  url(r"", include("snippet.urls", namespace = "snippet")),
  
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

handler404 = "nil.views.error404"
handler500 = "nil.views.error500"
