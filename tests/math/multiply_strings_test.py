import unittest

from problems.math.multiply_strings import MultiplyStrings


class TestMultiplyStrings(unittest.TestCase):

    def setUp(self):
        self.multiply_strings = MultiplyStrings()

    def test_multiply_with_zero(self):
        self.assertEqual(self.multiply_strings.multiply("0", "1234"), "0")
        self.assertEqual(self.multiply_strings.multiply("5678", "0"), "0")

    def test_multiply_single_digit_numbers(self):
        self.assertEqual(self.multiply_strings.multiply("3", "3"), "9")
        self.assertEqual(self.multiply_strings.multiply("5", "9"), "45")

    def test_multiply_multi_digit_numbers(self):
        self.assertEqual(self.multiply_strings.multiply("123", "456"), "56088")
        self.assertEqual(self.multiply_strings.multiply("999", "999"), "998001")


if __name__ == '__main__':
    unittest.main()
