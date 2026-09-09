from django.urls import path
from blog_core import views

urlpatterns = [
    # public
    path('', views.home_page, name='home'),
    path('blogs/', views.blogs_list, name='blogs_list'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),

    # private
    # As shown below, the route name has been updated to clearly distinguish
    # public URLs from private ones.
    path('my-blogs/', views.blogs_user_list, name='blogs_user_list'),
    # The create URL must come before the <slug:slug> pattern
    path('my-blogs/create/', views.blog_create, name='blog_create'),
    path('my-blogs/<slug:slug>/update/',
         views.blog_update, name='blog_update'),
    path('my-blogs/<slug:slug>/delete/',
         views.blog_delete, name='blog_delete'),
]
