# HTTP Methods:
# When your browser communicates with a server it uses HTTP methods to
# describe what it wants to do, these methods are:
# GET Retrieve/read data
# POST Send/submit data
# PUT Update data completely
# DELETE Delete data

# GET vs POST
# These are the two most common methods in Django:

# The GET method is used to request data by the browser from the server.
# e.g. browser request a page.

# The POST method is used to send data from the browser to the server.
# e.g. browser send blog data when creating a blog.

from django.shortcuts import render, redirect
from blog_core.forms import BlogPostForm


def blog_create(request):
    # POST request handles the submitted form by the user:
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', slug=blog.slug)
    # The GET request is handled here:
    else:
        form = BlogPostForm()           # GET request creates an empty form
    return render(request, 'blog_create.html', {'form': form})

# The flow is:
# User visits blogs/create/ → browser sends a GET request → Django returns the
# empty form
# User fills in the form and clicks submit → browser sends a POST request with
# the form data → Django saves it and redirects to another page in our example
# blog_detail

# GET here creates an empty form and sends it to the template for the user to
# fill in.

# POST is the secure way to send data from the browser to the server, which is
# why it's used for all form submissions in Django.


# In CBV Django handles POST and GET automatically behind the scenes.
# So instead of checking if request.method == 'POST' like in FBV, CBV routes
# the request to the correct method automatically.
