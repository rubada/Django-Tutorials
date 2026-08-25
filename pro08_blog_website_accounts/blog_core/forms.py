from django import forms
from .models import Blog


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
