"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
#from content_display.models import Cities
from content_display.models import Cities, Activities, Languages

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


# Testing Activities Model with dummy values

class ActivityTest(TestCase) :
    def setUp(self) :
        Activities.objects.create(name = 'Shark Diving', type_activity = 'Outdoor Recreation', pictures = '1')
        Activities.objects.create(name = 'Safari', type_activity = 'Scenery', pictures = '2')

    def test_a1(self) :
        sh = Activities.objects.get(name= 'Shark Diving')
        sa = Activities.objects.get(name= 'Safari')
        self.assertEqual(sh.name, 'Shark Diving')
        self.assertEqual(sa.name, 'Safari')
        self.assertEqual(Activities.objects.get(id = 1).name, 'Shark Diving')
        self.assertEqual(Activities.objects.get(id = 2).name, 'Safari')

    def test_a2(self) :
        sh = Activities.objects.get(name= 'Shark Diving')
        sa = Activities.objects.get(name= 'Safari')
        self.assertEqual(sh.coords, u'')
        self.assertEqual(sh.description, u'')
        self.assertEqual(sa.coords, u'')
        self.assertEqual(sa.description, u'')

    def test_a3(self) :
        sh = Activities.objects.get(name= 'Shark Diving')
        sa = Activities.objects.get(name= 'Safari')
        self.assertEqual(sh.type_activity, 'Outdoor Recreation')
        self.assertEqual(sa.type_activity, 'Scenery')
        self.assertEqual(sh.pictures, '1')


# Testing Languages Model with dummy data

class LanguagesTest(TestCase) :
    def setUp(self) :
        Languages.objects.create(name = 'English',  description = 'desc', cit_spoken = 'us')
        Languages.objects.create(name = 'Chinese',  description = 'desc', cit_spoken = 'lijiang')

    def test_l1(self) :
        e = Languages.objects.get(id = 1)
        c = Languages.objects.get(id = 2)
        self.assertEqual(e.name, 'English')
        self.assertEqual(c.name, 'Chinese')

    def test_l2(self) :
        e = Languages.objects.get(id = 1)
        c = Languages.objects.get(id = 2)
        self.assertEqual(e.script, u'')
        self.assertEqual(c.script, u'')
        self.assertEqual(e.pictures, u'')

    def test_l3(self) :
        e = Languages.objects.get(id = 1)
        c = Languages.objects.get(id = 2)
        self.assertEqual(e.cit_spoken, 'us')
        self.assertEqual(c.script, u'')
        self.assertEqual(c.cit_spoken, 'lijiang')


