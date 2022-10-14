from django.forms import PasswordInput
from .models import *
from django.contrib.auth import get_user_model
from django import forms


class UserForm(forms.ModelForm):
    username = forms.CharField
    password = forms.PasswordInput
    password2 = forms.PasswordInput