import unittest

from problems.intervals.insert_interval import InsertInterval


class TestInsertInterval(unittest.TestCase):

    def test_insert_empty_intervals(self):
        insert_interval = InsertInterval()
        intervals = []
        new_interval = [2, 5]
        expected = [[2, 5]]
        self.assertEqual(insert_interval.insert(intervals, new_interval), expected)

    def test_insert_non_overlapping_before(self):
        intsert_interval = InsertInterval()
        intervals = [[1, 2], [3, 5]]
        new_interval = [6, 8]
        expected = [[1, 2], [3, 5], [6, 8]]
        self.assertEqual(intsert_interval.insert(intervals, new_interval), expected)

    def test_insert_non_overlapping_after(self):
        intsert_interval = InsertInterval()
        intervals = [[6, 7], [8, 10]]
        new_interval = [2, 3]
        expected = [[2, 3], [6, 7], [8, 10]]
        self.assertEqual(intsert_interval.insert(intervals, new_interval), expected)

    def test_insert_overlapping_merge(self):
        intsert_interval = InsertInterval()
        intervals = [[1, 3], [6, 9]]
        new_interval = [2, 5]
        expected = [[1, 5], [6, 9]]
        self.assertEqual(intsert_interval.insert(intervals, new_interval), expected)

    def test_insert_overlapping_all(self):
        intsert_interval = InsertInterval()
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        new_interval = [4, 8]
        expected = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(intsert_interval.insert(intervals, new_interval), expected)


if __name__ == '__main__':
    unittest.main()
