from django.db import models

from delivery.models import DeliveryPrice
from users.models import Customer
from recipes.models import Recipe


# Create your models here.

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
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    delivery_price = models.ForeignKey(DeliveryPrice, on_delete=models.SET_NULL, blank=True, null=True)
    meal_size = models.IntegerField(choices=MEAL_SIZES, default=2)
    number_of_meals = models.IntegerField(choices=NUMBER_OF_MEALS, default=5)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete_value = models.BooleanField(default=False, blank=False, null=True)
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.number_of_meals} days box'


class ChoseMeals(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, blank=True, null=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.box} days box'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Box, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    # @property
    # def get_total_price(self):
    #     number_of_meals = self.order.number_of_meals
    #     meal_size = self.order.meal_size
    #     base_box_price = Recipe.base_price.price * (number_of_meals * meal_size)
    #     additional_cost = 0
    #     additional_cost += [meal for meal in self.chosen_meals]
    #     delivery = self.order.delivery_price
    #     final_price = base_box_price + additional_cost + delivery.price
    #     print(additional_cost)
    #     return final_price
