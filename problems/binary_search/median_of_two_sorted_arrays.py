from typing import List


class MedianOfTwoSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Make sure nums1 is the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        # Lengths of both arrays
        m, n = len(nums1), len(nums2)

        # Left and right pointers for binary search on the smaller array
        left, right = 0, m

        while left <= right:
            partition_m = left + (right - left) // 2
            partition_n = (m + n + 1) // 2 - partition_m

            # Handle edge cases for boundaries
            max_left_m = float('-inf') if partition_m == 0 else nums1[partition_m - 1]
            min_right_m = float('inf') if partition_m == m else nums1[partition_m]
            max_left_n = float('-inf') if partition_n == 0 else nums2[partition_n - 1]
            min_right_n = float('inf') if partition_n == n else nums2[partition_n]

            # Check if partitions are correct
            if max_left_m <= min_right_n and max_left_n <= min_right_m:
                if (m + n) % 2 == 0:
                    return (max(max_left_m, max_left_n) + min(min_right_m, min_right_n)) / 2
                else:
                    return max(max_left_m, max_left_n)
            elif max_left_m > min_right_n:
                right = partition_m - 1
            else:
                left = partition_m + 1

        # Should never reach here
        raise ValueError("Invalid input arrays")
