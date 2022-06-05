from django.contrib import admin
from storyapp.models import Story

# Register your models here.


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'author')
    raw_id_fields = ('author',)
