import unittest

from problems.heap.k_closest_points_to_origin import KClosestPointsToOrigin


class TestKClosestPointsToOrigin(unittest.TestCase):
    def test_k_closest(self):
        k_closest_points_to_origin = KClosestPointsToOrigin()

        self.assertEqual(k_closest_points_to_origin.kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertEqual(k_closest_points_to_origin.kClosest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
        self.assertEqual(k_closest_points_to_origin.kClosest([[0, 1], [1, 0]], 1), [[0, 1]])
        self.assertEqual(k_closest_points_to_origin.kClosest([[1, 1]], 1), [[1, 1]])
        self.assertEqual(k_closest_points_to_origin.kClosest([], 0), [])