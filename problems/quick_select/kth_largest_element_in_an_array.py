from typing import List


class KthLargestElementInAnArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Update k to make kth-largest element (because QuickSelect works
        # for kth-smallest element)
        k = len(nums) - k
        # Left and right pointers
        left, right = 0, len(nums) - 1
        # Process from both sidex
        while left < right:
            pivot_index = self.partition(nums, left, right)
            if pivot_index < k:
                left = pivot_index + 1
            elif pivot_index > k:
                right = pivot_index - 1
            else:
                break
        return nums[k]

    @staticmethod
    def partition(nums: List[int], left: int, right: int):
        pivot = nums[right]
        pivot_index = left
        for i in range(left, right):
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            pivot_index += 1
        nums[right] = nums[pivot_index]
        nums[pivot_index] = pivot
        return pivot_index - 1
