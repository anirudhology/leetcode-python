from typing import List


class SingleNumber:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        answer = nums[0]
        for i in range(1, len(nums)):
            answer ^= nums[i]
        return answer
