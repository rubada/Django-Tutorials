from django.shortcuts import render
from blog_core.models import Post
from django.shortcuts import get_object_or_404


def home_page(request):
    return render(request, 'home.html')


# Using get_object_or_404:
def blogs_list(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})


# def blog_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'blog_detail.html', {'post': post})


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})
