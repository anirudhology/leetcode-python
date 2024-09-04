from collections import deque
from typing import List


class CheapestFlightsWithinKStops:
    @staticmethod
    def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Adjacency list
        graph = []
        for i in range(n):
            graph.append([])
        for flight in flights:
            graph[flight[0]].append([flight[1], flight[2]])
        # Queue to perform BFS
        nodes = deque([[src, 0]])
        # Array to store minimum costs
        min_cost = [0x7fffffff] * n
        # Stops taken
        stops = 0
        # Process until queue is not empty and stops are less than equal to k
        while nodes and stops <= k:
            size = len(nodes)
            for i in range(size):
                current = nodes.popleft()
                # Process the neighbors of this current node
                for [node, cost] in graph[current[0]]:
                    if (cost + current[1]) >= min_cost[node]:
                        continue
                    min_cost[node] = cost + current[1]
                    nodes.append([node, min_cost[node]])
            stops += 1
        return min_cost[dst] if min_cost[dst] != 0x7fffffff else -1
