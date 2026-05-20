# Previously we list all the blogs on one webpage, but this apprach is not
# practical, what we should is to create two pages:
# - Page 1 (List View): shows all blogs with links.
# - Page 2 (Detail View): shows the content of a single blog post.

# This  is done by using the "get_object_or_404()" funtion.

# The "get_object_or_404" in Django is a shortcut function that retrieves a
# single object from the database and automatically raises an HTTP 404 error
# if the object doesn’t exist.
# This is especially useful in views where you expect one specific record and
# want to handle missing data gracefully without writing extra error-handling
# code.


# 📊 Why Use get_object_or_404
# - Cleaner Code: Avoids writing manual try/except blocks for DoesNotExist.
# - User-Friendly: Automatically returns a proper 404 page instead of crashing.
# - Security: Prevents exposing unnecessary error details to users.
# - Efficiency: Performs a single query, similar to .get(), but with built-in
# error handling.


# In the blog_core/views.py:
from django.shortcuts import render
from django.http import Http404
from blog_core.models import Post
from django.shortcuts import get_object_or_404


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})


# 1. This is how we can do it with out using "get_object_or_404" function:
def blog_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("No Post matches the given query.")
    return render(request, 'blog_detail.html', {'post': post})


# 2. This how to do it using "get_object_or_404" function:
def blog_detail_rev(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog_detail.html', {'post': post})
