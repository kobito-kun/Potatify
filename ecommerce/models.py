from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    total = models.FloatField(null=True)
    name = models.CharField(null=True, max_length=256)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.date}"