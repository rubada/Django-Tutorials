# Bind views to the authenticated user on login:
# This is done by using @login_required decorator, which is a view decorator
# that ensures only authenticated users can access a particular view.

# For example we can use it to filter posts by the logged in user in the view:
'''
from django.contrib.auth.decorators import login_required

@login_required
def blogs_list(request):
    posts = Post.objects.filter(author=request.user)  # only this user's posts
    return render(request, "blog/blogs_list.html", {"posts": posts})
'''

# filter(author=request.user): only fetches posts where author_id matches the
# logged in user's id

# This ensure that views accessing a user’s data are secured with
# @login_required.

# To redirect unauthenticated users to other URLs, in settings.py add:
# LOGIN_URL = "login"
# Then Django will redirect them to the URL pattern named "login".

# Without this, Django redirects to /accounts/login/ by default which may not
# match your URL (if a differnt route is defined) — this tells it to use
# your named login URL instead.


# 👥 Managing Authenticated and Open Pages

# 1. Two sets of views & templates:
# Private → Logged-in users can see, such as pages with their own blogs (with
# edit/delete access), and create blog page.
# Public → Everyone can see all posts (no login required).

# 2. Navigation links for authenticated users in templates
# In base.html:
'''
{% if request.user.is_authenticated %}
    <li><a href="{% url 'blogs_user_list' %}">My Blogs</a></li>
    <li><a href="{% url 'blog_create' %}">Create Blog</a></li>
{% endif %}
'''

# 3. Conditional edit/delete actions
# In blog_detail.html:
'''
{% if request.user == blog.author %}
    <div class="blog-actions">
        <a href="{% url 'blog_update' blog.slug %}">Edit</a>
        <a href="{% url 'blog_delete' blog.slug %}">Delete</a>
    </div>
{% endif %}
'''

# 4. Model & form adjustments
# a. Remove first_name and last_name from:
#   - BlogPostForm
#   - Blog model
#   - BlogAdmin (admin.py)

# b. Add author field to the Blog model:

'''
from django.contrib.auth.models import User

author = models.ForeignKey(User, on_delete=models.CASCADE)
'''
# 👉 Django automatically assigns the logged-in user as the author.

# c. Update the __str__ method to:
'''
    def __str__(self):
        return f"{self.title} by {self.author.first_name}\
{self.author.last_name}"
'''

# c. (Optional) Add a created_at field to the Blog model:

'''
created_at = models.DateTimeField(auto_now_add=True)
'''

# 5. Migrations after model updating:
'''
python manage.py makemigrations
python manage.py migrate
'''

# 6. Template updates (blog.html, blog_detail, user_blogs.html)
# Show author details:
'''
{{ blog.author.first_name }} {{ blog.author.last_name }}
'''
# Show created date:
'''
{{ blog.created_at }}
'''

# 7. Registration form
# In accounts/forms.py, extend RegisterForm to include first_name and
# last_name, so they appear in register.html.
