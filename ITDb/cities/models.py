from django.db import models

# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length = 30)
    description = models.TextField()
    pictures = models.TextField()
    videos = models.URLField(max_length = 250)
    coords = models.CharField(max_length=60)
    size = models.CharField(max_length=30)
    altitude = models.CharField(max_length= 30)
    climate = models.CharField(max_length= 30)
    population = models.CharField(max_length=30)
    time_zone = models.CharField(max_length= 30)
    languages = models.TextField()
