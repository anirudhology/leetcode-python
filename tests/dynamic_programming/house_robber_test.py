import unittest

from problems.dynamic_programming.house_robber import HouseRobber


class TestHouseRobber(unittest.TestCase):

    def setUp(self):
        self.house_robber = HouseRobber()

    def test_rob(self):
        # Test case for single element array
        self.assertEqual(self.house_robber.rob([10]), 10)

        # Test case for two elements array
        self.assertEqual(self.house_robber.rob([10, 20]), 20)

        # Test case for more elements
        self.assertEqual(self.house_robber.rob([1, 2, 3, 1]), 4)
        self.assertEqual(self.house_robber.rob([2, 7, 9, 3, 1]), 12)
        self.assertEqual(self.house_robber.rob([1, 2, 9, 4, 5, 10]), 20)


if __name__ == '__main__':
    unittest.main()
