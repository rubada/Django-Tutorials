from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog_core.models import Blog
from blog_core.forms import BlogPostForm


# ─── Public views (no login required) ────────────────────────────────
def home_page(request):
    return render(request, 'home.html')


def blogs_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_core/blog.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_core/blog_detail.html', {'blog': blog})


# ─── Private views (login required) ──────────────────────────────────
@login_required
def blogs_user_list(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'blog_core/user_blogs.html', {'blogs': blogs})


@login_required
def blog_user_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, author=request.user)
    return render(request, 'blog_core/user_blog_detail.html', {'blog': blog})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogPostForm()
    return render(request, 'blog_core/blog_create.html', {'form': form})


@login_required
def blog_update(request, slug):
    blog = get_object_or_404(Blog, slug=slug, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogPostForm(instance=blog)
    return render(request,
                  'blog_core/blog_update.html',
                  {'form': form, 'blog': blog})


@login_required
def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs_list')
    return render(request, 'blog_core/blog_delete.html', {'blog': blog})
