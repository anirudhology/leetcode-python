from typing import List


class RedundantConnection:
    @staticmethod
    def findRedundantConnection(edges: List[List[int]]) -> List[int]:
        # Total number of edges
        n = len(edges)
        # Arrays to store parents and ranks of each edge
        parents = [i for i in range(n + 1)]
        ranks = [1] * (n + 1)

        def find(node):
            p = parents[node]
            while p != parents[p]:
                # Path compression
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(node1, node2):
            # Find parents of both nodes
            p1 = find(node1)
            p2 = find(node2)
            # If parents are same, it means we cannot create
            # the edges without creating a cycle
            if p1 == p2:
                return False
            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                parents[p1] = p2
                ranks[p2] += ranks[p1]
            return True

        # Process every edge and see if it can be unionized
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
