from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Information',  # Label displayed above the custom fields
         {'fields': ('bio',
                     'date_of_birth',
                     'phone_number')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
