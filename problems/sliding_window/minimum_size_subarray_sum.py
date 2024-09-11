from typing import List


class MinimumSizeSubarraySum:
    @staticmethod
    def minSubArrayLen(target: int, nums: List[int]) -> int:
        # Special case
        if not nums:
            return 0
        # Length of list
        n = len(nums)
        # Left and right pointers of the window
        left, right = 0, 0
        # Minimum length
        min_length = 1 << 31 - 1
        # Sum of the window
        window_sum = 0
        # Process the list
        while right < n:
            window_sum += nums[right]
            right += 1
            # Squeeze the window, if possible
            while window_sum >= target:
                min_length = min(min_length, right - left)
                window_sum -= nums[left]
                left += 1
        return 0 if min_length == 1 << 31 - 1 else min_length
