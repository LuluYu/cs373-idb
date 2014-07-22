from django.db import models
from cities.models import Cities

# Create your models here.
class Activities(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.TextField()
    videos = models.URLField(max_length=250)
    coords = models.CharField(max_length=60)
    type_activity = models.CharField(max_length=50)
    city_id = models.ForeignKey('Cities')