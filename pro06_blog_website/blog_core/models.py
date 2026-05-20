from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# class Post(models.Model):

#     title = models.CharField(max_length=20, default="null")
#     message = models.TextField()
#     author = models.ForeignKey(
#         "auth.User",
#         on_delete=models.CASCADE,
#     )

#     def __str__(self):
#         return f"{self.title} by {self.author}"

#     # When you add methods to a Django model, you don’t need to run
#     # makemigrations or migrate, since these commands only apply when there
#     # are changes to the database schema, not to the model’s Python logic.
#     def get_absolute_url(self):
#         return reverse('blog-detail', kwargs={'post_id': self.pk})

# reverse(viewname, kwargs=...) takes a URL pattern name (as defined in your
# urls.py) and any arguments, and returns the actual URL string.


# Why We Add a Slug?
# A slug is a URL-friendly version of a text field (usually a title) that is
# used to identify a resource in a URL.

# It is typically lowercase, with spaces replaced by hyphens and special
# characters are removed, this done by using the "slugify" function, which
# converts a regular text string into a URL friendly slug:

# For example:
# "My First Post#1!!" → "my-first-post-1"

# Instead of having URLs like /posts/1/, you get clean readable URLs like
# /posts/my-first-post/. This is better for users and SEO.

# The slug attribute should have unique data, because it is used in the
# browser URL, and each URL should be unique from the other one, that is why
# the slug attribute should be defined when you first create the model.

# The slug attribute:
# slug = models.SlugField(unique=True, blank=True)

# "blank=True" is used if you want the admin/form to allow leaving the slug
# empty, but always add logic to auto-generate a unique slug.

# Examples:
# 1. In the Django admin panel if the slug field is visible and editable,
# so blank=True allows admins to leave it empty and let save() fill it in
# 2. Some developers add it as a safety net just in case the slug field appears
# somewhere unexpected.

# class Post(models.Model):

#     title = models.CharField(max_length=20, default="null")
#     message = models.TextField()
#     author = models.ForeignKey(
#         "auth.User",
#         on_delete=models.CASCADE,
#     )
#     slug = models.SlugField(unique=True, blank=True)

#     def __str__(self):
#         return f"{self.title} by {self.author}"

#     # Auto-generate slug from title when saving:
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             base_slug = slugify(self.title)
#             slug = base_slug
#             counter = 1

#             # The counter in the while loop ensures uniqueness and only adds
#             # a number when there is a duplicate title:
#             while Post.objects.filter(slug=slug).exists():
#                 slug = f"{base_slug}-{counter}"
#                 counter += 1
#             self.slug = slug
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('blog-detail', kwargs={'slug': self.slug})

# Why did we define "base_slug" and "slug":

# With One Variable ❌
# Iteration 1: slug = "my-first-post-1"
# Iteration 2: slug = "my-first-post-1-2"  ❌ wrong!
# Iteration 3: slug = "my-first-post-1-2-3"  ❌ wrong!

# With Two Variables ✅
# Iteration 1: slug = "my-first-post-1"  ✅
# Iteration 2: slug = "my-first-post-2"  ✅
# Iteration 3: slug = "my-first-post-3"  ✅

# The Problem With Existing Data:
# When you add a new column to a table that already has rows in it, the
# database doesn't know what value to put in that column for the existing
# rows. So all existing rows get null in the new slug column, if the "unique"
# parameter equal to "False".
# This becomes a problem if the "unique" parameter equal to "True", because
# the slug column values should be unique meaning no two posts can have the
# same slug, and if all existing rows have null, the database can't enforce
# uniqueness on empty values, and you may not able to run migrate.

# In this case to add the slug column to the table in the database, modify the
# migration to provide unique default values. Edit the migration file (in our
# case file 0003_post_slug.py) to add a default parameter that generates
# unique slugs.

# Steps to resolve the issue:
# Step 1 - models.py add this line with null=True.
#         slug = models.SlugField(unique=True, null=True, blank=True)
#                     ↓
# Step 2 - run makemigrations
#         generates 0003_post_slug.py
#                     ↓
# Step 3 - Edit 0003_post_slug.py
#         add generate_unique_slugs function
#         add RunPython operation
#
# Step 4 - migrate
#         Django executes in order:
#         AddField   → slug column added (all null)
#         RunPython  → generate_unique_slugs() called (all slugs populated)
#         AlterField → unique=True enforced (safely, no nulls left)
#                     ↓
#                    ✅ Done! All existing posts have slugs,
#                       all future posts auto-generate slugs via save()
#                       defined in the Post model.

class Post(models.Model):

    title = models.CharField(max_length=20, default="null")
    message = models.TextField()
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})


# Should You Remove null=True After Migration?

# Technically yes, you could remove it to make the constraint stricter:

# slug = models.SlugField(unique=True)  # cleaner final state

# But this requires to run makemigrations and migrate. Most developers just
# leave null=True since in practice no row will ever be null anyway thanks to
# the save() method.
