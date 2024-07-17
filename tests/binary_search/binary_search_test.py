import unittest

from problems.binary_search.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):
    def test_search_none(self):
        # noinspection PyTypeChecker
        self.assertEqual(BinarySearch.search(None, 5), -1)

    def test_search_empty(self):
        self.assertEqual(BinarySearch.search([], 5), -1)

    def test_search_single_element_found(self):
        self.assertEqual(BinarySearch.search([5], 5), 0)

    def test_search_single_element_not_found(self):
        self.assertEqual(BinarySearch.search([5], 3), -1)

    def test_search_multiple_elements_found(self):
        self.assertEqual(BinarySearch.search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(BinarySearch.search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(BinarySearch.search([1, 2, 3, 4, 5], 5), 4)

    def test_search_multiple_elements_not_found(self):
        self.assertEqual(BinarySearch.search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(BinarySearch.search([1, 2, 3, 4, 5], 6), -1)

    def test_search_with_duplicates(self):
        self.assertEqual(BinarySearch.search([1, 2, 2, 2, 3, 4, 5], 2), 3)


if __name__ == '__main__':
    unittest.main()
