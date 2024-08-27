import unittest

from problems.matrix.set_matrix_zeroes import SetMatrixZeroes


class TestSetMatrixZeroes(unittest.TestCase):

    def setUp(self):
        self.set_matrix_zeroes = SetMatrixZeroes()

    def test_set_zeroes_empty_matrix(self):
        matrix = []
        expected = self.set_matrix_zeroes.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_set_zeroes_single_element_zero(self):
        matrix = [[0]]
        expected = self.set_matrix_zeroes.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_set_zeroes_single_element_non_zero(self):
        matrix = [[1]]
        expected = self.set_matrix_zeroes.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_set_zeroes_matrix_with_no_zeroes(self):
        matrix = [[1, 2], [3, 4]]
        expected = self.set_matrix_zeroes.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_set_zeroes_matrix_with_zeroes(self):
        matrix = [[1, 0, 3], [4, 5, 6], [7, 8, 9]]
        expected = self.set_matrix_zeroes.setZeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_set_zeroes_matrix_with_multiple_zeroes(self):
        matrix = [[0, 2, 3], [4, 5, 0], [7, 8, 9]]
        expected = self.set_matrix_zeroes.setZeroes(matrix)
        self.assertEqual(matrix, expected)


if __name__ == '__main__':
    unittest.main()
