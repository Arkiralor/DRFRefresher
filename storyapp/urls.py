from django.urls import path
from storyapp.apis import GetAllStoriesAPI, AddStoryAPI, IndividualStoryAPI, IndividualStoryBySlugAPI


urlpatterns = [
    path('', IndividualStoryAPI.as_view(), name='single_story'),
    path('add/', AddStoryAPI.as_view(), name='new_story'),
    path('all/', GetAllStoriesAPI.as_view(), name='all_stories'),
    ## prithoot: added this path for story by slug last otherwise it was messing up the routes.
    ## TODO: Might need to do this in the other apps as well.
    path('ind/<slug:slug>', IndividualStoryBySlugAPI.as_view(), name='story_by_slug'),
]
