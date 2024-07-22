from collections import deque
from typing import List


class SlidingWindowMaximum:
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> list[int | list[int]] | None:
        # Special case
        if nums is None or len(nums) == 0 or k <= 0:
            return nums
        # Length of the array
        n = len(nums)
        # Array to store the sliding window elements
        sliding_window_max = []
        # Deque to store the elements of the sliding window
        window_elements = deque()
        # Process the array
        for i in range(n):
            # Remove elements from the left
            if window_elements and window_elements[0] < i - k + 1:
                window_elements.popleft()
            # Remove elements from the deque that are less than nums[i] as
            # they can never become max for this window
            while window_elements and nums[window_elements[-1]] < nums[i]:
                window_elements.pop()
            # Add current index to the deque
            window_elements.append(i)
            if i >= k - 1:
                sliding_window_max.append(nums[window_elements[0]])
        return sliding_window_max
