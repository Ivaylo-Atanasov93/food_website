from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.forms import ModelForm

from users.models import ProfileInformation


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileInformationForm(ModelForm):
    class Meta:
        model = ProfileInformation
        fields = ['name', 'surname', 'phone_number', 'email', 'gender', 'date_of_birth']
