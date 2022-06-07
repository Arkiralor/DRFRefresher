from django.urls import path
from storyapp.apis import GetAllStoriesAPI, AddStoryAPI, IndividualStoryAPI, IndividualStoryBySlugAPI


urlpatterns = [
    path('', IndividualStoryAPI.as_view(), name='single_story'),
    path('<slug:slug>', IndividualStoryBySlugAPI.as_view(), name='story_by_slug'),
    path('all/', GetAllStoriesAPI.as_view(), name='all_stories'),
    path('add/', AddStoryAPI.as_view(), name='new_story'),    
]