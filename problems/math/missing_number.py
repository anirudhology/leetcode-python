from typing import List


class MissingNumber:
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        n, total_sum = len(nums), sum(nums)
        return (n * (n + 1) // 2) - total_sum
