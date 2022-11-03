from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=50)
    calories = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ate {self.calories}"

class Progress (models.Model):
    improvement = models.CharField(max_length=200)
    user = models.ForeignKey('User', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f"{self.name}"





