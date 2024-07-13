from typing import List


class ThreeSum:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        # List to store triplets
        triplets = list()
        # Special case
        if nums is None or len(nums) < 3:
            return triplets
        # Length of the list
        n = len(nums)
        # Sort the list
        nums.sort()
        # Process the array
        for i in range(n):
            # Skip the duplicates, if any
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Left and right pointers for the remaining list
            j, k = i + 1, n - 1
            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]
                # Sum is zero!!!
                if triplet_sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Skip duplicates if any
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                # If sum is negative, it means we are too left,
                # and we need to move towards right
                elif triplet_sum < 0:
                    j += 1
                # If sum is positive, it means we are too right,
                # and we need to move towards left
                else:
                    k -= 1
        return triplets
