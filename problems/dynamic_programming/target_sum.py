from typing import List


class TargetSum:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Special case
        if not nums:
            return 0
        # Dictionary to keep track of overlapping subproblems
        lookup = dict()
        return self.evaluate(nums, target, 0, lookup)

    def evaluate(self, nums: List[int], target: int, index: int, lookup: dict):
        # Base case
        if index >= len(nums):
            return 1 if target == 0 else 0
        # Found the already evaluated solution
        key = str(index) + "-" + str(target)
        if key in lookup:
            return lookup[key]
        # Evaluate for both positive and negative signs
        ways = self.evaluate(nums, target - nums[index], index + 1, lookup) + self.evaluate(nums, target + nums[index],
                                                                                            index + 1, lookup)
        lookup[key] = ways
        return ways
