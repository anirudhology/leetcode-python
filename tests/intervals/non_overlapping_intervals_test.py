import unittest

from problems.intervals.non_overlapping_intervals import NonOverlappingIntervals


class TestNonOverlappingIntervals(unittest.TestCase):

    def setUp(self):
        self.non_overlapping_intervals = NonOverlappingIntervals()

    def test_erase_overlap_intervals(self):
        # Test case: Overlapping intervals
        intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
        self.assertEqual(self.non_overlapping_intervals.eraseOverlapIntervals(intervals1), 1)

        # Test case: Non-overlapping intervals
        intervals2 = [[1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.non_overlapping_intervals.eraseOverlapIntervals(intervals2), 0)

        # Test case: Single interval
        intervals3 = [[1, 2]]
        self.assertEqual(self.non_overlapping_intervals.eraseOverlapIntervals(intervals3), 0)

        # Test case: Empty array
        intervals4 = []
        self.assertEqual(self.non_overlapping_intervals.eraseOverlapIntervals(intervals4), 0)

        # Test case: Null input
        intervals5 = None
        # noinspection PyTypeChecker
        self.assertEqual(self.non_overlapping_intervals.eraseOverlapIntervals(intervals5), 0)

        # Test case: Multiple overlapping intervals
        intervals6 = [[1, 3], [2, 4], [3, 5], [1, 2]]
        self.assertEqual(self.non_overlapping_intervals.eraseOverlapIntervals(intervals6), 2)


if __name__ == '__main__':
    unittest.main()
