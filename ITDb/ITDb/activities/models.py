from django.db import models
from cities.models import Cities

# Create your models here.
class Activities(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField(max_length=150)
    videos = models.CharField(max_length=200)
    coords = models.CharField(max_length=20)
    type_activity = models.CharField(max_length=50)
    city_id = models.IntegerField()