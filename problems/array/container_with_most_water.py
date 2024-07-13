from typing import List


class ContainerWithMostWater:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        # Special case
        if height is None or len(height) == 0:
            return 0
        # Left and right pointers
        left, right = 0, len(height) - 1
        # Maximum area
        max_area = 0
        # Process array from both ends
        while left <= right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(h * w, max_area)
            # Update pointers accordingly
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_area
