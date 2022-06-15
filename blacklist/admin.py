from django.contrib import admin

from blacklist.models import BlacklistedPassword, BlacklistedEmail, BlacklistedPhoneNumber

# Register your models here.
@admin.register(BlacklistedPassword)
class BlacklistedPasswordAdmin(admin.ModelAdmin):
    list_display = ('id', 'plaintext_password', 'date_added')
    ordering = ('-date_added',)
    search_fields = ('plaintext_password', 'hashed_value')


@admin.register(BlacklistedEmail)
class BlacklistedEmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_added')
    ordering = ('-date_added',)
    search_fields = ('email',)


@admin.register(BlacklistedPhoneNumber)
class BlacklistedPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'date_added')
    ordering = ('-date_added',)
    search_fields = ('phone_number',)
    
