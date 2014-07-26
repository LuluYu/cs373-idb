"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from content_display.models import Cities, Activities, Languages
import urllib2
import json

# Testing Cities api with real data
class CityApiTest(TestCase) :
    def test_c1(self):
        response = urllib2.urlopen('http://flappybirds.pythonanywhere.com/api/cities/1/').read()
        response = json.load(response)
        self.assertEqual(response[0]["name"]=="Sydney")
        self.assertEqual(response[0]["id"]==1)
        self.assertEqual("description" in response)

    def test_c2(self):
        response = urllib2.urlopen('http://flappybirds.pythonanywhere.com/api/cities/9/').read()
        response = json.load(response)
        self.assertEqual(response[0]["name"]=="Vatican City")
        self.assertEqual(response[0]["id"]==9)
        self.assertEqual("description" in response)

    def test_c3(self):
        response = urllib2.urlopen('http://flappybirds.pythonanywhere.com/api/cities/19/').read()
        response = json.load(response)
        self.assertEqual("Error 400" in response)
        self.assertEqual(response["Error 400"]==" No such city exist in the in the database.")


# Testing Languages api with real data
class LanguagesApiTest(TestCase) :
    def test_c1(self):
        response = urllib2.urlopen('http://flappybirds.pythonanywhere.com/api/languages/1/').read()
        response = json.load(response)
        self.assertEqual(response[0]["name"]=="arabic")
        self.assertEqual(response[0]["id"]==1)
        self.assertEqual("description" in response)

    def test_c2(self):
        response = urllib2.urlopen('http://flappybirds.pythonanywhere.com/api/languages/9/').read()
        response = json.load(response)
        self.assertEqual(response[0]["name"]=="gujarati")
        self.assertEqual(response[0]["id"]==9)
        self.assertEqual("description" in response)

    def test_c3(self):
        response = urllib2.urlopen('http://flappybirds.pythonanywhere.com/api/languages/19/').read()
        response = json.load(response)
        self.assertEqual("Error 400" in response)
        self.assertEqual(response["Error 400"]==" No such city exist in the in the database.")


# Testing Activities api with real data
class LanguagesApiTest(TestCase) :
    def test_c1(self):
        response = urllib2.urlopen('http://flappybirds.pythonanywhere.com/api/activities/2/').read()
        response = json.load(response)
        self.assertEqual(response[0]["name"]=="Sydney Opera House")
        self.assertEqual(response[0]["id"]==2)
        self.assertEqual("description" in response)

    def test_c2(self):
        response = urllib2.urlopen('http://flappybirds.pythonanywhere.com/api/activities/201/').read()
        response = json.load(response)
        self.assertEqual("Error 400" in response)
        self.assertEqual(response["Error 400"]==" No such city exist in the in the database.")

    def test_c3(self):
        response = urllib2.urlopen('http://flappybirds.pythonanywhere.com/api/activities/200/').read()
        response = json.load(response)
        self.assertEqual("Error 400" in response)
        self.assertEqual(response["Error 400"]==" No such city exist in the in the database.")



# class CityTest(TestCase) :
#     def setUp(self) :
#         Cities.objects.create(name = 'Li Jiang', country = 'China', description = 'awesome', pictures = 'test.jpg', videos='test.jpg', coords = '0.0, 0.0', size = '8,193 sq mi', population = '1,244,769',time_zone = 'central')
#         Cities.objects.create( name = 'Chichen Itza', country = 'Mexico', description = 'awesome', pictures = 'test.jpg', videos='test.jpg', coords = '0.0, 0.0', size = '8,193 sq mi', population = '1,244,769',time_zone = 'central')
#         Cities.objects.create( name = 'Cape Town', country = 'Africa', description = 'awesome', pictures = 'test.jpg', videos='test.jpg', coords = '0.0, 0.0', size = '8,193 sq mi', population = '1,244,769',time_zone = 'central')
#         Cities.objects.create()

#     def test_c1(self) :
#         ci = Cities.objects.get(name= 'Chichen Itza')
#         self.assertEqual(ci.name, 'Chichen Itza')
#         self.assertEqual(ci.country, 'Mexico')
#         self.assertEqual(ci.description, 'awesome')
#         self.assertEqual(ci.pictures, 'test.jpg')
#         self.assertEqual(ci.videos, 'test.jpg')
#         self.assertEqual(ci.coords, '0.0, 0.0')
#         self.assertEqual(ci.size, '8,193 sq mi')
#         self.assertEqual(ci.population,'1,244,769')
#         self.assertEqual(ci.time_zone, 'central')

#     def test_c2(self) :
#         ct = Cities.objects.get(name= 'Cape Town')
#         self.assertEqual(ct.name, 'Cape Town')
#         self.assertEqual(ct.country, 'Africa')
#         self.assertEqual(ct.description, 'awesome')
#         self.assertEqual(ct.pictures, 'test.jpg')
#         self.assertEqual(ct.videos, 'test.jpg')
#         self.assertEqual(ct.coords, '0.0, 0.0')
#         self.assertEqual(ct.size, '8,193 sq mi')
#         self.assertEqual(ct.population,'1,244,769')
#         self.assertEqual(ct.time_zone, 'central')

#     def test_c3(self):
#         lj = Cities.objects.get(name= 'Li Jiang')
#         self.assertEqual(lj.name, 'Li Jiang')
#         self.assertEqual(lj.country, 'China')
#         self.assertEqual(lj.description, 'awesome')
#         self.assertEqual(lj.pictures, 'test.jpg')
#         self.assertEqual(lj.videos, 'test.jpg')
#         self.assertEqual(lj.coords, '0.0, 0.0')
#         self.assertEqual(lj.size, '8,193 sq mi')
#         self.assertEqual(lj.population,'1,244,769')
#         self.assertEqual(lj.time_zone, 'central')

