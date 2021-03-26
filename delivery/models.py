from django.db import models

# Create your models here.
# from orders.models import Box
from users.models import Customer


class DeliveryPrice(models.Model):
    price = models.FloatField()

    def __str__(self):
        return str(self.price)


class DeliveryInformation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    # order = models.ForeignKey(Box, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    day_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
