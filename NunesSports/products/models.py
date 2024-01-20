# products/models.py
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    cod = models.IntegerField(default=0)
    description = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name