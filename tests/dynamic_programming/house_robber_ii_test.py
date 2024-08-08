import unittest

from problems.dynamic_programming.house_robber_ii import HouseRobberII


class HouseRobberIITest(unittest.TestCase):

    def setUp(self):
        self.house_robber_ii = HouseRobberII()

    def test_rob(self):
        # Test case for empty array
        self.assertEqual(self.house_robber_ii.rob([]), 0)

        # Test case for single element array
        self.assertEqual(self.house_robber_ii.rob([10]), 10)

        # Test case for two elements array
        self.assertEqual(self.house_robber_ii.rob([10, 20]), 20)

        # Test case for more elements
        self.assertEqual(self.house_robber_ii.rob([2, 3, 2]), 3)
        self.assertEqual(self.house_robber_ii.rob([1, 2, 3, 1]), 4)
        self.assertEqual(self.house_robber_ii.rob([100, 2, 3, 100]), 103)


if __name__ == '__main__':
    unittest.main()
