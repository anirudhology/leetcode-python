from typing import List


class TopKFrequentElements:

    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        # Special case
        if nums is None or len(nums) == 0 or k < 0:
            return []
        # Dictionary to store the frequencies of the elements in the array
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        # List to store the buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for key in frequencies:
            frequency = frequencies[key]
            buckets[frequency].append(key)
        # List to store the final output
        result = [0] * k
        i = len(buckets) - 1
        j = 0
        while i >= 0 and j < k:
            if buckets[i] is not None:
                for element in buckets[i]:
                    result[j] = element
                    j += 1
            i -= 1
        return result
