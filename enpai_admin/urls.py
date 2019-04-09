from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.urls import re_path


from filebrowser.sites import site

urlpatterns = [
    path('backend/admin/filebrowser/', site.urls),
    path('backend/grappelli/', include('grappelli.urls')),
    path('backend/admin/', admin.site.urls),
    path('backend/manage/', include('backend.urls'))
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^backend/media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]