from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    total = models.FloatField(null=True)
    quantity = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.product} | {self.date}"