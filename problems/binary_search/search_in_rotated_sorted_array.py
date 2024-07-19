from typing import List


class SearchInRotatedSortedArray:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        # Special case
        if nums is None or len(nums) == 0:
            return -1
        # Left and right pointers
        left, right = 0, len(nums) - 1
        # Process the array from both ends
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
