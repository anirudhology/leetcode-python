from collections import deque
from typing import Optional, List

from problems.util.tree_node import TreeNode


class BinaryTreeLevelOrderTraversal:
    @staticmethod
    def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
        # List to store the final output
        output = []
        # Special case
        if root is None:
            return output
        # Queue to traverse the tree in BFS mode and add root node to it
        nodes = deque([root])
        # Traverse for all nodes in the tree
        while nodes:
            # Total number of nodes at the current level
            size = len(nodes)
            # List to store nodes at the current level
            current_level_nodes = []
            for _ in range(size):
                # Get node at the front of the queue
                node = nodes.popleft()
                # Add this node to the current level nodes list
                current_level_nodes.append(node.val)
                # Process left and right subtrees, if present
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            # Add current level nodes to the output list
            output.append(current_level_nodes)
        return output
