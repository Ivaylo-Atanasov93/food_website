from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


# class ProfileInformation(models.Model):
#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255, blank=True, null=True)
#     phone_number = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField()
#     gender = models.CharField(max_length=255)
