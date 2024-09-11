import unittest

from problems.sliding_window.minimum_size_subarray_sum import MinimumSizeSubarraySum


class TestMinimumSizeSubarraySum(unittest.TestCase):

    def setUp(self):
        self.minimum_size_subarray_sum = MinimumSizeSubarraySum()

    def test_min_sub_array_len_empty_array(self):
        self.assertEqual(self.minimum_size_subarray_sum.minSubArrayLen(7, []), 0)

    def test_min_sub_array_len_null_array(self):
        self.assertEqual(self.minimum_size_subarray_sum.minSubArrayLen(7, None), 0)

    def test_min_sub_array_len_no_subarray_exists(self):
        self.assertEqual(self.minimum_size_subarray_sum.minSubArrayLen(15, [1, 2, 3, 4, 5]), 5)

    def test_min_sub_array_len_exact_match(self):
        self.assertEqual(self.minimum_size_subarray_sum.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_min_sub_array_len_multiple_matches(self):
        self.assertEqual(self.minimum_size_subarray_sum.minSubArrayLen(4, [1, 4, 4]), 1)

    def test_min_sub_array_len_single_element(self):
        self.assertEqual(self.minimum_size_subarray_sum.minSubArrayLen(3, [3]), 1)


if __name__ == '__main__':
    unittest.main()
