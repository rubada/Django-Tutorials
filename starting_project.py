# Starting a project in Django:

# 1. Create the main folder.

# 2. Create the vitual enviorment
# python -m venv .venv

# 3. Activate the venv
# In Windows:
# .venv/Scripts/activate

# In Linux and MAC:
# source .venv/bin/activate

# 4. Install Django in your venv:
# pip install Django

# 5. Create a new project.
# django-admin startproject project-name .

# 6. Make a new app.
# python manage.py startapp app-name

# Creating the app:
# 1. Add the app URL in the main "urls.py" in the project folder.
# 2. Add the app name to the "INSTALLED_APPS" in the settings.py file.
# 3. Create a "urls.py" file in your app
# 4. After creating the view, add its URL to the app "urls.py" file.

# Create templates:
# 1. Create the "templates" folder.
# 2. Add the "templates" folder path in the templates list in settings.py.

# Create apps folder or folders:
# 1. Create your apps’ main folder.
# 2. Create the app folder with the desired name "app-name".
# 3. Create your app by typing in the console:
# python manage.py startapp app-name apps-folder-name/app-name
# 4. In the "apps.py" file (which is in the app folder), add to the "name"
# variable the apps folder name, as follows:
# name = "apps-folder-name.app-name"
# 5. Add the app folder name to the app name in the INSTALLED_APPS list in the
# "settings.py" in the project folder, as follows:
# "apps-folder-name.app-name"
# 6. In the project "urls.py" file, add the apps’ main folder name as follows:
# urlpatterns = [
#     path("app2/", include("appsfolder.app2.urls")),
#     path("", include("appsfolder.app1.urls")),
#     path('admin/', admin.site.urls),
# ]

# Activating your models:
# 1. Create a migrations file with the "makemigrations" command. Migration
# files record any changes to the database models, which means you can track
# changes over time and debug errors. These files are stored in the "migration"
# folder in your app, by typying in your console:

# python manage.py makemigrations
# This will migrate all the apps model in your project,

# or you can migrate a specific app:
# python manage.py makemigrations posts

# 2. Build the database with the "migrate" command, which executes the
# migration files against your database, by creates tables, adds columns, etc.,
# and ensures your database structure matches your current models.
# Type in console:

# python manage.py migrate

# Note: when you change your models after executing the "makemigrations"
# command.

# Django Admin:
# Create a superuser:
# In your project folder, run:
# python manage.py createsuperuser

# Provide credentials when prompted
# Username: Choose a unique username.
# Email address: Enter a valid or placeholder email.
# Password: Must meet Django’s password validation rules (minimum 8 characters,
# not too common, not entirely numeric).

# If your password doesn’t meet criteria, Django will ask if you want to
# bypass validation (useful in test environments).

# To open your admin page:
# http://127.0.0.1:8000/admin/

# Or

# You can add a link in your template, for example:
# <a href="{% url 'admin:index' %}">Admin</a>

# Then log in by entering the username and password you just created.

# If you’d like to see the admin, forms, and other default messages in a
# language other than English, adjust the LANGUAGE_CODE in the
# "settings.py" file, which is automatically set to American English “en-us”.

# Optional: Register your app model:
# If you want to register your apps models and display them in the admin page,
# you do it in "admin.py" in your app folder.

# To show your model on your page, you should create a view.

# This is the power of Django ORM, you can store your data in the database by
# creating a model and then retrieving your data easily using your object and
# the QuerySet methods, instead of storing your data in a normal list,
# dictionaries, etc.


# You can check the "QuerySet API reference" in Django docs, which covers
# methods like
# .all(), .filter(), .exclude(), .get(), .order_by(), .values(), .count(),
# .exists(), .aggregate(), and more.
# Here is the link:
# https://docs.djangoproject.com/en/6.0/ref/models/querysets/
# and,
# "Making queries" explains how to use QuerySets in practice, with
# examples of creating, retrieving, updating, and deleting objects:
# https://docs.djangoproject.com/en/6.0/topics/db/queries/

# Note you can make queries, update, delete, etc. using the Django Python
# shell:
# python manage.py shell
