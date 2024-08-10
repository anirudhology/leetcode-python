from typing import List


class PartitionEqualSubsetSum:
    @staticmethod
    def canPartition(nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        # Sum of all elements in the array
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        # Target sum to reach
        target = total_sum // 2
        # Lookup table to store if the sum is possible or not
        lookup = [True] + [False] * target
        # Populate the table
        for num in nums:
            for j in range(target, num - 1, -1):
                lookup[j] |= lookup[j - num]
        return lookup[target]
