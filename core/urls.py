from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('' , include('index_app.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('userapp.urls')),
    path('story/', include('storyapp.urls')),
]
