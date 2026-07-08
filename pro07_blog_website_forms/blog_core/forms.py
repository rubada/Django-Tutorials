from django import forms
from .models import Blog


# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = Blog

#         # This tells Django which model fields to include in the form.
#         fields = ['title', 'first_name', 'last_name', 'content']

# What is the Meta class?
# The Meta class is a nested inner class inside your form that acts as a
# configuration container. It tells Django how to build the form by linking it
# to a model and customizing its behavior. Django reads this class internally
# when setting up the form.
# When you use "forms.ModelForm", Django needs to know which model to base the
# form on and which fields to include. The Meta class is the place where you
# provide that configuration. Without it, Django has no idea what to do and
# will throw an error.

# Why Inside a Nested Class?
# Django uses this pattern intentionally to separate configuration from logic.
# Think of it this way:

# The outer class (BlogPostForm) contains the form's behavior — custom
# validation, custom methods, etc.
# The inner Meta class contains the form's configuration — which model, which
# fields, which widgets, etc.

# This keeps things organized and clean.

# The Meta class is purely a "ModelForm" concept, it only exists because
# "ModelForm" needs to bridge the gap between your form and your model.

# Adding Widgets:
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog

        # This tells Django which model fields to include in the form.
        fields = ['title', 'first_name', 'last_name', 'content']

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter blog title...'}
            ),
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter your first name...'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter your last name...'}
            ),
            'content': forms.Textarea(attrs={'rows': 10}),
        }

# widgets = {...}
# Widgets control how each field is rendered as HTML. By default Django picks
# a widget for each field type as shown in the above example, but you can
# override them here by using a widgets.

# The widgets dictionary is only needed when you want to customize something
# about the default widget, like:

# Adding a placeholder
# Adding a CSS class
# Changing the number of rows in a textarea
# Or even completely changing the widget type

# In our example we added:
# 1. TextInput renders an <input type="text"> for title, first_name, and
# last_name
# 2.Textarea renders a <textarea> for content, with rows=10 to make it taller

# The attrs dictionary inside each widget maps directly to HTML attributes on
# the rendered element, so placeholder becomes a standard HTML placeholder on
# the input.
