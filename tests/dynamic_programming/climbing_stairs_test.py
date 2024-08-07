import unittest

from problems.dynamic_programming.climbing_stairs import ClimbingStairs


class ClimbingStairsTest(unittest.TestCase):

    def setUp(self):
        self.climbing_stairs = ClimbingStairs()

    def test_climb_stairs(self):
        # Test case for n = 0
        self.assertEqual(self.climbing_stairs.climbStairs(0), 0)

        # Test case for n = 1
        self.assertEqual(self.climbing_stairs.climbStairs(1), 1)

        # Test case for n = 2
        self.assertEqual(self.climbing_stairs.climbStairs(2), 2)

        # Test case for n = 3
        self.assertEqual(self.climbing_stairs.climbStairs(3), 3)

        # Test case for n = 4
        self.assertEqual(self.climbing_stairs.climbStairs(4), 5)

        # Test case for n = 5
        self.assertEqual(self.climbing_stairs.climbStairs(5), 8)


if __name__ == '__main__':
    unittest.main()
