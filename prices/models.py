from django.db import models


# Create your models here.
class BaseMealPrice(models.Model):
    price = models.FloatField()

    def __str__(self):
        return str(self.price)


class DeliveryPrice(models.Model):
    price = models.FloatField()

    def __str__(self):
        return f'Delivery price'
