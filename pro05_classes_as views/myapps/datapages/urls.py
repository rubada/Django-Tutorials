from django.urls import path
from .views import (
    DataPageView
)


urlpatterns = [
    # App root url, main app page url
    path("", DataPageView.as_view(), name="datapage"),
]
