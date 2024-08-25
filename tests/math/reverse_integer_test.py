import unittest

from problems.math.reverse_integer import ReverseInteger


class TestReverseInteger(unittest.TestCase):
    def setUp(self):
        self.reverse_integer = ReverseInteger()

    def test_reverse_positive_number(self):
        self.assertEqual(self.reverse_integer.reverse(123), 321)

    def test_reverse_negative_number(self):
        self.assertEqual(self.reverse_integer.reverse(-123), -321)

    def test_reverse_zero(self):
        self.assertEqual(self.reverse_integer.reverse(0), 0)

    def test_reverse_overflow(self):
        self.assertEqual(self.reverse_integer.reverse(1534236469), 0)

    def test_reverse_single_digit(self):
        self.assertEqual(self.reverse_integer.reverse(9), 9)


if __name__ == '__main__':
    unittest.main()
