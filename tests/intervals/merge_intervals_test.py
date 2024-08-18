import unittest

from problems.intervals.merge_intervals import MergeIntervals


class TestMergeIntervals(unittest.TestCase):

    def setUp(self):
        self.merge_intervals = MergeIntervals()

    def test_merge_intervals(self):
        # Test case: Overlapping intervals
        intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result1 = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.merge_intervals.merge(intervals1), result1)

        # Test case: Non-overlapping intervals
        intervals2 = [[1, 4], [5, 6]]
        result2 = [[1, 4], [5, 6]]
        self.assertEqual(self.merge_intervals.merge(intervals2), result2)

        # Test case: Single interval
        intervals3 = [[1, 4]]
        result3 = [[1, 4]]
        self.assertEqual(self.merge_intervals.merge(intervals3), result3)

        # Test case: Empty array
        intervals4 = []
        result4 = []
        self.assertEqual(self.merge_intervals.merge(intervals4), result4)

        # Test case: Null input
        intervals5 = None
        result5 = None
        # noinspection PyTypeChecker
        self.assertEqual(self.merge_intervals.merge(intervals5), result5)

        # Test case: Continuous intervals
        intervals6 = [[1, 4], [4, 5]]
        result6 = [[1, 5]]
        self.assertEqual(self.merge_intervals.merge(intervals6), result6)


if __name__ == '__main__':
    unittest.main()
