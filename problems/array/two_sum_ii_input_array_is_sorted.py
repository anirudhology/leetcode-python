from typing import List


class TwoSumIIInputArrayIsSorted:

    @staticmethod
    def twoSum(numbers: List[int], target: int) -> List[int] | None:
        # Special case
        if numbers is None or len(numbers) < 2:
            return None
        # Left and right pointers
        left, right = 0, len(numbers) - 1
        # Array to store final result
        result = [0] * 2
        # Process the array from both ends
        while left <= right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                result[0] = left + 1
                result[1] = right + 1
                break
            elif sum < target:
                left += 1
            else:
                right -= 1
        return result
