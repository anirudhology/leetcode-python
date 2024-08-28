from typing import List


class JumpGame:
    @staticmethod
    def canJump(nums: List[int]) -> bool:
        # Current jump
        jump = nums[0]
        # Process the remaining array
        for i in range(1, len(nums)):
            if jump < i:
                return False
            jump = max(jump, i + nums[i])
        return True
