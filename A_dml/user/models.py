from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    
    avatar = models.ImageField(null=True, default='avatar.svg')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return str(self.username)