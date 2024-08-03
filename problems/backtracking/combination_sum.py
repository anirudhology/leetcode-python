from typing import List


class CombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # List to store the final output
        result = []
        # Special case
        if candidates is None or len(candidates) == 0:
            return result
        # Sort the array
        candidates.sort()
        # Perform backtracking
        self.backtrack(candidates, 0, [], target, result)
        return result

    def backtrack(self, candidates: List[int], index: int, combination: List[int], target: int,
                  result: List[List[int]]):
        # Base cases
        if target == 0:
            result.append(list(combination))
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.backtrack(candidates, i, combination, target - candidates[i], result)
            combination.pop()
