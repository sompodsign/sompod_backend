from django.db import models


# Create your models here.
class Todo(models.Model):
    _id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    date = models.IntegerField(max_length=10)
    month = models.IntegerField(max_length=10)
    year = models.IntegerField(max_length=10)

    def __str__(self):
        return self.title
