from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=50,unique=True,blank=True,null=True)
    email = models.EmailField(unique=True,blank=True,null=True)
    phone_number = PhoneNumberField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()








