from django.urls import path
from .views import home

urlpatterns = [
    # The empty string '' here is the root page for this app or
    # the default view for that app’s root.
    path("", home, name="homepage"),
]
