from typing import List


class MergeIntervals:
    @staticmethod
    def merge(intervals: List[List[int]]) -> list[list[int]] | None:
        # Special case
        if intervals is None or len(intervals) == 0:
            return intervals
        # Sort the intervals by their start time
        intervals.sort(key=lambda interval: interval[0])
        # List to store merged intervals
        merged_intervals = []
        # Current interval
        current_interval = intervals[0]
        # Add current interval to the list
        merged_intervals.append(current_interval)
        # Process all intervals
        for next_interval in intervals:
            current_end = current_interval[1]
            next_start, next_end = next_interval[0], next_interval[1]
            # If intervals are overlapping
            if current_end >= next_start:
                current_interval[1] = max(current_end, next_end)
            else:
                current_interval = next_interval
                merged_intervals.append(next_interval)
        return merged_intervals
