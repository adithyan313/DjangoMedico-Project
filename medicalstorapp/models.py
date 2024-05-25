from django.db import models

class medicalstore(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)