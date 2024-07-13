from typing import List


class TrappingRainWater:
    @staticmethod
    def trap(height: List[int]) -> int:
        # Special case
        if height is None or len(height) == 0:
            return 0
        # Left and right pointers
        left, right = 0, len(height) - 1
        # Variables to keep track of max height to the left
        # and max height to the right of the current element
        left_height, right_height = 0, 0
        # Trapped water area
        area = 0
        # Process array from both ends
        while left <= right:
            if height[left] <= height[right]:
                area += max(0, left_height - height[left])
                left_height = max(left_height, height[left])
                left += 1
            else:
                area += max(0, right_height - height[right])
                right_height = max(right_height, height[right])
                right -= 1
        return area
