from django.shortcuts import render

from django.http import HttpResponse

# Views are Python functions or classes that accept web requests and return
# responses.
# There are two main types:
# 1. Function-based views (FBVs)
# 2. Class-based views (CBVs).

# Creating our first response using HttpResponse class:
# HttpResponse is a class used to return an HTTP response from a view.
# It’s part of the django.http module and represents the content that will be
# sent back to the user's browser when they access a URL.
# - It wraps the response content (HTML, JSON, plain text, etc.)
# - Sets the HTTP status code (default is 200 OK) you can add any HTTP status
# code such as: 400, 404, 500.
# Check below link for HTTP status code:
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# - Allows setting headers (like content type, cookies, etc.)

# As for the "render" function, we will discuss it later.


def home(request):
    return HttpResponse("Django is Great")
