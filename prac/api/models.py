from django.db import models

# Create your models here.

class Stu(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)