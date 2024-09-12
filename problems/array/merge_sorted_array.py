from typing import List


class MergeSortedArray:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        # Indices to keep track of nums1 and nums2
        i, j = m - 1, n - 1
        # Current index
        index = m + n - 1
        # Process both arrays
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        # Process remaining elements
        while i >= 0:
            nums1[index] = nums1[i]
            i -= 1
            index -= 1
        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
        return nums1
