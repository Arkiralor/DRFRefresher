from django.contrib import admin
from django.urls import path, include, re_path
from core.swagger_schema import schema_view
from core import settings

urlpatterns = [
    path('' , include('index_app.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('userapp.urls')),
    path('story/', include('storyapp.urls')),
    path('location/', include('locationapp.urls')),
    path('search/', include('searchapp.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema_json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc'),
    ]