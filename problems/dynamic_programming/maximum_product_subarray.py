from typing import List


class MaximumProductSubarray:
    @staticmethod
    def maxProduct(nums: List[int]) -> int:
        # Special case
        if nums is None or len(nums) == 0:
            return 0
        # Maximum and minimum products until the current index
        current_max, current_min = nums[0], nums[0]
        # Final maximum product
        max_product = nums[0]
        # Process the array
        for i in range(1, len(nums)):
            # Handle negative
            if nums[i] < 0:
                current_max, current_min = current_min, current_max
            current_max = max(nums[i], current_max * nums[i])
            current_min = min(nums[i], current_min * nums[i])
            # Update max_product, if required
            max_product = max(current_max, max_product)
        return max_product
