from typing import List


class MaximumSubarray:
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        local_maxima, global_maxima = nums[0], nums[0]
        for i in range(1, len(nums)):
            local_maxima = max(local_maxima + nums[i], nums[i])
            global_maxima = max(local_maxima, global_maxima)
        return global_maxima
