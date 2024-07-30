from collections import deque
from typing import Optional, List

from problems.util.tree_node import TreeNode


class BinaryTreeRightSideView:
    @staticmethod
    def rightSideView(root: Optional[TreeNode]) -> List[int]:
        # List to store nodes visible from the right side
        right_nodes = []
        # Special case
        if root is None:
            return right_nodes
        # Queue to perform BFS
        nodes = deque([root])
        # Process all nodes in the tree
        while nodes:
            # Count of nodes at the current level
            size = len(nodes)
            for i in range(size):
                # Get node at the front of the queue
                node = nodes.popleft()
                if i == size - 1:
                    right_nodes.append(node.val)
                # Add left and right children, if present
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        return right_nodes
