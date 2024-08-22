import unittest

from problems.dynamic_programming.best_time_to_buy_and_sell_stocks_with_cooldown import \
    BestTimeToBuyAndSellStocksWithCooldown


class TestBestTimeToBuyAndSellStocksWithCooldown(unittest.TestCase):

    def test_max_profit_simple_case(self):
        bt = BestTimeToBuyAndSellStocksWithCooldown()
        self.assertEqual(bt.maxProfit([1, 2, 3, 0, 2]), 3)

    def test_max_profit_empty_prices(self):
        bt = BestTimeToBuyAndSellStocksWithCooldown()
        self.assertEqual(bt.maxProfit([]), 0)

    def test_max_profit_one_day(self):
        bt = BestTimeToBuyAndSellStocksWithCooldown()
        self.assertEqual(bt.maxProfit([1]), 0)

    def test_max_profit_two_days_profit(self):
        bt = BestTimeToBuyAndSellStocksWithCooldown()
        self.assertEqual(bt.maxProfit([1, 2]), 1)

    def test_max_profit_two_days_loss(self):
        bt = BestTimeToBuyAndSellStocksWithCooldown()
        self.assertEqual(bt.maxProfit([2, 1]), 0)

    def test_max_profit_all_decreasing_prices(self):
        bt = BestTimeToBuyAndSellStocksWithCooldown()
        self.assertEqual(bt.maxProfit([5, 4, 3, 2, 1]), 0)


if __name__ == '__main__':
    unittest.main()
