import heapq
from typing import List


class MinCostToConnectAllPoints:
    @staticmethod
    def minCostConnectPoints(points: List[List[int]]) -> int:
        # Special case
        if not points:
            return 0
        # Total number of points
        n = len(points)
        # List to store visited vertices
        visited = [False] * n
        # We only want to visit n - 1 vertices as we don't want to have
        # cycle in the graph
        edges_left_to_visit = n - 1
        # Total cost of connecting all points
        cost = 0
        # Since we always want nearest vertex to be chosen first, we will
        # choose min heap for that purpose
        edges = []
        heapq.heapify(edges)
        # We will start from vertex 0 to reach to all other points from here
        for i in range(1, n):
            distance = abs(points[i][0] - points[0][0]) + abs(points[i][1] - points[0][1])
            heapq.heappush(edges, Edge(0, i, distance))
        # Mark 0 as visited
        visited[0] = True
        # Process edges until edgesLeftToVisit becomes 0
        while edges and edges_left_to_visit > 0:
            # Get the current edge
            edge = heapq.heappop(edges)
            v, weight = edge.v, edge.weight
            if not visited[v]:
                # Add the cost and mark as visited
                cost += weight
                visited[v] = True
                # Now traverse all possible points from v
                for i in range(n):
                    if not visited[i]:
                        distance = abs(points[v][0] - points[i][0]) + abs(points[v][1] - points[i][1])
                        heapq.heappush(edges, Edge(v, i, distance))
                edges_left_to_visit -= 1
        return cost


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    # For comparisons if needed, otherwise the heap only uses the weight
    def __lt__(self, other):
        return self.weight < other.weight
