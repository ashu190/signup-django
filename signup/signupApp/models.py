from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)