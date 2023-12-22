from django.contrib import admin
from django.urls import path, include 

from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('', include('userprofile.urls', namespace='userprofile')),
    path('api-auth/', include('rest_framework.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))