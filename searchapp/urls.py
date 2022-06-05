from django.urls import path

from searchapp.apis import SearchStoryAPI, SearchUserAPI

urlpatterns = [
    path('story/', SearchStoryAPI.as_view(), name='search_story'),
    path('user/', SearchUserAPI.as_view(), name='search_user'),
]