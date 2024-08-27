import unittest

from problems.math.detect_squares import DetectSquares


class TestDetectSquares(unittest.TestCase):

    def test_add_and_count(self):
        detect_squares = DetectSquares()

        # Adding points
        detect_squares.add([1, 2])
        detect_squares.add([2, 1])
        detect_squares.add([1, 0])
        detect_squares.add([0, 1])

        # No squares should exist initially
        self.assertEqual(detect_squares.count([1, 1]), 0)

        # Adding points to form a square
        detect_squares.add([2, 2])
        self.assertEqual(detect_squares.count([1, 1]), 1)

        # Adding a point to form a second square
        detect_squares.add([0, 0])
        self.assertEqual(detect_squares.count([1, 1]), 2)

    def test_no_squares(self):
        ds = DetectSquares()

        # No points added, no squares should exist
        self.assertEqual(ds.count([0, 0]), 0)

    def test_multiple_same_points(self):
        ds = DetectSquares()

        # Adding the same point multiple times
        ds.add([0, 0])
        ds.add([0, 0])
        ds.add([1, 1])
        ds.add([1, 1])
        ds.add([0, 1])
        ds.add([1, 0])

        # Two squares are formed
        self.assertEqual(ds.count([0, 0]), 2)


if __name__ == '__main__':
    unittest.main()
