from typing import List


class FindTheDuplicateNumber:
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        # Slow and fast pointers
        slow, fast = nums[0], nums[nums[0]]
        # Traverse until both pointers meet
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # Reset fast pointer
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
