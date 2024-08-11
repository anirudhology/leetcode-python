from typing import Optional

from problems.util.graph_node import GraphNode


class CloneGraph:
    def cloneGraph(self, node: Optional['GraphNode']) -> Optional['GraphNode']:
        # Special case
        if node is None:
            return None
        # Dictionary to store the mappings of original node and clone node
        mappings = {}
        # Perform DFS on the graph
        return self.dfs(node, mappings)

    def dfs(self, node: Optional['GraphNode'], mappings) -> Optional['GraphNode']:
        # Create clone for the current node
        clone_node = GraphNode(node.val)
        mappings[node] = clone_node
        # List to store neighbors of the cloned node
        cloned_neighbors = []
        # Traverse through all the neighbors
        for neighbor in node.neighbors:
            # If we have already traversed this node
            if neighbor in mappings:
                cloned_neighbors.append(mappings[neighbor])
            else:
                cloned_neighbors.append(self.dfs(neighbor, mappings))
        clone_node.neighbors = cloned_neighbors
        return clone_node
