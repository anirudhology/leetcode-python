import unittest

from problems.dynamic_programming.coin_change import CoinChange


class CoinChangeTest(unittest.TestCase):

    def setUp(self):
        self.coin_change = CoinChange()

    def test_coin_change(self):
        # Test case for null coins array
        # noinspection PyTypeChecker
        self.assertEqual(self.coin_change.coinChange(None, 5), -1)

        # Test case for empty coins array
        self.assertEqual(self.coin_change.coinChange([], 5), -1)

        # Test case for negative amount
        self.assertEqual(self.coin_change.coinChange([1, 2, 5], -5), -1)

        # Test case for amount 0
        self.assertEqual(self.coin_change.coinChange([1, 2, 5], 0), 0)

        # Test case for amount that can't be reached
        self.assertEqual(self.coin_change.coinChange([2], 3), -1)

        # Test case for amount with exact coin matches
        self.assertEqual(self.coin_change.coinChange([1, 2, 5], 5), 1)

        # Test case for amount with no exact match but can be reached
        self.assertEqual(self.coin_change.coinChange([1, 2, 5], 11), 3)  # 5+5+1

        # Test case for large amount
        self.assertEqual(self.coin_change.coinChange([1, 2, 5], 100), 20)  # 20 coins of 5


if __name__ == '__main__':
    unittest.main()
