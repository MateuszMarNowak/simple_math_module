import unittest
from ..add import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        a, b = 1,2
        self.assertEquals(add(a, b), 3)

    def test_add_multiple_args(self):
        a, b, c, d = 1, 2, 3, 4
        self.assertEqual(add(a, b, c, d), 10)

    def test_add_single_argument(self):
        a = 2
        self.assertEqual(add(a), 2)

    def test_add_no_arguments(self):
        self.assertEqual(add(), 0)