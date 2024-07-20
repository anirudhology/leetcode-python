import unittest

from problems.sliding_window.best_time_to_buy_and_sell_stocks import BestTimeToBuyAndSellStocks


class TestBestTimeToBuyAndSellStocks(unittest.TestCase):
    def test_empty_prices(self):
        self.assertEqual(BestTimeToBuyAndSellStocks.maxProfit([]), 0)

    def test_none_prices(self):
        # noinspection PyTypeChecker
        self.assertEqual(BestTimeToBuyAndSellStocks.maxProfit(None), 0)

    def test_single_price(self):
        self.assertEqual(BestTimeToBuyAndSellStocks.maxProfit([10]), 0)

    def test_all_increasing_prices(self):
        self.assertEqual(BestTimeToBuyAndSellStocks.maxProfit([1, 2, 3, 4, 5]), 4)

    def test_all_decreasing_prices(self):
        self.assertEqual(BestTimeToBuyAndSellStocks.maxProfit([5, 4, 3, 2, 1]), 0)

    def test_mixed_prices(self):
        self.assertEqual(BestTimeToBuyAndSellStocks.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit_prices(self):
        self.assertEqual(BestTimeToBuyAndSellStocks.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_multiple_peaks_prices(self):
        self.assertEqual(BestTimeToBuyAndSellStocks.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]), 4)


if __name__ == '__main__':
    unittest.main()
