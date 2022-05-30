from django.contrib import admin
from userapp.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser', 'user_type', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'user_type', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)
