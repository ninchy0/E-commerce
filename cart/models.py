from django.db import models
from home.models import *

# Create your models here.
class Cart(models.Model):
    username = models.CharField(max_length=500)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    slug = models.CharField(max_length=300)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField()
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=400)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name