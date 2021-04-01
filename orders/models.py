from django.db import models

from prices.models import BaseMealPrice, DeliveryPrice
from users.models import User
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
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    meal_size = models.IntegerField(choices=MEAL_SIZES, default=2)
    number_of_meals = models.IntegerField(choices=NUMBER_OF_MEALS, default=5)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete_value = models.BooleanField(default=False, blank=False, null=True)
    transaction_id = models.CharField(max_length=255, null=True)

    @property
    def get_box_base_price(self):
        number_of_meals = self.number_of_meals
        meal_size = self.meal_size
        multiplier = number_of_meals * meal_size
        meal_price = BaseMealPrice.objects.all()[0].price
        base_box_price = meal_price * multiplier
        return base_box_price

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


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_shipping = models.BooleanField(default=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)

    @property
    def get_total_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    @property
    def get_total_price(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    @property
    def shipping(self):
        return self.is_shipping

    def __str__(self):
        return str(self.transaction_id)


class OrderItem(models.Model):
    product = models.ForeignKey(Box, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = (self.product.get_box_base_price * self.quantity) + DeliveryPrice.objects.all()[0].price
        return total


class DeliveryInformation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    day_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
