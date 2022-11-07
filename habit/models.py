from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    pass

class Habit(models.Model):
    name = models.CharField(max_length=50)
    metric = models.PositiveIntegerField(null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="habits", blank=True, null=True)
    unit_of_measure = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.metric} {self.unit_of_measure}"

class Record (models.Model):
    habitrecord = models.ForeignKey('Habit', on_delete=models.CASCADE, related_name="records", blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    amount = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Daily entry for {self.habit.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['habitrecord', 'date'], name='record')
    ]








