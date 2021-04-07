from django import forms
from django.forms import ModelForm

from .models import Box


class BoxForm(ModelForm):
    class Meta:
        model = Box
        meal_size_choices = Box.MEAL_SIZES
        number_of_meals_choices = Box.NUMBER_OF_MEALS
        fields = [
            'meal_size',
            'number_of_meals',
        ]
        widgets = {
            'meal_size': forms.Select(choices=meal_size_choices, attrs={'class': 'form-control'}),
            'number_of_meals': forms.Select(choices=number_of_meals_choices, attrs={'class': 'form-control'})
        }