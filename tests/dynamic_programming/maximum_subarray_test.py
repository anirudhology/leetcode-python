import unittest

from problems.dynamic_programming.maximum_subarray import MaximumSubarray


class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        self.maximum_subarray = MaximumSubarray()

    def test_max_sub_array_single_element(self):
        self.assertEqual(self.maximum_subarray.maxSubArray([5]), 5)

    def test_max_sub_array_all_negative(self):
        self.assertEqual(self.maximum_subarray.maxSubArray([-1, -2, -3, -4]), -1)

    def test_max_sub_array_mixed(self):
        self.assertEqual(self.maximum_subarray.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_max_sub_array_all_positive(self):
        self.assertEqual(self.maximum_subarray.maxSubArray([1, 2, 3, 4, 5]), 15)


if __name__ == '__main__':
    unittest.main()
