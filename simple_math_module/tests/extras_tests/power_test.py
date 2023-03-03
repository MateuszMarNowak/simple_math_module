import unittest
from ...extras.power import power

class TestPower(unittest.TestCase):

    def test_power(self):
        a, b = 4, 2
        self.assertEquals(power(a, b), 16)

    def test_power_negative(self):
        a, b = 8, -2
        self.assertAlmostEquals(round(power(a, b), 3), 0.016)

    def test_power_multiple_negative(self):
        args = [8, -2, 3]
        self.assertAlmostEquals(round(power(*args), 7), 3.814e-06)