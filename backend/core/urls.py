from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from core.swagger_schema import schema_view
from core import settings
from core import logger


urlpatterns = [
    path('blacklist/', include('blacklist.urls')),   
    path('location/', include('locationapp.urls')),
    path('payment/', include('payment_app.urls')), 
    path('search/', include('searchapp.urls')),
    path('story/', include('storyapp.urls')),
    path('user/', include('userapp.urls')),    
]

## These url patterns are only available in a development environment
if settings.DEBUG or settings.ENV_TYPE == 'dev':
    urlpatterns += [
        path('', include('index_app.urls')),
        path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('assets/images/favicon.ico'))),
        path('admin/', admin.site.urls),
        re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                schema_view.without_ui(cache_timeout=0), name='schema_json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger',
                cache_timeout=0), name='schema_swagger_ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc',
                cache_timeout=0), name='schema_redoc'),
    ]

    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## These url patterns are only available in a production environment
elif settings.ENV_TYPE == 'prod' and not settings.DEBUG:
    urlpatterns += [
        path('8ccb652246c932d0/', admin.site.urls),
    ]
