from typing import List


class ContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Special case
        if nums is None or len(nums) == 0:
            return False
        # Set to store elements in the array
        elements = set()
        # Process elements of the array one by one
        for num in nums:
            if num in elements:
                return True
            elements.add(num)
        return False
