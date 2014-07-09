"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from content_display.models import Cities Activities Languages

class CityTest(TestCase) :
    def test_c1(self):
        c1 = Cities.objects.create(name = 'Li Jiang')

        c = Cities(name = 'Li Jiang', size = '8,193 sq mi', population = '1,244,769')

