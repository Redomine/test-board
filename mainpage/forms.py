from django import forms

from .models import Post
from .models import Comment


class post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("post_name", "post_content")

class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_content",)