from django.db import models


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

    meal_size = models.IntegerField(choices=MEAL_SIZES, default=2)
    number_of_meals = models.IntegerField(choices=NUMBER_OF_MEALS, default=2)


    def __str__(self):
        return str(self.number_of_meals)

