from typing import List


class ProductOfArrayExceptSelf:
    
    @staticmethod
    def productExceptSelf(nums: List[int]) -> list[int] | None:
        # Special Case
        if nums is None or len(nums) < 2:
            return nums
        # Length of the array
        n = len(nums)
        # Array to store the final output
        product = [0] * n
        # Cumulative product of array elements
        cumulative_product = 1
        # Process the array from left to right
        for i in range(n):
            product[i] = cumulative_product
            cumulative_product *= nums[i]
        # Reset the cumulative_product
        cumulative_product = 1
        # Process the array from right to left
        for i in range(n - 1, -1, -1):
            product[i] *= cumulative_product
            cumulative_product *= nums[i]
        return product
