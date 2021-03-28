from django.db import models

# Create your models here.
from users.models import Customer


class DeliveryPrice(models.Model):
    price = models.FloatField()

    def __str__(self):
        return f'Delivery price'

