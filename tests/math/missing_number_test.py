import unittest

from problems.math.missing_number import MissingNumber


class TestMissingNumber(unittest.TestCase):

    def test_missing_number_with_single_element_zero(self):
        missing_number = MissingNumber()
        self.assertEqual(missing_number.missingNumber([0]), 1, "The missing number in [0] should be 1.")

    def test_missing_number_with_single_element_one(self):
        missing_number = MissingNumber()
        self.assertEqual(missing_number.missingNumber([1]), 0, "The missing number in [1] should be 0.")

    def test_missing_number_with_no_missing(self):
        missing_number = MissingNumber()
        self.assertEqual(missing_number.missingNumber([0, 1, 2, 3, 4]), 5,
                         "The missing number in [0, 1, 2, 3, 4] should be 5.")

    def test_missing_number_with_missing_in_middle(self):
        missing_number = MissingNumber()
        self.assertEqual(missing_number.missingNumber([3, 0, 1]), 2, "The missing number in [3, 0, 1] should be 2.")

    def test_missing_number_with_missing_at_end(self):
        missing_number = MissingNumber()
        self.assertEqual(missing_number.missingNumber([0, 1, 3]), 2, "The missing number in [0, 1, 3] should be 2.")

    def test_missing_number_with_large_array(self):
        missing_number = MissingNumber()
        self.assertEqual(missing_number.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8,
                         "The missing number in [9, 6, 4, 2, 3, 5, 7, 0, 1] should be 8.")

    def test_missing_number_empty_array(self):
        missing_number = MissingNumber()
        self.assertEqual(missing_number.missingNumber([]), 0, "The missing number in an empty array should be 0.")


if __name__ == '__main__':
    unittest.main()
