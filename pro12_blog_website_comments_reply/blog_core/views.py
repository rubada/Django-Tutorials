from django.urls import reverse
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect)
from django.contrib.auth.decorators import login_required
from blog_core.models import (
    Blog,
    Comment,        # Import the comment model
    )
from blog_core.forms import (
    BlogPostForm,
    CommentForm,    # Import the comment form
)
from django.http import HttpResponseForbidden
from django.utils.http import url_has_allowed_host_and_scheme


# ─── Public views (no login required) ────────────────────────────────
def home_page(request):
    return render(request, 'home.html')


def blogs_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_core/blog.html', {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    top_level_comments = blog.comments.filter(parent__isnull=True)
    return render(
        request,
        'blog_core/blog_detail.html',
        {
            'blog': blog,
            'top_level_comments': top_level_comments,
        }
    )


# ─── Private views (login required) ──────────────────────────────────
@login_required
def blogs_user_list(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'blog_core/user_blogs.html', {'blogs': blogs})


@login_required
def blog_user_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug, author=request.user)
    top_level_comments = blog.comments.filter(parent__isnull=True)
    return render(request, 'blog_core/user_blog_detail.html', {
        'blog': blog,
        'top_level_comments': top_level_comments,
    })


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


# Comment views:
# 📝 Add Comment View
# `parent_id` allows the same view to handle both creating a new top-level
# comment and replying to an existing comment.
# - **Top‑level comment:** When no `parent_id` is provided, the comment is
# saved without a parent, making it a root comment.
# All Top-level comments are saved with None in the parent column (stored as
# NULL in the database).
# - **Reply to a comment:** When a `parent_id` is passed, the new comment is
# linked to that parent, creating a nested reply.
@login_required
def add_comment(request, post_id, parent_id=None):
    post = get_object_or_404(Blog, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create object in memory only
            comment = form.save(commit=False)
            # Link the comment to its post (Blog)
            comment.post = post
            # Assign logged-in user
            comment.author = request.user

            # Attach reply to parent if parent_id is provided
            if parent_id:
                comment.parent = get_object_or_404(Comment, id=parent_id)

            # Save the comment in database:
            comment.save()
            return redirect("blog_detail", slug=post.slug)

    # If not POST, redirect back to detail view
    # If this view is called without a form submission, don’t do anything
    # special — just send the user back to the blog detail page.
    # (for example, typing the URL in the browser or hitting refresh on that
    # endpoint)
    return redirect("blog_detail", slug=post.slug)


# This 'get_next_url' function with the 'edit_comment' function allows users
# to edit their own comments and then return to the page they were viewing
# before starting the edit.
# 1. The 'edit_comment()' view first ensures that the user is authenticated
# and is the author of the comment. If the submitted form is valid, the
# existing comment is updated and saved.
# 2. Once the comment has been saved, the application needs to determine where
# to redirect the user. This responsibility is handled by the get_next_url()
# helper function.
# 3. The get_next_url() function checks for a next value submitted with the
# form. This value typically stores the URL of the page from which the user
# initiated the edit. Before redirecting, Django verifies that the URL belongs
# to the current site using 'url_has_allowed_host_and_scheme()'. This
# validation prevents open redirect vulnerabilities by blocking redirects to
# untrusted external websites.
# 4. If the next URL is present and passes the security check, the user is
# redirected back to that page. Otherwise, the view falls back to the blog
# post associated with the comment.
def get_next_url(request, fallback):
    # Get the next value from the form
    next_url = request.POST.get('next')
    # Validate the URL
    if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()}
            ):
        # Return the correct URL
        return next_url
    # Otherwise it returns the fallback which is a safe default URL.
    return fallback


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
    # The fallback URL serves as a safe destination. If the next URL is
    # missing or fails Django's security check, the user is redirected to the
    # related blog post page.
    fallback = reverse('blog_detail', kwargs={'slug': comment.post.slug})
    return redirect(get_next_url(request, fallback))


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden()
    post_slug = comment.post.slug
    if request.method == 'POST':
        comment.delete()
    return redirect('blog_detail', slug=post_slug)

# `HttpResponseForbidden` is one of Django’s built‑in HTTP response classes.
# It generates an HTTP **403 Forbidden** response, which tells the client:
# *“The request was understood, but the user does not have permission to
# perform this action.”*
