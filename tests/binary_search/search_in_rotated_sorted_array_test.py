import unittest

from problems.binary_search.search_in_rotated_sorted_array import SearchInRotatedSortedArray


class SearchInRotatedSortedArrayTest(unittest.TestCase):

    def test_search_found(self):
        self.assertEqual(SearchInRotatedSortedArray.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(SearchInRotatedSortedArray.search([4, 5, 6, 7, 0, 1, 2], 4), 0)
        self.assertEqual(SearchInRotatedSortedArray.search([4, 5, 6, 7, 0, 1, 2], 2), 6)
        self.assertEqual(SearchInRotatedSortedArray.search([1, 3], 1), 0)
        self.assertEqual(SearchInRotatedSortedArray.search([3, 1], 1), 1)

    def test_search_not_found(self):
        self.assertEqual(SearchInRotatedSortedArray.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(SearchInRotatedSortedArray.search([1], 0), -1)
        self.assertEqual(SearchInRotatedSortedArray.search([], 1), -1)

    def test_search_edge_cases(self):
        self.assertEqual(SearchInRotatedSortedArray.search([1], 1), 0)
        # noinspection PyTypeChecker
        self.assertEqual(SearchInRotatedSortedArray.search(None, 1), -1)


if __name__ == '__main__':
    unittest.main()
