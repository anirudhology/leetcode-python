import unittest

from problems.dynamic_programming.burst_balloons import BurstBalloons


class TestBurstBalloons(unittest.TestCase):

    def setUp(self):
        self.burst_balloons = BurstBalloons()

    def test_max_coins_single_balloon(self):
        self.assertEqual(self.burst_balloons.maxCoins([5]), 5)

    def test_max_coins_two_balloons(self):
        self.assertEqual(self.burst_balloons.maxCoins([3, 1]), 6)

    def test_max_coins_multiple_balloons(self):
        self.assertEqual(self.burst_balloons.maxCoins([3, 1, 5, 8]), 167)

    def test_max_coins_no_balloons(self):
        self.assertEqual(self.burst_balloons.maxCoins([]), 0)

    def test_max_coins_large_case(self):
        self.assertEqual(self.burst_balloons.maxCoins([1, 2, 3, 4, 5, 6]), 252)


if __name__ == '__main__':
    unittest.main()
