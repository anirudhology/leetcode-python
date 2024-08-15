from typing import List


class InsertInterval:
    @staticmethod
    def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # List to store the final output
        result = []
        if intervals is None or len(intervals) == 0:
            result.append(newInterval)
            return result
        # Total number of intervals
        n = len(intervals)
        # Add all intervals that are smaller than newInterval
        index = 0
        while index < n and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1
        # Add new interval and merge, if required
        while index < n and intervals[index][0] <= newInterval[1]:
            newInterval = [
                min(intervals[index][0], newInterval[0]),
                max(intervals[index][1], newInterval[1])
            ]
            index += 1
        result.append(newInterval)
        # Add remaining elements to the list
        while index < n:
            result.append(intervals[index])
            index += 1
        return result
