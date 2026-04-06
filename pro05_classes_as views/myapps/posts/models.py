# When the "models.py" is created, django will import the "models" module from
# "django.db"
from django.db import models


# Let's create a django ORM:
# The "Posts" class will be a table in the database:
class Posts(models.Model):

    # TextField is a Django model field used to store large text data in the
    # database.
    # IntegerField is a Django model field used to store integers data in the
    # database.
    # These fields maps to a database column type that can hold long strings,
    # integers, floats, binarys, etc.
    # There are other fields that we will discuss later.
    # The below attributes will be a columns in the "Posts" database.
    # CharField in Django is a model field used to store short-to-medium
    # length strings, such as names, titles, or identifiers. It requires a
    # max_length parameter to define the maximum number of characters allowed.

    # CharField in Django is a model field used to store short-to-medium
    # length strings, such as names, titles, or identifiers. It requires a
    # "max_length" parameter to define the maximum number of characters
    # allowed.

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    # # Here I added a new column:
    title = models.CharField(max_length=20, default="null")
    message = models.TextField()

    # The "__str__" method is used to define the human-readable string
    # representation of a model object.

    def __str__(self):
        return f"{self.title} by {self.first_name} {self.last_name}"
