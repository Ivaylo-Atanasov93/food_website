from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    picture = models.CharField(max_length=200)
    allergen = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    DIFFICULTY = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    TYPE = [
        ('M&V', 'Meat and Veggie'),
        ('VRN', 'Vegetarian'),
        ('VGN', 'Vegan'),
    ]
    name = models.CharField(max_length=200)
    main_ingredients = models.CharField(max_length=300)
    meal_picture = models.CharField(max_length=200)
    base_price = models.DecimalField(max_digits=3, decimal_places=2)
    additional_cost = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    origin = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=TYPE)
    description = models.TextField(max_length=600)
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY)

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):
    INGREDIENTS = [(str(ingredient.id), ingredient.name) for ingredient in Ingredient.objects.all()]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=10, choices=INGREDIENTS)
    quantity = models.IntegerField()


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=200)
