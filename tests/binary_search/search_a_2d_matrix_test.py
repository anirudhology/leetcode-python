import unittest

from problems.binary_search.search_a_2d_matrix import SearchA2DMatrix


class SearchA2DMatrixTest(unittest.TestCase):
    def test_searchMatrix_null(self):
        # noinspection PyTypeChecker
        self.assertFalse(SearchA2DMatrix.searchMatrix(None, 5))

    def test_searchMatrix_empty(self):
        self.assertFalse(SearchA2DMatrix.searchMatrix([], 5))

    def test_searchMatrix_single_element_found(self):
        self.assertTrue(SearchA2DMatrix.searchMatrix([[5]], 5))

    def test_searchMatrix_single_element_not_found(self):
        self.assertFalse(SearchA2DMatrix.searchMatrix([[5]], 3))

    def test_searchMatrix_multiple_elements_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        self.assertTrue(SearchA2DMatrix.searchMatrix(matrix, 3))
        self.assertTrue(SearchA2DMatrix.searchMatrix(matrix, 11))
        self.assertTrue(SearchA2DMatrix.searchMatrix(matrix, 60))

    def test_searchMatrix_multiple_elements_not_found(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        self.assertFalse(SearchA2DMatrix.searchMatrix(matrix, 0))
        self.assertFalse(SearchA2DMatrix.searchMatrix(matrix, 6))
        self.assertFalse(SearchA2DMatrix.searchMatrix(matrix, 61))

    def test_searchMatrix_with_empty_rows(self):
        self.assertFalse(SearchA2DMatrix.searchMatrix([[], [], []], 5))

    def test_searchMatrix_various_scenarios(self):
        # Matrix with one row
        self.assertTrue(SearchA2DMatrix.searchMatrix([[1, 2, 3, 4, 5]], 3))
        self.assertFalse(SearchA2DMatrix.searchMatrix([[1, 2, 3, 4, 5]], 6))

        # Matrix with one column
        self.assertTrue(SearchA2DMatrix.searchMatrix([[1], [2], [3], [4], [5]], 3))
        self.assertFalse(SearchA2DMatrix.searchMatrix([[1], [2], [3], [4], [5]], 6))


if __name__ == '__main__':
    unittest.main()
