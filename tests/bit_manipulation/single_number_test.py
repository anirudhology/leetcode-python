import unittest

from problems.bit_manipulation.single_number import SingleNumber


class TestSingleNumber(unittest.TestCase):
    def test_single_number_with_single_element(self):
        single_number = SingleNumber()
        self.assertEqual(single_number.singleNumber([5]), 5)

    def test_single_number_with_multiple_elements(self):
        single_number = SingleNumber()
        self.assertEqual(single_number.singleNumber([2, 2, 1]), 1)

    def test_single_number_with_all_negative_elements(self):
        single_number = SingleNumber()
        self.assertEqual(single_number.singleNumber([-3, -1, -1]), -3)

    def test_single_number_with_mixed_elements(self):
        single_number = SingleNumber()
        self.assertEqual(single_number.singleNumber([4, 1, 2, 1, 2]), 4)

    def test_single_number_with_zeros(self):
        single_number = SingleNumber()
        self.assertEqual(single_number.singleNumber([0, 1, 1]), 0)


if __name__ == '__main__':
    unittest.main()
