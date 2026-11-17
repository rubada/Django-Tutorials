# How to Add Comments and Replies:

# Now, let’s walk through the steps required to implement a **Comments and
# Replies** feature in Django:

# 1. Where to place them?
# - Since comments only exist on blogs, you can add their model, form, views,
# and URLs directly in the `blog_core` app.
# - Alternatively, create a dedicated `comments` app. This follows Django’s
# “one app, one job” principle and makes comments reusable across other models
# in the future.

# In our Blogs project, we will define the `Comment` model inside
# `blog_core/models.py`.

# 2. Create the Comment model:
# A comment model in Django is a database structure that allows users to leave
# feedback or discussions on specific content, such as blog posts, articles,
# or products. It defines how comments are stored, linked, and managed.

# Don't forget to run
# python manage.py makemigrations
# python manage.py migrate
# After creating the model.

# 3. Build the CommentForm:
# In forms.py, create a Form with Meta.model = Comment and
# fields = ['content'] only.
# We intentionally exclude post, author, and parent because these are set in
# the view.
# This prevents users from tampering with them and ensures those values are
# controlled by the application logic.
# e.g., assign their comment to someone else’s post, impersonate another
# author, or attach replies to the wrong parent.

# 4. Writing Comment Views:
# In Django, views define the logic for creating, displaying, and managing
# comments. A complete workflow typically includes:
# - **Add Comment View**
#   Handles form submission and attaches a new comment to the related post.
# - **Edit/Delete Views**
#   Provide functionality for updating or removing existing comments, ensuring
#   proper permissions (e.g., only the author or an admin can edit/delete).
# - **URL Configuration**
#   Map each view to a URL pattern so users can access comment actions
#   directly from the application.

# Add the views and URls in blog_core/views.py and urls.py.

# 5. Update the `blog_detail` and `blog_user_detail` Views
# Enhance these views to display the blog post together with all its
# associated comments.
# This ensures that when a user opens a blog detail page—whether their own
# post or another user’s—the full discussion thread (comments and replies) is
# visible alongside the blog content.

# 6. The templates required
# Step 1: Create the comment.html
# Create the file templates/blog_core/comment.html
# Step 2: Create edit_comment.html
# Create the file templates/blog_core/edit_comment.html
# Step 3: Add the comments to blog_detail.html
# Step 4: Add the comments to user_blog_detail.html

# 7. Display replies using recursive include in the comment.html
'''
    {% if comment.replies.exists %}
      {% include "blog_core/comment.html" with comments=comment.replies.all %}
    {% endif %}
'''
# comment.replies.exists → checks if the current comment has any replies.
# {% include "blog_core/comment.html" ... %} → reuses the same template
# (comment.html) to render replies.
# with comments=comment.replies.all → passes the replies queryset into the
# included template as the comments variable.
# Since the template includes itself (is recursive), each reply will render
# its own nested replies.
# The post (blog) variable is automatically passed through, so you don’t need
# to supply it again.
# because it’s already in the parent context from the blog_detail or
# user_blog_detail views.
