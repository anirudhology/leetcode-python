from typing import Optional

from problems.util.tree_node import TreeNode


class InvertBinaryTree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if root is None:
            return root
        # Left and right subtrees
        left = root.left
        right = root.right
        # Invert
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root
