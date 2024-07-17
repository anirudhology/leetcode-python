import unittest

from problems.stack.largest_rectangle_in_histogram import LargestRectangleInHistogram


class TestLargestRectangleInHistogram(unittest.TestCase):

    def test_empty_heights(self):
        self.assertEqual(LargestRectangleInHistogram.largestRectangleArea([]), 0)

    def test_none_heights(self):
        # noinspection PyTypeChecker
        self.assertEqual(LargestRectangleInHistogram.largestRectangleArea(None), 0)

    def test_single_height(self):
        self.assertEqual(LargestRectangleInHistogram.largestRectangleArea([2]), 2)

    def test_multiple_heights(self):
        self.assertEqual(LargestRectangleInHistogram.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)

    def test_all_same_heights(self):
        self.assertEqual(LargestRectangleInHistogram.largestRectangleArea([2, 2, 2, 2]), 8)

    def test_decreasing_heights(self):
        self.assertEqual(LargestRectangleInHistogram.largestRectangleArea([6, 5, 4, 3, 2, 1]), 12)

    def test_increasing_heights(self):
        self.assertEqual(LargestRectangleInHistogram.largestRectangleArea([1, 2, 3, 4, 5, 6]), 12)

    def test_alternating_heights(self):
        self.assertEqual(LargestRectangleInHistogram.largestRectangleArea([2, 1, 2, 1, 2, 1]), 6)


if __name__ == '__main__':
    unittest.main()
