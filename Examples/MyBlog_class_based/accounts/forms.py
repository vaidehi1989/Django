from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    # Fileds from auth.User model
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())

    gender = forms.ChoiceField(choices=(('male', 'Male'),('female', 'Female')), widget=forms.RadioSelect())
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'dob', 'gender','email', 'username', 'password1', 'password2',)
        help_texts = {
            'username': None,
        }
