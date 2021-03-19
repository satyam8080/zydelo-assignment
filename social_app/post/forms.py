from django import forms
from .models import Post


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post', 'user', 'post_image')
