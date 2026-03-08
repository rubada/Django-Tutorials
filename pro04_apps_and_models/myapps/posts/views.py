from django.shortcuts import render

from .models import Posts


# def posts_page(request):
#     emp_data = Posts.objects.all()
#     return render(
#         request,
#         "posts/posts_display.html",
#         {"emp_data": emp_data},
#     )

# 1. "Posts" is a model class, which represents a table in the database.

# 2. "objects" is the model manager.
# - Every Django model automatically gets a default manager called objects
# unless you override it.
# - A manager is the interface through which you query the database. It knows
# how to construct queries and return results.
# - Posts.objects gives you access to methods like .all(), .filter(), .get(),
# etc.
# - These methods are QuerySet methods.

# 3. ".all()" returns a QuerySet containing all rows from the posts table.

# A QuerySet is how Django represents a query against the database, and is
# used to retrieve objects.
# It’s not just raw SQL results — it’s an object that is:
# Lazy: They don’t run the SQL until needed.
# Chainable: You can stack methods like .filter(), .exclude(), .order_by()
# without executing multiple queries.
# Iterable: Once evaluated, you can loop through them like a list of objects.
# Flexible: You can slice, aggregate, and even convert them to dictionaries.
# When evaluated, it returns model instances (rows from your table).

# You can check the "QuerySet API reference" in Django docs, which covers
# methods like
# .all(), .filter(), .exclude(), .get(), .order_by(), .values(), .count(),
# .exists(), .aggregate(), and more.
# Here is the link:
# https://docs.djangoproject.com/en/6.0/ref/models/querysets/
# and,
# "Making queries" explains how to use QuerySets in practice, with
# examples of creating, retrieving, updating, and deleting objects:
# https://docs.djangoproject.com/en/6.0/topics/db/queries/

# Note you can make queries, update, delete, etc. using the Django Python
# shell:
# python manage.py shell
