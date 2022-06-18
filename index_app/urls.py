from django.urls import path
from index_app.views import index, see_users, see_stories

urlpatterns = [
    path('', index, name='site_index'),
    path('see/users', see_users, name='see_users'),
    path('see/stories', see_stories, name='see_stories'),
]
