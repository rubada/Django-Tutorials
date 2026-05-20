from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "title",
    )
    list_filter = ()  # Empty tuple hides filters


admin.site.register(Post, PostAdmin)
