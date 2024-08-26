import unittest

from problems.math.rotate_image import RotateImage


class TestRotateImage(unittest.TestCase):

    def test_rotate(self):
        rotate_image = RotateImage()

        # Test case 1: 3x3 matrix
        matrix1 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected1 = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        rotate_image.rotate(matrix1)
        self.assertEqual(matrix1, expected1)

        # Test case 2: 4x4 matrix
        matrix2 = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        expected2 = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
        rotate_image.rotate(matrix2)
        self.assertEqual(matrix2, expected2)

        # Test case 3: 1x1 matrix
        matrix3 = [[1]]
        expected3 = [[1]]
        rotate_image.rotate(matrix3)
        self.assertEqual(matrix3, expected3)

        # Test case 4: Empty matrix
        matrix4 = []
        expected4 = []
        rotate_image.rotate(matrix4)
        self.assertEqual(matrix4, expected4)

        # Test case 5: Null matrix
        matrix5 = None
        rotate_image.rotate(matrix5)
        self.assertIsNone(matrix5)


if __name__ == '__main__':
    unittest.main()
