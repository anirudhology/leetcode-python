import unittest

from problems.dynamic_programming.longest_increasing_subsequence import LongestIncreasingSubsequence


class TestLongestIncreasingSubsequence(unittest.TestCase):

    def setUp(self):
        self.lis = LongestIncreasingSubsequence()

    def test_length_of_lis(self):
        # Test case for null input
        # noinspection PyTypeChecker
        self.assertEqual(self.lis.lengthOfLIS(None), 0)

        # Test case for empty array
        self.assertEqual(self.lis.lengthOfLIS([]), 0)

        # Test case for single element array
        self.assertEqual(self.lis.lengthOfLIS([10]), 1)

        # Test case for array with all elements the same
        self.assertEqual(self.lis.lengthOfLIS([5, 5, 5, 5]), 1)

        # Test case for array with strictly increasing elements
        self.assertEqual(self.lis.lengthOfLIS([1, 2, 3, 4]), 4)

        # Test case for array with strictly decreasing elements
        self.assertEqual(self.lis.lengthOfLIS([5, 4, 3, 2, 1]), 1)

        # Test case for array with mixed increasing and decreasing elements
        self.assertEqual(self.lis.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

        # Test case for array with random elements
        self.assertEqual(self.lis.lengthOfLIS([3, 10, 2, 1, 20]), 3)


if __name__ == '__main__':
    unittest.main()
