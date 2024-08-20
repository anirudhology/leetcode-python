from collections import deque, defaultdict
from typing import List


class GraphValidTree:
    @staticmethod
    def validTree(n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n == 1
        # Adjacency list
        adjacency_list = defaultdict(list)
        for source, destination in edges:
            adjacency_list[source].append(destination)
            adjacency_list[destination].append(source)
        # List to store visited nodes
        visited = set()
        # Queue for BFS
        nodes = deque([edges[0][0]])
        while nodes:
            node = nodes.popleft()
            # Found cycle
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adjacency_list[node]:
                nodes.append(neighbor)
                adjacency_list[neighbor].remove(node)
        return len(visited) == n
