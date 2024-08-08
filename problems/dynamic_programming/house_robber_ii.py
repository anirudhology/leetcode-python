from typing import List


class HouseRobberII:
    def rob(self, nums: List[int]) -> int:
        # Total number of houses
        n = len(nums)
        # Special cases
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(self.rob_helper(nums, 0, n - 2), self.rob_helper(nums, 1, n - 1))

    @staticmethod
    def rob_helper(nums: List[int], start: int, end: int):
        previous, current = 0, 0
        for i in range(start, end + 1):
            temp = max(previous + nums[i], current)
            previous = current
            current = temp
        return current