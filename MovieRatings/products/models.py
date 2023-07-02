from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    ratings = models.FloatField(default=-1.0)

class MovieInfo(models.Model):
    identifier = models.PositiveIntegerField()
    totalratings = models.FloatField(default=0) 
    totalusers = models.PositiveIntegerField(default=0)
