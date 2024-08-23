from typing import List


class CoinChangeII:
    @staticmethod
    def change(amount: int, coins: List[int]) -> int:
        # Special case
        if not coins or amount < 0:
            return 0
        # Lookup table to store number of ways to make amount
        lookup = [0] * (amount + 1)
        # There is one way to make up amount = 0;
        # Don't take anything
        lookup[0] = 1
        # Populate for remaining amount values
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    lookup[i] += lookup[i - coin]
        return lookup[amount]
