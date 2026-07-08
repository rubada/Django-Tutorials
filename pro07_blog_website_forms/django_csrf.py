# What {% csrf_token %} Does?
# The {% csrf_token %} tag in your templates generates a hidden input field
# with a secret token.
# In html template:
# <input type="hidden" name="csrfmiddlewaretoken" value="someRandomToken">
# When the form is submitted, Django checks that this token matches. If it
# doesn't, Django rejects the request.
# This protects against Cross Site Request Forgery (CSRF) attacks.

# Django includes this middleware by default in the settings.py
# MIDDLEWARE = [
#     ...
#     'django.middleware.csrf.CsrfViewMiddleware',  # Handles CSRF globally
#     ...
# ]

# Django provides two decorators for special cases:
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_exempt  # Disables CSRF protection for this view (e.g. for APIs)
def my_api_view(request):
    pass


@csrf_protect  # Enforces CSRF on a specific view if you disabled it globally
def my_view(request):
    pass

# These are only needed when you want to override the global middleware
# behavior for a specific view.