#     def test_c4(self):
#         b = Cities.objects.get(name= u'')
#         self.assertEqual(b.name, u'')
#         self.assertEqual(b.country, u'')
#         self.assertEqual(b.description, u'')
#         self.assertEqual(b.pictures, u'')
#         self.assertEqual(b.videos, u'')
#         self.assertEqual(b.coords, u'')
#         self.assertEqual(b.size, u'')
#         self.assertEqual(b.population,u'')
#         self.assertEqual(b.time_zone, u'')


# # Testing Activities Model with dummy values
# '''
#     name = models.CharField(max_length=30)
#     description = models.TextField()
#     pictures = models.CharField(max_length=150)
#     videos = models.CharField(max_length=200)
#     coords = models.CharField(max_length=20)
#     type_activity = models.CharField(max_length=50)
#     city_id = models.IntegerField()
# '''
# class ActivityTest(TestCase) :
#     def setUp(self) :
#         Activities.objects.create(city_id = 1,name = 'Shark Diving', description = 'awesome', pictures='test.jpg', videos='test.jpg', coords='0.0, 0.0', type_activity = 'Outdoor Recreation')
#         Activities.objects.create(city_id = 2, name = 'Safari', type_activity = 'Scenery')
#         Activities.objects.create(city_id = 3,name = 'North Rim', description = 'awesome', pictures='test.jpg', videos='test.jpg', coords='0.0, 0.0', type_activity = 'Outdoor Recreation')
#         Activities.objects.create(city_id = 4)

#     def test_a1(self) :
#         sh = Activities.objects.get(name= 'Shark Diving')
#         self.assertEqual(Activities.objects.get(id = 1).name, 'Shark Diving')
#         self.assertEqual(sh.name, 'Shark Diving')
#         self.assertEqual(sh.description, 'awesome')
#         self.assertEqual(sh.pictures, 'test.jpg')
#         self.assertEqual(sh.videos, 'test.jpg')
#         self.assertEqual(sh.coords, '0.0, 0.0')
#         self.assertEqual(sh.type_activity, 'Outdoor Recreation')


#     def test_a2(self) :
#         sa = Activities.objects.get(name= 'North Rim')
#         self.assertEqual(Activities.objects.get(id=3).name, 'North Rim')
#         self.assertEqual(sa.name, 'North Rim')
#         self.assertEqual(sa.description, 'awesome')
#         self.assertEqual(sa.pictures, 'test.jpg')
#         self.assertEqual(sa.videos, 'test.jpg')
#         self.assertEqual(sa.coords, '0.0, 0.0')
#         self.assertEqual(sa.type_activity, 'Outdoor Recreation')

#     def test_a3(self) :
#         sh = Activities.objects.get(name= 'Shark Diving')
#         self.assertEqual(Activities.objects.get(id = 1).name, 'Shark Diving')
#         self.assertEqual(sh.name, 'Shark Diving')
#         self.assertEqual(sh.description, 'awesome')
#         self.assertEqual(sh.pictures, 'test.jpg')
#         self.assertEqual(sh.videos, 'test.jpg')
#         self.assertEqual(sh.coords, '0.0, 0.0')
#         self.assertEqual(sh.type_activity, 'Outdoor Recreation')

#     def test_a4(self):
#         b = Activities.objects.get(name= u'')
#         self.assertEqual(Activities.objects.get(id = 4).name, u'')
#         self.assertEqual(b.name, u'')
#         self.assertEqual(b.description, u'')
#         self.assertEqual(b.pictures, u'')
#         self.assertEqual(b.videos, u'')
#         self.assertEqual(b.coords, u'')
#         self.assertEqual(b.type_activity, u'')

# # Testing Languages Model with dummy data
# '''
#     name = models.CharField(max_length=30)
#     description = models.TextField()
#     pictures = models.TextField()
#     script = models.TextField()
# '''
# class LanguagesTest(TestCase) :
#     def setUp(self) :
#         Languages.objects.create(name = 'English',  description = 'awesome', pictures='test.jpg', script='script.jpg')
#         Languages.objects.create(name = 'Chinese',  description = 'desc')
#         Languages.objects.create(name = 'Spanish')
#         Languages.objects.create()

#     def test_l1(self) :
#         e = Languages.objects.get(id = 1)
#         self.assertEqual(e.name, 'English')
#         self.assertEqual(e.description, 'awesome')
#         self.assertEqual(e.pictures, 'test.jpg')
#         self.assertEqual(e.script, 'script.jpg')


#     def test_l2(self) :
#         c = Languages.objects.get(id = 2)
#         self.assertEqual(c.name, 'Chinese')
#         self.assertEqual(c.description, 'desc')
#         self.assertEqual(c.pictures, u'')
#         self.assertEqual(c.script, u'')

#     def test_l3(self) :
#         s = Languages.objects.get(id = 3)
#         self.assertEqual(s.name, 'Spanish')
#         self.assertEqual(s.description, u'')
#         self.assertEqual(s.pictures, u'')
#         self.assertEqual(s.script, u'')

#     def test_l4(self):
#         s = Languages.objects.get(id = 4)
#         self.assertEqual(s.name, u'')
#         self.assertEqual(s.description, u'')
#         self.assertEqual(s.pictures, u'')
#         self.assertEqual(s.script, u'')


