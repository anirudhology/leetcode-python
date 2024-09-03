import unittest

from problems.graph.min_cost_to_connect_all_points import MinCostToConnectAllPoints


class TestMinCostToConnectAllPoints(unittest.TestCase):

    def setUp(self):
        self.min_cost = MinCostToConnectAllPoints()

    def test_min_cost_connect_points_empty(self):
        self.assertEqual(self.min_cost.minCostConnectPoints([]), 0)

    def test_min_cost_connect_points_single_point(self):
        self.assertEqual(self.min_cost.minCostConnectPoints([[0, 0]]), 0)

    def test_min_cost_connect_points_two_points(self):
        self.assertEqual(self.min_cost.minCostConnectPoints([[0, 0], [1, 1]]), 2)

    def test_min_cost_connect_points_multiple_points(self):
        self.assertEqual(self.min_cost.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20)

    def test_min_cost_connect_points_negative_points(self):
        self.assertEqual(self.min_cost.minCostConnectPoints([[-1, -2], [1, 3], [4, 5]]), 12)


if __name__ == '__main__':
    unittest.main()
