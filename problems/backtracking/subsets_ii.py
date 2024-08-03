from typing import List


class SubsetsII:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # List to store final output
        power_set = []
        # Special case
        if nums is None or len(nums) == 0:
            return power_set
        # Sort the array
        nums.sort()
        # Perform backtracking
        self.backtrack(nums, 0, [], power_set)
        return power_set

    def backtrack(self, nums: List[int], index: int, subset: List[int], power_set: List[List[int]]):
        power_set.append(list(subset))
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.backtrack(nums, i + 1, subset, power_set)
            subset.pop()
