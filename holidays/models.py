from django.db import models
from django.contrib.auth.models import User


class Holiday(models.Model):
    country = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name


class UserProfile(User):
    country = models.CharField(max_length=20, default="Belarus")