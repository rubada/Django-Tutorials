from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "title",
    )
    list_filter = ()  # Empty tuple hides filters


admin.site.register(Blog, BlogAdmin)
