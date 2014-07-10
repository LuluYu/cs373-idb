from django.db import models
from cities.models import Cities

# Create your models here.
class Activities(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField()
    videos = models.CharField()
    coords = models.CharField()
    type_activity = models.CharField()
    city_id = models.ForeignKey(Cities)