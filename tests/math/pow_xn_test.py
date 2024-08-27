import unittest

from problems.math.pow_xn import PowXN


class TestPowXN(unittest.TestCase):

    def setUp(self):
        self.pow_xn = PowXN()

    def test_power_zero_exponent(self):
        self.assertAlmostEqual(self.pow_xn.myPow(2.0, 0), 1.0, places=5)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(self.pow_xn.myPow(2.0, -2), 0.25, places=5)

    def test_power_positive_exponent_even(self):
        self.assertAlmostEqual(self.pow_xn.myPow(2.0, 4), 16.0, places=5)

    def test_power_positive_exponent_odd(self):
        self.assertAlmostEqual(self.pow_xn.myPow(2.0, 3), 8.0, places=5)

    def test_power_base_zero(self):
        self.assertAlmostEqual(self.pow_xn.myPow(0.0, 5), 0.0, places=5)

    def test_power_base_one(self):
        self.assertAlmostEqual(self.pow_xn.myPow(1.0, 5), 1.0, places=5)

    def test_power_base_negative_one_odd(self):
        self.assertAlmostEqual(self.pow_xn.myPow(-1.0, 3), -1.0, places=5)

    def test_power_base_negative_one_even(self):
        self.assertAlmostEqual(self.pow_xn.myPow(-1.0, 2), 1.0, places=5)


if __name__ == '__main__':
    unittest.main()
