"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from activities.models import Activities

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
