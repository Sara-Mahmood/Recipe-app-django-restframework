from django.test import TestCase

from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """ test whether two numbers are adding or not"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ test subtraction between two numbers"""
        self.assertEqual(subtract(3, 8), -5)