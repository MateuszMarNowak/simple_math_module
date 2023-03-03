import unittest
from ..substract import substract

class TestAdd(unittest.TestCase):
    
    def test_substract(self):
        a, b = 2,1
        self.assertEquals(substract(a, b), 1)