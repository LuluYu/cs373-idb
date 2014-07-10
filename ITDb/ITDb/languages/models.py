from django.db import models
from cities.models import Cities

# Create your models here.
class Languages(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField(max_length=150)
    script = models.CharField(max_length=30)
    spoken_in = models.IntegerField()