from django.db import models


# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='ingredient_images', null=True, blank=True)
    allergen = models.CharField(max_length=255)

    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url

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
    name = models.CharField(max_length=255)
    main_ingredients = models.CharField(max_length=300)
    meal_picture = models.ImageField(upload_to='recipes_images', null=True, blank=True)
    additional_cost = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    origin = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPE)
    description = models.TextField(max_length=600)
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY)

    @property
    def imageURL(self):
        try:
            url = self.meal_picture.url
            print(url)
        except:
            url = '/images/img_placeholder.png'
        return url

    def __str__(self):
        return self.name


class AddIngredient(models.Model):
    INGREDIENTS = [(ingredient.name, ingredient.name) for ingredient in Ingredient.objects.all()]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=255, choices=INGREDIENTS)
    quantity = models.IntegerField()


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='steps_images', null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
