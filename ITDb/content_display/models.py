from django.db import models

# Create your models here.

class Cities(models.Model):
    '''
    Cities model has information for the Cities pages, this includes name, description,
    specific pictures, videos, map, coordinates, and other city information.
    '''
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.TextField()
    videos = models.TextField()
    coords = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    altitude = models.CharField(max_length= 30)
    climate = models.CharField(max_length= 30)
    population = models.CharField(max_length=20)
    time_zone = models.CharField(max_length= 20)
    lang = models.CharField(max_length = 60)
    act = models.TextField()

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s' % (self.name, self.description, self.pictures, self.videos, self.coords,
                        self.size, self.altitude, self.climate, self.population,
                        self.time_zone, self.lang, self.act)



class Activities(models.Model):
    '''
    The Activities has information that is specific
    to a particular activity. This includes name, description,
    pictures, videos, city, map coordinates, and type of activity.
    '''
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.TextField()
    videos = models.TextField()
    coords = models.CharField(max_length=60)
    type_activity = models.CharField(max_length=60)
    cit_name = models.TextField()
    city = models.ManyToManyField('Cities')

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.name, self.description, self.pictures,
                self.videos, self.coords, self.type_activity, self.cit_name)


class Languages(models.Model):
    '''
    The Languages has information that is specific
    to either a particular language. This includes name, description,
    and languages.
    '''
    name = models.CharField(max_length=30)
    description = models.TextField()
    pictures = models.TextField()
    script = models.TextField()
    cit_spoken = models.TextField()
    spoken_in = models.ManyToManyField('Cities')

    def __str__(self):
        return '%s %s %s %s %s' % (self.name, self.description,
                self.pictures, self.script, self.cit_spoken)