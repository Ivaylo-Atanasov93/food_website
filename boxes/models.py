from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse

from prices.models import BaseMealPrice
from recipes.models import Recipe


class Box(models.Model):
    MEAL_SIZES = [
        (2, 'Meal for 2'),
        (3, 'Meal for 3'),
        (4, 'Meal for 4'),
        (5, 'Meal for 5'),
    ]
    NUMBER_OF_MEALS = [
        (2, '2 day program'),
        (3, '3 day program'),
        (4, '4 day program'),
        (5, '5 day program'),
    ]
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    meal_size = models.IntegerField(choices=MEAL_SIZES, default=2)
    number_of_meals = models.IntegerField(choices=NUMBER_OF_MEALS, default=5)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete_value = models.BooleanField(default=False, blank=False, null=True)
    transaction_id = models.CharField(max_length=255, null=True)

    def get_absolute_url(self):
        return reverse('box_details', kwargs={'id': self.id})

    @property
    def get_box_base_price(self):
        number_of_meals = self.number_of_meals
        meal_size = self.meal_size
        multiplier = number_of_meals * meal_size
        meal_price = BaseMealPrice.objects.all()[0].price
        base_box_price = meal_price * multiplier
        return base_box_price

    @property
    def get_meals_number(self):
        return self.number_of_meals

    def __str__(self):
        return f'{self.number_of_meals} days box'


class ChoseMeals(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_additional_cost(self):
        meals = self.recipe.objects.all()
        additional_cost = sum(meal.additional_cost for meal in meals)
        return additional_cost

    def __str__(self):
        return f'{self.box}'
