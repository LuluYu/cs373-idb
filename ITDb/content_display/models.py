#from django.db import models

# Create your models here.
'''
Cities model has information for the Cities pages, this includes name, description,
specific pictures, videos, map, coordinates, and other city information.
'''
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
'''
The Activities has information that is specific
to a particular activity. This includes name, description,
pictures, videos, city, map coordinates, and type of activity.
'''
class Activities(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField(max_length=150)
    videos = models.CharField(max_length=200)
    coords = models.CharField(max_length=20)
    type_activity = models.CharField(max_length=50)
    city_id = models.IntegerField()

'''
The Languages has information that is specific
to either a particular language. This includes name, description,
and languages.
'''
class Languages(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.CharField(max_length=150)
    script = models.CharField(max_length=30)
    spoken_in = models.IntegerField()
