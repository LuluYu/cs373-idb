"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from languages.models import Languages


class LanguagesTest(TestCase) :
    def setUp(self) :
        Languages.objects.create(name = 'English', spoken_in = 3, description = 'desc')
        Languages.objects.create(name = 'Chinese', spoken_in = 1, description = 'desc')

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
        self.assertEqual(e.spoken_in, 3)
        self.assertEqual(c.script, u'')
        self.assertEqual(c.spoken_in, 1)
