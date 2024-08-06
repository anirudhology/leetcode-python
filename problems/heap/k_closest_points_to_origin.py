import heapq
from typing import List


class KClosestPointsToOrigin:
    @staticmethod
    def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
        # List to store k closest points
        k_closest_points = []
        # Special case
        if points is None or len(points) == 0:
            return k_closest_points
        # Heap to store k closes points
        min_heap = []
        for i, (x, y) in enumerate(points):
            distance = x ** 2 + y ** 2
            heapq.heappush(min_heap, (distance, i))
        # Get k closest points
        for _ in range(k):
            k_closest_points.append(points[heapq.heappop(min_heap)[1]])
        return k_closest_points
