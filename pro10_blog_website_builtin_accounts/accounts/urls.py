from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
# from accounts.forms import LoginForm

urlpatterns = [
    path("register/", views.register, name="register"),
]
