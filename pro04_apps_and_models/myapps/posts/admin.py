# This line is added when django creates your app:
from django.contrib import admin

# # Import your model:
from .models import Posts

# Then add the following to register your model:
admin.site.register(Posts)

# Django knows it should display our posts app and its database model
# "Posts" on the admin page.
