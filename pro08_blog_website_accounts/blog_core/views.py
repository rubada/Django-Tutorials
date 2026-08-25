# from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from blog_core.models import Blog
from blog_core.forms import BlogPostForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_core/blog.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_core/blog_detail.html'
    context_object_name = 'blog'
    slug_field = 'slug'


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogPostForm
    template_name = 'blog_core/blog_create.html'


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogPostForm
    template_name = 'blog_core/blog_update.html'
    context_object_name = 'blog'


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_core/blog_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blogs_list')
