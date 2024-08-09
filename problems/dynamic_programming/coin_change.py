import sys
from typing import List


class CoinChange:
    @staticmethod
    def coinChange(coins: List[int], amount: int) -> int:
        # Special case
        if coins is None or len(coins) == 0 or amount < 0:
            return -1
        # Lookup table to store number of ways to make amount i
        lookup = [sys.maxsize] * (amount + 1)
        lookup[0] = 0
        # Fill the table
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    difference = lookup[i - coin]
                    if difference != sys.maxsize:
                        lookup[i] = min(lookup[i], difference + 1)
        return -1 if lookup[amount] == sys.maxsize else lookup[amount]
