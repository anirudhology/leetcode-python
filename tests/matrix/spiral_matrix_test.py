import unittest

from problems.matrix.spiral_matrix import SpiralMatrix


class TestSpiralMatrix(unittest.TestCase):

    def setUp(self):
        self.spiral_matrix = SpiralMatrix()

    def test_spiral_order_empty_matrix(self):
        matrix = []
        expected = []
        self.assertEqual(self.spiral_matrix.spiralOrder(matrix), expected)

    def test_spiral_order_single_element(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(self.spiral_matrix.spiralOrder(matrix), expected)

    def test_spiral_order_single_row(self):
        matrix = [[1, 2, 3, 4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(self.spiral_matrix.spiralOrder(matrix), expected)

    def test_spiral_order_single_column(self):
        matrix = [[1], [2], [3], [4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(self.spiral_matrix.spiralOrder(matrix), expected)

    def test_spiral_order_rectangular_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(self.spiral_matrix.spiralOrder(matrix), expected)

    def test_spiral_order_rectangular_matrix_2x3(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [1, 2, 3, 6, 5, 4]
        self.assertEqual(self.spiral_matrix.spiralOrder(matrix), expected)


if __name__ == '__main__':
    unittest.main()
