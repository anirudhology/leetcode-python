import heapq
from collections import defaultdict
from typing import List


class NetworkDelayTime:
    @staticmethod
    def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
        # Dictionary to represent graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # Set to store visited nodes
        visited = set()
        # Min heap
        min_heap = [(0, k)]
        # Process all nodes in the heap
        while min_heap:
            travel_time, node = heapq.heappop(min_heap)
            visited.add(node)

            if len(visited) == n:
                return travel_time

            for neighbor, time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (travel_time + time, neighbor))

        return -1
