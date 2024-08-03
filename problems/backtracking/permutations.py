from typing import List


class Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # List to store final output
        permutations = []
        # Special case
        if nums is None or len(nums) == 0:
            return permutations
        # Perform backtracking
        self.backtrack(nums, [], permutations)
        return permutations

    def backtrack(self, nums: List[int], permutation: List[int], permutations: List[List[int]]):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
        else:
            for i in range(len(nums)):
                if nums[i] in permutation:
                    continue
                permutation.append(nums[i])
                self.backtrack(nums, permutation, permutations)
                permutation.pop()
