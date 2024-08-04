from typing import List


class CombinationSumII:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store final output
        combinations = []
        # Special case
        if candidates is None or len(candidates) == 0:
            return combinations
        # Sort the array
        candidates.sort()
        # Perform backtracking
        self.backtrack(candidates, 0, [], combinations, target)
        return combinations

    def backtrack(self, candidates: List[int], index: int, combination: List[int], combinations: List[List[int]],
                  target: int):
        if target == 0:
            combinations.append(list(combination))
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            combination.append(candidates[i])
            self.backtrack(candidates, i + 1, combination, combinations, target - candidates[i])
            combination.pop()
