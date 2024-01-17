from django.db import models

# Create your models here.
class Phone(models.Model):
    name=models.CharField(max_length=500)
    image=models.CharField(max_length=3000)
    price=models.CharField(max_length=500)

class Computer(models.Model):
    name=models.CharField(max_length=500)
    image=models.CharField(max_length=3000)
    price=models.CharField(max_length=500)