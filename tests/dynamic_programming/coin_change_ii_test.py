import unittest

from problems.dynamic_programming.coin_change_ii import CoinChangeII


class TestCoinChangeII(unittest.TestCase):

    def test_change_simple_case(self):
        coin_change = CoinChangeII()
        self.assertEqual(coin_change.change(5, [1, 2, 5]), 4)

    def test_change_zero_amount(self):
        coin_change = CoinChangeII()
        self.assertEqual(coin_change.change(0, [1, 2, 5]), 1)

    def test_change_no_coins(self):
        coin_change = CoinChangeII()
        self.assertEqual(coin_change.change(5, []), 0)

    def test_change_negative_amount(self):
        coin_change = CoinChangeII()
        self.assertEqual(coin_change.change(-1, [1, 2, 5]), 0)

    def test_change_no_solution(self):
        coin_change = CoinChangeII()
        self.assertEqual(coin_change.change(3, [2]), 0)


if __name__ == '__main__':
    unittest.main()
