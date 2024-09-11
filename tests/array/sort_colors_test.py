import unittest

from problems.array.sort_colors import SortColors


class TestSortColors(unittest.TestCase):

    def setUp(self):
        self.sort_colors = SortColors()

    def test_all_zeros(self):
        nums = [0, 0, 0]
        self.assertEqual(self.sort_colors.sortColors(nums), [0, 0, 0])

    def test_all_ones(self):
        nums = [1, 1, 1]
        self.assertEqual(self.sort_colors.sortColors(nums), [1, 1, 1])

    def test_all_twos(self):
        nums = [2, 2, 2]
        self.assertEqual(self.sort_colors.sortColors(nums), [2, 2, 2])

    def test_mixed(self):
        nums = [2, 0, 2, 1, 1, 0]
        self.assertEqual(self.sort_colors.sortColors(nums), [0, 0, 1, 1, 2, 2])

    def test_empty_array(self):
        nums = []
        self.assertEqual(self.sort_colors.sortColors(nums), [])

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.sort_colors.sortColors(nums), [1])

    def test_already_sorted(self):
        nums = [0, 1, 2]
        self.assertEqual(self.sort_colors.sortColors(nums), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
