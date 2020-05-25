from django import forms

from .models import Tred
from .models import Comment


class post_form(forms.ModelForm):
    class Meta:
        model = Tred
        fields = ("tred_name", "tred_content")

class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_content",)