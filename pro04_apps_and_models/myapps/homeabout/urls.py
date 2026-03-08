from django.urls import path
from .views import home_page_view, about_page_view


urlpatterns = [
    # This is the url for the about page (e.g. http://www.example.com/about)
    path("about/", about_page_view, name="aboutpage"),
    # App root url, main app page url
    path("", home_page_view, name="homepage"),
]
