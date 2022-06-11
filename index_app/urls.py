from django.urls import path
from index_app.views import index

urlpatterns = [
    path('', index, name='site_index'),
]
