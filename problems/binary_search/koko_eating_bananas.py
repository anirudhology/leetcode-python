import math
from typing import List


class KokoEatingBananas:
    @staticmethod
    def minEatingSpeed(piles: List[int], h: int) -> int:
        # Special case
        if piles is None or len(piles) == 0 or h <= 0:
            return 0
        # Koko can eat minimum one banana and maximum "the greatest number
        # in the array" bananas
        left = 1
        right = max(piles)
        # Minimum rate
        min_rate = right
        # Process the array in the range
        while left <= right:
            current_rate = left + (right - left) // 2
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / current_rate)
            if time_taken <= h:
                min_rate = current_rate
                right = current_rate - 1
            else:
                left = current_rate + 1
        return min_rate
