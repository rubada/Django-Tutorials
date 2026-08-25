# Accounts:
# As mentioned before Django comes with a built-in user system out of the box.
# You don't need to design a "users" database table, hash passwords manually,
# or build session logic — it's all already there.
# It lives in django.contrib.auth, and it's automatically included in every
# Django project.
# In the settings.py:
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',      # ← this is the auth app
    'django.contrib.contenttypes',
    ...
]
'''
# The moment you run python manage.py migrate on a new project, Django creates
# the auth_user table in your database automatically. No extra setup needed.

# The built-in User model comes with these fields ready to use:
# username, password (stored hashed, never plain text)
# email, first_name, last_name
# is_active, is_staff, is_superuser
# date_joined, last_login

# As mentioned before all the above can be displayed in the Admin page.

# Django handles the user model for us. Now we need to build the front-facing
# side — the forms, the pages, the views — so our blog visitors can actually
# sign up and log in. That's exactly what we'll build next.

# How to create accounts?

# Step 1 — Create the accounts app
# python manage.py startapp accounts
# In the settings.py register it in INSTALLED_APPS

# Step 2 — The form
# Django's built-in UserCreationForm handles username, password, and password
# confirmation out of the box.

# Step 3 — The view
# In accounts/views.py, handle both GET (show the empty form)
# and POST (save the new user)

# Step 4 — The URL
# In accounts/urls.py add the views urls
# Include the app urls in blogs/urls.py (the project folder).

# Step 5 — The templates
# Create the register.html and login.html
