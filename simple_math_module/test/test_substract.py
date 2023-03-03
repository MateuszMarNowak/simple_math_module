import unittest
from substract import substract

class TestSubstract(unittest.TestCase):
    
    def test_substract(self):
        a, b = 2,1
        self.assertEquals(substract(a, b), 1)
    
    def test_substract_negative_output(self):
        a, b = 3, 4
        self.assertEquals(substract(a, b), -1)

    def test_substract_negative_arguments(self):
        a, b = 3, -5
        self.assertEquals(substract(a, b), 8)