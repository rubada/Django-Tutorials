from django.urls import path
from .views import (
    data_page_view,
)


urlpatterns = [
    # App root url, main app page url
    path("", data_page_view, name="datapage"),
]
