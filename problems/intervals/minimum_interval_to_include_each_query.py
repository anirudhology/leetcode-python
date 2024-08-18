import heapq
from typing import List


class MinimumIntervalToIncludeEachQuery:
    @staticmethod
    def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Total number of queries
        n = len(queries)
        # Create new array to keep track of queries with indices
        query_index = []
        for i in range(n):
            query_index.append([queries[i], i])
        # Sort the array based on query value
        query_index.sort(key=lambda a: a[0])
        # Sort the intervals by their left values
        intervals.sort(key=lambda a: a[0])
        # Min heap to store pairs of size of interval and its right value
        min_heap = []
        # Array to store the final output
        result = [-1] * n
        # Index to keep track of intervals
        j = 0
        # Process all queries
        for i in range(n):
            query, index = query_index[i][0], query_index[i][1]
            # Add intervals to queue if their start value is less than or equal to
            # the current query value
            while j < len(intervals) and intervals[j][0] <= query:
                heapq.heappush(min_heap, [intervals[j][1] - intervals[j][0] + 1, intervals[j][1]])
                j += 1
            # Remove all pairs from heap whose end is smaller than current value
            while len(min_heap) > 0 and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            result[index] = min_heap[0][0] if min_heap else -1
        return result
