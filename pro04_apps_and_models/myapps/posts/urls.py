from django.urls import path
from .views import posts_page


urlpatterns = [
    path("", posts_page, name="post_page"),
]
