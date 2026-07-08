from django.urls import path
from blog_core import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('blogs/', views.blogs_list, name='blogs_list'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blogs/create/', views.blog_create, name='blog_create'),
    path('blogs/<slug:slug>/update/', views.blog_update, name='blog_update'),
    path('blogs/<slug:slug>/delete/', views.blog_delete, name='blog_delete'),
]
