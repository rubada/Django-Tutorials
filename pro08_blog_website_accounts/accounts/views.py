from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()          # creates the User in the database
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


# - form.cleaned_data is a dictionary that Django populates after the form has
# been validated.
# It only exists after you call form.is_valid(), after validates each field,
# that means checks required fields are filled, email looks like an email,
# passwords match, etc., then it cleans the data, that means converts raw
# string input from the browser into proper Python types and stores the result
# in form.cleaned_data, in our case the "username" and "password".
# If you try to access form.cleaned_data before calling is_valid(), it won't
# exist and you'll get an AttributeError.

# Example:
# raw request.POST — everything is a plain string
# request.POST = {
#     "username": "  ruba  ",
#     "password": "secret123",
# }

# after form.is_valid(), cleaned_data has proper values
# form.cleaned_data = {
#     "username": "ruba",        # whitespace stripped
#     "password": "secret123",
# }

# Then the cleaned values is passed to authenticate()

# - authenticate() checks the credentials (the username and password) against
# the database, it returns the User object if valid, or None if not. Nothing
# is saved anywhere.

# - login() creates the session — without calling it, the user won't actually
# be logged in even if credentials are correct.
# Calling the login() will create one row in the django_session table in the
# database that has three columns:
# session_key  — a long random string Django generates, which is sent to the
# browser as a cookie, so Django remembers this user on every future request.
# session_data — a dictionary containing _auth_user_id which is the logged in
# user's primary key from the User table. This is how Django knows who is
# logged in.
# expire_date  — when the session expires. By default Django sets this to
# 2 weeks, that means Django keeps you logged in for 2 weeks without needing
# to enter your username and password again.

# Django writes to the same django_session table also when you login to the
# admin page.

# Summary:
# authenticate() and login() do two different jobs.

# user = authenticate(request, username=username, password=password)
# at this point Django knows WHO the user is, but the browser doesn't know yet

# if user is not None:
#     login(request, user)
# NOW the browser knows the user is logged in

# - form.add_error(None, "...") attaches the error to the form as a non-field
# error — None means it's not tied to any specific field, just show a general
# error on the form when no user is found.


def logout_view(request):
    logout(request)
    return redirect("login")
