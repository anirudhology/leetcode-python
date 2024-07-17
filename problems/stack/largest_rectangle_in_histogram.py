from collections import deque
from typing import List


class LargestRectangleInHistogram:
    @staticmethod
    def largestRectangleArea(heights: List[int]) -> int:
        # Special case
        if heights is None or len(heights) == 0:
            return 0
        # Length of the array
        n = len(heights)
        # Monotonic stack for indices
        stack = deque()
        # Maximum area
        max_area = 0
        # Process the array
        for i in range(n + 1):
            height = 0 if i == n else heights[i]
            while stack and height < heights[stack[-1]]:
                current_height = heights[stack.pop()]
                current_width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)
        return max_area