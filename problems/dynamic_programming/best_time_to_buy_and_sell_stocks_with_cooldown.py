from typing import List


class BestTimeToBuyAndSellStocksWithCooldown:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        # Special case
        if not prices:
            return 0
        # Total number of days
        n = len(prices)
        # Arrays to store buy and sell prices
        buy, sell = [float('-inf')] * n, [0] * n
        buy[0] = -prices[0]
        # Process for remaining days
        for i in range(1, n):
            buy[i] = max(buy[i - 1], (sell[i - 2] - prices[i]) if i > 1 else -prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        return sell[-1]
