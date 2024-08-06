import heapq
from typing import List


class LastStoneWeight:
    @staticmethod
    def lastStoneWeight(stones: List[int]) -> int:
        # Special case
        if stones is None or len(stones) == 0:
            return 0
        # Max heap to store stones
        max_heap = []
        # Add all stones to heap
        for stone in stones:
            heapq.heappush(max_heap, (-stone, stone))
        # Smash stones
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)[0]
            y = -heapq.heappop(max_heap)[0]
            z = x - y
            heapq.heappush(max_heap, (-z, z))
        return -heapq.heappop(max_heap)[0]
