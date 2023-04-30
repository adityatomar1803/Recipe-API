"""
    samples tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(2, 3)

        self.assertEqual(res, 5)

    def test_sub_numbers(self):
        res = calc.subtract(5, 10)
        
        self.assertEqual(res, 5)
