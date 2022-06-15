from django.urls import path
from index_app.views import index, see_users

urlpatterns = [
    path('', index, name='site_index'),
    path('see/users', see_users, name='see_users'),
]
