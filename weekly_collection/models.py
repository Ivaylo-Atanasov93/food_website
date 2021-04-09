from django.db import models
import schedule
from datetime import date

# Create your models here.
from recipes.models import Recipe


class WeeklyCollection(models.Model):
    week_start = models.DateField()
    week_end = models.DateField()
    active = models.BooleanField(default=False, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)


class AddRecipe(models.Model):
    week = models.ForeignKey(WeeklyCollection, on_delete=models.CASCADE, blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
