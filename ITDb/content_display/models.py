from django.db import models

# Create your models here.

class Cities(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField()
    videos = models.CharField()
    coords = models.CharField()
    size = models.IntegerField()
    altitude = models.CharField()
    climate = models.CharField()
    population = models.CharField()
    time_zone = models.CharField()
    languages = models.CharField()

class Activities(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField()
    videos = models.CharField()
    coords = models.CharField()
    type_activity = models.CharField()
    city_id = models.ForeignKey(Cities)



class Languages(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField()
    script = models.CharField()
    spoken_in = models.ForeignKey(Cities)