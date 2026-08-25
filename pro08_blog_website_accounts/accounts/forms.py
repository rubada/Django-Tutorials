from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Why is the email field explicitly defined in RegisterForm when the User
# model already includes it?

# The User model does already have an email field — but it's optional by
# default!:
'''email = models.EmailField(blank=True)'''

# blank=True means email is not required. So if you just put "email" in fields
# list without redeclaring it in the "RegisterForm", the email field would
# show up in the form, but it would be optional — the user could skip it and
# submit the form with a blank email.

# By explicitly redeclaring it:
'''email = forms.EmailField(required=True)'''
# You are overriding the model's loose definition with a stricter form-level
# rule that forces the user to fill it in, because the required parameter is
# True by default.


# Django uses password1 and password2 because UserCreationForm requires the
# user to type their password twice:
# password1 — the password the user chooses
# password2 — "confirm password"

# When you call form.is_valid(), Django automatically checks that both fields
# match. If they don't, it adds a validation error and the form won't save.


class LoginForm(forms.Form):       # plain Form, not ModelForm
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
