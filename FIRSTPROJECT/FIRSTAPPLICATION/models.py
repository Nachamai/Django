from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=15)
    ID = models.CharField(max_length=10, default=0)
    contact = models.IntegerField()
    Address = models.TextField()

