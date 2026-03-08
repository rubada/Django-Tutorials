from django.shortcuts import render


# The "render" function in Django is a shortcut that combines a template with
# a context dictionary and returns an object.

# The "render()" function is part of the django.shortcuts module. It
# simplifies the process of returning HTML content in response to a request by:
# - The "request" argument is required (in function based views) and
# represents the incoming HTTP request. It contains information about the
# user's request.
# - Loading a template (e.g., homepage.html), Django will look for this
# template in your project's templates directory.
# - The "context" is a dictionary containing key-value pairs. These pairs
# provide data that can be inserted into the html template.
# - Returning an HttpResponse with the rendered HTML.
def home_page_view(request):
    return render(request, "homepage.html")


def about_page_view(request):
    page_context = {
        "name": "Ruba Dabbas",
        "about_page": "we will learn about Django",
    }
    return render(
        request,
        "about.html",
        context=page_context
    )
