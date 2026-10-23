# Custom User Authentication System in Django
# The built‑in `User` model from `django.contrib.auth` is a concrete,
# pre‑migrated model that cannot be directly extended with new fields.
# Attributes such as a bio, avatar, or profile picture cannot be added to this
# default model.
# Relying on the default `User` also locks you into using `username` as the
# login field, preventing the more common practice of authenticating with an
# email address.

# Why not just add a Profile model?

# A common beginner instinct is to keep `django.contrib.auth.User` and attach
# a Profile model via `OneToOneField`.

# This approach introduces several issues:
# - **Extra joins**: Queries involving both user and profile data always
# require a join.
# - **Increased complexity**: Admin, forms, and serializers must handle two
# models instead of one.
# - **Error risk**: If a User exists without a matching Profile, you’ll hit
# `RelatedObjectDoesNotExist`.
# - Etc.

# Recommended approach: Define a custom User model
# Create a custom User model in `accounts/models.py` before running your first
# migration, why?
# Starting with Django’s default `User` creates lock‑in:
# if you define a custom User model after the first migration, you cannot
# easily switch to it.
# By defining a custom model upfront—even if it’s initially empty, you keep
# future extensions simple, making it easy to add fields or adjust
# authentication behavior without painful refactors.

# To create a custum user model:

# 1. In settings.py, add:
'''
AUTH_USER_MODEL = 'accounts.CustomUser'
'''
# This line must be in place before running `python manage.py makemigrations`
# for the first time in the project.

# 2. In accounts/models.py create CustomUser model:
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add custom fields here now or in the future (e.g., bio, avatar, etc.)
    pass


# What is "AbstractUser"?
# Django’s default User model is built through inheritance:

# AbstractBaseUser  → is a base class in the Django web framework that
#                     provides core authentication features (like password
#                     hashing and last login tracking) while containing only
#                     the password field, allowing developers to build a
#                     completely custom user model from scratch.
#       ▲
#  AbstractUser     → Is an abstract base class (a blueprint) adds common
#                     fields (username, email, names, permissions).
#       ▲
#      User         → Concrete implementation used by default.
#                     Creates the 'auth_user' table.


# 3. In blog_core/models.py, change the author field to use:
# 'settings.AUTH_USER_MODEL' instead of 'User'

# 'settings.AUTH_USER_MODEL' will automatically point to accounts.CustomUser
# (since you set AUTH_USER_MODEL = 'accounts.CustomUser' in settings.py).

# When you use settings.AUTH_USER_MODEL, you’re working with the active user
# model which is CustomUser in your project, even if it is empty because it
# inherits the 'AbstractUser' class which gives you all the default fields
# (username, email, password, groups, user_permissions, etc.)

# 4. Update your registration form in `accounts/forms.py`
# - Replace the default `User` model with your `CustomUser`.
# - Include any additional fields you want users to complete during
# registration.

# 5. (Optional) Register your custom user model with the admin in
# `accounts/admin.py`.

# 6. First Migration
'''
python manage.py makemigrations
python manage.py migrate
'''
# Don't forget to create a superuser:
"""
python manage.py createsuperuser
"""

# 7. Views
# - You can create your own views as discussed earlier; `request.user` will
#   automatically reference your `CustomUser`.
# - Alternatively, you can rely on Django’s built‑in authentication views
#   and simply include their required URLs.

# 8. (Optional) Use your Custom Forms:
# As mentioned before, Django’s built-in authentication views (e.g., LoginView,
# PasswordResetView) use their default forms.
# If you want to use your own custom forms, you need to wire them manually in
# accounts/urls.py.
"""
from django.contrib.auth import views as auth_views
from accounts.forms import LoginForm

urlpatterns = [
    path("login/",
        auth_views.LoginView.as_view(
        template_name="accounts/login.html",
        form_class=LoginForm),
        name="login"),
        etc.
]"""

# 9. Email Backend (Development & Production)
# To enable password reset functionality, update your settings.py with
# appropriate email backend configuration (As demonstrated in the previous
# video):

"""
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY')

if DEBUG:
    # During development use console backend:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
"""

# 10. Update User Data in the Database
# To allow users to update their profile information, follow these steps:
# a. **Create a form** in `accounts/forms.py` named `CustomUserUpdateForm`.
# b. **Add a view** in `accounts/views.py` called `profile_update` to handle
# the form.
# c. **Register the view URL** in `accounts/urls.py`.
# d. **Create a template** at `accounts/profile_update.html` for the update
# form.
# e. **Add a navigation link** to `profile_update` in `base.html` so users can
# access it easily.
