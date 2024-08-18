from typing import List


class NonOverlappingIntervals:
    @staticmethod
    def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
        # Special case
        if intervals is None or len(intervals) == 0:
            return 0
        # Sort the array by their end times
        intervals.sort(key=lambda interval: interval[1])
        current_end = intervals[0][1]
        # Non overlapping intervals
        non_overlapping_intervals = 1
        # Process remaining intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] >= current_end:
                current_end = intervals[i][1]
                non_overlapping_intervals += 1
        return len(intervals) - non_overlapping_intervals
