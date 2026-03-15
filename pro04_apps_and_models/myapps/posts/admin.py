# This line is added when django creates your app:
from django.contrib import admin

# # Import your model:
from .models import Posts


# We can customize the app to determine how the Posts model appears in the
# Django Admin interface, this is done by:
# 1. Define a class that inherits "admin.ModelAdmin" to control how the model
# is displayed and interacted with in the Django Admin site.
# 2. Create a variable called "list_display", which is a tuple of field names
# from those that are defined in the model, it tells Django which fields to
# show in the list view of the Admin interface.
# Without list_display, Django would only show the string representation
# (__str__) of each object.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        # "age",
        "title",
        # "message",
    )

# Then add the following to register your model:
# admin.site.register(Posts)


# Then register this class as follows:
admin.site.register(Posts, PostAdmin)

# Django knows it should display our posts app and its database model
# "Posts" on the admin page.
