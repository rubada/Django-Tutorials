from django.shortcuts import render, get_object_or_404, redirect
from blog_core.models import Blog
from blog_core.forms import BlogPostForm


def home_page(request):
    return render(request, 'home.html')


def blogs_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})


# POST here carries the new blog data to be saved.
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogPostForm()
    return render(request, 'blog_create.html', {'form': form})


# POST here carries the updated blog data. The key difference is instance=blog
# which tells Django to update the existing blog instead of creating a new one.
# GET (in else statement) creates a form pre-filled with the existing blog
# data so the user can see what they are editing.
def blog_update(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', slug=blog.slug)
    # GET here creates a form pre-filled with the existing blog data so the
    # user can see what they are editing.
    else:
        form = BlogPostForm(instance=blog)
    return render(request, 'blog_update.html', {'form': form, 'blog': blog})


# POST here carries no data at all — it just acts as a confirmation signal.
def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs_list')
    return render(request, 'blog_delete.html', {'blog': blog})

# GET here simply shows the confirmation page.
# Notice there is no else block here because the GET response is the default,
# if it is not a POST request, Django just renders the confirmation page, the
# 'blog_delete.html'.
