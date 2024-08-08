from typing import List


class HouseRobber:
    @staticmethod
    def rob(nums: List[int]) -> int:
        # Total number of houses
        n = len(nums)
        # Special cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # Lookup table for remaining houses
        lookup = [0] * n
        lookup[0] = nums[0]
        lookup[1] = max(nums[0], nums[1])
        for i in range(2, n):
            lookup[i] = max(lookup[i - 2] + nums[i], lookup[i - 1])
        return lookup[n - 1]
