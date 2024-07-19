from typing import List


class FindMinimumInRotatedSortedArray:
    @staticmethod
    def findMin(nums: List[int]) -> int:
        # Left and right pointers
        left, right = 0, len(nums) - 1
        # Process the array in range
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return nums[left]
