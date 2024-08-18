import unittest

from problems.intervals.minimum_interval_to_include_each_query import MinimumIntervalToIncludeEachQuery


class TestMinimumIntervalToIncludeEachQuery(unittest.TestCase):

    def test_min_interval_basic_case(self):
        minimum_interval_to_include_each_query = MinimumIntervalToIncludeEachQuery()
        intervals = [[1, 4], [2, 4], [3, 6]]
        queries = [2, 3, 4]
        expected = [3, 3, 3]
        self.assertEqual(minimum_interval_to_include_each_query.minInterval(intervals, queries), expected)

    def test_min_interval_no_overlap(self):
        minimum_interval_to_include_each_query = MinimumIntervalToIncludeEachQuery()
        intervals = [[1, 2], [3, 4], [5, 6]]
        queries = [7, 8]
        expected = [-1, -1]
        self.assertEqual(minimum_interval_to_include_each_query.minInterval(intervals, queries), expected)

    def test_min_interval_multiple_queries(self):
        minimum_interval_to_include_each_query = MinimumIntervalToIncludeEachQuery()
        intervals = [[2, 5], [1, 10]]
        queries = [3, 4, 5, 6]
        expected = [4, 4, 4, 10]
        self.assertEqual(minimum_interval_to_include_each_query.minInterval(intervals, queries), expected)

    def test_min_interval_edge_case_empty_intervals(self):
        minimum_interval_to_include_each_query = MinimumIntervalToIncludeEachQuery()
        intervals = []
        queries = [1, 2, 3]
        expected = [-1, -1, -1]
        self.assertEqual(minimum_interval_to_include_each_query.minInterval(intervals, queries), expected)

    def test_min_interval_edge_case_empty_queries(self):
        minimum_interval_to_include_each_query = MinimumIntervalToIncludeEachQuery()
        intervals = [[1, 5], [3, 7]]
        queries = []
        expected = []
        self.assertEqual(minimum_interval_to_include_each_query.minInterval(intervals, queries), expected)


if __name__ == '__main__':
    unittest.main()
