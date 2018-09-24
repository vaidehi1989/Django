from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(), label='Comment')

    class Meta:
        model = Comment
        fields = ('text',)
