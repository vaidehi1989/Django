from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Post
        fields = ('title', 'text',)


class EditPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = Comment
        fields = ('comment',)
