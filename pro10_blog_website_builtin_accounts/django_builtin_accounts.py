# Django's built-in authentication system "django.contrib.auth":
# This is is one of the framework's best "batteries included" features. Out of
# the box, it handles everything from user sessions and password hashing to
# permissions and ready-to-use auth views.

# As mentioned before when creating a new Django project, "django.contrib.auth"
# is already installed and configured in your settings.py.
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',      # ← this is the auth app
    'django.contrib.contenttypes',
    ...
]
"""

# You will get the following:
# 1. The "User": Handles standard user fields like
# username, email, first_name, last_name, and password.

# 2. Permissions & Groups: Binary permission flags (add, change, delete, view)
# automatically generated for every model you create, plus group management.

# 3. Security: Built-in secure password hashing so raw passwords are never
# saved.

# 4. Built-in Auth Views: Pre-written views for login, logout, password change,
# and password reset flows.


# Using Django’s Built-in Authentication (django.contrib.auth):

# 1. Wire Up the Authentication URLs
# Instead of manually writing login/logout routes, you can include Django’s
# preconfigured URL set directly in your project’s urls.py:
"""
urlpatterns = [
    ...
    path('accounts/', include('django.contrib.auth.urls')),
]
"""

# That single line automatically provides the following routes:
# accounts/login/
# accounts/logout/
# accounts/password_change/
# accounts/password_change/done/
# accounts/password_reset/
# accounts/password_reset/done/
# accounts/reset/<uidb64>/<token>/
# accounts/reset/done/

# Each route maps to a ready-to-use class-based view (e.g., LoginView,
# LogoutView, PasswordChangeView, etc.).
# No need to touch views.py — Django handles the logic for you.

# 2. Supplying Templates for Built-in Auth Views
# Django’s built-in authentication views don’t render generic HTML.
# They expect templates at conventional paths under a registration/ directory:

# templates/
# └── registration/
#     ├── login.html
#     ├── password_change_form.html
#     ├── password_change_done.html
#     ├── password_reset_form.html
#     ├── password_reset_done.html
#     ├── password_reset_confirm.html
#     └── password_reset_complete.html

# Default vs. Custom Paths
# The registration/ folder is conventional, not mandatory.

# If you use include('django.contrib.auth.urls'), Django will look under
# registration/ by default.

# If you prefer a different folder (e.g., accounts/), you must declare each
# URL explicitly and pass a template_name.

# In the accounts/urls.py
"""
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logged_out.html'
    ), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html'
    ), name='password_reset'),
    # etc.
]
"""

# 3. Point Django to Your Login and Logout Redirects
# After a user signs in or out, Django needs to know where to send them next.
# You configure this in your project’s settings.py:
"""
LOGIN_REDIRECT_URL = 'home'   # where to go after successful login
LOGOUT_REDIRECT_URL = 'home'  # where to go after logout
"""

# 4. Registration Stays Custom
# Django provides built‑in views for login, logout, and password management,
# but there is no built‑in signup view.
# That means your existing custom registration flow (the one you already built)
# is the correct approach.

# In your setup, views.py only defines the register view, and accounts/urls.py
# only maps the register route.

# 5. Using Custom Forms with Built-in Auth Views
# By default, Django’s built-in authentication views (e.g., LoginView,
# PasswordResetView) use their default forms.
# If you want to use your own custom forms, you need to wire them manually in
# accounts/urls.py.
"""
from django.contrib.auth import views as auth_views
from accounts.forms import LoginForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        form_class=LoginForm
    ), name='login'),
]
"""

# 6. Updating Logout in base.html:
# By default, Django’s LogoutView only accepts POST requests for security
# reasons (to prevent accidental or malicious logouts via a simple link click).
# That means you need to replace your logout link with a form.

# Before:
"""
<a href="{% url 'logout' %}" class="btn-logout">Logout</a>
"""
# After:
"""
<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button class="btn-logout" type="submit">Logout</button>
</form>
"""

# 7. Create the Required Templates
# Django’s built‑in authentication views expect specific templates. Here’s
# what each one does:

# a. login.html
# Standard login page. Context includes a form (usually AuthenticationForm).

# b. password_change_form.html
# For logged‑in users changing their password voluntarily.
# Context: form (instance of PasswordChangeForm).

# c. password_change_done.html
# Confirmation page shown after a successful password change.
# No special context variables.

# d. password_reset_form.html
# “Forgot password?” page where users enter their email.
# Context: form (instance of PasswordResetForm, single email field).

# e. password_reset_done.html
# Shown immediately after submitting the email.
# Appears regardless of whether the email exists in the database.
# No context variables needed.

# f. password_reset_confirm.html
# Page reached via the reset link in the email.
# Context: form (new password form) and validlink (boolean indicating if the
# token is valid).

# g. password_reset_complete.html
# Final confirmation page after the new password is saved.
# No special context variables.
