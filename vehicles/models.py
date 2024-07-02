from django.db import models

from clients.models import Client

class Vehicle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    vin = models.CharField(max_length=17)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"