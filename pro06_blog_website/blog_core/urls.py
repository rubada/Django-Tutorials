from django.urls import path
from .views import (
    home_page,
    blog_detail,
    blogs_list,
)

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', blogs_list, name='blogs_list'),
    path('blog/<slug:slug>/', blog_detail, name='blog-detail'),
    # path("blog/<int:post_id>/", blog_detail, name="blog-detail"),
]

# blog/<int:post_id>/ is the url to each blog using the pk.
