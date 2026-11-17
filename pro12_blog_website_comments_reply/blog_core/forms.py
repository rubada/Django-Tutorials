from django import forms
from .models import Blog, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content"]

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter blog title...'}
            ),
            'content': forms.Textarea(attrs={'rows': 10}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
