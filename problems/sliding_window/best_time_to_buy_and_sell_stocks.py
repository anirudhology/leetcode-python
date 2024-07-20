from typing import List


class BestTimeToBuyAndSellStocks:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        # Special case
        if prices is None or len(prices) == 0:
            return 0
        # Max profit and min price so far
        max_profit, min_price = 0, prices[0]
        # Process the array
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit
