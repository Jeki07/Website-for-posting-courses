from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, FileInput, Textarea

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Электронный Адрес')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    