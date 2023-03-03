import unittest
from ...extras.multiply import multiply

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        a, b  = 3, 4
        self.assertEquals(multiply(a, b), 12)

    def test_multiply_multiple_arguments(self):
        a, b, c  = 3, 4, 2
        self.assertEquals(multiply(a, b, c), 24)

    def test_multiplu_negative_argument(self):
        args = [2, 4, -1]
        self.assertEquals(multiply(*args), -8)
