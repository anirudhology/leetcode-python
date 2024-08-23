from typing import List


class CountingBits:
    @staticmethod
    def countBits(n: int) -> List[int]:
        # Lookup table to store count of set bits
        lookup = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
            lookup[i] = lookup[i - offset] + 1
        return lookup
