from django.views.generic import ListView

from .models import Posts

# ListView class is a generic class-based view. It’s designed to display a
# list of objects from a database model without requiring you to write
# repetitive boilerplate code.
# That means if you wrote a FBV to list objects, you’d need to:
# - Query the database (MyModel.objects.all())
# - Write logic to handle context naming, Pagination support, etc.

# With ListView, Django handles most of this automatically:

# - Model-driven: You specify a model, and it automatically queries all
# objects from that model.

# - Context variable: By default, the list of objects is available in the
# template as "object_list". You can override this with "context_object_name"
# attribute.
# "object_list" is the default context variable that a "ListView" provides to
# your template, it is passed into the template as "object_list".
# By default, ListView queries all objects of the model you specify
# (e.g., Posts.objects.all()).

# - Template naming convention: If you don’t specify a template, Django looks
# for <app>/<model>_list.html.

# - Pagination support: Built-in support for paginating large datasets.
# It means you can automatically split a long list of objects into multiple
# pages, instead of dumping everything into one giant list.

# - Custom querysets: You can override "get_queryset()" method" to filter or
# customize the data that gets passed into "object_list".
# You can use any queryset methods that read or refine data with
# "get_queryset()", but you should avoid using the following methods:
# - .delete() → removes rows.
# - .update() → modifies rows (should be done in UpdateView or a custom POST
# handler (that handles post requests)).
# - .create() → inserts new rows (belongs in CreateView or a form handler).
# Using these methods with "get_queryset()" will modify the database every time
# someone loads the page — which is not what you want.


class PostsView(ListView):

    # Use the "nodel" attribute to define the model:
    model = Posts
    # template_name = "posts/posts_display.html"
    # context_object_name = "emp_data"
    # paginate_by = 2  # show 2 messages per page
