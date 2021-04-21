import datetime

from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()

    def __repr__(self):
        return self.email


class ProfileInformation(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, default='Empty')
    surname = models.CharField(max_length=255, blank=True, null=True, default='Empty')
    phone_number = models.CharField(max_length=255, blank=True, null=True, default='Empty')
    email = models.EmailField(default='Empty')
    gender = models.CharField(max_length=255, default='Empty')
    date_of_birth = models.DateField(default=datetime.date.today)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.email
