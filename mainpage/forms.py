from django import forms

from .models import Posts

class post_form(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("post_name", "post_content")