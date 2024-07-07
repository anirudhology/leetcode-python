import unittest
from problems.array.two_sum import TwoSum


class TestTwoSum(unittest.TestCase):

    def test_found_at_start(self):
        self.assertEqual(TwoSum.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_found_at_end(self):
        self.assertEqual(TwoSum.twoSum([3, 2, 4], 6), [1, 2])

    def test_no_result(self):
        with self.assertRaises(Exception) as context:
            TwoSum.twoSum([1, 2, 3, 4], 8)
        self.assertTrue("Invalid inputs" in str(context.exception))

    def test_empty_array(self):
        with self.assertRaises(Exception) as context:
            TwoSum.twoSum([], 5)
        self.assertTrue("Invalid inputs!" in str(context.exception))

    def test_single_element(self):
        with self.assertRaises(Exception) as context:
            TwoSum.twoSum([5], 5)
        self.assertTrue("Invalid inputs!" in str(context.exception))

    def test_duplicates(self):
        self.assertEqual(TwoSum.twoSum([3, 3], 6), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(TwoSum.twoSum([-3, 4, 3, 90], 0), [0, 2])

    def test_zeroes(self):
        self.assertEqual(TwoSum.twoSum([0, 4, 3, 0], 0), [0, 3])

    def test_large_numbers(self):
        self.assertEqual(TwoSum.twoSum([1000000000, 999999999, 1, 2], 1999999999), [0, 1])

    def test_none_input(self):
        with self.assertRaises(Exception) as context:
            # noinspection PyTypeChecker
            TwoSum.twoSum(None, 5)
        self.assertTrue("Invalid inputs!" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
