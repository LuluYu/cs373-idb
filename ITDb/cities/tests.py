"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from cities.models import Cities

# Testing City Model with dummy data

class CityTest(TestCase) :
    def setUp(self) :
        Cities.objects.create(name = 'Li Jiang', size = '8,193 sq mi', population = '1,244,769')
        Cities.objects.create(name = 'Chichen Itza', size = '123 sq mi', coords = '1.0, 2.0')

    def test_c1(self) :
        lj = Cities.objects.get(name= 'Li Jiang')
        ci = Cities.objects.get(name= 'Chichen Itza')
        self.assertEqual(lj.name, 'Li Jiang')
        self.assertEqual(ci.name, 'Chichen Itza')
        self.assertEqual(Cities.objects.get(id = 1).name, 'Li Jiang')
        self.assertEqual(Cities.objects.get(id = 2).name, 'Chichen Itza')

    def test_c2(self) :
        lj = Cities.objects.get(name= 'Li Jiang')
        ci = Cities.objects.get(name= 'Chichen Itza')
        self.assertEqual(lj.altitude, u'')
        self.assertEqual(lj.time_zone, u'')
        self.assertEqual(ci.description, u'')

    def test_c3(self) :
        lj = Cities.objects.get(name= 'Li Jiang')
        ci = Cities.objects.get(name= 'Chichen Itza')
        self.assertEqual(lj.population, '1,244,769')
        self.assertEqual(lj.time_zone, u'')
        self.assertEqual(ci.size, '123 sq mi')
        self.assertEqual(ci.coords, '1.0, 2.0')
