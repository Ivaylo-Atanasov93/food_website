from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
# class UserManager(BaseUserManager):
#     def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
#         if not email:
#             raise ValueError("You must enter an email address.")
#         if not password:
#             raise ValueError("You must enter a password.")
#         if not full_name:
#             raise ValueError("User must have a full name.")
#         user = self.model(
#             email=self.normalize_email(email),
#             full_name=full_name,
#         )
#         user.set_password(password)
#         user.active = is_active
#         user.staff = is_staff
#         user.admin = is_admin
#         user.save(using=self._db)
#         return user
#
#     def create_staff_user(self, email, full_name, password):
#         user = self.create_user(email, full_name=full_name, password=password, is_staff=True)
#         return user
#
#     def create_superuser(self, email, full_name, password):
#         user = self.create_user(email, full_name=full_name, password=password, is_staff=True, is_admin=True)
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)
#     admin = models.BooleanField(default=False)
#     time_stamp = models.DateTimeField(auto_now_add=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['full_name']
#
#     def get_email_name(self):
#         return self.email
#
#     def get_full_name(self):
#         return self.full_name
#
#     def get_short_name(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#
#     @property
#     def is_staff(self):
#         return self.staff
#
#     @property
#     def is_admin(self):
#         return self.admin
#
#     @property
#     def is_active(self):
#         return self.active
#
#     def __str__(self):
#         return self.email
#
#     objects = UserManager()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name
