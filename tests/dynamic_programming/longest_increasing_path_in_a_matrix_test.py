import unittest

from problems.dynamic_programming.lonest_increasing_path_in_a_matrix import LongestIncreasingPathInAMatrix


class TestLongestIncreasingPathInAMatrix(unittest.TestCase):

    def setUp(self):
        self.longest_increasing_path_in_a_matrix = LongestIncreasingPathInAMatrix()

    def test_longest_increasing_path(self):
        # Test case 1: Single element matrix
        matrix1 = [[5]]
        self.assertEqual(self.longest_increasing_path_in_a_matrix.longestIncreasingPath(matrix1), 1)

        # Test case 2: 2x2 matrix with no increasing path
        matrix2 = [[3, 2], [1, 0]]
        self.assertEqual(self.longest_increasing_path_in_a_matrix.longestIncreasingPath(matrix2), 3)

        # Test case 3: 2x2 matrix with a simple increasing path
        matrix3 = [[1, 2], [3, 4]]
        self.assertEqual(self.longest_increasing_path_in_a_matrix.longestIncreasingPath(matrix3), 3)

        # Test case 4: 3x3 matrix with a more complex path
        matrix4 = [
            [9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]
        ]
        self.assertEqual(self.longest_increasing_path_in_a_matrix.longestIncreasingPath(matrix4), 4)

        # Test case 5: 3x3 matrix with all elements the same
        matrix5 = [
            [7, 7, 7],
            [7, 7, 7],
            [7, 7, 7]
        ]
        self.assertEqual(self.longest_increasing_path_in_a_matrix.longestIncreasingPath(matrix5), 1)

        # Test case 6: 4x4 matrix with multiple increasing paths
        matrix6 = [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [6, 5, 4, 3],
            [7, 8, 9, 10]
        ]
        self.assertEqual(self.longest_increasing_path_in_a_matrix.longestIncreasingPath(matrix6), 9)


if __name__ == "__main__":
    unittest.main()
