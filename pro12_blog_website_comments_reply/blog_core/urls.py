from django.urls import path
from blog_core import views

urlpatterns = [
    # public
    path('', views.home_page, name='home'),
    path('blogs/', views.blogs_list, name='blogs_list'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),

    # private
    path('my-blogs/', views.blogs_user_list, name='blogs_user_list'),
    # The create URL must come before the <slug:slug> pattern
    path('my-blogs/create/', views.blog_create, name='blog_create'),
    path('my-blogs/<slug:slug>/',
         views.blog_user_detail,
         name='blog_user_detail'),
    path('my-blogs/<slug:slug>/update/',
         views.blog_update,
         name='blog_update'),
    path('my-blogs/<slug:slug>/delete/',
         views.blog_delete,
         name='blog_delete'),
    # private Comments Urls:
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    # URL pattern for replying to a specific comment
    # Includes both the post_id (to identify the blog post)
    # and parent_id (to identify the comment being replied to).
    path(
        "post/<int:post_id>/comment/<int:parent_id>/reply/",
        views.add_comment,
        name="reply_comment"),
    path(
        'comment/<int:comment_id>/edit/',
        views.edit_comment,
        name='edit_comment'),
    path(
        'comment/<int:comment_id>/delete/',
        views.delete_comment,
        name='delete_comment'),
]
