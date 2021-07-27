from django.db import models


# Create your models here.
class Todo(models.Model):
    _id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=10)
    month = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
