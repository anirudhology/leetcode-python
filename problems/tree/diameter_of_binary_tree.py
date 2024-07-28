from typing import Optional

from problems.util.tree_node import TreeNode


class DiameterOfBinaryTree:

    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Calculate maximum depth and update diameter
        self.max_depth(root)
        return self.diameter

    def max_depth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if root is None:
            return 0
        # Calculate heights of left and right subtrees
        left_height = self.max_depth(root.left)
        right_height = self.max_depth(root.right)
        # Update diameter, if needed
        self.diameter = max(self.diameter, left_height + right_height)
        return 1 + max(left_height, right_height)
