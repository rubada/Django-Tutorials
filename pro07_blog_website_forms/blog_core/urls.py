from django.urls import path
from blog_core import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('blogs/', views.BlogListView.as_view(), name='blogs_list'),
    path('blogs/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path(
        'blogs/<slug:slug>/',
        views.BlogDetailView.as_view(),
        name='blog_detail',
    ),
    path(
        'blogs/<slug:slug>/update/',
        views.BlogUpdateView.as_view(),
        name='blog_update',
    ),
    path(
        'blogs/<slug:slug>/delete/',
        views.BlogDeleteView.as_view(),
        name='blog_delete',
    ),
]
