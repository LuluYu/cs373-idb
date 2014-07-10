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
