from typing import List


class LongestConsecutiveSequence:
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        # Special case
        if nums is None or len(nums) == 0:
            return 0
        # Set to store all elements in the array for O(1) retrieval
        elements = set()
        for num in nums:
            elements.add(num)
        # Length of the longest consecutive sequence
        lcs_length = 0
        # Process every element in the array
        for num in nums:
            current_element = num
            # If the previous number to current_element is not present
            # in the set, it means it is the first element in a sequence
            if (current_element - 1) not in elements:
                current_length = 1
                while (current_element + 1) in elements:
                    current_element += 1
                    current_length += 1
                lcs_length = max(lcs_length, current_length)
        return lcs_length
