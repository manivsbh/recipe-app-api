"""
Sample Tests

"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Tests the Calc Module"""

    def test_add_number(self):
        """Tests Adding numbers together """

        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """ Test Subtracting two numbers"""
        res = calc.subtract(10,15)

        self.assertEqual(res, 5)
