from typing import Optional

from problems.util.tree_node import TreeNode


class MaximumDepthOfBinaryTree:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Special case
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
