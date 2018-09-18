from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(), label="Post heading")
    text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ('author', 'title', 'text',)
        # fields = '__all__'

class PostEditForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput())
    text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ('title', 'text',)

