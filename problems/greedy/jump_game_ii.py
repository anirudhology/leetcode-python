from typing import List


class JumpGameII:
    @staticmethod
    def jump(nums: List[int]) -> int:
        # Total number of jumps required
        jumps = 0
        # Left and right pointers for the window
        left, right = 0, 0
        # Process the elements in the list
        while right < len(nums) - 1:
            # Longest distance that can be reached in
            # the current window
            longest = 0
            for i in range(left, right + 1):
                longest = max(longest, i + nums[i])
            # Update the pointers for next window
            left = right + 1
            right = longest
            jumps += 1
        return jumps
