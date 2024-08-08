import unittest

from problems.dynamic_programming.min_cost_climbing_stairs import MinCostClimbingStairs


class MinCostClimbingStairsTest(unittest.TestCase):

    def setUp(self):
        self.min_cost_climbing_stairs = MinCostClimbingStairs()

    def test_min_cost_climbing_stairs(self):
        # Test case for two elements array
        self.assertEqual(self.min_cost_climbing_stairs.minCostClimbingStairs([10, 15]), 10)

        # Test case for more elements
        self.assertEqual(self.min_cost_climbing_stairs.minCostClimbingStairs([10, 15, 20]), 15)
        self.assertEqual(self.min_cost_climbing_stairs.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)


if __name__ == '__main__':
    unittest.main()
