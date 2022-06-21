from django.contrib import admin
from .models import CustomUserModel

class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'last_login'
    )
admin.site.register(CustomUserModel, CustomUserAdmin)