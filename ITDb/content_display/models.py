from django.db import models

# Create your models here.

class Cities(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField(max_length=150)
    videos = models.CharField(max_length=200)
    coords = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    altitude = models.CharField(max_length= 30)
    climate = models.CharField(max_length= 20)
    population = models.CharField(max_length=20)
    time_zone = models.CharField(max_length= 20)
    languages = models.TextField()

class Activities(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField(max_length=150)
    videos = models.CharField(max_length=200)
    coords = models.CharField(max_length=20)
    type_activity = models.CharField(max_length=50)
    city_id = models.IntegerField()



class Languages(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField(max_length=150)
    script = models.CharField(max_length=30)
    spoken_in = models.IntegerField()