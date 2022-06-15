from django.contrib import admin
from userapp.models import User, UserProfile, UserOTP

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff',
                    'is_superuser', 'user_type', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'user_type', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'headline', 'location')
    raw_id_fields = ('user',)
    search_fields = ('user__username', 'user__email')
    ordering = ('-created_at',)


@admin.register(UserOTP)
class UserOTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'otp', 'expiry')
    raw_id_fields = ('user',)
    search_fields = ('user__username', 'user__email')
    ordering = ('-created_at',)
