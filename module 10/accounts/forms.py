from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }), label='Confirm Password')
    dob = forms.DateField(widget=forms.DateInput(format="%dd/%mm/%YYYY"), label='Date of Birth')
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'dob', 'username', 'email', 'password1', 'password2',)
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
