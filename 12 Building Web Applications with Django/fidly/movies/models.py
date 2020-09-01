from django.db import models
from django.utils import timezone


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    relase_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
