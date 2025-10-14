"""
sample test
"""

from django.test import SimpleTestCase


from app import calc


class CalcTests(SimpleTestCase):
    """Test Calc module"""

    def test_add_number(self):
        """Adding Numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """subtract Numbers"""

        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
