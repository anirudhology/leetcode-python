import unittest

from problems.binary_search.find_minimum_in_rotated_sorted_array import FindMinimumInRotatedSortedArray


class TestFindMinimumInRotatedSortedArray(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(FindMinimumInRotatedSortedArray.findMin([1]), 1)

    def test_no_rotation(self):
        self.assertEqual(FindMinimumInRotatedSortedArray.findMin([1, 2, 3, 4, 5]), 1)

    def test_full_rotation(self):
        self.assertEqual(FindMinimumInRotatedSortedArray.findMin([1, 2, 3, 4, 5]), 1)

    def test_half_rotation(self):
        self.assertEqual(FindMinimumInRotatedSortedArray.findMin([3, 4, 5, 1, 2]), 1)

    def test_multiple_rotations(self):
        self.assertEqual(FindMinimumInRotatedSortedArray.findMin([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_decreasing_order(self):
        self.assertEqual(FindMinimumInRotatedSortedArray.findMin([3, 2, 1]), 1)

    def test_ascending_order(self):
        self.assertEqual(FindMinimumInRotatedSortedArray.findMin([1, 2, 3, 4, 5]), 1)

    def test_min_at_end(self):
        self.assertEqual(FindMinimumInRotatedSortedArray.findMin([2, 3, 4, 5, 1]), 1)

    def test_min_at_start(self):
        self.assertEqual(FindMinimumInRotatedSortedArray.findMin([1, 2, 3, 4, 5]), 1)


if __name__ == '__main__':
    unittest.main()
