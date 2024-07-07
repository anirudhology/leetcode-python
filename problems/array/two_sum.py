from typing import List


class TwoSum:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        # Special case
        if nums is None or len(nums) < 2:
            raise Exception("Invalid inputs!")
        # Dictionary to store the complement of a number w.r.t target
        # and its index
        mappings = {}
        # Traverse through each element of the array one by one
        for i in range(len(nums)):
            # Check if the element is already present in the dictionary
            if nums[i] in mappings:
                return [mappings[nums[i]], i]
            # Add the complement of the current element in the dictionary
            mappings[target - nums[i]] = i
        raise Exception("Invalid inputs")
