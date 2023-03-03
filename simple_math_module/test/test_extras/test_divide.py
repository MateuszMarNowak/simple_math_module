import unittest
from extras.divide import divide

class TestDivide(unittest.TestCase):
    
    def test_divide(self):
        a, b = 2, 1
        self.assertEquals(divide(a, b), 2)

    def test_divide_float(self):
        a, b = 1, 2
        self.assertEquals(divide(a, b), 0.5)

    def test_divide_negative_arguments(self):
        a, b = 4, -2
        self.assertEquals(divide(a, b), -2)

    def test_division_by_zero_raise_exception(self):
        a, b = 4, 0
        with self.assertRaises(Exception) as context:
            divide(a, b)
        
        self.assertTrue("Division by zero is not permitted" in str(context.exception))
        