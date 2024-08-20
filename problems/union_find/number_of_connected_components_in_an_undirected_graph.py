from typing import List


class NumberOfConnectedComponentsInAnUndirectedGraph:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Array to store the parent of each node
        parents = [i for i in range(n)]
        # Perform union by connecting every edge
        for edge in edges:
            self.union(edge[0], edge[1], parents)
        # Count number of connected components by count nodes that are their
        # own parents
        count = 0
        for i in range(n):
            if i == self.find(parents[i], parents):
                count += 1
        return count

    def union(self, a, b, parents):
        # Find roots of both nodes
        root_a = self.find(a, parents)
        root_b = self.find(b, parents)
        parents[root_a] = root_b

    @staticmethod
    def find(node, parents):
        if parents[node] != node:
            # Path compression
            parents[node] = parents[parents[node]]
        return parents[node]
