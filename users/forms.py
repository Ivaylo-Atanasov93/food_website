from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.forms import ModelForm

from users.models import ProfileInformation


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileInformationForm(ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'form-control',
    }), validators=[])
    surname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Your surname',
        'class': 'form-control',
    }), validators=[])
    phone_number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={
        'placeholder': '07 123 456 789',
        'class': 'form-control',
    }), validators=[])
    gender = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Gender',
        'class': 'form-control',
    }), validators=[])
    date_of_birth = forms.DateField(widget=DateInput(attrs={
        'class': 'form-control',
        'placeholder': 'MM/DD/YYYY'
    }), validators=[])

    class Meta:
        model = ProfileInformation
        fields = ['name', 'surname', 'phone_number', 'gender', 'date_of_birth']
