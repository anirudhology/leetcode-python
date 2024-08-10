from typing import List


class LongestIncreasingSubsequence:
    @staticmethod
    def lengthOfLIS(nums: List[int]) -> int:
        # Special case
        if nums is None or len(nums) == 0:
            return 0
        # Lookup table for length of LIS until current index
        lookup = [1] * len(nums)
        # Process array
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    lookup[i] = max(lookup[i], 1 + lookup[j])
        return max(lookup)
