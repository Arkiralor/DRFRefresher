from django.urls import path

from searchapp.apis import SearchStoryAPI, SearchUserAPI, AllStoriesByAuthorAPI

urlpatterns = [
    path('story/', SearchStoryAPI.as_view(), name='search_story'),
    path('story/by', AllStoriesByAuthorAPI.as_view(), name='all_stories_by_author'),
    path('user/', SearchUserAPI.as_view(), name='search_user'),
]