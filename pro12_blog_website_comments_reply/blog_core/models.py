from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings


class Blog(models.Model):

    title = models.CharField(max_length=200, blank="True")
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               default=1)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} \
by {self.author.first_name} {self.author.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_user_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    # Each comment must be tied to the object it belongs to (e.g., a Blog).
    # post: Connects the comment to a blog post.
    post = models.ForeignKey(
        Blog,

        # Delete a blog post, and all its comments are deleted
        on_delete=models.CASCADE,

        # In Django, the related_name attribute defines the name used to access
        # related objects from the reverse side of a relationship (Means
        # starting from post (blog) and access all its comments, because the
        # Blog model does not have a field named comments. Django creates this
        # relationship automatically because Comment points to Blog.)
        # Allows you to access all comments belonging to a post (blog) using:
        # post.comments.all()
        related_name='comments')

    # User association: Tracks which user authored the comment.
    # author: Identifies the comment author.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # Delete a user, and every comment they wrote is deleted
        on_delete=models.CASCADE)

    # Replies (nested comments): Achieved by linking a comment back to another
    # comment using a parent field.
    # parent: points to the comment being replied to.
    parent = models.ForeignKey(
        'self',
        # Delete a comment, and all its replies are deleted
        on_delete=models.CASCADE,
        # Allows the parent column to store NULL in database, required because
        # top-level comments do not have a parent.
        null=True,
        # Form-validation setting:
        # Allows the parent field to be left empty in Django forms and the
        # Django admin.
        # Needed because top-level comments do not have a parent comment.
        blank=True,
        # Allows you to access all replies to a comment using:
        # `comment.replies.all()`
        related_name='replies'
    )

    # content: field stores the text of the comment. Since every
    # comment—whether a top‑level entry or a reply—requires text, both use the
    # same column.
    content = models.TextField()

    # created_at / updated_at: Automatically record when a comment is created
    # or updated. Manage chronological order. (إدارة الترتيب الزمني)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


# What does `on_delete` mean?

# - **`on_delete=models.CASCADE`**

# - **`on_delete=models.SET_NULL`**
#  "post" field	(Blog):	Delete a blog post, and its comments stay with
# post = NULL
#  "author" field (the user): Delete a user, and their comments stay with
# author = NULL
#  "parent" field (Comment): Delete a comment, and its replies stay with
# parent = NULL
# All replies become top-level comments when their parent comment is deleted
# using SET_NULL.

# Before deleting:
'''
#1 Great post!
 ├─ #2 I agree
 │   └─ #4 Thanks!
 └─ #3 Me too
'''

# After deleting:
'''
#2 I agree
 └─ #4 Thanks!
#3 Me too
'''
# Custom approach (soft delete)
# Rather than removing a comment from the database, mark it as deleted using
# the following field:
'''is_deleted = models.BooleanField(default=False)'''

# As shown below:
'''
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='replies',
        null=True,
        blank=True
    )
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)
'''
# Before deleting:
'''
#1 Great post!
 ├─ #2 I agree
 │   └─ #4 Thanks!
 └─ #3 Me too
'''

# After deleting:
'''
#1 [This comment was deleted]
 ├─ #2 I agree
 │   └─ #4 Thanks!
 └─ #3 Me too
'''
# Django doesn’t do this automatically. Your template has to check the field
# when it renders each comment:
'''
{% if comment.is_deleted %}
    <em>This comment was deleted</em>
{% else %}
    {{ comment.body }}
{% endif %}
'''
