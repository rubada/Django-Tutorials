# "get_absolute_url()" Method:
# Currently, we are using this URL pattern in our template "blog.html":
# <a href="{% url 'blog_detail' post.id %}">{{ post.title }}</a>
# in our blog template, which is used to display a blog post in this template
# or any other template.

# But what if this URL pattern changes (you changed the URL name), then you
# need to update every template where the URL name is used, and this will
# increase the risk of errors.

# A better approach is to use the built-in "get_absolute_url()" method in
# your model, and then the URL pattern used in the template is:
# <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>

# which tells Django to return the canonical (official) URL for a
# single instance, what does this means?


# The "get_absolute_url()" method can return blog URL for a single post or blog
# (insrance or object), either by:
# 1. Using the pk, which is not recommended, because it is not a SEO-friendly:

'''def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})'''

# returns → '/blog/5/'


# 2. Using a slug instead of pk in URLs because it is readable and
# SEO-friendly than the pk.

'''def get_absolute_url(self):
    return reverse('post-detail', kwargs={'slug': self.slug})'''

# returns → '/blog/my-first-blog-post/'


# Common Patterns:

# 1. Using pk:
# URL pattern: /blog/<pk>/
'''def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})'''

# 2.Using a single kwargs:
# URL pattern: /blog/<slug>/
'''def get_absolute_url(self):
    return reverse('post-detail', kwargs={'slug': self.slug})'''

# 3.Using multiple kwargs:
# URL pattern: /blog/<year>/<slug>/
'''def get_absolute_url(self):
    return reverse('post-detail', kwargs={
        'year': self.created_at.year,
        'slug': self.slug,
    })'''

# 3. Also you can use args instead of kwargs:
# URL pattern: /blog/<slug>/
'''def get_absolute_url(self):
    return reverse('post-detail', args=[self.slug])'''
