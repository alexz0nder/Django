from django.test import TestCase

from app.calc import adduser

class CalcTests(TestCase):

    def test_add_numer(self):

        self.assertEqual(add(3, 8), 11)
