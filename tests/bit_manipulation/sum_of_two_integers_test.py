import unittest

from problems.bit_manipulation.sum_of_two_integers import SumOfTwoIntegers


class TestSumOfTwoIntegers(unittest.TestCase):
    def setUp(self):
        self.sum_of_two_integers = SumOfTwoIntegers()

    def test_get_sum_both_positive(self):
        self.assertEqual(self.sum_of_two_integers.getSum(2, 3), 5)

    def test_get_sum_one_positive_one_negative(self):
        self.assertEqual(self.sum_of_two_integers.getSum(3, -2), 1)

    def test_get_sum_both_negative(self):
        self.assertEqual(self.sum_of_two_integers.getSum(-2, -3), -5)

    def test_get_sum_first_zero(self):
        self.assertEqual(self.sum_of_two_integers.getSum(0, 4), 4)

    def test_get_sum_second_zero(self):
        self.assertEqual(self.sum_of_two_integers.getSum(-4, 0), -4)

    def test_get_sum_both_zero(self):
        self.assertEqual(self.sum_of_two_integers.getSum(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
