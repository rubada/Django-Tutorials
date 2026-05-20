from django.db import models


# Don't forget:
# To run 'makemigrations' and 'migrate'.
# To create a super user to access the Admin page.
class Post(models.Model):

    title = models.CharField(max_length=20, default="null")
    message = models.TextField()
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )

    # Here I removed the first_name and last_name from the str
    # because they are not defined in the Post model:
    def __str__(self):
        return f"{self.title} by {self.author}"

# "auth.User" is Django's built-in User model from the django.contrib.auth
# application.
# auth = the app name (django.contrib.auth)
# User = the model name within that app

# Django references "auth.User", it maps to the auth_user table in your
# database.
# This creates a foreign key relationship between the blog_core_post table and
# the auth_user table. The author field in each post record stores the ID of a
# user from that auth_user table.
