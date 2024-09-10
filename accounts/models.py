from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True) 
    name = models.CharField(max_length=100) 
    nickname = models.CharField(max_length=100) 
    birthday = models.DateField()